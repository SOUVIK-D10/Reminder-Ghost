import time
import tkinter as tk
import win32gui
import win32con
import win32console
import win32com.client as wincom

def make_click_through(window_handle):
    """Uses pywin32 to make the window completely transparent to mouse clicks."""
    styles = win32gui.GetWindowLong(window_handle, win32con.GWL_EXSTYLE)
    new_styles = styles | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
    win32gui.SetWindowLong(window_handle, win32con.GWL_EXSTYLE, new_styles)

def hide_console():
    """Hides the black command prompt window immediately using pywin32."""
    console_window = win32console.GetConsoleWindow()
    if console_window:
        win32gui.ShowWindow(console_window, win32con.SW_HIDE)

def show_overlay():
    hide_console()
    root = tk.Tk()
    root.title("Water Overlay")
    root.attributes("-topmost", True)
    root.overrideredirect(True)
    chroma_key_color = "#abcdef"
    root.attributes("-transparentcolor", chroma_key_color)
    root.config(bg=chroma_key_color)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 800
    window_height = 150
    x = (screen_width // 2) - (window_width // 2)
    y = 100
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    label = tk.Label(
        root, 
        text="💧 DRINK WATER NOW! 💧", 
        font=("Impact", 48, "bold"), 
        fg="#00E5FF", 
        bg=chroma_key_color
    )
    label.pack(expand=True)
    root.update()
    hwnd = win32gui.FindWindow(None, "Water Overlay")
    make_click_through(hwnd)
    root.after(5000, root.destroy)
    root.mainloop()
def speak_reminder():
    global speaker
    speaker.Speak("Warning. You have been coding for one hour. Drink water or you will be dehydrated! ",1)

def main_loop():
    while True:
        speak_reminder()
        show_overlay()
        time.sleep(600)

if __name__ == "__main__":
    speaker = wincom.Dispatch("SAPI.SpVoice")
    speaker.Rate=1
    speaker.Volume=100
    speaker.Voice = speaker.GetVoices().Item(0)
    main_loop()