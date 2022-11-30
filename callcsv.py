import os
import csv

png_list = os.listdir('/media/rastech/T71/event_data_20221102/rosbag2_2022_11_02-13_22_34_E/camera')
os.path.splitext(png_list)[0]
print(png_list)


