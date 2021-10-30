#Dependency Python ofc 
#pip install pywin32
#pip install Pillow
#pip install keyboard
#pip install pyautogui
#pip install opencv-python

import win32gui, win32api, win32con, pyautogui, sys, time, keyboard, time

#def click(x,y):
    #win32gui.SetCursorPos((x,y))
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #time.sleep(0.4)
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def checkBookmarks():
    Mystic_pos=pyautogui.locateOnScreen('Pics\\mystic.png',grayscale=False,confidence=0.7)
    Coven_pos=pyautogui.locateOnScreen('Pics\\covenant.png',grayscale=False,confidence=0.7)

    if Mystic_pos:
        Mystic_point=pyautogui.center(Mystic_pos)
        x = pyautogui.locateOnScreen('Pics\\mystic.png')[0]
        y = pyautogui.locateOnScreen('Pics\\Buy_button_Mystic.png')[1]
        pyautogui.click(x+800,y+50)
        pyautogui.click(pyautogui.locateOnScreen('Pics\\mystic.png'))
    
    if Coven_pos:
        Coven_point=pyautogui.center(Coven_pos)
        x = pyautogui.locateOnScreen('Pics\\covenant.png')[0]
        y = pyautogui.locateOnScreen('Pics\\covenant.png')[1]
        pyautogui.click(x+800,y+50)
        pyautogui.click(pyautogui.locateOnScreen('Pics\\Buy_button_Covenant.png'))

def scroll():
    pyautogui.scroll(-5, x=1263, y=590)
    time.sleep(3)
    pyautogui.click(x=1263,y=590)

def Refresh():
    while keyboard.is_pressed('q') == False: 
        RB_pos=pyautogui.locateOnScreen('Pics\\refresh_button.png', grayscale=False,confidence=0.7)
        checkBookmarks()
        scroll()
        checkBookmarks()     
        pyautogui.click(RB_pos)

def FindEmulator():
    hwnd = win32gui.FindWindow(None, "Epic 7")
    try:
        if not hwnd:
            emuName = input("Enter name of the Epic 7 emulator. ")
            hwnd = win32gui.FindWindow(None, emuName)
        if not hwnd:
            raise ValueError()
        return hwnd
    except ValueError:
        print("%s application not found" % emuName)
        sys.exit()
    

def FindSizeOfEmulator(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    print("Application Name: %s" % win32gui.GetWindowText(hwnd))
    print("\tLocation: (%d, %d)" % (x, y))
    print("\t    Size: (%d, %d)" % (w, h))


def main():
    bookmarks,mystics,refreshes = 0,0,0
    targetWindow = FindEmulator()
    FindSizeOfEmulator(targetWindow)

if __name__ == '__main__':
    main()

