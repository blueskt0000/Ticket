import requests


class APP_Show_Action:
    def __init__(self):
        self.session =  requests.session()

    def AP_Action(self,method,url,para):
        res = self.session.request(method=method,url=url,data=para)
        return res