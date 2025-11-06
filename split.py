import argparse
import os
import logging


logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

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
        logging.info(f"Created {new_file_name} with {len(split_lines)} lines.")

def stream_lines(file_path, chunk_size=1024*64):
    """Generator: returns line-per-line (str), uses rb and decoding by chunk. 64KB by chunk"""

    with open(file_path, 'rb') as f:
        leftover = b''
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            data = leftover + chunk
            lines = data.split(b'\n')
            leftover = lines.pop()
            for bline in lines:
                yield bline.decode('utf-8', errors='replace')
        if leftover:
                yield leftover.decode("utf-8", errors='replace')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split CLI tool")
    parser.add_argument("--file", type = str, help = "Path to txt file")
    parser.add_argument("--lines", type = int, help = "Number of lines per split file")
    args = parser.parse_args()
    logging.info(f"File: {args.file}. Lines per file: {args.lines}")

    split_file(args.file, args.lines)