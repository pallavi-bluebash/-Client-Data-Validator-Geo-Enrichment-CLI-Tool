import sys
import argparse
from processor import process_csv

def main():
    parser = argparse.ArgumentParser(description="Validate and enrich client data from a CSV file.")
    parser.add_argument("input", nargs="?", type=argparse.FileType('r'), default=sys.stdin,
                        help="Input CSV file (default: stdin)")
    args = parser.parse_args()

    output_csv = process_csv(args.input)
    print(output_csv)

if __name__ == "__main__":
    main()
