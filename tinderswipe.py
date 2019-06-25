import pyautogui

#taking screenshot
image_data = pyautogui.screenshot()

huntcomplete = 10
counter = 0

while(True):
    #move cursor to desired pos.
    pyautogui.moveTo(720,483)
    #draggg
    pyautogui.dragTo(1150,414,1.5,button='left')
    
    counter = counter + 1
    if(counter == huntcomplete):
        break
