import pyautogui
import pyautogui as pg
import subprocess
import time
import datetime

# import os
# import paramiko
# from datetime import date

# import cv2
# opening the application
firefox_path = "firefox.exe"

# Specify the URL you want to open in Firefox.
url_to_open = "url_link"

try:
    # Open Firefox using subprocess.
    subprocess.Popen(firefox_path)
    print("Opened the Firefox application")
except Exception as e:
    print("An unrecognized mistake occurred while opening Firefox")

# Wait for Firefox to open.
time.sleep(5)


class ImageRecognition:
    @staticmethod
    def image_to_lookup(image_path, click="left"):
        while True:
            try:
                location = pyautogui.locateOnScreen(image_path)
                if location:
                    x, y, width, height = location
                    center_x = x + width // 2
                    center_y = y + height // 2
                    pyautogui.moveTo(center_x, center_y)
                    if click == "left":
                        pyautogui.click(center_x, center_y)
                    elif click == "right":
                        pyautogui.rightClick(center_x, center_y)
                    elif click == "double":
                        pyautogui.doubleClick(center_x, center_y)
                    elif click == "backspace":
                        pyautogui.press("Backspace")
                    elif click == "none":
                        while True:
                            location = pyautogui.locateOnScreen(image_path)
                            if location is not None:
                                break
                    return
            except pyautogui.ImageNotFoundException:
                pass


# Search for an image.
ImageRecognition.image_to_lookup("g_search.png")
time.sleep(5)
# Type the URL into the browser's address bar.
pyautogui.hotkey('ctrl', 'l')  # Focus on the address bar.
pyautogui.typewrite(url_to_open)
time.sleep(5)
pyautogui.press('enter')
time.sleep(5)

