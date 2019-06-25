import pyautogui

image_data = pyautogui.screenshot()

huntcomplete = 10
counter = 0

while(True):
    
    pyautogui.moveTo(720,483)
    pyautogui.dragTo(1150,414,1.5,button='left')
    
    counter = counter + 1
    if(counter == huntcomplete):
        break
quit() 
