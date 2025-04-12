import tkinter as tk
from tkinter import ttk
from pynput import keyboard
from pynput.keyboard import Controller
import asyncio
import threading
import time

macro_thread = None
running_macro = False
keyboard_controller = Controller()
current_keybind_pressed = False

keys_pressed = set()

def run_macro_loop(value):
    global running_macro
    running_macro = True
    while running_macro and current_keybind_pressed:
        if value == "ZQSD":
            macro_zqsd()
        elif value == "ZDSQ":
            macro_zdsq()
        elif value == "DSQZ (PENCHER)":
            macro_dsqz_pencher()
        elif value == "ZQSD (PENCHER)":
            macro_zqsd_pencher()

def on_press(key):
    global macro_thread, current_keybind_pressed
    try:
        if activer_var.get() == 1:
            keys_pressed.add(key.char)
            keybind = keybind_entry.get().lower()
            if key.char == keybind and not running_macro:
                current_keybind_pressed = True
                value = macro_var.get()
                macro_thread = threading.Thread(target=run_macro_loop, args=(value,))
                macro_thread.start()
    except AttributeError:
        pass

def on_release(key):
    global running_macro, current_keybind_pressed
    try:
        keys_pressed.discard(key.char)
        keybind = keybind_entry.get().lower()
        if key.char == keybind:
            running_macro = False
            current_keybind_pressed = False
    except AttributeError:
        pass

def exit_app():
    root.destroy()

def macro_zqsd():
    ms = f"0.0{int(slider.get())}"
    keyboard_controller.press('z')
    time.sleep(float(ms))
    keyboard_controller.release('z')
    keyboard_controller.press('q')
    time.sleep(float(ms))
    keyboard_controller.release('q')
    keyboard_controller.press('s')
    time.sleep(float(ms))
    keyboard_controller.release('s')
    keyboard_controller.press('d')
    time.sleep(float(ms))
    keyboard_controller.release('d')

def macro_zdsq():
    ms = f"0.0{int(slider.get())}"
    keyboard_controller.press('z')
    time.sleep(float(ms))
    keyboard_controller.release('z')
    keyboard_controller.press('d')
    time.sleep(float(ms))
    keyboard_controller.release('d')
    keyboard_controller.press('s')
    time.sleep(float(ms))
    keyboard_controller.release('s')
    keyboard_controller.press('q')
    time.sleep(float(ms))
    keyboard_controller.release('q')

def macro_dsqz_pencher():
    ms = f"0.0{int(slider.get())}"
    keyboard_controller.press('z')
    time.sleep(float(ms))
    keyboard_controller.release('z')
    keyboard_controller.press('s')
    time.sleep(float(ms))
    keyboard_controller.release('s')
    keyboard_controller.press('q')
    time.sleep(float(ms))
    keyboard_controller.release('q')
    keyboard_controller.press('z')
    time.sleep(float(ms))
    keyboard_controller.release('z')

def macro_zqsd_pencher():
    ms = f"0.0{int(slider.get())}"
    keyboard_controller.press('z')
    time.sleep(float(ms))
    keyboard_controller.release('z')
    keyboard_controller.press('q')
    time.sleep(float(ms))
    keyboard_controller.release('q')
    keyboard_controller.press('s')
    time.sleep(float(ms))
    keyboard_controller.release('s')
    keyboard_controller.press('d')
    time.sleep(float(ms))
    keyboard_controller.release('d')

root = tk.Tk()
root.title("MACRO FiveM")
root.geometry("300x400")
root.configure(bg="black")
tk.Label(root, text="FiveM Macro Strafe \\ by scolaptre", fg="olive drab", bg="black", font=("Arial", 12, "bold")).pack(pady=10)
activer_var = tk.BooleanVar()
tk.Checkbutton(root, text="Activer la macro", variable=activer_var, fg="white", bg="black", selectcolor="black").pack(anchor="w", padx=20)
tk.Label(root, text="Choisissez la macro :", fg="white", bg="black").pack(anchor="w", padx=20, pady=(10, 0))
macro_var = tk.StringVar()
macros = [("ZQSD", "ZQSD"), ("ZDSQ", "ZDSQ"), ("DSQZ (PENCHER)", "DSQZ (PENCHER)"), ("ZQSD (PENCHER)", "ZQSD (PENCHER)")]

for text, value in macros:
    tk.Radiobutton(root, text=text, variable=macro_var, value=value,
                   fg="white", bg="black", selectcolor="black").pack(anchor="w", padx=40)

tk.Label(root, text="Keybind Strafe :", fg="white", bg="black").pack(anchor="w", padx=20, pady=(10, 0))
keybind_entry = tk.Entry(root, width=5)
keybind_entry.pack(anchor="w", padx=40)
tk.Label(root, text="Delay Strafe (ms):", fg="white", bg="black").pack(anchor="w", padx=20, pady=(10, 0))
delay_var = tk.IntVar(value=40)
slider = tk.Scale(root, from_=20, to=80, orient="horizontal", variable=delay_var, bg="black", fg="white", highlightthickness=0)
slider.pack(anchor="w", padx=40)
delay_label = tk.Label(root, textvariable=delay_var, fg="white", bg="black")
delay_label.pack(anchor="w", padx=40)
tk.Button(root, text="Exit", command=exit_app).pack(pady=10)

def start_listener():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

async def start_rec():
    start_listener()

asyncio.run(start_rec())
root.mainloop()
