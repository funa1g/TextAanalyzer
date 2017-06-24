import sys
from lib import TextAnalyzer

def main(file_path: str):
    analyzer = TextAnalyzer()
    analyzer.read(file_path)
    analyzer.execute()

if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[1])
