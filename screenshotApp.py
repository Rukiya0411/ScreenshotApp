import pyautogui
import os
import time
import tkinter as tk

# Define the path for saving screenshots
screenshot_folder = os.path.join(os.getcwd(), "screenshots")

# Create the folder if it doesn't exist
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# Function to display a white flash on the screen
def flash_effect():
    flash = tk.Tk()
    flash.attributes("-fullscreen", True)
    flash.configure(bg="white")
    flash.attributes("-topmost", True)
    flash.after(50, flash.destroy)  # Flash duration (50 milliseconds)
    flash.mainloop()

# Function to take a screenshot
def take_screenshot():
    flash_effect()  # Show flash before screenshot
    time.sleep(0.1)  # Small delay to avoid capturing the flash
    timestamp = time.strftime('%y-%m-%d_%H-%M-%S')
    screenshot_path = os.path.join(screenshot_folder, f"screenshot_{timestamp}.png")
    pyautogui.screenshot(screenshot_path)
    print(f" Screenshot saved at: {screenshot_path}")

# Run the screenshot function
if __name__ == "__main__":
    take_screenshot()
