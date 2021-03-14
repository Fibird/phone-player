#!/usr/bin/env python3
import os
import time
import random
import easyocr
import cv2


def dhash(image):
    # 将图片转化为8*8
    image = cv2.resize(image, (9, 8), interpolation=cv2.INTER_CUBIC)
    # 将图片转化为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    dhash_str = ''
    for i in range(8):
        for j in range(8):
            if gray[i, j] > gray[i, j + 1]:
                dhash_str = dhash_str + '1'
            else:
                dhash_str = dhash_str + '0'
    result = ''
    for i in range(0, 64, 4):
        result += ''.join('%x' % int(dhash_str[i: i + 4], 2))
    # print("dhash值",result)
    return result


def campHash(hash1, hash2):
    n = 0
    # hash长度不同返回-1,此时不能比较
    if len(hash1) != len(hash2):
        return -1
    # 如果hash长度相同遍历长度
    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            n = n + 1
    return n


def open_gold_ingot():
    pos = '144 1019'
    adb_cmd = ('adb shell input tap ' + pos)
    a = os.system(adb_cmd)


def play_with():
    pos = '144 1019'
    adb_cmd = ('adb shell input tap ' + pos)
    a = os.system(adb_cmd)


def give_apple():
    pos = ' 771 1569'
    adb_cmd = ('adb shell input tap ' + pos)
    a = os.system(adb_cmd)


def image_if_like(img1_path, img2_path):
    img1 = cv2.imread(img1_path, cv2.IMREAD_UNCHANGED)
    hash1 = dhash(img1)
    img2 = cv2.imread(img2_path, cv2.IMREAD_UNCHANGED)
    hash2 = dhash(img2)

    return campHash(hash1, hash2) < 5


def get_time_from_img(img_path):
    reader = easyocr.Reader(['ch_sim', 'en'])  # need to run only once to load model into memory
    result = reader.readtext(img_path)
    return result


def img2gray(img_path):
    img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    ret, thresh1 = cv2.threshold(img_gray, 190, 255, cv2.THRESH_BINARY)
    cv2.imwrite('./images/img_gray.png', thresh1)


def task():
    return 0


if __name__ == '__main__':
    # print(image_if_like('./images/screen2.png', './images/screen3.png'))
    print(get_time_from_img('./images/img_gray.png'))
    #img2gray('./images/screen.png')
