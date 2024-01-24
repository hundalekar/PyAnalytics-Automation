import pyautogui
import subprocess
import time

# Specify the path to the Firefox executable.
firefox_path = "firefox.exe"

# Specify the URL you want to open in Firefox.
url_to_open = ("url_link")

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

# Type the URL into the browser's address bar.
pyautogui.hotkey('ctrl', 'l')  # Focus on the address bar.
pyautogui.typewrite(url_to_open)
pyautogui.press('enter')

# Optional: Wait for a few seconds.
time.sleep(7)
pyautogui.typewrite("username")
print("username done")
pyautogui.sleep(4)
pyautogui.hotkey("tab")
pyautogui.typewrite("pass")
print("password done")
pyautogui.sleep(4)
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.sleep(3)
pyautogui.hotkey("enter")
time.sleep(4)

ImageRecognition.image_to_lookup("agree.png")
pyautogui.hotkey("enter")
print("agree done")
time.sleep(4)

# ImageRecognition.image_to_lookup("Network_Management.png",
#                                  click="left")
# ImageRecognition.image_to_lookup("Network_Management.png")
ImageRecognition.image_to_lookup("huawei 2\\net.png")
time.sleep(5)
print("net done")
pyautogui.hotkey("enter")
time.sleep(20)  # Wait for 20 seconds

ImageRecognition.image_to_lookup("resource.png")
pyautogui.hotkey("enter")
print("resource done")
time.sleep(4)
# Add the delay here if needed

ImageRecognition.image_to_lookup("physical.png")
pyautogui.hotkey("enter")
print("physical done")
time.sleep(4)

ImageRecognition.image_to_lookup("10.png", click="left")
# pyautogui.click("left")
# time.sleep(4)
# pyautogui.hotkey("enter")
# pyautogui.hotkey("enter")
print("10 done")
time.sleep(4)

ImageRecognition.image_to_lookup("100.png", click="left")
# time.sleep(3)
# pyautogui.hotkey("enter")
print("100 done")
time.sleep(4)
# x,y=pyautogui.locateOnScreen("select_all.png", confidence=0.9)
# a=x+10
# b=y+3
# pyautogui.moveTo(a,b)

# ImageRecognition.image_to_lookup("select_all.png")
# location = pyautogui.locateOnScreen("select_all.png")
x, y = pyautogui.locateCenterOnScreen("select_all.png",
                                      confidence=0.9)
a = x - 40
b = y
pyautogui.moveTo(a, b, 3)
pyautogui.click()
time.sleep(4)
print("select done")

ImageRecognition.image_to_lookup("export_all.png")
pyautogui.click()
time.sleep(4)
print("export_all done")

ImageRecognition.image_to_lookup("csv.png")
pyautogui.click()
print("csv done")
time.sleep(4)

# ImageRecognition.image_to_lookup("Physical_Inventory_1.png")
# pyautogui.hotkey("enter")
# time.sleep(4)

ImageRecognition.image_to_lookup("huawei 2\\ar.png", "left")
# ImageRecognition.image_to_lookup("huawei 2\\nm.png", "left")
# ImageRecognition.image_to_lookup("more.png")
# pyautogui.hotkey("enter")
print("ar done")
time.sleep(4)

# ImageRecognition.image_to_lookup("optical_electrical_module.png")
# pyautogui.hotkey("enter")
# time.sleep(4)
#
# #
# ImageRecognition.image_to_lookup("filter.png",click="left")
# #pyautogui.hotkey("enter")
# time.sleep(10)
#
# pyautogui.hotkey("tab")
# time.sleep(6)
# pyautogui.hotkey("enter")
# time.sleep(6)
# ImageRecognition.image_to_lookup("huawei3\\phy_root_3.png")
# pyautogui.click("left")
# time.sleep(4)
# ImageRecognition.image_to_lookup("huawei 2\\ok_2.png")
# pyautogui.hotkey("enter")
# time.sleep(4)

ImageRecognition.image_to_lookup("optical_electrical_module.png")
time.sleep(4)
pyautogui.hotkey("enter")
print("OP Module")

pyautogui.moveTo("filter.png")
time.sleep(4)
pyautogui.click()
print("filter")

pyautogui.hotkey("tab")
time.sleep(7)
pyautogui.hotkey("enter")
time.sleep(15)
print("ok")

