import argparse
from lib import TextAnalyzer


def main(file_path: str):
    """execute TextAnalyzer
    """
    analyzer = TextAnalyzer()
    analyzer.read(file_path)
    analyzer.execute()

if __name__ == "__main__":
    # execute only if run as a script
    parser = argparse.ArgumentParser(description='Analyzing text')
    parser.add_argument('text_file_path', metavar='f', type=str,
                        help='analyzing text file path')
    parser.add_argument('-T', dest='text', metavar='T', type=str,
                        required=False, help='analyzing text')
    args = parser.parse_args()
    main(args.text_file_path)
