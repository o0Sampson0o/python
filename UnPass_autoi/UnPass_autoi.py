from pynput.keyboard import Key, Controller, Listener
import sys
import webbrowser
from decouple import config
import ast

stage = 0;

keyboard = Controller();

usernpass = ast.literal_eval(config("usernpass"));



def enter_usernpass(media):
    for key in usernpass[media]["nav"]:
        keyboard.press(key);
        keyboard.release(key);
    keyboard.type(usernpass[media]["username"]);
    keyboard.press(Key.tab);
    keyboard.release(Key.tab);
    keyboard.type(usernpass[media]["password"]);

def browse(media):
    webbrowser.open(usernpass[media]["url"]);

def press_on(key):
    return;

def press_off(key):
    global stage;
    if key == Key.backspace:
        if stage == 0:
            stage = 1;
            if sys.argv[2] == "OPEN":
                browse(sys.argv[1]);
            elif sys.argv[2] != "NOOPEN":
                return;
        elif stage == 1:
            enter_usernpass(sys.argv[1] if len(sys.argv)>1 else 0);
            sys.exit();

with Listener(on_press = press_on, on_release = press_off) as listener:
    listener.join();