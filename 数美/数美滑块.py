# -*- coding: utf-8 -*-
import base64
import json
import random
import time
import urllib.parse
import cv2

from pyDes import des, ECB
import numpy as np
import requests


class shumei:
    domain_url="https://castatic.fengkongcloud.cn/"
    bg_url=""
    fg_url=""
    rid=""
    bg=None
    fg=None
    def __init__(self):
        self.r=requests.session()

    def get_captcha(self,organization):
        url="https://captcha.fengkongcloud.cn/ca/v1/register"
        param={
            "rversion": "1.0.3",
            "sdkver": "1.1.3",
            "data": "{}",
            "callback": "sm_"+str(int(time.time()*1000)),
            "organization": organization,
            "model": "slide",
            "lang":"zh-cn",
            "appId": "default",
            "channel": "DEFAULT"
        }
        response=self.r.get(url,params=param)
        try:
            if response.status_code==200:
                sm_json=json.loads(response.text[17:-1])
                bg=sm_json["detail"]["bg"]
                fg=sm_json["detail"]["fg"]
                self.bg_url=urllib.parse.urljoin(self.domain_url,bg)
                self.fg_url=urllib.parse.urljoin(self.domain_url,fg)
                self.rid=sm_json["detail"]["rid"]
                # print(param,"params")
                # print(response.text,"请求")

        except:
            print(response.text)
            print("未知失败，自己验证")

    #访问背景前景页面
    def _visit_bg_fg(self):
        try:
            self.bg=self.r.get(self.bg_url).content
            self.fg=self.r.get(self.fg_url).content
            with open("a.png","wb") as f:
                f.write(self.r.get(self.bg_url).content)
            with open("b.png","wb") as f:
                f.write(self.r.get(self.fg_url).content)

            return True
        except:
            print("获取前景背景图片失败")
            return None
    def get_distance(self):
        if self._visit_bg_fg() is None:
            return
        # with open('a.png', 'rb') as f:
        #     background_bytes = f.read()
        #
        # with open('b.png', 'rb') as f:
        #     target_bytes = f.read()
        # res = det.slide_match(self.fg, self.bg)
        # # 获取的图片是600像素 但验证是300 所以除以二
        # print(res)
        # return int(res["target"][0])

        target = cv2.imdecode(np.asarray(bytearray(self.fg), dtype=np.uint8), 0)
        template = cv2.imdecode(np.asarray(bytearray(self.bg), dtype=np.uint8), 0)
        result = cv2.matchTemplate(target, template, cv2.TM_CCORR_NORMED)
        _, distance = np.unravel_index(result.argmax(), result.shape)
        return distance

    def pad(self,b):
        """
        块填充
        """
        block_size = 8
        while len(b) % block_size:
            b += b'\0'
        return b
    def getEncryptContent(self,a, b):
        # js = execjs.compile(self.js_code)
        #
        # print(a,b,js.call("getEncryptContent", a, b))
        # return js.call("getEncryptContent", a, b)
        des_obj = des(b.encode(), mode=ECB)
        content = self.pad(str(a).replace(' ', '').encode())
        return base64.b64encode(des_obj.encrypt(content)).decode('utf-8')

    def get_trajectory(self,distance):
        ge = []
        y = 0
        v = 0
        t = 1
        current = 0
        mid = distance * 3 / 4
        exceed = 20
        z = t

        ge.append([0, 0, 1])

        while current < (distance + exceed):
            if current < mid / 2:
                a = 15
            elif current < mid:
                a = 20
            else:
                a = -30
            a /= 2
            v0 = v
            s = v0 * t + 0.5 * a * (t * t)
            current += int(s)
            v = v0 + a * t

            y += random.randint(-5, 5)
            z += 100 + random.randint(0, 10)

            ge.append([min(current, (distance + exceed)), y, z])

        while exceed > 0:
            exceed -= random.randint(0, 5)
            y += random.randint(-5, 5)
            z += 100 + random.randint(0, 10)
            ge.append([min(current, (distance + exceed)), y, z])
        # print(ge)
        return ge

        # return "{}".format(ge).replace(" ", ""), ge[-1][2]
        # return "{}".format(ge).replace(" ", "")

    def ok(self,tq,ub,zs,organization):
        url="https://captcha.fengkongcloud.cn/ca/v2/fverify"
        params={
            "sdkver": "1.1.3",
            "cn": "4gX7HfzFoIE=",
            "je": "J95iyFR+B34=",
            "rid": self.rid,
            "vm": "kRSb3H6Sr+M=",
            "zj": "YXtzSGH4Kx4=",
            "protocol": "148",
            "act.os": "web_pc",
            "tq": tq,
            "ox": "ixh0fmsqQqE=",
            "tb": "jbIXAuW9ClU=",
            "organization": organization,
            "fp": "ePjf+CsNviw=",
            "ub": ub,
            "rr": "yYCBEY0C7PQ=",
            "ostype": "web",
            "rversion": "1.0.3",
            "zs":zs,
            "callback": "sm_1646734280304"
           }
        res=self.r.get(url,params=params)
        print(res.text)
        if json.loads(res.text[17:-1])["riskLevel"]=="PASS":
            return True

    def main(self,organization="RlokQwRlVjUrTUlkIqOg"):
        self.get_captcha(organization)
        #distance距离
        distance = self.get_distance()
        print(distance,"距离")
        # tq加密的滑动距离
        tq=self.getEncryptContent(distance/600,"c78a7666")
        #ub滑动时间
        ub=self.getEncryptContent(random.randint(2001,4999),"eb994a6b")
        #zs滑动轨迹
        trajectory=self.get_trajectory(distance/2)
        # print(trajectory)
        zs=self.getEncryptContent(trajectory,"201cab4a")
        if self.ok(tq,ub,zs,organization):
            return self.rid



sm=shumei()
requestId=sm.main(organization="xQsKB7v2qSFLFxnvmjdO")
if requestId  is not None:
    print("滑块成功")
    # url="http://jpebook.ly.com/suppliersharing/Account/Login"
    # headers={
    #     "Host": "jpebook.ly.com",
    #     "Connection": "keep-alive",
    #     "Accept": "application/json, text/plain, */*",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    #     "Content-Type": "application/json;charset=UTF-8",
    #     "Origin": "http://jpebook.ly.com",
    #     "Referer": "http://jpebook.ly.com/suppliersharing/Account/Login?ReturnUrl=%2Fsuppliersharing",
    #     "Accept-Language": "zh-CN,zh;q=0.9"
    # }
    # data={"type":0,"loginName":"你是黑脸怪","password":"8ae252facf16cf0b0d8677bb3f889d33","checkPassword":"","validCode":"","codeResponse":requestId,"codeType":"sm"}
    # res=requests.post(url=url,json=data,headers=headers)
    # print(res.text)
else:
    print("滑块失败，重来一次吧")

# print(distance,get_random(distance))

