import os


class Character:

    def __init__(self):
        pass

    @staticmethod
    def get_chars():
        if os.path.exists('characters'):
            return os.listdir('characters')
        else:
            return 'no directory'


if __name__ == '__main__':
    Character.get_chars()
