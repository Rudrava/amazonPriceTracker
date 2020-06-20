import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
}


def toInt(string):
    string.split()
    number = ""
    for letter in string:
        if letter not in ('₹',','):
            if letter != '.':
                number += letter
            else:
                return int(number)


def getData(link):
    page = requests.get(link, headers = headers)

    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle")
    price = soup.find(id="priceblock_ourprice").get_text()
    price = toInt(price)
    print(title.text.strip(), "\n   COSTS:- ",price  )


links = [
    "https://www.amazon.in/TP-Link-A5-Supports-Snooping-Streaming/dp/B07DYWS92W/ref=sr_1_5?dchild=1&keywords=tp+link+routers+5g&qid=1592655546&s=computers&sr=1-5",
    "https://www.amazon.in/gp/product/B078BNQ318/ref=s9_acss_bw_cg_oneplus_2a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=JR4XRHAK8ZYR55591ENN&pf_rd_t=101&pf_rd_p=6ea832c7-9954-443c-b4cf-c62faba53ec6&pf_rd_i=21439725031",
    "https://www.amazon.in/Cosmic-Byte-GS410-Headphones-Green/dp/B07K7YR8SP/ref=lp_2591139031_1_4?s=videogames&ie=UTF8&qid=1592657539&sr=1-4"]

for link in links:
    getData(link)
