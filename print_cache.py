import pyperclip


class PrintCache:
    def __init__(self):
        self.cache = list()

    def print(self, strvalue):
        self.cache.append(strvalue)
        print(strvalue)

    def copy_to_clipboard(self):
        printed_text = '\n'.join(self.cache)
        pyperclip.copy(printed_text)
        print('This output text is copied to your clipboard')
