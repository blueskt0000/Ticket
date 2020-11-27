























# import logging
# logger = logging.getLogger(__name__)
# logger.setLevel(level = logging.INFO)
# handler = logging.FileHandler("log.txt")
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
# handler.setFormatter(formatter)
#
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
#
# logger.addHandler(handler)
# logger.addHandler(console)
#
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
a = None
b = 1
if not None:
    print(1)
else:
    print(2)

