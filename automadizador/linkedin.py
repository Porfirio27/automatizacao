import pyautogui as pa
import time
pa.PAUSE = 1

pa.press('win')
pa.write('chrome')
pa.press('ENTER')
pa.write('https://www.linkedin.com/feed/')
pa.press('ENTER')