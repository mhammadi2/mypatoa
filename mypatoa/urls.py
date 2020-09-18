from django.contrib import admin
from django.urls import path,include
#from patoa.views import scrape,clear, new 

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('',views.scrape, name="scrape"),
    #path('delete/',views.clear, name="clear"),
    #path('',views.linkfilename, name="linkfilename"),
    #path('download/', views.download, name="download"),
    #path('', views.new, name='new'),
    path('', include('patoa.urls')),
 
    
    
]