#
ImageRecognition.image_to_lookup("huawei 2\\phy_root_3.png")
pyautogui.hotkey("enter")
time.sleep(6)
print("phy_root")

# #
ImageRecognition.image_to_lookup("huawei 2\\ok_2.png")
time.sleep(4)
pyautogui.hotkey("enter")
time.sleep(4)
print("ok1")
time.sleep(15)
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
# pyautogui.hotkey("tab")
# pyautogui.hotkey("tab")
# pyautogui.hotkey("tab")
# pyautogui.hotkey("tab")
# pyautogui.hotkey("tab")
# pyautogui.hotkey("enter")
# time.sleep(20)
# pyautogui.hotkey("tab")
# time.sleep(4)
# pyautogui.hotkey("enter")
# time.sleep(10)
# ImageRecognition.image_to_lookup("huawei3\\close.png")
# pyautogui.click("left")
# time.sleep(4)

# ImageRecognition.image_to_lookup("huawei3\\save_as.png")
# pyautogui.click("left")
time.sleep(4)
#
# pyautogui.hotkey("tab")
# pyautogui.hotkey("tab")
# pyautogui.hotkey("tab")
# pyautogui.hotkey("enter")
# time.sleep(10)
# pyautogui.hotkey("tab")
# pyautogui.hotkey("tab")
# pyautogui.hotkey("tab")
# pyautogui.hotkey("tab")
# pyautogui.hotkey("enter")
# time.sleep(10)
# pyautogui.hotkey("tab")
# pyautogui.hotkey("enter")
# time.sleep(10)
ImageRecognition.image_to_lookup("huawei3\\save_as.png")
time.sleep(4)
pyautogui.hotkey("enter")
time.sleep(4)

pyautogui.hotkey("tab")
time.sleep(4)
pyautogui.hotkey("tab")
time.sleep(4)
pyautogui.hotkey("tab")
time.sleep(4)
pyautogui.hotkey("tab")
time.sleep(4)
pyautogui.hotkey("enter")
time.sleep(4)

ImageRecognition.image_to_lookup("slot_usage_statistics.png")
pyautogui.hotkey("enter")
print("slot_usage done")
time.sleep(4)

ImageRecognition.image_to_lookup("filter.png", click="left")
# pyautogui.hotkey("enter")
print("filter done")
time.sleep(10)

# pyautogui.hotkey("tab")
# time.sleep(6)
# pyautogui.hotkey("enter")
# time.sleep(6)
ImageRecognition.image_to_lookup("huawei3\\phy_root_4.png", "left")
# ImageRecognition.image_to_lookup("huawei3\\phy_root_3.png")
# pyautogui.click("left")
time.sleep(4)
print("phy root done")

ImageRecognition.image_to_lookup("ok_1.png")
pyautogui.hotkey("enter")
time.sleep(4)
print("ok1 done")

#
# pyautogui.hotkey("tab")
# pyautogui.hotkey("tab")
# pyautogui.hotkey("tab")
# pyautogui.hotkey("tab")
# pyautogui.hotkey("tab")
# pyautogui.hotkey("enter")
# time.sleep(10)
# pyautogui.hotkey("tab")
# time.sleep(7)
# pyautogui.hotkey("enter")
# time.sleep(7)
# ImageRecognition.image_to_lookup("huawei3\\close.png")
# pyautogui.click("left")
# time.sleep(4)
ImageRecognition.image_to_lookup("sv_as.png", "left")
# ImageRecognition.image_to_lookup("huawei3\\save_as.png")
# pyautogui.click("left")
time.sleep(4)
print("save done")

pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
time.sleep(10)
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
time.sleep(20)
ImageRecognition.image_to_lookup("m_cross.png","left")
time.sleep(3)
print("m_cr done")
ImageRecognition.image_to_lookup('p_cross.png',"left")
time.sleep(4)
print("p_cr done")
print("close the inventory and more")
time.sleep(20)
####################m------------------------Huawei2------------------------------------------#########
img = ImageRecognition
#
img.image_to_lookup("resource.png")
pyautogui.hotkey("enter")
time.sleep(4)
print("resource")
img.image_to_lookup("inventory_report.png")
pyautogui.hotkey("enter")
time.sleep(4)
print("inv")

