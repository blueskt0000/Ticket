import requests
from tools.service import Service


class APP_Show_Action:
    def __init__(self):
        self.session =  requests.session()
    def AP_Action(self,method,url,para):
        res = self.session.request(method=method,url=url,params=para)
        return res
if __name__ == '__main__':
    para= {"id":"1"}
    print(APP_Show_Action().AP_Action(method="GET",url="http://192.172.4.60:9000/showservice/showDetails?",para = para))