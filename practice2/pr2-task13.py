# This version of the script runs on Windows
# To make it run on Linux you should change '\\' to '/'

import os
import graphviz

tree = graphviz.Digraph()

# THESE ARE CONFIGURABLE OPTIONS

# files and directories in this list will be ignored
IGNORE = {'.git'}

# this directory will be the root for graph and search
ROOT_PATH = 'C:\\'

# maximum graph and search depth
MAX_DEPTH = 2

# if False, only directories are included in graph
# if True, both files and directories are included
GRAPH_FILES = False


# Recursive function that adds directories and files to graph
def add_dir(depth, prev, path):
    if depth > 0:
        for subdir in os.listdir(path):
            if subdir not in IGNORE:
                current_dir = path + subdir

                # adding subdirectory or file to graph
                if GRAPH_FILES or os.path.isdir(current_dir):
                    name = current_dir.split('\\')[-1]
                    tree.node(name, name)
                    tree.edge(prev, name, constraint='true')

                # calling function for subdirectory
                if os.path.isdir(current_dir):
                    try:
                        current_dir += '\\'
                        temp = os.listdir(current_dir)
                        add_dir(depth - 1, name, current_dir)

                    # there are 'legacy' folders in Windows that deny read permissions
                    # they are located at C:\, C:\Users\, C:\ProgramData\ and any drive's root
                    except WindowsError:
                        print(f'Caught a Windows error when trying to read {current_dir}')
                    except not WindowsError:
                        print(f'Caught a Windows-unrelated error when trying to read {current_dir}')


# Function for building directory graph at ROOT_PATH
def build_graph(depth):
    tree.node('root', ROOT_PATH.split('\\')[-2])
    add_dir(depth, 'root', ROOT_PATH)
    print('Rendering...')

    # change output directory, name and format here
    tree.render('graphs\\output', format='png', cleanup=True)

    print('Done.')


def main():
    build_graph(MAX_DEPTH)


if __name__ == "__main__":
    main()
