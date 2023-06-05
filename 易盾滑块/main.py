import requests
import execjs
import re
import json
import cv2
import numpy as np
import random


class dun163():
    def __init__(self) -> None:
        with open("enc.js",mode="r",encoding="utf-8") as f:
            jscode = f.read()
        self.ctx = execjs.compile(jscode)

        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Referer': 'https://dun.163.com/',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        self.sess = requests.session()
        self.cb = ""
    def run(self):

        verifyInfo = self.getVerifyImg()
        loc_x = self.getVerifyImgLocationX(verifyInfo)
        track_arr = self.build_tracks(loc_x)
        _data = self.ctx.call("get_data",track_arr,verifyInfo["token"],loc_x)
        self.checkCode(verifyInfo['token'],_data,self.cb)
        

    
    def getVerifyImg(self):
        params = {
            'referer': 'https://dun.163.com/trial/jigsaw',
            'zoneId': 'CN31',
            'acToken': '',
            'id': '07e2387ab53a4d6f930b8d9a9be71bdf',
            'fp': 'CJaGvGNcJp\\XmBSLHdVtqc6nsmUjKuHg\\3xxhiGs4U5obw7tzuZ/h6dg8dtESJaGu13Z43\\qgUHHK5YQtPd6M/QGn7/zuQ1VxKLUPpeVMe/2UbaVLTdw9q2b8w784wW4R+qipx+x1S0HzaR4k09Y6hKdQDKk9808zmr8WN1uTrz7KBv2:1680618143464',
            'https': 'true',
            'type': '2',
            'version': '2.21.3',
            'dpr': '1.25',
            'dev': '1',
            'cb': 'fz+UhOn8RyxEg\\KlHIoIPlP\\NzqL5ucIQWQl+b7u9Z7Jl\\4t8pt/FZ9/15kUNmXN',
            'ipv6': 'false',
            'runEnv': '10',
            'group': '',
            'scene': '',
            'lang': 'zh-CN',
            'sdkVersion': 'undefined',
            'width': '320',
            'audio': 'false',
            'sizeType': '10',
            'smsVersion': 'v2',
            'token': '',
            'callback': '__JSONP_7k6jiz0_0',
        }
        params['fp'] = self.ctx.call("get_fp")
        params['cb'] = self.ctx.call("get_cb")
        self.cb = params['cb']
        response = self.sess.get('https://c.dun.163.com/api/v3/get', params = params, headers = self.headers)
        regx = re.compile(r".*?\((?P<dic>.*?)\)",re.S)
        jdata = json.loads(regx.search(response.text).group("dic"))['data']
        return {
            'bg':jdata['bg'][0],
            'front':jdata['front'][0],
            'token':jdata['token']
        }
    
    def getVerifyImgLocationX(self,verifyInfo):
        bg = requests.get(verifyInfo['bg']).content
        with open("bg.jpg",mode="wb") as f:
            f.write(bg)
        bg_arr = np.asarray(bytearray(bg),dtype=np.uint8)
        bg_img = cv2.imdecode(bg_arr,-1)

        front = requests.get(verifyInfo['front']).content
        front_arr = np.asarray(bytearray(front),dtype=np.uint8)
        front_img = cv2.imdecode(front_arr,-1)

        loc_x = self.identify_gap(bg_img,front_img)
        return loc_x

    def identify_gap(self,bg,tp,out=""):
        ''' 識別滑塊缺口位置,返回x坐標
            bg: 背景图片
            tp: 缺口图片
            out:输出图片
        '''
        # 读取背景图片和缺口图片
        bg_img = bg # 背景图片
        tp_img = tp # 缺口图片
        
        # 识别图片边缘
        bg_edge = cv2.Canny(bg_img, 100, 200)
        tp_edge = cv2.Canny(tp_img, 100, 200)
        
        # 转换图片格式
        bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
        tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)
        
        # 缺口匹配
        res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) # 寻找最优匹配
        
        # 绘制方框
        th, tw = tp_pic.shape[:2] 
        tl = max_loc # 左上角点的坐标
        br = (tl[0]+tw,tl[1]+th) # 右下角点的坐标
        # cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2) # 绘制矩形
        # cv2.imwrite(out, bg_img) # 保存在本地
        
        # 返回缺口的X坐标
        return tl[0]

    def build_tracks(self,target):
        '''自定義的軌跡方程
        Args:
            target: 目標水平位置
        '''

        track_res = []

        x = 4
        y = 0
        t = 46
        track_res.append([x,y,t])
        while x < target:
            x = x + random.randint(1,4)
            if x > target:
                x = target
            if len(track_res) % 30 == 0:
                y = y - 1
            t = t + random.randint(8,10)
            track_res.append([x,y,t])
        
        return track_res

    def checkCode(self,token,data,cb):
        params = {
            'referer': 'https://dun.163.com/trial/jigsaw',
            'zoneId': 'CN31',
            'id': '07e2387ab53a4d6f930b8d9a9be71bdf',
            'token': token,
            'acToken': 'undefined',
            'data': '{"d":"QSX9uO911ZlbyxTHyBlR/Ydu9GSVj4lQ9lgI4z8eL1QO1Ly1m58ODys0gNvHJqnUoUfGB\\\\Ls5pDHp6iY8AL987GnTkBYdNjqSVODNbtw97PqFRpLnAL6m7uo4HM5SvlkLluNtfuejxj3","m":"","p":"zkmpOtobmURbSGvK1EbMEgI6bOGjDKqP","ext":"phktVx2iKUW/k8W9aUp/ji/p1ka3"}',
            'width': '320',
            'type': '2',
            'version': '2.21.3',
            'cb': 'lL1ebHabbB7Ay67cu\\gP/ErHOc7GcA8Ax7tNJcQ5EnaxXV6mnrhnyzt/bePQ9uEJ',
            'extraData': '',
            'bf': '0',
            'runEnv': '10',
            'sdkVersion': 'undefined',
            'callback': '__JSONP_ik2ginl_1',
        }
        params['data'] = data
        params['cb'] = cb
        
        response = self.sess.get('https://c.dun.163.com/api/v3/check', params=params, headers=self.headers)
        print(response.text)






if __name__ == "__main__":
    dun = dun163()
    dun.run()
