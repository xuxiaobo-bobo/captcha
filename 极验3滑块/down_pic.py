# -*- coding: utf-8 -*-
# @Time    : 2022/6/1 10:30
# @Author  : xiaobo
# @Site    : 
# @File    : down_pic.py
# @Software: PyCharm
import json
import time

import requests
import urllib.request

def get_chall_gt(sess):
    headers = {
        "authority": "www.geetest.com",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://www.geetest.com/demo/slide-float.html",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.40 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    sess.headers = headers
    url = "https://www.geetest.com/demo/gt/register-slide"
    params = {
        "t": int(time.time() * 1000)
    }
    response = sess.get(url, headers=headers, params=params).json()
    print(response)
    # get_php()
    return response


def get_php(res_chall_gt, sess):
    headers = {
        # "Host": "apiv6.geetest.com",
        # "Connection": "keep-alive",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.40 Safari/537.36",
        "sec-ch-ua-platform": "\"Windows\"",
        # "Accept": "*/*",
        # "Sec-Fetch-Site": "same-site",
        # "Sec-Fetch-Mode": "no-cors",
        # "Sec-Fetch-Dest": "script",
        # "Referer": "https://www.geetest.com/",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "GeeTestUser=d0f290c60ff46c8308097fc8e8ea1459"
    }
    sess.headers = headers

    url = "https://apiv6.geetest.com/get.php"
    params = {
        "gt": "019924a82c70bb123aae90d483087f94",
        "challenge": res_chall_gt['challenge'],
        "lang": "zh-cn",
        "pt": "0",
        "client_type": "web",
        "w": "A3HF(MKLkgJ5I3)5PW3Itdt0gglu8cs75N0wnyQZTktFj(EzyPIDhOQ8Qsl7DqSBy8AiRry(hsnzN)6uUXl9eECrhpxAS9AiCr40drGCjlgul(38Cj0oxtnDlxzpZZH4HZIrzgUSqneLkdiNg46osZmGhz4)7sToym)Rmwjvb2ASIkszDAUX(r80LOsegrPaWsIS5nUyEnWMlUDkGTA4CRy)7TyHxkYpWDT87P8cUMv(qX)FhA3PtMT)JrG1flESJSP7Eq7SHE66RmrvesBIth9nIrW3fCaIqzXxQ9N6V(s4xLLAyBRF(SgkR093bzj191aBKpYLQSYNwHLLkls3RuGFCfrfpoe6(XaEHhv9vpOM3g0yJPqo5aX2QCTiWC775wl(CyY1Qh8xKvcA(Wml7kSS(SFWQD7mq7Eg6YO2HSapD)CyltwymUbsDsM1WyStENQRxVgooZ6bvMN0r20n2LdoBEMUIVz4gk)gMVHScfmXXoTDbq5pB6z9EOzZTPRUEIWw6F4f4SE3SbcpD0qQEzwrtkgFpf5UANBXhYqxJIB0vG4JaaqS0jiXwDOSHeCwW1b1y0TJbpN7iwPJQBZPyG(lvTM5eODIuYLo9zOPBIP04VPp94v0I3LJF84v93S4FOr5s764RQEwV530LUYE7vbW(aeb29XCn7b2kEVDiQfnlF(Xs4AtFnK6eYO5(cD36bCw1H)5ptBSpfgRpzf7bIRD6jlX0qsaOHFEEwcI)2k6iG064YBgvFiylaAxmDGehnZ19c309YmLxpRljXlXoEx)DsOMBX9NirSc94KEpcNLZcAtBdwnUf04FuVnxDZdn29zs87rHuPRHwazF04pLrGX)4cqgwKOsvooDzyvQFrNJahJPzBB3IbbZRDjoVGCoJpfSIzP7pDMaVS1ExN8rXHDH)C0H5u2MxbcuUEMhaAT9zJIqaQsbcBGgWRMh17TGP5LBZ8ADNiE7)9Vz8KaSxYZYvD1(PzsB2HTiKesyLyx3eN31UsjfyOU85z4y8UbaFt5j0yjVaOxKPdBrJK496yYEc3brY2VeHlX1YaxSnZkXIpBVVoFVLM3DVty0b(hH2Ubtlidcv6HrtSMbDNU2PNhytTVWKEaB0kU23967K1h9DM4wEQw5ZW6AFnJ6oXWnfq3tzTWTFByL3F6ZJo7sVvqW6in0ijtALK6ndHePz534tKpIfsX3FbX0JxqvbjLo6RZoVkCoVvcn5(jf9we48sZF8wOZWdaAYudeav4Ii0Kap6Vgy6ttG0oNB3f3lpTI2RHbndi8Bpzmx80n2dIfwOtx3S(o6zBq)3jzO2UdCxnrUscTb)2uPophLZgDKNwX1cF6lXf)0WsSRlArMnzEnABAHBQ7be0ULoXiYQpPlHUTAN72x9nCsz3AxfXj2nWHCHgqgmOvu)ohlaq8JRr08YvTl)fePuooslJgfHvTVlgSOG)24y2KvmMljYMf)Kv5Aw)fs9)NLV6Nije27UG73(hYuNwC8GetewzoNYVY9B7A6evOW8GWl8x2kbV(WXAhWDq7tnNtn)LDfZrpi5aIBH8yoPtzUcJdz92C5zowBisWM68vWInfpcmF3voXEWE3eLGgqJ(7YCT1oQ5nUGk8WaVlC9A7KDrC0eg7yU)5A8bTotrXTL8ofLLFpS70tVJmtSGv3CusYXjULTyHJcw4ZwJ8Z1tLVMwZphNnfiWgVmUdVmE7K(7pZIEdizj(aBcnsx53LruFJFT6T9Hu6Dny1DYXdANW(x3GT6gfRMtozDH)V7OY98cPDgM7GRMFzD6DvJA7LSMnUKAn(5U0szViHc9aWEPUZCR6xg8fQw)ognrTBvC2Rz1akEjF7fBrHXAbcRIQ67Om64sgWv1MxNudF)zEdUuUAfJfvotlS39ZhF92ET2OTE2sTgm(SnKFboUcVMMipLiImYKADBnBW5KuVyxsLhuvOwbtGorxxEPIrzAoSlCPGKEAILk)uS4lNtOgI3re2ftWX9L5jazND)w7noeSfp7b(L3UrUXpyHyNy345TGZ(S83MUdBmY6zKDUYnyHlXw0)4mC7p(43xsbb3rPSbSFFXiN39lfs7twkCsk.17497f2c2e7be7382505daaaaea6f3b28cd3b568626c8a0294f8b8f05ebdf29457819e41746711777c5b2b273df2030f32e47f72717d940d6c26f5cafbd9b62b13244efcdcf51ec1d03bd9c7bff66cc208fb6e15d245b052852c3f82cad1cb25c4e64595cc33d95dae90c6fc6ab58413693f8a1d64f1143d804edf34342adffb",
        "callback": f"geetest_{int(time.time() * 1000)}"
    }
    response = sess.get(url, headers=headers, params=params).text[22:-1]

    c,s=json.loads(response)['data']['c'],json.loads(response)['data']['s']

    return c,s

def get_ajax_php(res_chall_gt, sess):
    headers = {
        "Host": "api.geetest.com",
        "Connection": "keep-alive",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.40 Safari/537.36",
        "sec-ch-ua-platform": "\"Windows\"",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Dest": "script",
        "Referer": "https://www.geetest.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "GeeTestAjaxUser=c02c2c61d4eb11ea629cbff0a07b19df; GeeTestUser=ec59f466abfb8dc5a76b9e35c44273ae"
    }
    params = {
        "gt": "019924a82c70bb123aae90d483087f94",
        "challenge": res_chall_gt['challenge'],
        "lang": "zh-cn",
        "pt": "0",
        "client_type": "web",
        'w': '',
        "callback": f"geetest_{int(time.time() * 1000)}"
    }
    sess.headers = headers
    url = 'https://api.geetest.com/ajax.php?'
    print(sess.get(url=url, params=params).text)


def getpic(res_chall_gt, sess):
    headers = {
        # "Host": "api.geetest.com",
        # "Connection": "keep-alive",
        # "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
        # "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.40 Safari/537.36",
        # "sec-ch-ua-platform": "\"Windows\"",
        # "Accept": "*/*",
        # "Sec-Fetch-Site": "same-site",
        # "Sec-Fetch-Mode": "no-cors",
        # "Sec-Fetch-Dest": "script",
        # "Referer": "https://www.geetest.com/",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "GeeTestAjaxUser=c02c2c61d4eb11ea629cbff0a07b19df; GeeTestUser=ec59f466abfb8dc5a76b9e35c44273ae"
    }
    sess.headers = headers

    url = "https://api.geetest.com/get.php?"
    params = {
        "is_next": "true",
        "type": "slide3",
        "gt": "019924a82c70bb123aae90d483087f94",
        "challenge": res_chall_gt['challenge'],
        "lang": "zh-cn",
        "https": "true",
        "protocol": "https://",
        "offline": "false",
        "product": "embed",
        "api_server": "api.geetest.com",
        "isPC": "true",
        "autoReset": "true",
        "width": "100%",
        "callback": f"geetest_{int(time.time() * 1000)}"
    }
    response = sess.get(url, headers=headers, params=params).text[22:-1]
    print(json.loads(response))
    challenge=json.loads(response)['challenge']
    s_=json.loads(response)['s']
    bg=json.loads(response)['bg']
    fullbg=json.loads(response)['fullbg']
    slice=json.loads(response)['slice']
    urllib.request.urlretrieve('http://static.geetest.com/'+bg,'bg.jpg')
    urllib.request.urlretrieve('http://static.geetest.com/'+fullbg,'fullbg.jpg')
    urllib.request.urlretrieve('http://static.geetest.com/'+slice,'slice.jpg')
    return challenge,s_


if __name__ == '__main__':
    sess = requests.session()

    res_chall_gt = get_chall_gt(sess)  #获取challenge,以及gt

    c,s=get_php(res_chall_gt, sess)  #获取s以及c的值

    get_ajax_php(res_chall_gt, sess)

    getpic(res_chall_gt, sess)   #获取图片信息
