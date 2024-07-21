from ecommapp import views
from django.urls import path
from ecommapp.views import ContactForm
from django.conf.urls.static import static
from django.conf import settings
'''
    path('about',views.about),
    path('delete/<rid>',views.delete),
    path('edit/<x>',views.edit),
    path('contact/<cid>',ContactForm.as_view()),
    path('hello',views.hello),
    path('base',views.base),
    path('contact',views.contact),
    
'''
urlpatterns = [
    
    path('products',views.products),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('about',views.about),
    path('catfilter/<cv>',views.catfilter),
    path('sort/<sv>',views.sort),
    path('filterbyprice',views.filterbyprice),
    path('product_details/<pid>',views.product_detail),
    path('addcart/<pid>',views.cart),
    path('viewcart',views.viewcart),
    path('updateqty/<x>/<cid>',views.updateqty),
    path('removecart/<cid>',views.removecart),
    path('placeorder',views.placeorder),
    path('fetchorder',views.fetchorder),
    path('makepayment',views.makepayment),
    path('paymentsuccess',views.paymentsuccess),
    path('search',views.search),
]   

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)