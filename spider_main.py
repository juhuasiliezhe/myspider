#coding:utf-8
'''
Created on 2017-7-28

@author: DELL
'''
import url_manager
import html_downloader
import datetime

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()

    def craw(self, root_url):
        now = datetime.datetime.now()
        print now.strftime('%Y-%m-%d %H:%M:%S')  
        count = 1

        # while self.urls.has_new_url():
        try:
            # for num in range(17):
            # while self.urls.has_new_url():
            # new_url = self.urls.get_new_url()
            # if num==5:
            self.downloader.download(root_url)


        except ValueError, Argument:
            print 'craw failed' ,Argument

        nows = datetime.datetime.now()
        print '结束时间：'+nows.strftime('%Y-%m-%d %H:%M:%S')

if __name__=="__main__":
    # root_url = "http://www.ccgp.gov.cn/cggg/zygg/cjgg/index.htm"
    root_url = "http://xyq.cbg.163.com/equip?s=221&eid=201801282100113-221-M8QVIGPDKX4G"
    # root_url = "http://xyq.cbg.163.com/equip?s=221&eid=201712160000113-221-UTJFJVSHVDAC"

    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    