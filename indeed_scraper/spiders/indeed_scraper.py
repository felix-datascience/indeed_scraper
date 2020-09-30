import scrapy

# base url
search_phrase = 'data+science'
base_url = 'https://de.indeed.com/jobs?q={}&sort=date&filter=0&start='.format(search_phrase)

class JobSpider(scrapy.Spider):

    name = 'jobs'

    # for each page append (page number - 1) * 10
    # e.g.: page 1: 0, page 2: 10, page 15: 140
    # highest possible page number: 100
    start_urls = [base_url + str(page_num) for page_num in range(0, 1000, 10)]
    
    def parse(self, response):
        for job in response.xpath('//div[@class="jobsearch-SerpJobCard unifiedRow row result"]'):
            yield {

                'title': job.xpath('.//a/@title').get(),

                # company names are sometimes nested inside hyperlink tag
                # // searches for text nodes in all depths (nested in <a> or not)
                # [string-length() > 2] ignores texts only containing "\n"
                'company': job.xpath('.//span[@class="company"]//text()[string-length()>2]').get(),

                # <span> & <div> tags are used for location
                # * allows for both
                'location': job.xpath('.//*[@class="location accessible-contrast-color-location"]/text()').get(),

                'salary': job.xpath('.//span[@class="salaryText"]/text()').get(),

                'description': job.xpath('.//li/text()').getall(),
            }
