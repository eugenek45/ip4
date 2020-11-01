from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^welcome/',views.welcome,name='welcome'),
    url(r'^profile/(\d+)',views.profile,name = 'profile'),
    url(r'^updateProfile',views.updateProfile,name = 'updateProfile'),
    url(r'^new/hood/$',views.create_neighbourhood, name='newHood'),
    url(r'^all/hoods/',views.neighbourhoods, name='allHoods'),
    url(r'^neighborhood/(\d+)',views.neighbourhood_details, name='pickHood'),
    url(r'^follow/(\d+)', views.follow, name='follow'),
    url(r'^unfollow/(\d+)', views.unfollow, name='unfollow'),
    url(r'^new/business/',views.create_business, name='newBusiness'),
    url(r'^business/(\d+)',views.business_details, name='business'),
    url(r'^post/', views.new_post, name='post'),
    url(r'^search/', views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)