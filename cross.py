import pyautogui, os
import time

pyautogui.useImageNotFoundException(False)

def detectcross(region: tuple):

    pyautogui.moveTo(region[0]/2, region[1]/2, duration=0.1)
    pyautogui.moveTo(region[0]/2 + region[2]/2, region[1]/2 + region[3]/2, duration=0.1)


    for i,cross in enumerate(os.listdir('dataset/Crosswalk')):

        print("crossimg" + str(i))

        file_path = f'dataset/Crosswalk/{cross}'

        crosslocation = pyautogui.locateOnScreen(file_path,region=region,confidence=0.80,grayscale=True)
          
        if crosslocation:

            
            crosscenter = pyautogui.center(crosslocation)

            pyautogui.screenshot('images/my_screenshot.png')

            print("Crosswalk found at %s",crosscenter)
            crossx, crossy = crosscenter
            
            pyautogui.moveTo(crossx/2, crossy/2,0.1)
            pyautogui.click()

    