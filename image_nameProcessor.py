import PIL.Image
import os

class image_nameProcessor():

    def process(self, directory):  # directory use raw string if path include '\', e.g. process(r'.\targetpath')

        t_path = os.listdir(directory)  # os.listdir() can pick up both rel and abs path

        for file in t_path:
            f_path = os.path.join(directory, file)
            if os.path.isfile(f_path):
                r, ext = os.path.splitext(f_path)
                if ext == ".png" or ext == ".jpg":
                    img = PIL.Image.open(f_path)
                    img_w, img_h = img.size
                    cropimg_w = min(img_w, img_h)
                    crop_region = (img_w - cropimg_w)//2, (img_h - cropimg_w)//2, (img_w + cropimg_w)//2, (img_h + cropimg_w)//2
                    img_Cropped = img.crop(crop_region)
                    img_Cropped = img_Cropped.convert("L")
                    img_Cropped = img_Cropped.resize((512, 512), resample=1)  # resize with Resampling mode set to Nearest
                    img_Cropped.save(r + '_Cropped' + ext, None, quality=100)

        pass


'''
python version ：3.8
pillow version ：8.0 （ 支持 python 版本 3.6 - 3.9 ）

基于Python PIL（Python Image Library）制作一个小程序：
1、该类能处理一个文件夹下的所有jpg/png图片，并将处理后的文件在原文件名的后缀中加上 '_cropped'，
保存到原文件夹下。

2、处理要求：
 a:将图片居中裁切成正方形
 b:将裁切后的图片统一分辨率在512*512
 c.将图片转换为灰度图

3、独立完成此作业（十分重要）。

4、测试代码：
from image_nameProcessor import *
a1 = image_nameProcessor()
#开始绝对路径测试
print('>>> absolute path test <<<')
a1.process('D:/Desktop/Python/Resource')
#开始相对路径测试
print('>>> relative path test <<<')
a1.process('./Resource')

4、测试图片文件在Resource文件中

基本要求：
提交python代码文件名为image_nameProcessor.py、测试代码、测试视频
image_nameProcessor.py中包函一个class，类名为image_nameProcessor，image_nameProcessor类中包含方法 
process(self, directory)，按上文要求处理一个指定的文件夹，支持绝对路径和相对路径；

'''