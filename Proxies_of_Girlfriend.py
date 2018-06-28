import requests
import json


URL = "http://openapi.tuling123.com/openapi/api/v2"
JSONDATA = {
    "perception": {"inputText": {"text": ""}},
    "userInfo": {"apiKey": "63387193886c4f4daba9bf92f000b9e6","userId": "285037"},
}
HEDADERS = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
}

def get_reponse(content):
	JSONDATA["perception"]["inputText"]["text"] = content
	try:
		response = requests.post(url = URL, headers=HEDADERS, json=JSONDATA)
		response.raise_for_status()
		response.encoding = "utf-8"
	except requests.HTTPError:
		return None
	
	return response.text

def handle_data(response):
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
	
	bot.SendTo(contact, reply)
