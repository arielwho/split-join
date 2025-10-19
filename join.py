import os 
import argparse

def join_files(file_list, output_file):
    with open(file_list, "w", encoding='utf-8')  as f:
        lines = f.readlines()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Join CLI tool")
    parser.add_argument("-f" ,"--file", type=str, nargs="+", help="List of txt files to combine")
    parser.add_argument("-o", "--output", default="combined.txt", help="Name of the output file.")
    parser.add_argument("-v", "--verbose", action = "store_true", help="Show detailed output")
    args = parser.parse_args()      #pristupam kao args.files; args.output; args.verbose