from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.registerUser, name="register"),
    path('wallet/', views.wallet, name="wallet"),

]

admin.site.site_header = 'wallet Adminsitration'                    # default: "Django Administration"
admin.site.index_title = 'Website Features'                 # default: "Site administration"
admin.site.site_title = 'E wallet' # default