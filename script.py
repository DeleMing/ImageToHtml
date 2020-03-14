# encoding:utf-8
import os
import chardet
import json
import socket
import re
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_file_name(file_dir):
    """
    获取所有文件名并生成html标签
    :param file_dir:
    :return:
    """
    for root, dirs, files in os.walk(file_dir):
        pass
    string = ''
    temp = ''
    for i in files:
        temp = '<div class="large-4 columns"><img src="./img/'+i.decode("gb2312").encode('utf-8')+'"><p align="center">'+i.decode("gb2312").encode('utf-8')+'</p> </div>'
        string = temp + string
    return string


def read_file(file_name):
    """
    读取文件
    :param file_name:
    :return:
    """
    string = ''
    with open(file_name, 'r') as f:
        i = f.read()
        string += i
    f.close()
    return i


def html_string(image_dir):
    """

    :param image_dir:图片路径
    :return:
    """
    string = get_file_name(image_dir)
    return string


def write_file(atuo_file_name, result):
    """
    自动生成文件
    :param atuo_file_name:
    :return:
    """
    f = open(atuo_file_name, 'w')
    f.write(result)
    f.close()


if __name__ == '__main__':
	# 此处为图片路径，当img更改时，get_file_name里的路径也需要更改
    image_dir = 'C:/Users/X1 Carbon/Desktop/index/img'
    # 此处为生成的文件目录，需要与图片路径同级
    atuo_file_name = 'C:/Users/X1 Carbon/Desktop/index/index.html'
    pre = read_file('pre.html')
    suf = read_file('suf.html')
    string = html_string(image_dir)
    result = pre + suf + string
    write_file(atuo_file_name, result)




