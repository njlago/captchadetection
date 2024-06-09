import pyautogui, os
import time

from cross import detectcross

# Take a screenshot and save it
image_filename = 'my_screenshot.png'
im2 = pyautogui.screenshot(image_filename)

# Get the absolute path of the saved screenshot
image_path = os.path.abspath(image_filename)

# Print the absolute path
print(f"Screenshot saved at: {image_path}")

pyautogui.useImageNotFoundException(False)

def checkbox_move():


    while True:
        
        boxlocation = pyautogui.locateOnScreen('images/checkbox.png',confidence=0.9)

        if boxlocation:

            boxcenter = pyautogui.center(boxlocation)
            boxx, boxy = boxcenter
            
            boxwidth = boxlocation.width
            pyautogui.moveTo(boxx/2-(boxwidth/5.5), boxy/2,0.1)
            pyautogui.click()
           

            # pyautogui.moveTo(int(boxx/2-(boxwidth/10)), boxy/2-boxwidth,0.2)

            # pyautogui.move(int(boxwidth*1.4),0,0.2)
            # pyautogui.move(0,int(boxwidth*0.42),0.2)


            
            region = (
                int(boxx - (boxwidth/5)),  
                int((boxy - boxwidth*2)+(boxwidth*0.84)),       
                int(398*2),          
                int(398*2)           
            )
            titleregion = (
                int(boxx - (boxwidth/5)),  
                int((boxy - boxwidth*2)+(boxwidth*0.84)-260),       
                int(398*2),         
                int(260)          
            )

            print(region)
            print(titleregion)

            # Draw a rectangle to visualize the region
            pyautogui.moveTo(titleregion[0]/2, titleregion[1]/2, duration=0.1)
            pyautogui.moveTo(titleregion[0]/2 + titleregion[2]/2, titleregion[1]/2 + titleregion[3]/2, duration=0.1)

            crossimg = pyautogui.locateOnScreen('images/crossimg.png',region=titleregion,confidence=0.82)
            busimg = pyautogui.locateOnScreen('images/busimg.png',region=titleregion,confidence=0.82)
            bikeimg = pyautogui.locateOnScreen('images/bikeimg.png',region=titleregion,confidence=0.82)
            hydrantimg = pyautogui.locateOnScreen('images/hydrantimg.png',region=titleregion,confidence=0.82)


            if crossimg:
                
                print("cross-test")
                detectcross(region)

            if busimg:
                print("bus-test")
                # detectcross()

            if bikeimg:
                print("bike-test")
                # detectcross()

            if hydrantimg:
                print("hydrant-test")
                # detectcross()

            # break

            

        time.sleep(0)



checkbox_move()