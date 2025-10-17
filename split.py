import argparse
import os

def split_file(file_path, lines_per_file):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total_lines = len(lines)
    file_count = 1

    for i in range(0, total_lines, lines_per_file):
        split_lines = lines [i:i + lines_per_file]
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        new_file_name = f"{base_name}_part{file_count}.txt"
        
        with open(new_file_name, "w", encoding="utf-8") as nf:
            nf.writelines(split_lines)
        print(f"Created {new_file_name} with {len(split_lines)} lines.")
 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split CLI tool")
    parser.add_argument("--file", type = str, help = "Path to txt file")
    parser.add_argument("--lines", type = int, help = "Number of lines per split file")
    args = parser.parse_args()
    print(f"File: {args.file}, Lines per file: {args.lines}")

    split_file(args.file, args.lines)