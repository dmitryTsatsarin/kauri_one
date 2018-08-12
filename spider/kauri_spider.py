import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['wss://stream.binance.com:9443/stream?streams=!miniTicker@arr@3000ms']

    def parse(self, response):
        print('here')
        print(response.text)
        print('here end')
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)

