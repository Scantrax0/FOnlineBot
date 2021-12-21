import os


class Character:

    def __init__(self, name, load=True):

        self.char_url = 'characters/' + name + '.txt'
        self.name = name

        if load:
            with open(self.char_url, 'r', encoding='utf-8') as char_file:

                data = char_file.readlines()

                self.special = list(map(int, data[1].split()))

                progress = data[2].split()
                self.lvl = int(progress[0])
                self.location = progress[1]
                self.seq = int(progress[2])
                print(self)
        else:
            while True:
                special = list(map(int, input('Введите характеристики SPECIAL. Например: 10 4 8 2 3 9 1\n').split()))
                if len(special) != 7:
                    print('Ошибка в SPECIAL!')
                    continue
                error = False
                for x in special:
                    if x > 10 or x < 1:
                        error = True
                if error:
                    print('Ошибка в SPECIAL!')
                    continue
                else:
                    break

            self.special = special

            self.lvl = 1
            self.location = 'Noob'
            self.seq = 0

            print(self)
            self.save_char()

    def save_char(self):
        with open(self.char_url, 'w', encoding='utf-8') as char_file:
            char_file.write(self.name + '\n')
            char_file.write(' '.join(map(str, self.special)) + '\n')
            char_file.write(' '.join([str(self.lvl), self.location, str(self.seq)]))
        return True

    @staticmethod
    def get_chars():
        if os.path.exists('characters'):
            return os.listdir('characters')
        else:
            os.mkdir('characters')
            print('characters directory created')
            return 'characters directory created'

    def __str__(self):
        s = ''.join([f'{sym}: {value}\n' for sym, value in zip(list('SPECIAL'), self.special)])
        return f'{self.name}\n{s}Level: {self.lvl}\nLocation: {self.location}\nNext sequence: {self.seq}'


if __name__ == '__main__':
    load = Character('Paragon')
    print()
