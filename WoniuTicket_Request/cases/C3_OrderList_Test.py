# 订单列表
import unittest
import warnings

from data.Get_TestData.Get_C1_LMT_Data import Get_LM_TestData
from ddt import data, unpack,ddt
from lib.C3_OrderList_Action import OL_Action
from tools.util import Utility

@ddt
class OL_Test(unittest.TestCase):
    def setUp(self) -> None:
        self.a = OL_Action()
        warnings.simplefilter('ignore', ResourceWarning)

    @data(*Get_LM_TestData.get_OMT_orderlist_data())
    @unpack
    def test_orderlist(self, url, method, page,limit ,orderSn,state,payWay, casesname, expect):
        test_data = {"URL": url, "METHOD": method,
                     "CASESNAME": casesname, "EXPECT": expect}
        para = {"page": page, "limit": limit,"orderSn": orderSn, "state": state,"payWay":payWay}
        res = self.a.AP_Action(method=test_data["METHOD"], url=test_data["URL"], para=para)
        text = res.json()

        if len(text['data']) > 0:
            result = "query-pass"
        else:
            result = "query-fail"

        Utility.logger(test_data["CASESNAME"], len(text['data']), result, test_data["EXPECT"])
        self.assertEqual(result, test_data["EXPECT"])


if __name__ == '__main__':
    unittest.main()