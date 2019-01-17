from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^testimony',views.testimony,name='testimony'),
    url(r'^search/$',views.search , name='search'),
    url('edit_profile/',views.edit_profile, name='edit_profile'),
    url('edit/',views.edit, name='edit'),
    url( r'^profile/$' , views.profile , name='profile' ),
    url( r'prof/(?P<pk>[0-9]+)/$' , views.ProfileUpdate.as_view( ) , name='profile-update' ) ,
    url( r'profile/(?P<pk>[0-9]+)/delete/$' , views.ProfileDelete.as_view( ) , name='profile-delete' ) ,
    url( r'^create/$' , views.create , name='create' ),
    
 
]
