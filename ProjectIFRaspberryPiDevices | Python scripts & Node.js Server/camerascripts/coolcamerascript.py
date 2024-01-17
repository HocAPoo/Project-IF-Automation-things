from picamera import PiCamera
import time
from gpiozero import Button
import os
import shutil
camera = PiCamera()
camera.resolution = (600, 450)
camera.framerate = 15
camera.rotation = 0
camera.brightness = 65
camera.start_preview()
button = Button(14)
i=1
j=1
#folder_path = '/home/pi/PiGpioProgram/PiVid'
folder_path = '/var/www/html/PiVid1'

if os.path.exists(folder_path):
    
    
    shutil.rmtree(folder_path)
    print("folder removed")
        

print(folder_path)
os.mkdir(folder_path)
        

while True:
    camera.capture(folder_path + '/image.jpg')
    time.sleep(1)
    os.rename(folder_path + '/image.jpg', folder_path + '/backup_image.jpg')
    

    if button.is_pressed:
        #os.remove(folder_path + '/image.jpg')
        os.remove(folder_path + '/backup_image.jpg')
        print('I got pushed :D')
        os.rmdir(folder_path)
        break
camera.stop_preview()
