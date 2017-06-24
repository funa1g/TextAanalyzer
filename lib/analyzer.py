class TextAnalyzer(object):
    """module implementation
    """
    def __init__(self):
        self.path = ""

    def read(self, file_path: str):
        """
        file_path: str
        """
        self.path = file_path

    def execute(self):
        """output analyzing result
        """
        print('path: ' + self.path)
