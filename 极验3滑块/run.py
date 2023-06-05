# -*- coding: utf-8 -*-
# @Time    : 2022/6/2 12:09
# @Author  : xiaobo
# @Site    : 
# @File    : run.py
# @Software: PyCharm


import os
import subprocess
import time

import execjs
import requests
import down_pic
import picsestore
import gapsidentified
import slider
import json
import sys
# sys.setdefaultencoding('utf8')
def downloadpic():
    """图片下载"""
    sess = requests.session()

    res_chall_gt = down_pic.get_chall_gt(sess)  # 获取challenge,以及gt

    c, s = down_pic.get_php(res_chall_gt, sess)  # 获取s以及c的值

    down_pic.get_ajax_php(res_chall_gt, sess)

    pic_chall_gt, s_ = down_pic.getpic(res_chall_gt, sess)  # 获取图片信息

    return c, s_, pic_chall_gt


def pic_reset():
    """图片还原"""
    picsestore.parse_bg_captcha("bg.jpg", im_show=True, save_path='bg1.jpg')


def gap():
    """缺口识别"""
    return gapsidentified.get_distance(
        bg='bg1.jpg',
        tp='slice.jpg',
        im_show=False,
        save_path='./assets/bg.jpg'
    )


def _slider(slider_):
    """滑块轨迹"""
    _list = []
    for _ in slider.get_slide_track(slider_):
        _list.append(_)
    return _list


def getw(c, s_, g, gt, pic_chall_gt, passtime, jl):
    """读取js文件,获取加密值"""
    jscode = open('w.js', 'r', encoding='utf-8').read()
    ctx = execjs.compile(jscode)
    # print(jscode)
    arguments = [c, s_, g, gt, pic_chall_gt, passtime, jl]
    print(arguments)

    res = ctx.call('getw', arguments)
    return res


def getres(w, pic_chall_gt):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://www.geetest.com/",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.40 Safari/537.36",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "GeeTestAjaxUser": "c02c2c61d4eb11ea629cbff0a07b19df",
        "GeeTestUser": "ec59f466abfb8dc5a76b9e35c44273ae"
    }
    url = "https://api.geetest.com/ajax.php"
    params = {
        "gt": '019924a82c70bb123aae90d483087f94',
        "challenge": pic_chall_gt,
        "lang": "zh-cn",
        "%24_BBF": "0",
        "client_type": "web",
        'w': w,
        "callback": f"geetest_{int(time.time() * 1000)}"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params).text[22:-1]
    print('response-----', response)


if __name__ == '__main__':
    # sucesslist=[]
    # for i in range(100):
    c, s_, pic_chall_gt = downloadpic()  # 下载图片
    pic_reset()  # 图片还原
    slider_ = gap()

    g = _slider(slider_)
    g_list = []
    for i in g:
        g_list.append(i[0])

    jl = (g_list[-1])

    w = getw(c, s_, g, '019924a82c70bb123aae90d483087f94', pic_chall_gt, g[-1][2], jl)

    getres(w, pic_chall_gt)
