from django.contrib import admin
from django.urls import path
from Bcapp.views import user_signup,user_login,user_logout,user_resetpassword,user_personal_details
from Bapp.views import home,contact,privacy,partner
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url
from Bmapp.views import information,hello,boom,rocket,control

from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home, name="home"),
    path("user_signup", user_signup, name="user_signup"),
    path("user_login", user_login, name="user_login"),
    path("user_logout", user_logout, name="user_logout"),
    path("user_resetpassword", user_resetpassword, name="user_resetpassword"),
    path("user_personal_details", user_personal_details, name="user_personal_details"),
    path("information", information,name="information"),
    path("contact", contact,name="contact"),
    path("privacy", privacy,name="privacy"),
    path("partner", partner,name="partner"),
    path("hello", hello,name="hello"),
    path("boom", boom,name="boom"),
    path("rocket", rocket,name="rocket"),
    path("control", control,name="control"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
]

if settings.DEBUG:
	urlpatterns += [
		url(r'^media/(?P<path> .*)$', serve, {
			'document_root' : settings.MEDIA_ROOT,
		}),
	]