img = ImageRecognition
# level3 part--------------------------------------------------------------------
pg.sleep(4)
pg.typewrite("username")
pg.sleep(4)
pg.hotkey("tab")
pg.typewrite("pass")
pg.sleep(5)
# pg.hotkey("enter")
# img.image_to_lookup("login.png", click="left")
# time.sleep(1)
pg.hotkey("tab")
time.sleep(3)
pg.hotkey("enter")
time.sleep(4)
img.image_to_lookup("dt.png", click="left")
time.sleep(12)
img.image_to_lookup('new\\report.png', click="left")
time.sleep(3)
img.image_to_lookup("inventory.png", click="left")
time.sleep(6)
img.image_to_lookup("new\\cv.png", "left")
time.sleep(4)
img.image_to_lookup("new\\dt.png", click="left")
time.sleep(6)
img.image_to_lookup("inventory_report.png", click="left")
time.sleep(3)
img.image_to_lookup("new\\inventory_report.png", click="left")
time.sleep(6)
img.image_to_lookup("new\\custom.png", click="left")
time.sleep(6)
pg.hotkey("tab")
current_datetime = datetime.datetime.now()
# today = date.today()
# formatted_date = "{:02d}{:02d}{:02d}".format(today.day, today.month, today.year % 100)
formatted_date = current_datetime.strftime("%d%m%y")
file_name = "Tej2_Inv_{}".format(formatted_date)
pg.typewrite(file_name, interval=0.3)
time.sleep(7)
pg.hotkey("tab")
pg.typewrite("ip")
time.sleep(4)
pg.hotkey("tab")
pg.typewrite("ems")
time.sleep(4)
pg.hotkey("tab")
pg.typewrite("iltwat")
time.sleep(4)
pg.hotkey("tab")
pg.typewrite("/home/ems")
time.sleep(4)
img.image_to_lookup("new\\check.png", click="left")
time.sleep(3)
# hold ctrl-----------------------------------
pyautogui.keyDown('ctrl')
img.image_to_lookup('new\\ptn.png', click="left")
time.sleep(3)
img.image_to_lookup('new\\ptn2.png', click="left")
time.sleep(3)
pyautogui.keyUp('ctrl')
# -------------------------------------------------
pg.scroll(-340)
# pg.hotkey("")
img.image_to_lookup('new\\gen.png', "left")
pg.scroll(340)
time.sleep(3)
img.image_to_lookup('new\\ok.png')
time.sleep(4)
img.image_to_lookup('new\\notification.png', "left")
time.sleep(3)
# ------------------------------------------------------------------
img.image_to_lookup('new\\report.png', click="left")
time.sleep(3)
img.image_to_lookup("backup.png", click="left")
time.sleep(6)
img.image_to_lookup("dt.png", click="left")
time.sleep(3)
img.image_to_lookup("new\\cv.png", "left")
time.sleep(4)
img.image_to_lookup("new\\dt.png", click="left")
time.sleep(6)
img.image_to_lookup("inventory_report.png", click="left")
time.sleep(3)
img.image_to_lookup("new\\inventory_report.png", click="left")
time.sleep(6)
img.image_to_lookup("new\\custom.png", click="left")
time.sleep(6)
pg.hotkey("tab")
current_datetime = datetime.datetime.now()
# today = date.today()
# formatted_date = "{:02d}{:02d}{:02d}".format(today.day, today.month, today.year % 100)
formatted_date = current_datetime.strftime("%d%m%y")
file_name = "Tej2_NEB_{}".format(formatted_date)
pg.typewrite(file_name, interval=0.3)
time.sleep(7)
pg.hotkey("tab")
pg.typewrite("ip")
time.sleep(4)
pg.hotkey("tab")
pg.typewrite("ems")
time.sleep(4)
pg.hotkey("tab")
pg.typewrite("iltwat")
time.sleep(4)
pg.hotkey("tab")
pg.typewrite("/home/ems")
time.sleep(4)
img.image_to_lookup("new\\check.png", click="left")
time.sleep(3)
# hold ctrl-------------------
pyautogui.keyDown('ctrl')
img.image_to_lookup('new\\ptn.png', click="left")
time.sleep(3)
img.image_to_lookup('new\\ptn2.png', click="left")
time.sleep(3)
pyautogui.keyUp('ctrl')
pg.scroll(-340)
# ---------------------------------------------
# pg.hotkey("")
img.image_to_lookup('new\\gen.png', "left")
pg.scroll(340)
time.sleep(3)
img.image_to_lookup('new\\ok.png')
time.sleep(4)
img.image_to_lookup('new\\notification.png', "left")
time.sleep(10)
# -----------------------------------------------------------------
img.image_to_lookup('new\\report.png', click="left")
time.sleep(3)
img.image_to_lookup("allnms.png", click="left")
time.sleep(3)
img.image_to_lookup('new\\alarm.png', click="left")
time.sleep(3)
img.image_to_lookup('new\\nodes.png', click="left")
time.sleep(3)
img.image_to_lookup('new\\browse.png', click="left")
time.sleep(3)
img.image_to_lookup('new\\var.png', click="left")
time.sleep(3)
img.image_to_lookup('new\\plus.png', click="left")
time.sleep(3)
img.image_to_lookup('new\\nms.png', click="left")
time.sleep(3)
img.image_to_lookup('new\\apply.png', click="left")
time.sleep(3)
img.image_to_lookup('new\\apply2.png', click="left")
time.sleep(25)
img.image_to_lookup('new\\cr.png', click="left")
time.sleep(3)
# mj report part-----------------------------
# img.image_to_lookup("home.png", click="left")
# time.sleep(3)
# img.image_to_lookup("manage.png", click="left")
# time.sleep(3)
# img.image_to_lookup("hun.png", click="left")
# time.sleep(3)
# img.image_to_lookup("fivhu.png", click="left")
# time.sleep(3)
# img.image_to_lookup("report1.png", click="left")
# time.sleep(3)
# img.image_to_lookup("sucsv.png", click="left")
# time.sleep(3)
#
# exit code-------------------------------------------------------------
img.image_to_lookup('new\\exit.png', click="left")
time.sleep(3)
img.image_to_lookup('new\\ok1.png', click="left")
time.sleep(3)
img.image_to_lookup('new\\cross.png', click="left")
time.sleep(3)
