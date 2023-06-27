# pip install opencv-python
import cv2
import numpy as np

source = "ajit.jepg"
destination = "newImage.png"
scale_percent = 50


src = cv2.imread(source, cv2.IMREAD_UNCHANGED)


new_width = int(src.shape[1] * scale_percent /100)
new_height = int(src.shape[0] * scale_percent /100)


output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination,output)
cv2.waitKey(0)
