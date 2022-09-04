import json

import undetected_chromedriver as uc
from bs4 import BeautifulSoup


class Crawler:
    def crawl(self, keyword: str, page: int):
        url = "https://api.pixivel.moe/v2/pixiv/illust/search/{}?page={}&sortpop=false&sortdate=false".format(keyword,
                                                                                                              page)

        driver = uc.Chrome()
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, features='lxml')
        response = soup.find(name="pre").text
        ids = []
        try:
            resp_json = json.loads(response)
            for illust in resp_json['data']['illusts']:
                id = illust['id']
                ids.append(id)
            return ids
        except Exception as e:
            print(e)


if __name__ == '__main__':
    c = Crawler()
    print(c.crawl("甘雨", 0))
