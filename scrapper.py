import requests
from bs4 import BeautifulSoup

def scrapSnapdeal(query):
    url="https://www.snapdeal.com/search"
    params={
      "keyword":query,
      "sort": "phtl"
    }        
    r=requests.get(url,params=params)
    soup=BeautifulSoup(r.content)

    products = soup.findAll('div', attrs = {"class": "product-tuple-listing"})
    result=[]
    e = {
          "img": None,
          "title": "Showing Results from Snapdeal",
          "price": None
        }
    result.append(e)
    for product in products:
        img_tag = product.find('img')
        if 'src' in img_tag.attrs:
            img = img_tag.attrs['src']
        else:
            img = img_tag.attrs['data-src']
        title = product.find('p', attrs = {"class": "product-title"}).text
        price = product.find('span', attrs = {"class": "product-price"}).text
        

        d = {
          "img": img,
          "title": title,
          "price": price
        }
        result.append(d)
      
    e = {
          "img": None,
          "title": "Above results were from Snapdeal, Now showing Results from Amazon",
          "price": None
        }
    result.append(e)


    url="https://www.amazon.in/s"
    params={
      "keyword":query,
      "s": "price-desc-rank"
    }  
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    r=requests.get(url,params=params, headers = headers)
    soup=BeautifulSoup(r.content)
    products = soup.findAll('div', attrs = {'class': 's-result-item'})
    for product in products:
        img_tag = product.find('img')
        if 'src' in img_tag.attrs:
            img = img_tag.attrs['src']
        try:
            title = product.find('span', attrs = {"class": "a-text-normal"}).text
        except:
            print("This was an advertisement")
        try:
            price = product.find('span', attrs = {"class": "a-price-whole"}).text
        except:
            print("This was an advertisement")
        d = {
          "img": img,
          "title": title,
          "price": "Rs. "+price
        }
        result.append(d)


    return result

