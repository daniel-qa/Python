import os,sys
import datetime
import paramiko
from dingtalkchatbot.chatbot import DingtalkChatbot

def DingMsg(msg,flag=False):

        #WebHook地址
        #webhook = 'https://oapi.dingtalk.com/robot/send?access_token=xxx'  # test
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token=xxx'   # Official

        # 初始化机器人小丁
        xiaoding = DingtalkChatbot(webhook)

        #Text消息@所有人

        if(flag==True):
                xiaoding.send_text(msg, is_at_all=True)
        else:
                xiaoding.send_text(msg, is_at_all=False)


if __name__ == '__main__':

        if(0):
                DingMsg('IES TW 上傳 Sokrates OK !')
        else:
                DingMsg("IES TW 上傳 Sokrates 失敗 !",True)
