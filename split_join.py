import argparse
from ast import arg
from split import split_file
from join import join_files
from tqdm import tqdm

def main() -> None:
    parser = argparse.ArgumentParser(description="Split or join text files easily.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    parser.add_argument("--verbose", action="store_true", help="Show detailed progress")

    #Split 
    split_parser = subparsers.add_parser("split", help="Split a text file")
    split_parser.add_argument("--file", required=True, help="Path to the file to split")
    split_parser.add_argument("--lines", type=int, required=True, help="Lines per file")

    #Join
    join_parser = subparsers.add_parser("join", help="Join multiple text files")
    join_parser.add_argument("--files", nargs="+", required=True, help="Files to join")
    join_parser.add_argument("--output", required=True, help="Output file name")

    args = parser.parse_args()

    if args.command == "split":
        split_file(args.file, args.lines)
    elif args.command == "join":
        join_files(args.files, args.output, args.verbose)

    if args.command == "split":
        with open(args.file, "r", encoding="utf-8") as f:
            total_lines = sum(1 for _ in f)
        with tqdm(total=total_lines, unit="lines") as pbar:     #progress bar
            def progress_cb(frac, info):
                pbar.n = int(frac * total_lines)
                pbar.refresh()
        split_file(args.file, args.lines, progress_cb=progress_cb)
    elif args.command == "join":
        join_files(args.files, args.output, args.verbose)
       

if __name__ == "__main__":
    main()