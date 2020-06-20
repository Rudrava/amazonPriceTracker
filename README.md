# amazonPriceTracker

This would be my personal favorite project as I everyday stare at Amazon Pages to check if the items in my wishlist droppped prices or not...


This Project would use SQL and PYTHON (BeautifulSoup, requests)


## The DESIGN
  
 ![alt text](https://github.com/Rudrava/amazonPriceTracker/blob/master/amazonPriceTracker.jpg?raw=true)


### *THE SCRAPER*
      IT WORKS USING REQUESTS AND BEAUTIFUL SOUP
       Initially I made a list of links of which every link is parsed with **BeautifulSoups html.parser** after fetching the content 
       with requests.get() method
       
       The name is got with soup.find(**html id**) similarly the price was fetched
       
       ####THE toInt 
        coding it was a miracle as it maybe hte first time where I wrote a ALGO and it worked in first go 
        
        it Just converts the string to int as it would help us to compare prices !!!
