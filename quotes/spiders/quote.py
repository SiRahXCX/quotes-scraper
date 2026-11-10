import scrapy
from quotes.items import QuotesItem


class QuoteSpider(scrapy.Spider):
  name = "quote"
  allowed_domains = ["quotes.toscrape.com"]
  start_urls = ["https://quotes.toscrape.com/"]

  def parse(self, response):
    quotes = response.css('div.quote')
    for quote in quotes:
      new_quote = QuotesItem()
      new_quote['quote'] = quote.css('span.text::text').get()
      new_quote['author'] = quote.css('small.author::text').get()
      yield new_quote
