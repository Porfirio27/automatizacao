import pyautogui as pa
import time
pa.PAUSE = 1

pa.press('win')
pa.write('chrome')
pa.press('ENTER')
pa.write('https://www.udemy.com/home/my-courses/learning/')
pa.press('ENTER')
time.sleep(4)
pa.click(x=284, y=628)
time.sleep(7)
pa.click(x=507, y=354)


