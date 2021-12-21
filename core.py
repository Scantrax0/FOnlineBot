import pyautogui
from pyxdameraulevenshtein import damerau_levenshtein_distance as dld
from pyxdameraulevenshtein import normalized_damerau_levenshtein_distance as ndld
import time
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def get_dialog_answers():

    """
    находит диалоговое окно и расшифровывает текст
    возвращает список кортежей, в которых первый элемент у-координата строки, второй - сама строка

    :return:
    """
    pyautogui.moveTo(10, 10)
    dialog = pyautogui.locateOnScreen('locate/dialog_anchor.png')

    if dialog:

        x, y = dialog[0], dialog[1]
        dx = -1
        dy = 118

        # получаем область распознования
        scr = pyautogui.screenshot(region=(x - dx, y + dy, 320, 100))
        pixels = scr.load()

        # красим пиксели в черный и белый
        for i in range(scr.size[0]):
            for j in range(scr.size[1]):
                if pixels[i, j] == (60, 249, 0):
                    pixels[i, j] = (0, 0, 0)
                else:
                    pixels[i, j] = (255, 255, 255)

        # получаем расшифровку
        data = pytesseract.image_to_data(scr, lang='rus', output_type='dict')

        # парсим (надо переделать нормально)
        word_nums = data['word_num']
        y_coordinates = data['top']
        values = data['text']
        prev_n = 0
        out = []
        string = []

        for i in range(len(word_nums)):

            if word_nums[i] - prev_n == 1:
                prev_n = word_nums[i]
                string.append((y_coordinates[i], values[i]))
            else:
                prev_n = 0
                out.append(string)
                string = []
        out.append(string)

        response = []
        for elem in out:
            if elem:
                coordinates = elem[0][0]
                response.append((coordinates, ' '.join([_[1] for _ in elem])))

        if response:
            print(response)
            return response
        else:
            return 'nothing'

    else:
        return 'no dialog window'


def find_answer(string, answers_list):

    """
    выбирает из списка ответов ближайший к string по расстоянию Дамерау-Левенштейна и возвращает у-координату
    :param string:
    :param answers_list:
    :return:
    """
    diff_list = []

    # создаем список с расстоянием ДЛ и у-координатой
    for answer in answers_list:
        diff_list.append((dld(string, answer[1]), answer[0]))

    # находим элемент с минимальным расстоянием
    correct_answer = min(diff_list, key=lambda x: x[0])

    # здесь нужна проверка на адекватность ответа
    if correct_answer[0] > len(string) // 2:
        return 'cannot find correct answer'

    return correct_answer[1]


def pick_answer(answer_y=2):
    """
    выбирает реплику в диалоге по координате, если вызвана без аргумента - выбирается первая строка
    :param answer_y:
    :return:
    """
    pyautogui.moveTo(10, 10)
    dialog = pyautogui.locateOnScreen('locate/dialog_anchor.png')

    if dialog:
        dialog_x, dialog_y = dialog[0], dialog[1]
        pyautogui.moveTo(dialog_x, dialog_y + 120 + answer_y)
        pyautogui.click()
        return True
    else:
        return 'no dialog window'


def run(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.rightClick()
    pyautogui.click()
    pyautogui.rightClick()
    pyautogui.moveTo(10, 10)
    return True


def check_running():
    if pyautogui.locateOnScreen('locate/red_dot.png'):
        return True
    if pyautogui.locateOnScreen('locate/red_dot.png'):
        return True
    return False


def talk(img_url):
    char = pyautogui.locateOnScreen(img_url)
    if char:
        # print(char[0] + char[2] // 2, char[1] + char[3] // 2)
        pyautogui.moveTo(char[0] + char[2] // 2, char[1] + char[3] // 2)
        pyautogui.click()
        pyautogui.moveTo(10, 10)
        return True
    else:
        print('cannot find character')
        return 'cannot find character'


def talk_xy(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.moveTo(10, 10)
    return True


def proceed_dialog(answers_list):
    for elem in answers_list:
        if elem == 0:
            pick_answer()
        else:
            answers = get_dialog_answers()
            if answers == 'no dialog window':
                print(answers)
                return False
            elif answers == 'nothing':
                # здесь надо сделать изменение области сканирования
                print(answers)
                return False
            else:
                found_answer = find_answer(elem, answers)
                if found_answer == 'cannot find correct answer':
                    raise Exception('cannot find correct answer')
                pick_answer(found_answer)
        time.sleep(0.5)
