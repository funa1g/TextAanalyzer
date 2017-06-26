from typing import Sequence


class Paragraph(object):
    def __init__(self, paragraph):
        self.text = paragraph.strip()
        self.lines = []
        self.parse()

    def parse(self):
        lines = self.split_text(self.text)
        for line in lines:
            line = line.strip()
            if not line:
                continue
            self.lines.append(line)

    def split_text(self, text: str) -> Sequence[str]:
        return text.split('。')


class TextAnalyzer(object):
    """module implementation
    """
    def __init__(self):
        self.path = ""
        self.paragraphs = []
        self.word_count = 0
        self.line_count = 0

    def read(self, file_path: str):
        """
        file_path: str
        """
        self.path = file_path
        f = open(self.path, 'r')
        for text in f:
            text = text.strip()
            if not text:
                continue
            paragraph = Paragraph(text)
            self.paragraphs.append(paragraph)
        for paragraph in self.paragraphs:
            self.word_count += len(paragraph.text)
            self.line_count += len(paragraph.lines)

    def execute(self):
        """output analyzing result
        """
        print('path: ' + self.path)
        print('文字数: ' + str(self.word_count))
        print('行数: ' + str(self.line_count))
        print('段落数: ' + str(len(self.paragraphs)))
