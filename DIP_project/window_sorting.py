from pynput.keyboard import Key, Controller # to simulate keystrokes
from win32gui import *

from win32con import SW_SHOWNOACTIVATE
from time import sleep



class windows_selection:
    def __init__(self) -> None:
        self.process_names = []
    
    def window_find(self, handles=[]):
        if len(self.process_names) != 0:
            self.process_names = []
        EnumWindows(window_enum_handler, handles)
        for handle in handles:
            self.process_names.append(handle)
    
    def find_PID(self, name:str):
        if len(self.process_names) == 0:
            self.window_find()
        PID = 0
        for i in range(len(self.process_names)):
            
            if name.upper() in (self.process_names[i][1]).upper():
                PID = self.process_names[i][0]
        return PID

    def setFocus(self, PID) -> None:
        try:
            ShowWindow(PID, SW_SHOWNOACTIVATE)
            SetForegroundWindow(PID)
        except:
            print("This is error.")

    def keystrokes(self, combo: bool = False, key: list = []):
        print(key[0])
        keyboard = Controller() # to send virtual keyboard events to system
        if combo:
            with keyboard.pressed(key[0]):
                keyboard.tap(key[1])
        else:
            keyboard.tap(key[0])


def window_enum_handler(handle, resultlist):
    if IsWindowVisible(handle) and GetWindowText(handle) != 0:
        resultlist.append([handle, GetWindowText(handle)])
