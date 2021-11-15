import os
import cv2
import shutil

color_folder='../vml_line_dataset/3157556/'
binary_folder='../vml_line_dataset/3157556_binary/'
shutil.rmtree(binary_folder, ignore_errors=True)
os.makedirs(binary_folder, exist_ok=True)

for img_name in os.listdir(color_folder):
    if img_name.endswith(".png"):
        img = cv2.imread(color_folder+img_name,0)
        _, binary = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
        #_, binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
        cv2.imwrite(binary_folder+img_name, binary)