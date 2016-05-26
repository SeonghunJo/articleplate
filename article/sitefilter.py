#-*- coding: utf-8 -*-

from newspaper.parsers import Parser
import re
"""
1. Check HTML and find special things of website
2. Redirect to real article url
"""
class SiteFilter(object):

    def __init__(self, url, doc):
        self.url = url
        self.doc = doc
        self.parser = Parser
        self.origin = None
        return

    def filter_naver(self):
        """If the article has meta wlwmanifest link set in the url
        """
        kwargs = {'tag': 'link', 'attr': 'rel', 'value': 'wlwmanifest'}
        meta = self.parser.getElementsByTag(self.doc, **kwargs)
        if meta is not None and len(meta) > 0:
            href = self.parser.getAttribute(meta[0], 'href')
            m = re.match(r"http://blog\.naver\.com/NBlogWlwLayout\.nhn\?blogId=\w*", href)
            if m is not None:
                blog_id = href.split('blogId=')[-1]
                log_no = self.url.split('/')[-1]
                self.origin = 'http://blog.naver.com/PostView.nhn?blogId=%s&logNo=%s' % (blog_id, log_no)
                return True
        return False

    def get_real_url(self):
        self.filter_naver()
        if(self.origin is not None):
            return self.origin
        return self.url
