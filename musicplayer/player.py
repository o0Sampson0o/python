import multiprocessing
from playsound import playsound
from pynput import keyboard
from pynput.keyboard import KeyCode
import os
from mutagen.mp3 import MP3
from threading import Timer

path = "C:/Users/User/everything/audio/music/"

loop_mode = 1


def quit():
    global t
    t.cancel()
    if process_now == 'p':
        p.terminate()
    else:
        q.terminate()
    os._exit(0)


def dothings():
    global loop_mode, music_now, list_length, music_list
    command = input(":::")
    if command == "QUIT":
        quit()
    elif command == "LOOP":
        mode = input("   :::")
        if mode == "LIST":
            loop_mode = 1
            print("Looping music list")
        elif mode == "SINGLE":
            loop_mode = 0
            print("Looping this music")
        else:
            print("Unknown command")
    elif command == "OPEN":
        os.system("start "+path)
    elif command == "PLAY":
        for (i, name) in enumerate(music_list):
            print(i, name)
        mode = input("   :::")
        mode = int(mode)
        music_now = mode - 1
        music_now = mode - 1 if music_now > 0 else list_length-1
        nextSong(True)


def printOutput():
    global music_now, duration
    d = round(duration)

    os.system("cls")
    print()
    print("now playing: ", music_list[music_now])
    print(f"{(d//3600):02d}h : {(d//60 % 60):02d}m : {(d%60):02d}s")


def nextSong(force=False):
    global music_now, process_now, p, q, list_length, duration, t
    if (loop_mode == 1 or force):
        music_now = music_now+1 if music_now < list_length-1 else 0

    audio = MP3(path + music_list[music_now])
    audio_info = audio.info
    duration = audio_info.length

    if process_now == 'p':
        p.terminate()

        q = multiprocessing.Process(target=playsound, args=(
            path + music_list[music_now],))
        q.start()
        process_now = 'q'
    else:
        q.terminate()

        p = multiprocessing.Process(target=playsound, args=(
            path + music_list[music_now],))
        p.start()
        process_now = 'p'

    t.cancel()
    t = Timer(duration, nextSong)
    t.start()

    printOutput()


def on_press(key):
    global p_pressed, music_now, process_now, p, q, list_length, duration, t
    if (key == KeyCode.from_char('p') or key == KeyCode.from_char('P')):
        p_pressed = True
    elif (p_pressed and (key == keyboard.Key.esc)):
        quit()
    elif (p_pressed and (key == keyboard.Key.right or key == keyboard.Key.left)):
        if (key == keyboard.Key.right):
            nextSong(force=True)
        else:
            music_now = music_now - \
                2 if music_now > 1 else (
                    list_length-1 if music_now == 1 else list_length-2)
            nextSong(force=True)


def on_release(key):
    global p_pressed
    if (key == KeyCode.from_char('p') or key == KeyCode.from_char('P')):
        p_pressed = False


if __name__ == "__main__":
    music_list = os.listdir(path)
    list_length = len(music_list)
    music_now = 0
    audio = MP3(path + music_list[music_now])
    audio_info = audio.info
    duration = audio_info.length

    p_pressed = False

    process_now = 'p'

    t = Timer(duration, nextSong)

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)

    printOutput()

    p = multiprocessing.Process(
        target=playsound, args=(path + music_list[0],))
    p.start()

    t.start()

    listener.start()
    while (True):
        dothings()
