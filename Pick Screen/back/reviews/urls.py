from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.review_list_create),
    path('<int:review_pk>/',views.review_detail_delete_update),
    path('comment/<int:review_pk>/', views.comment_list_create),
    path('comment/<int:review_pk>/<int:comment_pk>/', views.comment_delete_update),
    path('likes/<int:review_pk>/', views.likes),

]