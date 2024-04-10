'''
Created on 11 Jan 2024

@author: mpayen
'''

from django.template import loader
from django.http.response import HttpResponse
from website.models import Menu, Foodtruck
from Ohmygaufre.settings import MEDIA_URL
from Ohmygaufre.settings import STATIC_URL
from website.forms import MessageForm
from django.shortcuts import render
from django.template import RequestContext

def index(request):
    # Fetch objects that needs to be displayed on the main page
    foodtruck = Foodtruck.objects.first()
    menus = Menu.objects.all()
    
    template = loader.get_template('index.html')
    context = {
        'foodtruck' : foodtruck,
        'menus' : menus,
        'MEDIA_URL' : MEDIA_URL,
        'STATIC_URL' : STATIC_URL
    }
     
    return HttpResponse(template.render(context, request))


def send_message(request):
    foodtruck = Foodtruck.objects.first()
    template = loader.get_template('messagesent.html')
    context = {
        'foodtruck' : foodtruck,
        'MEDIA_URL' : MEDIA_URL,
        'STATIC_URL' : STATIC_URL
    }
    
    if request.method == "POST":
        form = MessageForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return render(request, 'messagesent.html', {
                'form': form,
                'success': True,
                'foodtruck' : foodtruck,
                'MEDIA_URL' : MEDIA_URL,
                'STATIC_URL' : STATIC_URL
            })
    else:
        form = MessageForm()
    
      
    return render(request, template.render(context, request), {'form': form})
  
def my_custom_page_not_found_view(request, *args, **argv):
    response = render('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def my_custom_error_view(request, *args, **argv):
    return render(request, '500.html')

def my_custom_permission_denied_view(request, *args, **argv):
    return render(request, '403.html')

def my_custom_bad_request_view(request, *args, **argv):
    return render(request, '400.html')
