from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('uploadplace/', views.upload_place, name="upload_place"),
    path('place/', views.place_list, name="place_list"),
    path('place/<int:id>/upload/',
         views.upload, name='upload'),
    # id는 위치
    path('place/<int:id>/detail', views.detail, name='detail'),
    # id는 사진
    path('place/<int:id>/moredetail', views.more_detail, name='moredetail'),
    # id는 사진
    path('place/<int:id>/delete', views.delete, name='delete'),

    path('place/<int:id>/reviewcreate',
         views.review_create, name='review_create'),
    path('place/<int:pic_id>/<int:review_id>/reviewdelete',
         views.review_delete, name='review_delete'),
    path('sec/',
         views.seceret_img, name='sec'),
]
