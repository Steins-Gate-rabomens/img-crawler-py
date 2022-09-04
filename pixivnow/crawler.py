import json

import requests


class Crawler:
    # page should start from 1
    def crawl(self, keyword: str, page: int):
        url = "https://pixiv.js.org/ajax/search/artworks/{}?p={}&mode=undefined".format(keyword, page)
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) "
                          "Version/5.1 Safari/534.50", }
        response = requests.get(url=url, headers=headers)
        urls = []
        try:
            resp_json = json.loads(response.text)
            for illust in resp_json['illustManga']['data']:
                url = "https://pximg.wjghj.cn/" + illust['url'][2:]
                urls.append(url)
            return urls
        except Exception as e:
            print(e)


if __name__ == '__main__':
    c = Crawler()
    print(c.crawl("甘雨", 1))
