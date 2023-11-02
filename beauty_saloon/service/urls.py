from django.urls import path

from service.views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('filter/', Filter.as_view(), name='filter'),
    path('new_items/', NewProduct.as_view(), name='new_items'),
    path('add-rating/', AddStarRating.as_view(), name='add_rating'),
    path('catalog/<str:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('<slug:cat_slug>/', ProductOtherList.as_view(), name='product_list_cat'),
    path('<slug:cat_slug>/<slug:subtitle_slug>/', ProductList.as_view(), name='product_list_sub'),
    path('<slug:cat_slug>/<slug:subtitle_slug>/<slug:subsub_slug>/', ProductList.as_view(), name='product_list_subsub'),
]
