import pyautogui

print("=== Screenshot Tool ===")

screenshot = pyautogui.screenshot()

screenshot.save("my_screenshot.png")

print("Screenshot saved ✅")