import glob
import os
import cv2
import shutil

import matplotlib.pyplot as plt

upload_folder = './input'
resize_folder = './resize'

if os.path.isdir(resize_folder):
    shutil.rmtree(resize_folder)
os.mkdir(resize_folder)

input = sorted(glob.glob(os.path.join(upload_folder, '*')))
if os.path.isdir(resize_folder):
    shutil.rmtree(resize_folder)
os.mkdir(resize_folder)

for i in input:
  img = cv2.imread(i)
  height,width=img.shape[:2]
  if height > width:
    img = cv2.resize(img, (0, 0), fx=min(1280/height,720/width), fy=min(1280/height,720/width))
  else:
    img = cv2.resize(img, (0, 0), fx=min(720/height,1280/width), fy=min(720/height,1280/width))

cv2.imwrite(resize_folder+"/"+i.split("\\")[-1],img)