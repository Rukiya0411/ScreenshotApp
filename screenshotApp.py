import pyautogui
import os
import time
import tkinter as tk

# Folder to save screenshots
screenshot_folder = os.path.join(os.getcwd(), "screenshots")

# Create folder if not exists
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# Flash effect like camera
def flash_effect():
    flash = tk.Tk()
    flash.attributes("-fullscreen", True)
    flash.configure(bg="white")
    flash.attributes("-topmost", True)
    flash.after(50, flash.destroy)
    flash.mainloop()

# Take screenshot and save with timestamp
def take_screenshot():
    flash_effect()
    timestamp = time.strftime('%y-%m-%d_%H-%M-%S')
    screenshot_path = os.path.join(screenshot_folder, f"screenshot_{timestamp}.png")
    pyautogui.screenshot(screenshot_path)
    print(f"✅ Screenshot saved at: {screenshot_path}")

# Run
take_screenshot()
