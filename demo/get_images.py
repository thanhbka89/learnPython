# -*- coding: utf-8 -*-
import os
import shutil
import urllib.request
from bs4 import BeautifulSoup
import re
import argparse

parser = argparse.ArgumentParser(description=u"Tải ảnh girl xinh :D")
parser.add_argument('--start', '-s', default=1, type=int)
parser.add_argument('--end', '-e', default=546, type=int)
parser.add_argument('--save_dir', '-d', default="ngamvnn_saved_images", type=str)
parser.add_argument('--save_file', '-f', default="img_list_file.txt", type=str)
args = parser.parse_args()

# Tạo thư mục lưu ảnh và image list file
save_folder = args.save_dir
current_path = os.path.dirname(os.path.realpath(__file__))
save_dir = os.path.join(current_path, save_folder)

#print(save_folder,current_path,save_dir)

if os.path.exists(save_dir):
    for the_file in os.listdir(save_dir):
        file_path = os.path.join(save_dir, the_file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)
else:
    os.makedirs(save_dir)
img_list_file = os.path.join(current_path, args.save_file)
try:
    os.remove(img_list_file)
except Exception as e:
    print(e)

list_file = open(img_list_file, 'w')

# Tải mã HTML và tìm thẻ img có thuộc tính src bắt đầu bằng /images/
pages_no = range(args.start, args.end, 1)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
base_url = "http://ngamvnn.com"
for page_no in pages_no:
    url = base_url + "/anh-girl?page=" + str(page_no)
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    soup = BeautifulSoup(response)
    tags = soup.findAll('img')
    for tag in tags:
        match = re.match(r'^/images/.*', tag['src'])
        if match:
            image_url = base_url + match.group()
            print(image_url)
            name = os.path.basename(image_url)  # Lấy tên file ảnh
            img_req = urllib.request.Request(image_url, headers=headers)
            try:
                data = urllib.request.urlopen(img_req).read()
                save_img = os.path.join(save_dir, name)
                output = open(save_img, 'wb')
                output.write(data)
                output.close()
                list_file.write(image_url + "\n")
            except:
                continue

list_file.close()