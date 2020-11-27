import os
import unittest
from lib.B3_ChangePassword_Action import CP_Action
import sys
path = 'D:\pyFileDM_New\WoniuTicket_GUI\wts.sql'

# 修改密码
class CP_Test(unittest.TestCase):

    def setUp(self) -> None:
        self.cp = CP_Action()
        os.system(f"mysql -h192.172.4.60 -u root -p123456 --default-character-set=utf8 wts <{path}")

