import json

import requests


class Crawler:
    def __init__(self):
        self.url = "https://rt.huashi6.com/search/all"
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) "
                          "Version/5.1 Safari/534.50", }

    def crawl(self, keyword: str, index: int):
        post_data = {
            "word": keyword,
            "index": index
        }
        try:
            res_raw = requests.post(url=self.url, data=post_data, headers=self.headers)
            res_json = json.loads(res_raw.text)

            print("collecting img urls...")
            works = res_json['data']['works']

            prefix = "https://img2.huashi6.com/"
            urls = []
            for work in works:
                postfix = work['coverImage']['originalPath']
                urls.append(prefix + postfix)
            print(urls)
        except Exception as e:
            print(e)
