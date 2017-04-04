from scrapy.http import FormRequest
from spider.items import SpiderItem
from spider.spiders.base_spider import BaseSpider


class NewYork(BaseSpider):
    name = 'new_york'
    allowed_domains = ['http://www.elections.ny.gov']
    start_url = 'http://www.elections.ny.gov/ContributionSearchB_Name.html'
    request_url = 'http://www.elections.ny.gov:8080/plsql_browser/CONTRIBUTORB_NAME'

    def parse(self, response):

        param = self.params  # redis keys which spider can use

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'www.elections.ny.gov:8080',
            'Origin': 'null',
        }
        data = {
            'LAST_NAME_IN': 'Adam',
            'NAME_IN': '',
            'position_IN': 'START',
            'date_from': '01/01/2013',
            'date_to': '01/01/2017',
            'AMOUNT_from': '0',
            'AMOUNT_to': '100000',
            'ORDERBY_IN': 'N',
        }
        return [FormRequest(self.request_url, formdata=data,
                           headers=headers, callback=self.parse_detail, dont_filter=True)]

    def parse_detail(self, response):
        results = response.xpath('//div[@id="cfContent"]//table[2]/td')
        step = 10
        table_result = [results[step*i:step*(i+1)] for i in range(int(len(results)/step))]

        for item in table_result:
            items = SpiderItem()
            items['contribution_name'] = ' '.join(item[0].xpath(
                './font/text()').extract_first().split())
            items['address'] = item[6].xpath('./font/text()').extract_first()
            items['contributor_type'] = 'person'
            items['candidate_name'] = item[3].xpath(
                './font/a/text()').extract_first()
            items['state'] = self.__class__.name
            items['amount'] = item[1].xpath(
                './font/text()').extract_first().strip()
            items['transaction_date'] = item[4].xpath(
                './font/text()').extract_first()

            yield items