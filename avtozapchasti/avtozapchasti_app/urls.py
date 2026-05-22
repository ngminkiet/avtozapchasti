from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'), # name - это имя маршрута
    path('auf/', views.auf, name='auf'),
    path('reg/', views.reg, name='reg'),
    path('logout/', views.logout_view, name='logout'),
    path('item/<int:id>', views.item_template, name='item'),
    path('items/<str:spare_parts_type>', views.items_list, name='items_list'),
    path('account/', views.account, name='account'),
    path('confirm/', views.confirm, name='confirm'),
    path('email/', views.email, name='email')
    # path('cart/', views.cart_detail, name='cart_detail'),
    # path('cart/add/<int:item_id>', views.cart_add, name='cart_add'),
    # path('cart/remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
    # path('cart/clear/', views.cart_clear, name='cart_clear')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)