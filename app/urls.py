from django.urls import path
from .import views

urlpatterns = [
  path('' , views.home , name='home'),
  path('login/' , views.login_user , name='login'),
  path('logout/' , views.logout_user , name='logout'),
  path('register/' , views.register , name='register'),
  path('category/<int:category_id>/' , views.category , name='category'),
  path('cart/' , views.cart , name = 'cart'),
  path('checkout/' , views.checkout , name='ckeckout'),
  path('update_item/' , views.updateItem , name='update_item'),
  path('delete_item/<order>/' , views.updateItem , name='delete_item'),
  path('detail_product/<int:id>' , views.detail_product , name='detailproduct'),
]
