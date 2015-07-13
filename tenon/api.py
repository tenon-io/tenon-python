from urlparse import urlparse
import json
import requests

class TenonIOError(Exception):
    pass

class TenonIO(object):

    TENON_BASE_URL = "http://tenon.io/api/"

    def __init__(self, key=None, endPoint=TENON_BASE_URL):
        self.key = key
        self.endPoint = endPoint

    def __isUrl(self, str):
        return urlparse(str).netloc != ""

    def __isHtmlDocument(self, str):
        if str:
            str = str.lstrip().lower()
            return str.startswith("<!doctype") or str.startswith('<html')
        else:
            return False

    def __validate(self, data):
        data['key'] = self.key
        return requests.post(self.endPoint, data=data)

    def analyze(self, target=None, **kwargs):
        if target:
            if self.__isUrl(target):
                return self.checkUrl(target, **kwargs)
            elif self.__isHtmlDocument(target):
                return self.checkSrc(target, **kwargs)
            else:
                return self.checkFragment(target, **kwargs)
        else:
            raise TenonIOError("You must specify a URL or HTML to be checked.")

    def checkUrl(self, url=None, **kwargs):
        if url:
            kwargs['url'] = url
            return self.__validate(kwargs)
        else:
            raise TenonIOError("You must specify a URL to be checked.")

    def checkSrc(self, src=None, **kwargs):
        if src:
            kwargs['src'] = src
            return self.__validate(kwargs)
        else:
            raise TenonIOError("You must specify a block of HTML source code to be checked.")

    def checkFragment(self, src=None, **kwargs):
        if src:
            kwargs['src'] = src
            kwargs['fragment'] = "1"
            return self.__validate(kwargs)
        else:
            raise TenonIOError("You must specify a block of HTML source code to be checked.")
