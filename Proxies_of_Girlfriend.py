import requests
import json


# 图灵机器人web api v2.0接口
URL = "http://openapi.tuling123.com/openapi/api/v2"
# 构建向图灵机器人post的json数据
JSONDATA = {
    "perception": {"inputText": {"text": ""}},
    "userInfo": {"apiKey": "633871********92f000b9e6","userId": "28***7"},
}
# 请求头，我认为可以不需要加，但习惯了
HEDADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
}

def get_reponse(content):
    """
    向图灵机器人发送对方聊天信息，并且获取响应
    """
    # 动态添加聊天内容
    JSONDATA["perception"]["inputText"]["text"] = content
    try:
        response = requests.post(url = URL, headers=HEDADERS, json=JSONDATA)
        response.raise_for_status()
        response.encoding = "utf-8"
    except requests.HTTPError:
        return None
    
    return response.text

def handle_data(response):
    """
    处理图灵机器人的返回信息，获取回复文本
    """
    try:
        reply = response["results"][0]["values"]["text"]
    except:
        reply = "提取回复消息失败"
    finally:
        return reply

def onQQMessage(bot, contact, member, content):
    
    response = get_reponse(content)
    if not response:
        reply = "向图灵请求数据失败"
    else:
        reply = handle_data(json.loads(response))
    
    # 发送消息
    bot.SendTo(contact, reply)
