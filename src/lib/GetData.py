# -*- coding: utf-8 -*-
# @Time: 2024.11.3
# @Author: R
# @File: GetData.py
# 功能: 爬取天气数据
import requests

class GetData:
    url = ""
    headers = ""

    def __init__(self, url, header=""):
        """
        :param url: 
        :param header: 请求头
        """
        self.url = url
        if header == "":
            self.headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
            }
        else:
            self.headers = header

    def Get(self):
        """
        :return: 网址对应的网页内容
        """
        res=requests.get(url=self.url,headers=self.headers)
        print("res_code:"+str(res.status_code))
        return res.content.decode("utf-8")

