from time import sleep
from win32gui import GetWindowText, GetForegroundWindow
from time import time
from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as mouseListener
from pyautogui import position
import threading

timeGap = 30
mouseSleep = 0.1
timerOn = True
movement_key = ["'a'", "'w'", "'s'", "'d'", "'e'", "'q'", "'z'", "'A'", "'W'", "'S'", "'D'", "'E'", "'Q'", "'Z'", Key.ctrl_l, Key.shift]
log = {'movement': 0, 'useless': 0, 'begin_time':time()}
start = time()
mouseRecord = []
lastMousePos = position()

filename = 'cheat.log'


def on_press(key):
    # print('{0} pressed'.format(key))zzz
    # print(key)
    pass


def on_release(key):
    global log
    global timerOn
    print('{0} release'.format(key))
    if (str(key) in movement_key) or (key in movement_key):
        log['movement']+=1
    else:
        log['useless']+=1
    # if key == Key.esc:
    #     # Stop listener
    #     timerOn = False
    #     return False

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    # if not pressed:
    #     # Stop listener
    #     return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))


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
        f = open(filename, 'a')
        f.write(str(log) + '\n')
        f.close()
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
        # on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# with mouseListener(
#         # on_move=on_move,
#         on_click=on_click) as anotherlistener:
#     anotherlistener.join()

tmr.join()
mouseTmr.join()
