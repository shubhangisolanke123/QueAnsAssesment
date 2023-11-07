from django.urls import path
from . import views

urlpatterns=[
    path('que/',views.post_question,name='addque_url'),
    path('ql/',views.question_list,name='showque_url'),
    path('ans/',views.post_answer,name='addans_url'),
    path('queans/',views.queans_list,name='addqueans_url'),
    path('like/',views.addlike,name='addlike_url'),
    path('displaylike/',views.display_likes,name='displaylikes_url'),
    
    
    


]