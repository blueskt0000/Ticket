import os
import time,unittest
from lib.B2_RoleManagement_Action import Role_Action


path = 'D:\pyFileDM_New\WoniuTicket_GUI\wts.sql'

# 角色列表
class S_Test(unittest.TestCase):
    def setUp(self) -> None:
        self.st = Role_Action()
        self.st.driver.maximize_window()
        os.system(f"mysql -h192.172.4.60 -u root -p123456 --default-character-set=utf8 wts <{path}")
