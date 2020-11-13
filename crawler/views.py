from django.shortcuts import render
from .models import Sale
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from fake_useragent import UserAgent
import requests
import bs4
from bs4 import BeautifulSoup
import re

# Create your views here.
def index(request):
    
    sale_product = Sale.objects.all().order_by('-sale_date')
    paginator = Paginator(sale_product, 21)
    page = request.GET.get('page')
    paged_sale_product = paginator.get_page(page)

    context = {
        'sale_product': paged_sale_product,
      
    }

    if request.method == "POST":
        url = 'https://www.momoshop.com.tw/main/Main.jsp'
        crawler_work = SaleCrawler(url)
        crawler_work.get_sale_product()
        
   
    return render(request, 'crawler/index.html', context)




class SaleCrawler(object):
    def __init__(self, url):
        self.ua = UserAgent(verify_ssl=False)
        self.headers = {"User-Agent": self.ua.random}
        self.url = url
    
    def get_sale_product(self):
        response = requests.get(self.url, headers=self.headers)
        
        soup = BeautifulSoup(response.text, 'lxml')

        for product in soup.select('div.TabContent > div.TabContentD > ul > li'):
            print('-----------')

            if product is not None:

                try:
                    title = product.select_one(' .prdname').text
                    print(title)
                    
                    a_link = product.select_one('a')['href']
                    if 'https://www.momoshop.com.tw' not in a_link:
                        link = 'https://www.momoshop.com.tw' + a_link
                    else:
                        link = a_link 
                    
                    
                    image_link = product.select_one('img')['org']
                    
                    if 'ecm' in image_link:
                        continue
                    elif 'https:' not in image_link:
                        image = 'https:'+ image_link 
                    else:
                        image = image_link
                    print(image)

                    discount = product.select_one(' .prdprice .prdprice_box01 b').text
                    print(discount)
                    
                    price = product.select_one('.prdprice .prdprice_box02 b').text
                    print(price)

                    sale_products = Sale(title=title, link=link, image=image, discount=discount, price=price)

                    sale_products.save()
                    print(sale_products)
                
                except:
                    continue

    





