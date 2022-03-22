#Dependency Python ofc 
#pip install pywin32
#pip install Pillow
#pip install keyboard
#pip install pyautogui
#pip install opencv-python

import win32gui, win32api, win32con, pyautogui, sys, time, keyboard
def checkBookmarks():
    Mystic_pos=pyautogui.locateOnScreen('Pics\\mystic.png',grayscale=False,confidence=0.7)
    Coven_pos=pyautogui.locateOnScreen('Pics\\covenant.png',grayscale=False,confidence=0.7)

    if Mystic_pos:
        Mystic_point=pyautogui.center(Mystic_pos)
        x = Mystic_point[0]
        y = Mystic_point[1]
        pyautogui.click(x+800,y+50)
        #Shold use size here from FindEmulatorSize
        time.sleep(0.5)
        pyautogui.click(pyautogui.locateOnScreen('Pics\\Buy_button_Mystic.png', grayscale=False,confidence=0.5))
        global mystic
        mystic+=1
        time.sleep(1)
    
    if Coven_pos:
        Coven_point=pyautogui.center(Coven_pos)
        x = Coven_point[0]
        y = Coven_point[1]
        pyautogui.click(x+800,y+50)
        time.sleep(0.5)
        pyautogui.click(pyautogui.locateOnScreen('Pics\\Buy_button_Covenant.png', grayscale=False,confidence=0.5))
        global covenant
        covenant+=1
        time.sleep(1)


def scroll():
    pyautogui.scroll(-10)
    time.sleep(1.5)

def Refresh():
    #while keyboard.is_pressed('q') == False: 
    RB_pos=pyautogui.locateOnScreen('Pics\\refresh_button.png', grayscale=False,confidence=0.5)
    checkBookmarks()
    scroll()
    checkBookmarks()     
    pyautogui.click(RB_pos)
    time.sleep(1.5)
    Confirm_pos=pyautogui.locateOnScreen('Pics\\confirm button.png', grayscale=False,confidence=0.5)
    pyautogui.click(Confirm_pos)
    global autos
    autos+=1
    time.sleep(1.5)


mystic,autos,covenant = 0,0,0

try:
    while keyboard.is_pressed('q') == False:
        Refresh()
except KeyboardInterrupt:
    print('ctrl+c interrupted')
    print("Total Covenant: ",covenant)
    print("Total Mystic: ",mystic)
    print("Total Refreshes: ",autos)
