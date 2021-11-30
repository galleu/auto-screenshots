import pyscreenshot as ImageGrab
import sys
import glob
import keyboard 
import time

def saveImage():
    filepath = sys.argv[1]

    indexs = glob.glob(filepath+"/*.png")
    name_list = []
    for i in indexs:
        i = int(i.replace("\\", "/").split("/")[-1].split(".")[0])
        name_list.append(i)
    name_list.sort()
    index = name_list[-1] + 1
    print("New Index",index)
    # part of the screen
    img=ImageGrab.grab(bbox=(369,128,1550,970))
    img.save(filepath+'/'+str(index)+'.png')
    print("Saved", index)



time.sleep(5)
while True:
    time.sleep(1)
    saveImage()
    keyboard.press_and_release('space')
    time.sleep(5)
