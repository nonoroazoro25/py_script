import exifread
from PIL import Image
from PIL import ExifTags
import csv
import os
import json

path = r"G:\at_kml_2\1\02"
files = os.listdir(path)
exifData = {}
row_data = []

# 取出照片GPS信息
for file in files:
    if not os.path.isdir(file):
        try:
            file_path = os.path.join(path, file)
            photo_name = os.path.basename(file_path).split(".")[0]
            img = Image.open(file_path)
            exifDataRaw = img._getexif()
            for tag, value in exifDataRaw.items():
                decodedTag = ExifTags.TAGS.get(tag, tag)
                exifData[decodedTag] = value
                # 存储GPS信息
                if decodedTag is not "GPSInfo":
                    continue
                row_data.append(exifData["GPSInfo"])
        except:
            print("photo error!")

# 生成CSV文件并写入
res_list = []
for data in row_data:
    res_list.append({"E": str(data[4][0]), "N": str(data[2][0]), "H": str(data[6])})

with open('gg.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for item in res_list:
        writer.writerow([item['E'], item['N'], item['H']])

# # 生成JSON文件并写入
# res_list = {}
# i = 0
# for data in row_data:
#     res_list.update({"name" + str(i): {"E": str(data[4][0]), "N": str(data[2][0]), "H": str(data[6])}})
#     i += 1

# data_str = str(res_list)
# with open("c.json", "w") as file:
#     file.write(data_str.replace("\'", "\""))
