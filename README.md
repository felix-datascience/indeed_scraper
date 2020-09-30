# Indeed Scraper

A simple web scraper that scrapes indeed.com.
It is built with Scrapy.

### What data does it scrape?

It scrapes the job title, company, location, salary and the short description
of the jobs on the search results page. It doesn't go any further to the more
detailed pages. There is more text data on these pages, but they are listed
on the robots.txt file.

### How can I use it?

First of all you have to have Python 3 and Scrapy installed on your computer.
Then clone this repository. Move to the root direcory of the project and run:
`scrapy crawl jobs -o jobs.json`

This will write the data to a json file in the project's root directory.

By default the scraper searches for the keyphrase "data science". You can change
this behaviour by changing the variable "search_phrase" in
indeed_scraper/spiders/indeed_scraper.py.
