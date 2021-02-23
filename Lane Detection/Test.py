import numpy as np
import cv2
import picamera
import PIL
from PIL import Image
import time



def main():

    # initialization
    camera = picamera.PiCamera(resolution=(640,480), framerate=15)
    time.sleep(2)
    image = np.empty((480 * 640 * 3), dtype=np.uint8)

    # capture an image
    camera.capture(image, 'bgr', use_video_port=True,)

    # process image for lane det
    image = image.reshape((480, 640, 3))

    # store image
    cv2.imwrite('Lane Detection/img.png', image)

    





if __name__ == "__main__":
    main()
