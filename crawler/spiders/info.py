import scrapy


class InfoSpider(scrapy.Spider):
    name = 'info'
    start_urls = ["https://urltocrawl.com"]

    def parse(self, response):
        for products in response.css('div.entry-content-wrap'):
            try:
                yield{
                    'name': products.css('h1.entry-title::text').get(),
                    'instructions': products.css('ol').getall(),

                }
            except:
                yield{
                    'name': products.css('h1.entry-title::text').get(),
                    'instructions': products.css('ol').getall(),

                }
        #next_page = response.css('a.post-thumbnail kadence-thumbnail-ratio-2-3').attrib['href']
        # if next_page is not None:
        #   yield response.follow(next_page, callback=self.parse)
