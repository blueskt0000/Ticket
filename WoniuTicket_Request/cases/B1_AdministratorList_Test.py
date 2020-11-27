import os
import unittest
import sys
from lib.B1_AdministratorList_Action import AL_Action

path = 'D:\pyFileDM_New\WoniuTicket_GUI\wts.sql'

# 管理员列表
class AL_Test(unittest.TestCase):

    def setUp(self) -> None:
        self.al = AL_Action()
        os.system(f"mysql -h192.172.4.60 -u root -p123456 --default-character-set=utf8 wts <{path}")


