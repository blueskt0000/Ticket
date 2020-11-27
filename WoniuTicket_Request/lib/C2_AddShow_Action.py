# 添加演出
from tools.service import Service
class AS_Action:

    def __init__(self):
        self.session = Service.get_cookie()

    def AddShow_Action(self,url,method,para):
        res = self.session.request(url=url , method=method,params=para)
        return res

if __name__ == '__main__':
    pass
