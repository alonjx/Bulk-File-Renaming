import argparse
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description='Use this script for bulk file renaming, I encourage you to read the '
                                                 'HELP menu in order to be familiar with the different options you have'
                                                 '. *** Python3.4+ required.')
    parser.add_argument("src")
    parser.add_argument('-d', '--dst', help='Destination folder files are going to be move to.', nargs='?', const='True')
    parser.add_argument('-p', '--pattern', help='Use pattern to filter the files that will be effected, \n'
                                                "e.g: \"*.py$\" -> effects all files with \"py\" suffix.")
    parser.add_argument('-r', '--recursive', help='Effects all files including those located in sub-directories.',
                        nargs='?', const='True')
    parser.add_argument('-n', '--new-name', help='set new name for matching files with an id (e.g xxx-1, xxx-2).',
                        nargs='?', const='True')
    parser.add_argument('-c', '--handle-collisions', help='Automatically handle name collision that might occur when '
                                                          ' moving files without defining "-n" arg', nargs='?',
                        const='True')

    args = parser.parse_args()
    assert args.new_name or args.dst, "You have to use at least one of the arguments (--dst, --new-name)"
    return args


def rename_only(path, glob_str, dst_name):
    previous_parent = None
    for f in path.glob(glob_str):
        if previous_parent != f.parent:
            previous_parent = f.parent
            i = 0
        if not f.is_dir():
            name = "%s-%s" % (dst_name, i)
            f.rename(f.with_name(name).with_suffix(f.suffix))
            i += 1


def move_only(path, glob_str, dst, handle_collisions=True):
    destination_path = Path(dst)
    for f in path.glob(glob_str):
        if not f.is_dir():
            new_path = (destination_path / f.name)
            if handle_collisions:
                i = 0
                while new_path.exists():
                    i += 1
                    new_name = "%s-%s" % (f.stem, i)
                    new_path = new_path.with_name(new_name).with_suffix(new_path.suffix)
            f.rename(new_path)


def move_and_rename(path, glob_str, dst, dst_name):
    destination_path = Path(dst)
    i = 0

    for f in path.glob(glob_str):
        if not f.is_dir():
            name = "%s-%s" % (dst_name, i)
            f.rename((destination_path / name).with_suffix(f.suffix))
            i += 1


def main():
    args = parse_args()
    path = Path(args.src)
    glob_str = args.pattern if args.pattern else "*"
    if args.recursive:
        glob_str = "**/" + glob_str

    if args.dst:
        if args.new_name:
            move_and_rename(path, glob_str, args.dst, args.new_name)
        else:
            move_only(path, glob_str, args.dst,  args.handle_collisions)
    elif args.new_name:
        rename_only(path, glob_str, args.new_name)


if __name__ == '__main__':
    main()
