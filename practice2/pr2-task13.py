import os
import graphviz

SLASH = os.path.sep
tree = graphviz.Digraph()

# THESE ARE CONFIGURABLE OPTIONS

# files and directories in this list will be ignored
IGNORE = {'.git', '.idea', '.files', '__pycache__', 'graphs'}

# this directory will be the root for graph and search
ROOT_PATH = f'F:{SLASH}coding-kispython{SLASH}'

# maximum graph and search depth
MAX_DEPTH = 10

# if False, only directories are included in graph
# if True, both files and directories are included
GRAPH_FILES = True


# Recursive function that adds directories and files to graph
def add_dir(depth, prev, path):
    if depth <= 0:
        return
    for subdir in os.listdir(path):
        if subdir in IGNORE:
            continue
        current_dir = path + subdir

        # adding subdirectory or file to graph
        if not GRAPH_FILES and not os.path.isdir(current_dir):
            continue
        name = current_dir.split(SLASH)[-1]
        tree.node(name, name)
        tree.edge(prev, name, constraint='true')

        # calling function for subdirectory
        if not os.path.isdir(current_dir):
            continue
        try:
            current_dir += SLASH
            temp = os.listdir(current_dir)
            add_dir(depth - 1, name, current_dir)

        # there are 'legacy' folders in Windows that deny read permissions
        # they are located at C:\, C:\Users\, C:\ProgramData\ and any drive's root
        except WindowsError:
            print(f'Caught a Windows error when trying to read {current_dir}')
        except not WindowsError:
            print(f'Caught a Windows-unrelated error when trying to read {current_dir}')


def main():
    tree.node('root', ROOT_PATH.split(SLASH)[-2])
    add_dir(MAX_DEPTH, 'root', ROOT_PATH)
    print('Rendering...')

    # change output directory, name and format here
    tree.render(f'graphs{SLASH}output', format='png', cleanup=True)

    print('Done.')


if __name__ == "__main__":
    main()
