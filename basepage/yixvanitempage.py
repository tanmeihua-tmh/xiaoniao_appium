# -*- coding: utf-8 -*-
#已选项目页面
import time
import logging
from common.commonfunc import Common_func
class Yixvanitem_page(Common_func):
    def yixvanitempage(self):
        #
        yixvanitem='new UiSelector().resourceId("com.hs.mywork.activity:id/tv_toolbar").text("已选项目")'

        yixvanitemtye=self.check_element(yixvanitem,"已选项目页")
        if yixvanitemtye:
            return True
        else:
            return False