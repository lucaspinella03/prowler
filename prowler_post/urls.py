from django.urls import path
from . import views 

app_name = 'prowler_post'

urlpatterns = [
    #home page

    #entry page
    path('entry/', views.prowler_entry, name='prowler_entry'),

    #new entry page 

    path('new_prowler_entry/', views.new_prowler_entry, name='new_prowler_entry')
       
]
