from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Link


# Create your views here.

def scrape(request):
    # page = requests.get('https://www.google.com')
    #link_address = []
    if request.method == "POST":
        site = request.POST.get('site','')
        page=requests.get(site)
        soup = BeautifulSoup(page.text,'html.parser')

   
        for link in soup.find_all('a'):
            #link_address.append(link.get('href')) # for directly displaying in template
            link_address = link.get('href')
            link_text =link.string
            Link.objects.create(address=link_address)
        
        return HttpResponseRedirect('/')
    else:    
        data = Link.objects.all()
    
    return render(request, 'patoa/result.html', {'data':data})
        #return render(request, 'patoa/result.html', {'link_address':link_address}) # for displaying from list Link_address

def clear(request):
    Link.objects.all().delete()
    return render(request,'patoa/result.html')