import os
import graphviz
import argparse

SLASH = os.path.sep


class Tree:
    def __init__(self):
        self.tree = graphviz.Digraph()
        self.root_path = os.getcwd()
        self.graph_files = False
        self.max_depth = 3
        self.render_format = 'png'
        self.filename = 'output'
        self.ignore_list = {'.git', '.idea', '__pycache__'}

    # Recursive function that adds directories and files to graph
    def add_node_rec(self, depth, prev, path):
        if depth <= 0:
            return
        for subdir in os.listdir(path):
            if subdir in self.ignore_list:
                continue
            current_dir = path + SLASH + subdir

            # adding subdirectory or file to graph
            if not self.graph_files and not os.path.isdir(current_dir):
                continue
            name = current_dir.split(SLASH)[-1]
            self.tree.edge(prev, name)

            # calling function for subdirectory
            if not os.path.isdir(current_dir):
                continue
            try:
                current_dir += SLASH
                catch = os.listdir(current_dir)
                self.add_node_rec(depth - 1, name, current_dir)

            # there are 'legacy' folders in Windows that deny read permissions
            # they are located at C:\, C:\Users\, C:\ProgramData\ and any drive's root
            except WindowsError:
                print(f'Caught a Windows error when trying to read {current_dir}')
            except not WindowsError:
                print(f'Caught a Windows-unrelated error when trying to read {current_dir}')

    # Driver function for graph building
    def build_tree_rec(self):
        path = [x for x in self.root_path.split(SLASH) if x != '']
        self.tree.node('root', path[-1])
        self.add_node_rec(self.max_depth, 'root', self.root_path)

    def render_tree(self):
        self.tree.render(self.filename, format=self.render_format, cleanup=True, view=True)
        print(f'Rendered to output.{self.render_format}')

    def print_tree(self):
        print(self.tree.source)


def main():
    # graphics file extensions for rendering
    ext = {'jpeg', 'jpg', 'tiff', 'tif', 'svg', 'png', 'gif', 'pdf'}

    # parsing command line arguments
    parser = argparse.ArgumentParser(description='Build and print/render directory tree.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-r', '--reldir', metavar='DIR', help='relative directory')
    group.add_argument('-a', '--absdir', metavar='DIR', help='absolute directory')
    parser.add_argument('-f', '--files', help='include files in graph', action='store_true')
    parser.add_argument('-d', '--depth', metavar='LVL', type=int, help='maximum search depth')
    parser.add_argument('-n', '--name', help='output file name')
    parser.add_argument('-o', '--out', metavar='EXT', help='output file extension', choices=ext)
    parser.add_argument('-i', '--ignore', metavar='DIR', nargs='*', help='list of files and dirs to ignore')
    args = parser.parse_args()

    tree = Tree()

    # applying command line arguments
    if args.reldir:
        tree.root_path += args.reldir
    if args.absdir:
        tree.root_path = args.absdir
    if args.files:
        tree.graph_files = True
    if args.depth and args.depth > 0:
        tree.max_depth = args.depth
    if args.name:
        tree.filename = args.name
    if args.out:
        tree.render_format = args.out
    if args.ignore:
        tree.ignore_list.update(args.ignore)

    # tree building and output
    tree.root_path = os.path.normpath(tree.root_path + SLASH)
    tree.build_tree_rec()
    if args.out:
        tree.render_tree()
    else:
        tree.print_tree()


if __name__ == '__main__':
    main()
