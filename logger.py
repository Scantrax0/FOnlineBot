from datetime import datetime
import os


class Logger:

    def __init__(self):

        # создаем лог-файл

        current_datetime = datetime.now()
        self.log_name = current_datetime.strftime('%Y.%m.%d_%H-%M-%S.txt')

        if not os.path.exists('logs'):
            os.makedirs('logs')
        elif os.path.isfile('logs'):
            raise Exception('There is file "logs" in folder!')

        self.log_url = 'logs/' + self.log_name
        with open(self.log_url, 'w', encoding='utf-8') as log_file:
            log_file.write('<----Log started!---->\n')

    def log(self, s: str):
        with open(self.log_url, 'a', encoding='utf-8') as log_file:
            current_datetime = datetime.now()
            formatted_time = current_datetime.strftime('[%H-%M-%S]: ')
            log_file.write(formatted_time + s + '\n')


if __name__ == '__main__':

    import time

    l = Logger()
    l.log('smth')
    time.sleep(10)
    l.log('and smth')


