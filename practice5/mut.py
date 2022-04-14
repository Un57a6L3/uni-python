import random
from collections import defaultdict
import inspect
from ast import *


# Forms a dictionary of nodes with class as key
class Locator(NodeVisitor):
    def __init__(self):
        self.locs = defaultdict(list)

    def visit(self, node):
        self.locs[type(node)].append(node)
        self.generic_visit(node)


# Changes target nodes in code
class Mutator(NodeTransformer):
    def __init__(self, locs: defaultdict):
        # List of node classes with explicit visitor methods
        implemented = [BinOp, UnaryOp, BoolOp, Compare]

        # Find intersection of the list above and the located classes
        node_types = [x for x in list(locs.keys()) if x in implemented]

        # Pick one of the classes, choose random node of that class
        node_type = random.choice(node_types)
        self.target = random.choice(locs[node_type])

    def visit(self, node):
        if self.target != node:
            return self.generic_visit(node)
        if isinstance(node, BinOp):
            return self.visit_BinOp(node)
        if isinstance(node, UnaryOp):
            return self.visit_UnaryOp(node)
        if isinstance(node, BoolOp):
            return self.visit_BoolOp(node)
        if isinstance(node, Compare):
            return self.visit_Compare(node)
        raise Exception('Unimplemented node class')

    def visit_BinOp(self, node: BinOp):
        # Choose new operator
        new_op = None
        if isinstance(node.op, Add):
            new_op = Sub
        if isinstance(node.op, Sub):
            new_op = Add
        if isinstance(node.op, Mult):
            new_op = random.choice([Div, Pow])
        if isinstance(node.op, Mod):
            new_op = random.choice([Div, FloorDiv])

        # Make new node
        if not new_op:
            return node
        result = BinOp(
            left=node.left,
            right=node.right,
            op=new_op()
        )
        return copy_location(result, node)

    def visit_UnaryOp(self, node: UnaryOp):
        # Choose new operator
        new_op = None
        if isinstance(node.op, UAdd):
            new_op = USub
        if isinstance(node.op, USub):
            new_op = UAdd

        # Make new node
        if not new_op:
            return node
        result = UnaryOp(
            op=new_op(),
            operand=node.operand
        )
        return copy_location(result, node)

    def visit_BoolOp(self, node: BoolOp):
        # Choose new operator
        new_op = None
        if isinstance(node.op, And):
            new_op = Or
        if isinstance(node.op, Or):
            new_op = And

        # Make new node
        if not new_op:
            return node
        result = BoolOp(
            op=new_op(),
            values=node.values
        )
        return copy_location(result, node)

    def visit_Compare(self, node: Compare):
        # Choose new operator
        new_op = None
        if isinstance(node.ops[0], Gt):
            new_op = random.choice([GtE, Lt, LtE])
        if isinstance(node.ops[0], GtE):
            new_op = random.choice([Gt, Lt, LtE])
        if isinstance(node.ops[0], Lt):
            new_op = random.choice([LtE, Gt, GtE])
        if isinstance(node.ops[0], LtE):
            new_op = random.choice([Lt, Gt, GtE])

        # Make new node
        if not new_op:
            return node
        result = Compare(
            left=node.left,
            ops=[new_op()]+node.ops[1:],
            comparators=node.comparators
        )
        return copy_location(result, node)


def mutate_code(src, max_changes):
    '''Makes one mutant from given source'''

    # Parse source and call a visit with Locator
    tree = parse(src)
    loc = Locator()
    loc.visit(tree)

    # loc.locs now contains a dictionary with all nodes
    for _ in range(random.randint(1, max_changes)):
        mut = Mutator(loc.locs)
        tree = mut.visit(tree)
    return unparse(tree)


def make_mutants(func, size, max_changes):
    '''Makes a list of mutants'''

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


def mut_test(func, test, size=20, max_changes=3):
    '''Main mutation testing function'''

    # Making list of mutants
    survived, killed = [], []
    mutants = make_mutants(func, size, max_changes)

    # Loop for testing each mutant
    for mutant in mutants:
        try:
            exec(mutant, globals())
            test()
            survived.append(mutant)
        except:
            killed.append(mutant)
            pass
    return survived, killed


# Function for testing
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


# Testing function
def test():
    assert fact(7) == 5040
    assert fact(5) == 120
    assert fact(0) == 1
    assert fact(-1) == -1
    assert fact(-2) == 2
    assert fact(-3) == -6
    assert fact(-4) == 24


def main(user_input=False, filename='muttest.log'):
    # Input of parameters
    num, chs = 6, 2
    if user_input:
        num = int(input('Enter number of mutants: '))
        chs = int(input('Enter max number of changes: '))

    # Running the test
    try:
        survived, killed = mut_test(fact, test, size=num, max_changes=chs)
    except AssertionError:
        print('Failed to generate unique mutants')
        print('Try to lower the number of mutants')
        return
    surv, dead = len(survived), len(killed)

    # Logging results
    with open(filename, 'w') as f:
        f.write('Survived mutants:\n')
        f.write('None.\n' if survived == [] else '-----------------\n')
        count = 1
        for mutant in survived:
            f.write(f'\n--- Survived mutant #{count} ---\n')
            f.write(mutant + '\n')
            count += 1
        count = 1
        f.write('\nKilled mutants:\n')
        f.write('None.\n' if killed == [] else '---------------\n')
        for mutant in killed:
            f.write(f'\n--- Killed mutant #{count} ---\n')
            f.write(mutant + '\n')
            count += 1
    print(f'Testing done. Survived: {surv}, killed: {dead}.')
    print(f'See more info in {filename}')


if __name__ == '__main__':
    main(user_input=True)