img.image_to_lookup("wdm.png")
pyautogui.hotkey("enter")
time.sleep(4)
pyautogui.scroll(-90)
time.sleep(4)
print("wdm done")

img.image_to_lookup("statistics_port_resources.png")
pyautogui.hotkey("enter")
time.sleep(4)
print("st_port done")

img.image_to_lookup("phy_root.png")
pyautogui.hotkey("enter")
time.sleep(4)
print("phy_root done")

location = pyautogui.locateCenterOnScreen("refer1.png",
                                          confidence=0.9)

if location is not None:
    x, y = location
    a = x + 100
    b = y - 10
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")

pyautogui.click()
time.sleep(4)
a = "cancel.png"
b = "activated.png"
while True:
    if a == a:
        img.image_to_lookup(a, click="none")
        print("image found")
        time.sleep(10)
    if b == b:
        img.image_to_lookup(b, click="none")
        print("process done")
        break
time.sleep(10)
print("done")
img.image_to_lookup("sav.png", click="left")
img.image_to_lookup("New folder\\all3.png", click="left")
img.image_to_lookup("New folder\\all3.png", click="left")

time.sleep(3)
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")

location = pyautogui.locateCenterOnScreen(
    "New folder\\save_options_1.png", confidence=0.9)

if location is not None:
    x, y = location
    a = x + 110
    b = y - 20
    pyautogui.moveTo(a, b, duration=3)

pyautogui.click()
time.sleep(4)
print("save done")
pyautogui.press('up', presses=2)
pyautogui.hotkey("enter")

location = pyautogui.locateCenterOnScreen("save.png",
                                          confidence=0.9)
pyautogui.hotkey("enter")

pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
time.sleep(4)
print("done")
# img.image_to_lookup("huawei 2\\activate.png", click="left")

location = pyautogui.locateCenterOnScreen(
    "huawei 2\\statistics_4cross.png",
    confidence=0.7)

if location is not None:
    x, y = location
    a = x + 160
    b = y - 9
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")
pyautogui.click()
time.sleep(5)
print("cross done")

#
# img.image_to_lookup("s.png", click="left")
# time.sleep(3)
print("4th done")

# *****************************************************************5
img.image_to_lookup("wdm\\wdm_link.png", click="left")
time.sleep(3)

img.image_to_lookup("phy_root.png")
pyautogui.hotkey("enter")
time.sleep(4)
print("done")

location = pyautogui.locateCenterOnScreen("refer1.png",
                                          confidence=0.9)

if location is not None:
    x, y = location
    a = x + 100
    b = y - 10
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")

pyautogui.click()
time.sleep(4)
print("done")
img.image_to_lookup("sav.png", click="left")
time.sleep(3)
pyautogui.hotkey("enter")
time.sleep(5)
print("done")

location = pyautogui.locateCenterOnScreen(
    "huawei 2\\WDM_5cross.png",
    confidence=0.7)

if location is not None:
    x, y = location
    a = x + 110
    b = y - 9
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")
pyautogui.click()
time.sleep(5)
print("5th done")
# ***********************************************************7
img.image_to_lookup("wdm\\bandwidth_resources.png", click="left")
time.sleep(3)
img.image_to_lookup("phy_root.png")
pyautogui.hotkey("enter")
time.sleep(4)
print("done")
location = pyautogui.locateCenterOnScreen("refer1.png",
                                          confidence=0.9)

if location is not None:
    x, y = location
    a = x + 100
    b = y - 10
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")

pyautogui.click()
time.sleep(4)
img.image_to_lookup("sav.png", click="left")
time.sleep(3)
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")

location = pyautogui.locateCenterOnScreen(
    "huawei 2\\WDM_7cross.png",
    confidence=0.7)

if location is not None:
    x, y = location
    a = x + 90
    b = y - 9
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")
pyautogui.click()
time.sleep(5)
print("7th done")
# *********************************************************8
img.image_to_lookup("wdm\\channel_resource.png", click="left")
time.sleep(3)
img.image_to_lookup("phy_root.png")
pyautogui.hotkey("enter")
time.sleep(4)
print("done")

location = pyautogui.locateCenterOnScreen("refer1.png",
                                          confidence=0.9)

if location is not None:
    x, y = location
    a = x + 100
    b = y - 10
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")

