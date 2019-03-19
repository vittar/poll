from django.urls import path

from .views import *


urlpatterns = [
    path('', polls_list, name='polls_list_url'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('user_results/', user_results, name='user_results'),
#    path('<str:slug>/', poll_detail, name = 'poll_detail_url'),
    path('<str:slug>/', PollDetail.as_view(), name = 'poll_detail_url'),
    path('<str:slug>/vote/', poll_vote, name='vote'),
    path('<str:slug>/result/', poll_result, name='poll_result'),
]
