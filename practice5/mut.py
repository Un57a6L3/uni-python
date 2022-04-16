"""
Mutation testing module.

You can add any function you want to test to the code. You'll need to pass the
source and the testing functions as parameters: ``main(func, test)``.
Example functions given are ``fact`` and ``test_fact``.

NOTE: This module was written from a code template by Peter Sovietov
(check github.com/true-grue/kispython) as a university assignment, which I went
a little overboard with.

Author: Arseny Antonov (github.com/Un57a6L3/uni-python).
"""

import random
from collections import defaultdict
import inspect
from ast import *
import multiprocessing as mp


class Locator(NodeVisitor):
    """
    Class for locating nodes.

    Running ``visit(tree)`` on a parsed tree will form a dictionary with node
    classes as keys, and lists of nodes of those classes as values.
    """

    def __init__(self):
        self.locs = defaultdict(list)

    def visit(self, node):
        self.locs[type(node)].append(node)
        self.generic_visit(node)


# Changes target nodes in code
class Mutator(NodeTransformer):
    """
    Class for mutating nodes.

    Selecting a target node with ``set_target(locs)`` is required before you
    call ``visit(tree)`` to mutate said node.
    """

    # List of node classes with implemented mutations
    implemented = [UnaryOp, BinOp, BoolOp, Compare]

    # These dictionaries describe the mutations that can occur in nodes
    # The keys are the existing operators
    # The values are lists of what operators they can mutate into
    muts_UnaryOp = {
        UAdd: [USub],
        USub: [UAdd]
    }
    muts_BinOp = {
        Add: [Sub, Mult],
        Sub: [Add, Div],
        Mult: [Add, Div, Pow],
        Div: [Sub, Mult, FloorDiv, Mod],
        Mod: [Sub, Mult, Div, FloorDiv],
        Pow: [Mult],
        LShift: [RShift],
        RShift: [LShift],
        BitOr: [BitXor, BitAnd],
        BitXor: [BitOr, BitAnd],
        BitAnd: [BitOr, BitXor]
    }
    muts_BoolOp = {
        And: [Or],
        Or: [And]
    }
    muts_Compare = {
        Eq: [NotEq, Is],
        NotEq: [Eq, IsNot],
        Is: [IsNot, Eq],
        IsNot: [Is, NotEq],
        In: [NotIn],
        NotIn: [In],
        Gt: [GtE, Lt, LtE],
        GtE: [Gt, Lt, LtE],
        Lt: [LtE, Gt, GtE],
        LtE: [Lt, Gt, GtE]
    }

    def __init__(self):
        self.target = None

    def set_target(self, locs: defaultdict):
        """Randomly selects target node for mutation."""

        # Form a list of the classes in locs that have implemented mutations
        node_types = [x for x in list(locs.keys()) if x in Mutator.implemented]

        # Pick one of the classes, choose random node of that class
        node_type = random.choice(node_types)
        self.target = random.choice(locs[node_type])

    def visit(self, node):
        """
        Overridden default visitor method.

        Calls ``generic_visit`` for any node except the target node which is
        mutated with ``visit_target``.
        """

        if self.target is None:
            raise Exception('No target chosen')
        if self.target != node:
            return self.generic_visit(node)
        return self.visit_target(node)

    def visit_target(self, node):
        """
        Visitor method that mutates target nodes.

        Randomly selects mutation based on node class and operator, calls a
        mutation method for the node class.
        """

        # ``Compare`` node type has a list of operators rather than one
        old_op = node.ops[0] if type(node) in [Compare] else node.op
        new_op = None

        # Choose mutation from static dictionary for the node type
        muts = getattr(Mutator, f'muts_{type(node).__name__}')
        for key, value in muts.items():
            if isinstance(old_op, key):
                new_op = random.choice(value)

        # Call mutation method for the node type
        if not new_op:
            return node
        for x in Mutator.implemented:
            if isinstance(node, x):
                return getattr(self, f'mut_{x.__name__}')(node, new_op)
        raise Exception('Unimplemented node class')

    def mut_UnaryOp(self, node, new_op):
        """Mutation method for UnaryOp nodes."""
        return copy_location(UnaryOp(
            operand=node.operand,
            op=new_op()
        ), node)

    def mut_BinOp(self, node, new_op):
        """Mutation method for BinOp nodes."""
        return copy_location(BinOp(
            left=node.left,
            right=node.right,
            op=new_op()
        ), node)

    def mut_BoolOp(self, node, new_op):
        """Mutation method for BoolOp nodes."""
        return copy_location(BoolOp(
            values=node.values,
            op=new_op()
        ), node)

    def mut_Compare(self, node, new_op):
        """Mutation method for Compare nodes."""
        return copy_location(Compare(
            left=node.left,
            comparators=node.comparators,
            ops=[new_op()]+node.ops[1:]
        ), node)


