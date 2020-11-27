import time

from tools.util import Utility
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests

#封装操作软件的工具类
class Service:

    # 获取软件网址,需要传入元素对象和网址配置文件路径
    @classmethod
    def get_cookie(cls):
        contents = Utility.get_json(Utility.get_root_path()+"\\conf\\Base_conf\\base.conf")[0]
        # url = cls.get_url_head(uri)
        url = f"{contents['PROTOCOL']}://{contents['IP']}:{contents['PORT']}/{contents['PROGRAM']}"
        data = {"username":"admin" , "password":"123456" , "captcha":"1111"}
        session = requests.session()
        session.post(url , data)
        return session






if __name__ == '__main__':
    pass
    Service.get_url_head('/1')