pyautogui.click()
time.sleep(4)
img.image_to_lookup("sav.png", click="left")
time.sleep(3)
pyautogui.hotkey("enter")
img.image_to_lookup("New folder\\all3.png", click="left")
img.image_to_lookup("New folder\\all3.png", click="left")

time.sleep(3)
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
time.sleep(3)

location = pyautogui.locateCenterOnScreen(
    "huawei 2\\WDM_8cross.png",
    confidence=0.7)

if location is not None:
    x, y = location
    a = x + 100
    b = y - 9
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")
pyautogui.click()
time.sleep(5)
print("8th done")
# ************************************************9

img.image_to_lookup("wdm\\wavelength.png")
time.sleep(3)

img.image_to_lookup("phy_root.png")
pyautogui.hotkey("enter")
time.sleep(4)
location = pyautogui.locateCenterOnScreen("refer1.png",
                                          confidence=0.6)

if location is not None:
    x, y = location
    a = x + 90
    b = y - 8
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")

pyautogui.click()
time.sleep(4)
# img.image_to_lookup("close.png",click="left")
# time.sleep(3)
img.image_to_lookup("sav.png", click="left")
time.sleep(3)
img.image_to_lookup("New folder\\all3.png", click="left")
img.image_to_lookup("New folder\\all3.png", click="left")
print("done")

time.sleep(3)
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
time.sleep(3)

location = pyautogui.locateCenterOnScreen(
    "huawei 2\\WDM_9cross.png",
    confidence=0.7)

if location is not None:
    x, y = location
    a = x + 115
    b = y - 9
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")
pyautogui.click()
print("done")
time.sleep(5)
print("9th done")
# ********************************************10
img.image_to_lookup("wdm\\otu.png", click="left")
time.sleep(3)

location = pyautogui.locateCenterOnScreen("refer4.png",
                                          confidence=0.6)

if location is not None:
    x, y = location
    a = x + 90
    b = y - 8
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'otu_refer.png' not found.")

pyautogui.click()
time.sleep(4)
img.image_to_lookup("close.png", click="left")
time.sleep(3)
img.image_to_lookup("sav.png", click="left")
time.sleep(3)
img.image_to_lookup("New folder\\all3.png", click="left")
img.image_to_lookup("New folder\\all3.png", click="left")

time.sleep(3)
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
time.sleep(3)

location = pyautogui.locateCenterOnScreen(
    "huawei 2\\WDM_10cross.png",
    confidence=0.7)

if location is not None:
    x, y = location
    a = x + 115
    b = y - 9
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")
pyautogui.click()
time.sleep(5)
print("10th done")
# **************************************************11
img.image_to_lookup("wdm\\optical_power.png", click="left")
time.sleep(3)
location = pyautogui.locateCenterOnScreen("refer4.png",
                                          confidence=0.6)
print("done")
if location is not None:
    x, y = location
    a = x + 90
    b = y - 8
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")

pyautogui.click()
time.sleep(4)
a = "details.png"
b = "close.png"
while True:
    if a == a:
        img.image_to_lookup(a, click="none")
        print("image found")
        time.sleep(10)
    if b == b:
        img.image_to_lookup(b)
        print("process done")
        break
time.sleep(10)
# img.image_to_lookup("close.png",click="left")
# time.sleep(3)
img.image_to_lookup("sav.png", click="left")
time.sleep(3)
img.image_to_lookup("New folder\\all3.png", click="left")
img.image_to_lookup("New folder\\all3.png", click="left")

time.sleep(3)
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
time.sleep(3)

location = pyautogui.locateCenterOnScreen(
    "huawei 2\\WDM_11cross.png",
    confidence=0.7)

if location is not None:
    x, y = location
    a = x + 190
    b = y - 9
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")
pyautogui.click()
time.sleep(5)

print("11th done")
# ***********************************************************12
img.image_to_lookup("wdm\\osu.png", click="left")
time.sleep(3)
location = pyautogui.locateCenterOnScreen("refer4.png",
                                          confidence=0.9)

if location is not None:
    x, y = location
    a = x + 90
    b = y - 8
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")

pyautogui.click()
time.sleep(5)
img.image_to_lookup("sav.png", click="left")
time.sleep(3)
pyautogui.hotkey("enter")
time.sleep(5)
location = pyautogui.locateCenterOnScreen("cross\\osu_cross.png",
                                          confidence=0.9)

