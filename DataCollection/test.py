from time import sleep
from win32gui import GetWindowText, GetForegroundWindow
from time import time
from pynput.keyboard import Key, Listener
from pyautogui import position
import threading

timeGap = 5
mouseSleep = 0.1
timerOn = True
movement_key = ["'a'", "'w'", "'s'", "'d'", "'e'", "'q'", "'z'", "'A'", "'W'", "'S'", "'D'", "'E'", "'Q'", "'Z'", Key.ctrl_l, Key.shift]
log = {'movement': 0, 'useless': 0, 'begin_time':time()}
start = time()
mouseRecord = []
lastMousePos = position()


def on_press(key):
    # print('{0} pressed'.format(key))zzz
    # print(key)
    pass


def on_release(key):
    global log
    global timerOn
    # print('{0} release'.format(key))
    if (str(key) in movement_key) or (key in movement_key):
        log['movement']+=1
    else:
        log['useless']+=1
    if key == Key.esc:
        # Stop listener
        timerOn = False
        return False


def timer():
    global log
    global TimerOn
    global timeGap
    global mouseRecord
    while timerOn:
        sleep(timeGap)
        log['keys_per_min'] = (log['movement'] + log['useless']) * 60 / timeGap
        log['speed_of_mouse_moved'] = sum(mouseRecord)/len(mouseRecord)
        mouseRecord = []
        print(log)
        log = {'movement': 0, 'useless': 0, 'begin_time':time()}

def mouseMoveTmr():
    global mouseRecord
    global lastMousePos
    while timerOn:
        sleep(mouseSleep)
        now = position()
        spd = ((((now.x - lastMousePos.x )**2) + ((now.y-lastMousePos.y)**2) )**0.5)/mouseSleep
        mouseRecord.append(spd)
        lastMousePos = now



tmr = threading.Thread(name='timer', target=timer)
tmr.start()
mouseTmr = threading.Thread(name='mouseTmr', target=mouseMoveTmr)
mouseTmr.start()
# desired_window_name = "微信"

# Collect events until release2312233
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

tmr.join()
mouseTmr.join()
