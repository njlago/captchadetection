import pyautogui, sys

pyautogui.moveTo(700, 200, 1,pyautogui.easeOutQuad) 
pyautogui.click(clicks=2, interval=0.25)
pyautogui.press('enter')
pyautogui.write('Hello world!')
pyautogui.scroll(-1) 
im = pyautogui.screenshot(region=(0,0, 300, 400))
pyautogui.locateOnScreen('calc7key.png')
pyautogui.move(0, 200, 0.5) 
pyautogui.move(200, 0, 0.5) 
pyautogui.move(0, -200, 0.5) 
pyautogui.move(-200, 0, 0.5) 
pyautogui.scroll(1) 
print(im)


# print('Press Ctrl-C to quit.')

# try:
#     while True:

#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')