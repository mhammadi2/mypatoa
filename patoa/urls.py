from  django.urls import path
from . import views

urlpatterns = [
    #path('',views.post_patent)
    #path('new',views.new,name="new"),
    path('',views.scrape_post, name="result"),
    path('clear',views.clear, name="clear"),
    #path('',views.scrape_get, name="scrape_get"),

]