# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 11:12
# @Author  : DannyDong
# @File    : wxrobot.py
# @describe: 初试微信机器

from wxpy import *
import json
import requests
from jieba import *


# 初试图灵机器人
def auto_ai(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "***"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "***"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return "[机智的小南瓜[机智]]" + result["text"]


bot = Bot(cache_path=True)  # 实现微信扫码登录，并且缓存信息
print('AI小南瓜已上线')


# 自动接受好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friend(msg):
    if '天王盖地虎' in msg.text.lower():
        new_friend = bot.accept_friend(msg.card)
        new_friend.send('[AI小南瓜]你好啊~')


# 监听微信信息并回复
@bot.register(chats=[Friend])
def my_friend_message(msg):
    print('[接收]' + str(msg))
    if msg.type != 'Text':
        ret = '[得意][得意]'
    else:
        ret = auto_ai(msg.text)
    print('[发送]' + str(ret))

    # 将手机上的信息置为已读
    bot.auto_mark_as_read = True

    return ret


# 打印所有好友
friends = bot.friends()
# # 遍历所有好友
# for friend in friends:
#     print(friend)

# 统计
print(friends.stats_text())

# '''
#  制作词云，未完成
# '''

# 获取所有公众号
public = bot.mps()
# for mp in public:
#     print(mp)

# 获取所有群聊
groups = bot.groups()

# 进程不结束
embed()