def mutate_code(src, max_changes):
    """
    Makes one mutant from given source.

    :param src: source code to mutate
    :param max_changes: maximum number of mutations allowed
    :returns: a mutant (mutated source code)
    """

    # Parse source and call a visit with Locator
    tree = parse(src)
    loc = Locator()
    loc.visit(tree)

    # loc.locs now contains a dictionary with all nodes
    mut = Mutator()
    for _ in range(random.randint(1, max_changes)):
        mut.set_target(loc.locs)
        tree = mut.visit(tree)
    return unparse(tree)


def make_mutants(func, size, max_changes):
    """
    Makes a list of mutants from given function.

    :param func: source function to mutate
    :param size: number of mutants to make
    :param max_changes: maximum number of mutations allowed per mutant
    :returns: list of mutants
    :raises AssertionError: raises error if fails to make enough unique mutants
    """

    # Getting program source
    mutant = src = unparse(parse(inspect.getsource(func)))
    mutants = [src]

    # Fills mutant list, returns all but first element (source)
    while len(mutants) < size + 1:
        # Mutates source and appends the mutant to list
        attempts = 0
        while mutant in mutants:
            assert attempts < 20, 'Too many failed attempts'
            mutant = mutate_code(src, max_changes)
            attempts += 1
        mutants.append(mutant)
    return mutants[1:]


def mut_process(mutant, test):
    """
    Single mutant testing function that is meant to be run in a subprocess.

    :param mutant: a mutant (mutated source code) to test
    :param test: testing function with ``assert`` statements
    """

    # Mutants are mutated definitions of the source function
    # So executing them redefines the function in the scope
    exec(mutant, globals())

    # Exceptions have to be caught inside the process
    # Otherwise ``stderr`` will be filled with exceptions info
    try:
        test()
    except:
        exit(1)


def mut_test(func, test, size=20, max_changes=3):
    """
    Main mutation testing function. 

    :param func: source function to mutation test
    :param test: testing function with ``assert`` statements
    :param size: number of mutants to make and test
    :param max_changes: maximum number of mutations allowed per mutant
    :returns: list of survived mutants, list of killed mutants
    """

    # Making list of mutants
    survived, killed, timedout = [], [], []
    mutants = make_mutants(func, size, max_changes)

    # Loop for testing each mutant
    for mutant in mutants:
        p = mp.Process(target=mut_process, args=(mutant, test))
        p.start()
        p.join(1)
        if p.exitcode is None:
            p.terminate()
            p.join()
            timedout.append(mutant)
        elif p.exitcode == 0:
            survived.append(mutant)
        else:
            killed.append(mutant)
    return survived, killed, timedout


# Implementation of factorial function
# This function is an example of function to test
# You can add other functions and test them as well
def fact(n):
    result = 1
    positive = True
    if n < 0:
        n *= -1
        if n % 2:
            positive = False
    while n > 0:
        result *= n
        n -= 1
    if not positive:
        result *= -1
    return result


# Testing function for the ``fact`` function
# This function is an example of a testing function
# You can add other testing functions as well
def test_fact():
    assert fact(7) == 5040
    assert fact(5) == 120
    assert fact(0) == 1
    assert fact(-1) == -1
    assert fact(-2) == 2
    assert fact(-3) == -6
    assert fact(-4) == 24


def main(func, test, num=None, chs=None, filename='muttest.log'):
    """
    Driver function for mutation testing.

    :param func: source function to mutation test
    :param test: testing function with ``assert`` statements
    :param num: number of mutants to make and test
    :param chs: maximum number of mutations allowed per mutant
    :param filename: name of the log file with testing info and results
    """

    # Input of parameters
    if num is None:
        num = int(input('Enter number of mutants: '))
    if chs is None:
        chs = int(input('Enter max number of changes: '))

    # Running the test
    try:
        surv, dead, timed = mut_test(func, test, size=num, max_changes=chs)
    except AssertionError:
        print('Failed to generate unique mutants')
        print('Try to lower the number of mutants')
        return

    # Logging results
    pools = [(surv, 'Survived'), (dead, 'Killed'), (timed, 'Timed out')]
    with open(filename, 'w') as f:
        # Options and results summary
        f.write('--- Testing options ---\n')
        f.write(f'Number of mutants: {num}\n')
        f.write(f'Maximum changes:   {chs}\n\n')
        f.write('--- Testing results ---\n')
        f.write(f'Mutants survived:  {len(surv)}\n')
        f.write(f'Mutants killed:    {len(dead)}\n')
        f.write(f'Mutants timed out: {len(timed)}\n')

        # Survived, killed and timed out mutant pools print
        for pool, msg in pools:
            if pool:
                f.write(f'\n\n{msg} mutants:\n')
                f.write(f'{"-" * (len(msg) + 9)}\n')
            count = 1
            for mutant in pool:
                f.write(f'\n--- {msg} mutant #{count} ---\n')
                f.write(f'{mutant}\n')
                count += 1

    # Terminal prints
    print(f'Testing done.')
    print(f'Survived:  {len(surv)}')
    print(f'Killed:    {len(dead)}')
    print(f'Timed out: {len(timed)}')
    print(f'See more info in {filename}')


if __name__ == '__main__':
    main(fact, test_fact, filename='muttest_fact.log')
