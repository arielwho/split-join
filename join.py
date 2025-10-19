import os 
import argparse

def join_files(files, output, verbose):
    total_lines = 0 

    with open(output, "w", encoding='utf-8')  as outfile:
        for file in files:
            if os.path.exists(file):
                with open(files, "r", encoding="utf-8") as infile:
                    lines = infile.readlines()
                    total_lines += len(lines)
                    outfile.writelines(lines)
                    outfile.write("\n")
            else:
                print("Selected file does not exist.")

                if verbose:
                    print(f"Added {len(lines)} from {file}")
    
    print(f"Created {outfile} with total {total_lines} lines.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Join CLI tool")
    parser.add_argument("-f" ,"--file", type=str, nargs="+", help="List of txt files to combine")
    parser.add_argument("-o", "--output", default="combined.txt", help="Name of the output file.")
    parser.add_argument("-v", "--verbose", action = "store_true", help="Show detailed output")
    args = parser.parse_args()      #pristupam kao args.files; args.output; args.verbose