import os 
import argparse
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

def join_files(files: list, output: str, verbose: bool):
    total_lines = 0 

    with open(output, "w", encoding='utf-8')  as outfile:
        for file_path in files:
            if not os.path.exists(file_path):
                logging.error(f"Selected file does not exist: {file_path}")
                continue
            try:
                with open(file_path, "r", encoding="utf-8") as infile:
                    file_lines = 0
                    for line in infile:
                        outfile.write(line)
                        file_lines += 1
                    total_lines += file_lines
                if verbose:
                    logging.info(f"Added {file_lines} lines from {file_path}")
            except Exception as e:
                logging.exception(f"Failed to read {file_path}: {e}")

    logging.info(f"Created '{output}' with total {total_lines} lines.")

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
    parser = argparse.ArgumentParser(description="Join CLI tool")
    parser.add_argument("-f" ,"--file", type=str, nargs="+", help="List of txt files to combine")
    parser.add_argument("-o", "--output", default="combined.txt", help="Name of the output file.")
    parser.add_argument("-v", "--verbose", action = "store_true", help="Show detailed output")
    args = parser.parse_args()      #pristupam kao args.file; args.output; args.verbose

    if not args.file:
        logging.info("No input files provided. Use -f to specify files.")
    else:
        join_files(args.file, args.output, args.verbose)