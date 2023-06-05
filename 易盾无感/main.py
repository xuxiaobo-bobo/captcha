import requests
import execjs
import re
import json

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.zyhxjh.com/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
with open("enc.js",mode="r",encoding="utf-8") as f:
            jscode = f.read()
ctx = execjs.compile(jscode)
session = requests.session()



def getToken():
        
    params = {
        'referer': 'https://www.zyhxjh.com/#/login',
        'zoneId': 'CN31',
        'id': 'a32a66b67ede4b7f8f47e6d4822d3259',
        'fp': 'GHNf+laPsJ\3WTv7jwnzhzOr1N9VaUwh3aZ\\RjX26VHXtaZ\BMnWBKdCyLy3GAGX8VaOAS\alq/t3lZwOl/JHtwchokQf/BiZLgIooND+HRVZVPl5IT921XjdMP9gaasKQYBBlv4HCsTRTcnaxY9xv8zAKZR+zfyILxrsnm8Zpidjny:1681042660574',
        'https': 'true',
        'type': 'undefined',
        'width': '',
        'sizeType': 'undefined',
        'version': '2.21.4',
        'dpr': '1.25',
        'dev': '1',
        'cb': 'FaYKx5wouyjmFWQOsiBgDz0H5aUccsjWpy6ulCL8Onz4CfeFhGXq8cPBHCwX850a',
        'acToken': '9ca17ae2e6fecda16ae2e6eeb5cb528ab69db8ea65bcaeaf9ad05b9c94a3a3c434898987d2b25ef4b2a983bb2af0feacc3b92ae2f4ee95a132e29aa3b1cd72abae8cd1d44eb0b7bb82f55bb08fa3afd437fffeb3', # 不確定是否長期有效
        'ipv6': 'false',
        'runEnv': '10',
        'group': '',
        'scene': '',
        'sdkVersion': 'undefined',
        'smsVersion': 'v2',
        'callback': '__JSONP_bifn4ay_0',
    }

    fp = ctx.call("get_fp")
    cb = ctx.call("get_cb")
    params['cb'] = cb
    params['fp'] = fp


    response = session.get('https://c.dun.163.com/api/v3/get', params=params, headers=headers)
    regx = re.compile(r".*?\((?P<dic>.*?)\)",re.S)
    jdata = json.loads(regx.search(response.text).group("dic"))['data']

    token = jdata['token']
    return token


# 易盾無感
def check(token):
    params = {
        'referer': 'https://www.zyhxjh.com/#/login',
        'zoneId': 'CN31',
        'id': 'a32a66b67ede4b7f8f47e6d4822d3259',
        'version': '2.21.4',
        'cb': '',
        'extraData': '',
        'bf': '0',
        'runEnv': '10',
        'sdkVersion': 'undefined',
        'token': '7ace297b5b7046e7a17431caee0f73a8',
        'type': '5',
        'width': '240',
        'data': '{"d":"","m":"JJpIGrgk7n8SVcke+4YFXp33","p":"DfXrtzsFqwijA5jrIp1MIt+lnwRXgC6XmgDXJc33","ext":"idBTGPWdIuRtnUxXQP8zv1w15AZ3"}',
        'callback': '__JSONP_wd68u86_3',
    }

    params['token'] = token
    params['data'] = ctx.call("_getData2",token)
    params['cb'] = ctx.call("get_cb") # cb 可以與前面相同/不同

    response = session.get('https://c.dun.163.com/api/v3/check', params=params, headers=headers)
    print(response.text)


if __name__ == "__main__":
       token = getToken()
       check(token)