import time
import picamera
import subprocess
import os
from gpiozero import Button
# Configuration

mac_mini_ip = '192.168.1.100'
mac_mini_username = 'hocvuu'
mac_mini_password = 'HocADoo'
remote_directory = '/usr/local/var/www/raspi_photos'
image_filename = "image.jpg"

button = Button(14)
def capture_image():
    with picamera.PiCamera() as camera:
        camera.resolution = (600, 450)
        camera.brightness = 57
        camera.capture(image_filename)
        print(f"Image {image_filename} captured")
        return image_filename

def rename_remote_image(remote_filename):
    ssh_command = [
        'sshpass', '-p', mac_mini_password, 'ssh',
        f"{mac_mini_username}@{mac_mini_ip}",
        f"mv {remote_filename} {remote_directory}/backup.jpg"
    ]
    subprocess.run(ssh_command)
    print(f"Remote image {remote_filename} renamed")

def main():
    while True:
        image_filename = capture_image()
        remote_filename = os.path.join(remote_directory, os.path.basename(image_filename))
        
        scp_command = [
            'sshpass', '-p', mac_mini_password, 'scp', image_filename,
            f"{mac_mini_username}@{mac_mini_ip}:{remote_directory}"
        ]
        subprocess.run(scp_command)
        print(f"Image {image_filename} sent")

        time.sleep(1)  # Wait for 1 second

        rename_remote_image(remote_filename)
        os.remove(image_filename)
        print(f"Image {image_filename} renamed to backup.jpg")
        if button.is_pressed:
            break

if __name__ == "__main__":
    main()



