import pyautogui
from pyxdameraulevenshtein import damerau_levenshtein_distance as dld
from pyxdameraulevenshtein import normalized_damerau_levenshtein_distance as ndld
import time
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# print('Ученый')

# start = pyautogui.locateCenterOnScreen('locate/main/main_done.png')
# pyautogui.moveTo(start, duration=0.25)
# pyautogui.click()
# pyautogui.moveTo(pyautogui.locateCenterOnScreen('locate/noob/augusto.png'), duration=0.25)
# pyautogui.click()
pyautogui.getWindowsWithTitle('FOnline Requiem')[0].activate()
# pyautogui.moveTo(pyautogui.locateCenterOnScreen('locate/noob/augusto.png'), duration=0.25)
# pyautogui.click()
# time.sleep(3)
dialog = pyautogui.locateOnScreen('locate/dialog_anchor.png')
# s = pyautogui.locateAllOnScreen('locate/string_anchor.png')
# print(*s)
# print(dialog)
x, y = dialog[0], dialog[1]
print(x, y)
pyautogui.moveTo(x, y)
dx = -1
dy = 118

# pyautogui.moveRel(dx, dy, duration=0.5)
# for i in range(3):
#     pyautogui.moveRel(300, 0, duration=0.5)
#     pyautogui.moveRel(0, 13, duration=0.5)
#     pyautogui.moveRel(-300, 0, duration=0.5)
#     pyautogui.moveRel(0, 13, duration=0.5)
#
# print(x + dx, y + dy)
scr = pyautogui.screenshot(region=(x - dx, y + dy, 320, 100))
pixels = scr.load()
for i in range(scr.size[0]):
    for j in range(scr.size[1]):
        if pixels[i, j] == (60, 249, 0):
            pixels[i, j] = (0, 0, 0)
        else:
            pixels[i, j] = (255, 255, 255)


data = pytesseract.image_to_data(scr, lang='rus', output_type='dict')
word_num = data['word_num']
top = data['top']
text = data['text']
prev_n = 0
out = []
string = []
# print(word_num)
# print(top)
# print(text)
for i in range(len(word_num)):

    if word_num[i] - prev_n == 1:
        prev_n = word_num[i]
        string.append((top[i], text[i]))
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
print(*response, sep='\n')



