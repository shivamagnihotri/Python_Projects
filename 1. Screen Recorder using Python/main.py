import cv2
from PIL import ImageGrab
import numpy as np

res = ImageGrab.grab()
width, height = res.size

format_vid = cv2.VideoWriter_fourcc("m", "p", "4", "v")
store_vid = cv2.VideoWriter("output.mp4", format_vid, 30, (width, height))

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    conv_img = np.array(img)
    final_img = cv2.cvtColor(conv_img, cv2.COLOR_BGR2RGB)
    store_vid.write(final_img)
    if cv2.waitKey(10) == ord("q"):
        break

