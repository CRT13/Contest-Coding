""" Python3: Skew correction for OCR images """
import numpy as np
import cv2
import argparse

# Receive I/P image
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to input image file")
args = vars(ap.parse_args())
img = cv2.imread(args["image"])
# Convert to grayscale, then invert background-foreground
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)
cv2.namedWindow("Bin",cv2.WINDOW_NORMAL)
cv2.imshow("Bin",gray)

# Binarize the image
_,img_bimodal = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# Isolate text-regions using min-bounding rectangle
coordinates = np.column_stack(np.where(img_bimodal > 0))
angle = cv2.minAreaRect(coordinates)[-1]

if angle < -45:
    angle = -(90+angle)
else:
    angle = -angle
# Rotate the image and deskew it
(h,w) = img.shape[:2]
center = (w//2,h//2)
M = cv2.getRotationMatrix2D(center,angle,1.0)
rotated = cv2.warpAffine(img,M,(w,h),flags=cv2.INTER_CUBIC,borderMode=cv2.BORDER_REPLICATE)
# Specify the rotation-angle for physical validation
cv2.putText(rotated,"Angle:{:.2f} degrees".format(angle),(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
# Display O/P image
print("[INFO] angle: {:.3f}".format(angle))
cv2.namedWindow("Input",cv2.WINDOW_NORMAL)
cv2.namedWindow("Rotated",cv2.WINDOW_NORMAL)
cv2.imshow("Input",img)
cv2.imshow("Rotated",img)
cv2.waitKey(0)