from ..core import *


class Noob:

    # 1 quarter
    augusto = (1056, 434)

    # 2 quarter
    kid = (1484, 370)

    # 2 quarter
    ed = (1151, 415)

    # 2 quarter
    auto = (972, 641)

    @staticmethod
    def move_to_quarter(quarter):
        if quarter == 1:
            pyautogui.moveTo(1919, 0)
        elif quarter == 2:
            pyautogui.moveTo(0, 0)
        elif quarter == 3:
            pyautogui.moveTo(0, 1079)
        elif quarter == 4:
            pyautogui.moveTo(1919, 1079)
        else:
            raise Exception('wrong argument: should be int')
        time.sleep(1)
        pyautogui.moveTo(10, 10)
        return True

    @staticmethod
    def seq1():
        Noob.move_to_quarter(1)
        talk_xy(*Noob.augusto)
        while check_running():
            time.sleep(1)
        proceed_dialog([0, 0, 0, 0, 0])
        return 'success'

    @staticmethod
    def seq2():
        Noob.move_to_quarter(1)
        talk_xy(*Noob.augusto)
        proceed_dialog([
            'Я спросить.',
            'Есть мелочь?',
            'Вот спасибо'
        ])
        return 'success'

    @staticmethod
    def seq3():
        Noob.move_to_quarter(1)
        run(94, 434)
        Noob.move_to_quarter(2)
        while check_running():
            time.sleep(1)
        talk_xy(*Noob.kid)
        proceed_dialog([
            'Секреты - это хорошо. Держи копейку.',
            0,
            0,
            0,
            'Нож, значит? Окей, будет тебе нож.'
        ])
        return 'success'

    @staticmethod
    def seq4():
        Noob.move_to_quarter(2)
        talk_xy(*Noob.ed)
        while check_running():
            time.sleep(1)
        proceed_dialog([
            0,
            'А, ну да, точно.',
            'Чем занят?',
            'Что за Вескер',
            'Так ты знаешь, как пройти через дверь?!',
            0,
            'Окей, пойду к нему.'
        ])
        return 'success'

    @staticmethod
    def seq5():
        Noob.move_to_quarter(2)
        talk_xy(*Noob.auto)
        while check_running():
            time.sleep(1)
        proceed_dialog(['Придумать, способ, как вытащить пару монет.'])
        pyautogui.press('esc')
        return 'success'

    functions_list = [
        seq1,
        seq2,
        seq3,
        seq4
    ]


# TODO: переписать этот модуль без класса (ибо не нужен), методы все статичные
if __name__ == '__main__':
    Noob.seq1()
    Noob.seq2()
    Noob.seq3()
    Noob.seq4()
