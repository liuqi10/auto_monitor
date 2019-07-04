#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import requests,json
#推送钉钉消息
class AutoInfo():
    def __init__(self):
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=93970e0a1f796c7e839ff289f9d4314bd5600868d6cabd5b8ab6159bb5577f9d'
        self.headers = {
            'Content-type': 'application/json'
        }
    def send_info(self,data):
        try:
            r = requests.post(self.url, data=json.dumps(data), headers=self.headers)
        except Exception as e:
            print(e)
        r_text_datas = r.json()
        if r_text_datas['errmsg']=='ok':
            print("推送消息成功",r.json())
        else:
            print("推送消息失败")
if __name__ == '__main__':
    #推送内容
    data_text = {
        "msgtype": "text",
        "text": {
            "content": "我就是我,  @17611682976 是不一样的烟火"
        }
    }
    #推送链接
    data_link = {
        "msgtype": "link",
        "link": {
            "text": "text1",
            "title": "自定义协议",
            "messageUrl": "url连接地址",
            "picUrl": "图片URL地址"
        }
    }
    #推送图片
    data_markdown = {
     "msgtype": "markdown",
     "markdown": {
         "title":"杭州天气",
         "text":"#### 杭州天气  \n > 9度，@1825718XXXX 西北风1级，空气良89，相对温度73%\n\n > ![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n  > ###### 10点20分发布 [天气](http://www.thinkpage.cn/) "
     },
     "at": {
        "atMobiles": ["1825718XXXX"],
        "isAtAll": 'false'
     }
    }

    data = AutoInfo()
    data.send_info(data_text)