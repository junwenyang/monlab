import requests
import json
import sys

class DingDing():
    def __init__(self, webhook):
        self.webhook = webhook
        self.session = requests.session()
        self.session.headers = {"Content-Type": "application/json;charset=utf-8"}
 
    def Send_Text_Msg(self, Content: str, atMobiles: list = [], isAtAll: bool = False) -> dict:
        try:
            data = {
                "msgtype": "text",
                "text": {
                    "content": Content
                },
                "at": {
                    "atMobiles": atMobiles,
                    "isAtAll": isAtAll
                }
            }
            response = self.session.post(self.webhook, data=json.dumps(data))
            if response.status_code == '200':
                result = {"status": True, "message": "Message has been sent"}
                return result
            else:
                return response.text
        except Exception as error:
            result = {"status": False, "message": f"Failed to send message,Error stack:{error}"}
            return result
 
    def Send_Link_Msg(self, Content: str, Title: str, MsgUrl: str, PicUrl: str = ''):
        try:
            data = {
                "msgtype": "link",
                "link": {
                    "text": Content,
                    "title": Title,
                    "picUrl": PicUrl,
                    "messageUrl": MsgUrl
                }
            }
            response = self.session.post(self.webhook, data=json.dumps(data))
            if response.status_code == '200':
                result = {"status": True, "message": "Message has been sent"}
                return result
            else:
                return response.text
        except Exception as error:
            result = {"status": False, "message": f"Failed to send message,Error stack:{error}"}
            return result
 
    def Send_MardDown_Msg(self, Content: str, Title: str, atMobiles: list = [], isAtAll: bool = False):
        try:
            data = {
                "msgtype": "markdown",
                "markdown": {
                    "title": Title,
                    "text": Content
                },
                "at": {
                    "atMobiles": atMobiles,
                    "isAtAll": isAtAll
                }
            }
            response = self.session.post(self.webhook, data=json.dumps(data))
            if response.status_code == '200':
                result = {"status": True, "message": "Message has been sent"}
                return result
            else:
                return response.text
        except Exception as error:
            result = {"status": False, "message": f"Failed to send message,Error stack:{error}"}
            return result



if __name__ == "__main__":
    dd = DingDing(webhook='https://oapi.dingtalk.com/robot/send?access_token=')
    print(sys.argv[0]) 
    # ??????????????????
    #print(dd.Send_Text_Msg(Content='test:????????????'))
    # ??????????????????
    #print(dd.Send_Link_Msg(Content='test',Title='????????????',MsgUrl='',PicUrl=''))
    # ??????Markdown???????????????
    for i in range(10):
        print(dd.Send_MardDown_Msg(Content="## AWSL 10????????????%d" %i+ "??????????????????\n" + "> testone", Title='????????????'))