import requests
import re
import json
import execjs
import cv2
import numpy as np
import random

captcha_id = '24f56dc13c40dc4a02fd0318567caef5' # 要根據不同網站來改

class Geetest():
    def __init__(self) -> None:
        self.sess = requests.session()
        with open("main.js",mode="r",encoding="utf-8") as f:
            jscode = f.read()
        self.ctx = execjs.compile(jscode)
        pass

    def run(self):
        initInfo = self.getSlideInit()
        loc_x = self.getVerifyLocationX(initInfo['data'])
        tracks = self.build_tracks(loc_x)
        self.verify(loc_x,tracks,initInfo['data'])


    def getSlideInit(self):
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Referer': 'https://www.geetest.com/',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'captcha_id': captcha_id, 
            # 'challenge': '80191920-8a98-4520-bc54-df989fe5a2b5',
            'client_type': 'web',
            'risk_type': 'slide',
            'lang': 'zh',
            'callback': 'geetest_1681309323439',
        }

        response = self.sess.get('https://gcaptcha4.geetest.com/load', params=params, headers=headers)
        regx = re.compile(r"geetest_.*?\((?P<data>.*)\)")
        data = regx.search(response.text).group('data')
        return json.loads(data)

    def getVerifyLocationX(self,data):
        bg = requests.get(f"https://static.geetest.com/"+data['bg']).content
        bg_arr = np.asarray(bytearray(bg),dtype=np.uint8)
        bg_img = cv2.imdecode(bg_arr,-1)

        front = requests.get(f"https://static.geetest.com/"+data['slice']).content
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

    def verify(self,x,tracks,data):
        # x: 缺口x座標
        w = self.ctx.call("get_w",x,tracks,data)

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': 'gt_captcha_v4_user=5226998c519348cfb93480d099a00193; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221879e83c4f2504-0e251547d93b35-26031b51-1327104-1879e83c4f37bd%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.geetest.com%2Fadaptive-captcha-demo%22%7D%2C%22%24device_id%22%3A%221879e83c4f2504-0e251547d93b35-26031b51-1327104-1879e83c4f37bd%22%7D; Hm_lvt_25b04a5e7a64668b9b88e2711fb5f0c4=1681991649; language=zh; Hm_lpvt_25b04a5e7a64668b9b88e2711fb5f0c4=1682002364',
            'Pragma': 'no-cache',
            'Referer': 'https://www.geetest.com/',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'callback': 'geetest_1682004074403',
            'captcha_id': captcha_id,
            'client_type': 'web',
            'lot_number': data['lot_number'],
            'risk_type': 'slide',
            'payload': data['payload'],
            'process_token': data['process_token'],
            'payload_protocol': data['payload_protocol'],
            'pt': data['pt'],
            'w': w,
        }
        resp = self.sess.get('https://gcaptcha4.geetest.com/verify', params=params, headers=headers)

        print(resp.text)

if __name__ == '__main__':
    geet = Geetest()
    geet.run()