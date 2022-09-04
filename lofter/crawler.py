import requests
from bs4 import BeautifulSoup


class Crawler:
    def crawl(self, keyword: str):
        url = "https://www.lofter.com/tag/{}/total".format(keyword)
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) "
                          "Version/5.1 Safari/534.50", }
        resp = requests.get(url=url, headers=headers)
        try:
            soup = BeautifulSoup(resp.text, features='lxml')
            imgs = soup.find_all(name="img", attrs={"data-origin": True})
            urls = []

            for img in imgs:
                url = img.get("data-origin")
                urls.append(url)

            return urls
        except Exception as e:
            print(e)


if __name__ == '__main__':
    c = Crawler()
    print(c.crawl("甘雨"))
