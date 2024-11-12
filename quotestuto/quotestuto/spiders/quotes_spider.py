import scrapy

class QuotesSpider(scrapy.Spider):  # scrapy.spider will give a lot of tool stuff and we won't have to do a lot of coding
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]
    # don't change the name of name annd start_url var as the class we are inheriting from expect us to have this two variable

    def parse(self,response):   #response will content the source code of the website you want to scrap
        # let's just scrap the title for now 
        # title = response.css('title').extract()   # response tag contains whole source code but we don't whole, we just want title which is inside title tag (check in source code of website)
        title = response.css('title::text').extract() 
        yield {'title_text': title}  # for return purpose(show us the answer in dict format)
        ''' yield is used with generator and generator is used by scrapy behind the scenes, so instead of simple return statement use yield '''

        ''' if we only extract title it will give us answer like this 
        ['<title>Quotes to Scrape</title>']
        we only want text we have to specify title::text 
        '''


        ''' idea of selecting a tag or particular html tag or a particular CSS or an ID inside
        in the sourcce cide is known as CSS Selector, so use it typing ".css" 
        '''


        """ scrapy shell and "website_link" will open the website here, we do it so we can find the different
        types of ids or tags in it
        shell is like cmd for windows  in scrapy 

        response.css("title")
        [<Selector query='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]
        >>> response.css("title").extract() 
        ['<title>Quotes to Scrape</title>']
        >>> response.css("title::text").extract()
        ['Quotes to Scrape']
        >>> response.css("title::text")[0].extract() 
        'Quotes to Scrape'
        >>> response.css("title::text").extract_first() 
        'Quotes to Scrape'

        when we are scrapping any website it doesn't contain anything then it will give error if we use 
        [0]  but if we use extract_first it won't throw error and will return null 
        """

