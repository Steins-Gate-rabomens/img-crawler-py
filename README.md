# ImgCrawlerPy

一些 python 版本的图片爬虫，返回结果是根据关键字获取的图片链接数组。

之所以会有这个东西的原因是，`Golang` 在爬虫这块没有像 `Python` 这样有大量强大的相关库。`Golang` 可以通过调用 `Python` 代码甚至使用跨语言工具来使用 `Python` 
开发的爬虫。

## 支持的图源

+ [x] [触站](https://www.huashi6.com/)
+ [x] [Lofter](https://www.lofter.com/)
+ [x] [PixivNow](https://pixiv.js.org/)
+ [ ] [Pixivel](https://pixivel.moe/)

对于 `Pixivel` 而言，由于使用了 `Cloudflare` 反爬，所以使用了 `undetected_chromedriver` 库模拟浏览器，经测试，`windows` 下能够正确爬取，
`linux` 云服务器上尝试使用 `Xvfb` + `Chrome driver` 和 `Chrome driver + headless` 均会被 block，尚未找到合适的方案。