if location is not None:
    x, y = location
    a = x + 70
    b = y - 10
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")

pyautogui.click()
print("th done")
# ***************************************************13
img.image_to_lookup("wdm\\tansport_ne.png", click="left")
time.sleep(3)
location = pyautogui.locateCenterOnScreen("refer4.png",
                                          confidence=0.6)

if location is not None:
    x, y = location
    a = x + 90
    b = y - 8
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")

pyautogui.click()
img.image_to_lookup("close.png", click="left")
time.sleep(3)
img.image_to_lookup("sav.png", click="left")
time.sleep(3)
img.image_to_lookup("New folder\\all3.png", click="left")
img.image_to_lookup("New folder\\all3.png", click="left")
#
time.sleep(3)
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
time.sleep(5)

# img.image_to_lookup("e.png", click="left")
# time.sleep(3)

# location = pyautogui.locateCenterOnScreen(
#     "cross\\transport_cross.png",
#     confidence=0.9)
#
# img.image_to_lookup("huawei 2\\activate.png", click="left")

location = pyautogui.locateCenterOnScreen(
    "cross\\transport_cross.png",
    confidence=0.7)

if location is not None:
    x, y = location
    a = x + 120
    b = y - 9
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")
pyautogui.click()
time.sleep(5)

pyautogui.click()
print("13th done")
# **********************************14
img.image_to_lookup("wdm\\lldp.png", click="left")
time.sleep(3)
location = pyautogui.locateCenterOnScreen("refer4.png",
                                          confidence=0.6)

if location is not None:
    x, y = location
    a = x + 90
    b = y - 8
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")

pyautogui.click()

pyautogui.hotkey("enter")
img.image_to_lookup("close.png", click="left")
time.sleep(3)
img.image_to_lookup("sav.png", click="left")
time.sleep(3)
pyautogui.hotkey("enter")

location = pyautogui.locateCenterOnScreen(
    "huawei 2\\WDM_14cross.png",
    confidence=0.7)

if location is not None:
    x, y = location
    a = x + 75
    b = y - 9
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'refer.png' not found.")
pyautogui.click()
time.sleep(5)
print("14th done")

###############-----------------------------Huawei3---------------------###########
img.image_to_lookup("huawei3\\monitor.png")
pyautogui.hotkey("enter")
time.sleep(4)

img.image_to_lookup("huawei3\\wdm_performance.png")
pyautogui.hotkey("enter")
time.sleep(4)

img.image_to_lookup("huawei3\\phy_root_3.png")
pyautogui.hotkey("enter")
time.sleep(4)

location = pyautogui.locateCenterOnScreen("huawei3\\refer5.png",
                                          confidence=0.9)

if location is not None:
    x, y = location
    a = x + 90
    b = y - 10
    pyautogui.moveTo(a, b, duration=3)
else:
    print("Image 'huawei3_refer.png' not found.")

pyautogui.click()
time.sleep(6)

img.image_to_lookup("huawei3\\select_none.png")
pyautogui.hotkey("enter")
time.sleep(4)

img.image_to_lookup("huawei3\\transmitted_optical_power.png")
pyautogui.hotkey("enter")
time.sleep(4)

img.image_to_lookup('query.png', "left")
# pyautogui.hotkey("enter")
time.sleep(4)

img.image_to_lookup("yes.png")
pyautogui.hotkey("enter")
time.sleep(4)

img.image_to_lookup("huawei3\\close.png")
pyautogui.hotkey("enter")
time.sleep(4)

img.image_to_lookup("huawei3\\save_as.png")
pyautogui.hotkey("enter")
time.sleep(4)
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")

pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")

img.image_to_lookup("huawei3\\download.png")
pyautogui.hotkey("enter")
time.sleep(4)

img.image_to_lookup("huawei3\\select_none.png")
pyautogui.hotkey("enter")
time.sleep(4)

img.image_to_lookup("huawei3\\recieved_optical_power.png")
pyautogui.hotkey("enter")
time.sleep(4)

img.image_to_lookup("huawei3\\save_as.png")
pyautogui.hotkey("enter")
time.sleep(4)
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")

pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")

# ImageRecognition.image_to_lookup("save.png")
# pyautogui.hotkey("enter")
# time.sleep(4)
