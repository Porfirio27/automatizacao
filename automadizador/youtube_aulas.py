import pyautogui as pa
import time
pa.PAUSE = 2

pa.press('win')
pa.write('chrome')
pa.press('ENTER')
pa.write('https://www.youtube.com/playlist?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-')
pa.press('ENTER')