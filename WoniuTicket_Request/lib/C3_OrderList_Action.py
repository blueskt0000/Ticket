
from tools.service import Service


class OL_Action:
    def __init__(self):
        self.session = Service.get_cookie()

    def AP_Action(self, method, url, para):
        res = self.session.request(method=method, url=url, params=para)
        return res