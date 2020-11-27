# 登录
import os
import time
import unittest
import warnings

from BeautifulReport import BeautifulReport
from ddt import data, ddt, unpack
from lib.A1_Login_Action import L_Action
from parameterized import parameterized

from data.Get_TestData.Get_A1_LT_Data import Get_LG_TestData
from tools.service import Service

path = 'D:\pyFileDM_New\WoniuTicket_GUI\wts.sql'
@ddt
class L_Test(unittest.TestCase):
    login_data = Get_LG_TestData.get_login_excel_data()
    print(login_data)
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        self.lg = L_Action(Service.get_cookie())

    @data(*login_data)
    @unpack
    def test_do_login(self , casesname , url , method , username , password , captcha , expect):
        test_data ={"CASESNAME":casesname,"URL":url , "METHOD":method,
                    "DATA":{"USERNAME":username , "PASSWORD":password , "CAPTCHA":captcha},  "EXPECTED":expect}
        res = self.lg.do_login(test_data["URL"] , test_data["METHOD"] , test_data["DATA"])

        text = res.json()
        if text["msg"] == '登录失败':
            resutl = 'login-fail'
        else:
            resutl = 'login-pass'
        self.assertEqual(resutl , expect)








if __name__ == '__main__':
    unittest.main(verbosity=2)