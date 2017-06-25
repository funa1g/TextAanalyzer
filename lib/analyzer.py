class TextAnalyzer(object):
    """module implementation
    """
    def __init__(self):
        self.path = ""
        self.lines = []
        self.paragraphs = []
        self.word_count = 0

    def read(self, file_path: str):
        """
        file_path: str
        """
        self.path = file_path
        f = open(self.path, 'r')
        for paragraph in f:
            self.paragraphs.append(paragraph.strip())
            lines = paragraph.split('。')
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                self.lines.append(line)
        for paragraph in self.paragraphs:
            self.word_count += len(paragraph)

    def execute(self):
        """output analyzing result
        """
        print('path: ' + self.path)
        print('文字数: ' + str(self.word_count))
        print('行数: ' + str(len(self.lines)))
        print('段落数: ' + str(len(self.paragraphs)))
