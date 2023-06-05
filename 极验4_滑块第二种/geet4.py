# -*- coding: utf-8 -*-
import json
import random
import time
import urllib.parse
import uuid
import execjs
import ddddocr
import requests


class Geet4():
    static_domain = "https://static.geetest.com/"
    bg_url = ""
    slice_url = ""
    lot_number = ""
    ptime = 0

    def __init__(self, captcha_id):
        # self.r 保持session
        self.r = requests.session()
        self.captcha_id = captcha_id
        self.challenge = uuid.uuid4()
        with open("./1.js") as f:
            js = f.read()
        self.js_exec = execjs.compile(js)

    def _get_nowTime(self):
        return int(time.time() * 1000)

    def One_reg(self):
        params = {
            "captcha_id": self.captcha_id,
            "challenge": self.challenge,
            "client_type": "web",
            "risk_type": "slide",
            "lang": "zh",
            "callback": "geetest_{}".format(self._get_nowTime())
        }
        url = "https://gcaptcha4.geetest.com/load"
        res = self.r.get(url, params=params).text
        res = res.replace(params["callback"], "")[1:-1]
        res_json = json.loads(res)
        self.bg_url = urllib.parse.urljoin(self.static_domain, res_json["data"]["bg"])
        self.slice_url = urllib.parse.urljoin(self.static_domain, res_json["data"]["slice"])
        self.lot_number = res_json["data"]["lot_number"]

    def get_bg_slice(self):
        bg = requests.get(self.bg_url).content
        slice = requests.get(self.slice_url).content
        # with open("./bg.jpg","wb") as f:
        #     f.write(self.bg)
        # with open("./slice.jpg","wb") as f:
        #     f.write(self.slice)
        return bg, slice

    def notch_position_x(self, bg, slice):
        det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
        res = det.slide_match(slice, bg, simple_target=True)
        return res["target"][0]

    def get_track(self, distance):
        def __ease_out_expo(sep):
            if sep == 1:
                return 1
            else:
                return 1 - pow(2, -10 * sep)

        if not isinstance(distance, int) or distance < 0:
            raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
            # 初始化轨迹列表
        slide_track = [
            [random.randint(-50, -10), random.randint(-50, -10), 0],
            [0, 0, 0],
        ]
        # 共记录count次滑块位置信息
        count = 30 + int(distance / 2)
        # 初始化滑动时间
        t = random.randint(50, 100)
        # 记录上一次滑动的距离
        _x = 0
        _y = 0
        for i in range(count):
            # 已滑动的横向距离
            x = round(__ease_out_expo(i / count) * distance)
            # 滑动过程消耗的时间
            t += random.randint(10, 20)
            if x == _x:
                continue
            slide_track.append([x, _y, t])
            _x = x
        slide_track.append(slide_track[-1])
        self.ptime = slide_track[-1][-1]
        return slide_track

    def get_w(self, distance, track):
        eee = {
            "device_id": "A59C",
            "em": "{ph: 0, cp: 0, ek: '11', wd: 1, nt: 0, sc: 0,si: 0}",
            "ep": "123",
            "geetest": "captcha",
            "lang": "zh",
            "lot_number": self.lot_number,
            "passtime": self.ptime,
            "setLeft": distance + 1,
            "userresponse": (distance + 1) / 1.0059466666666665,
            "fxy6": "143036667"
        }
        res = self.js_exec.call("get_w", eee, track)
        return res

    def ok(self, w):
        params = {
            "captcha_id": self.captcha_id,
            "challenge": self.challenge,
            "client_type": "web",
            "lot_number": self.lot_number,
            "risk_type": "slide",
            "pt": "1",
            "w": w,
            "callback": "geetest_{}".format(self._get_nowTime())

        }
        url = "https://gcaptcha4.geetest.com/verify"
        res = self.r.get(url, params=params).text
        res = res.replace(params["callback"], "")[1:-1]
        return json.loads(res)

    def main(self):
        # 初始化获取id和滑块图
        self.One_reg()
        # 访问图片获得字节集
        bg, slice = self.get_bg_slice()
        distance = self.notch_position_x(bg, slice)
        print("距离：", distance)
        track = self.get_track(distance)
        # print(track)
        w = self.get_w(distance, track)
        # print(w)
        return self.ok(w)


if __name__ == '__main__':
    sucess=0
    for i in range(100):
        geet = Geet4(captcha_id="24f56dc13c40dc4a02fd0318567caef5")
        res=geet.main()
        try:
            if res["data"]["seccode"]["pass_token"]:
                sucess+=1
                print("滑块成功")
        except KeyError:
            print("滑块失败")
        print(res)
    print('成功率',sucess/100)
