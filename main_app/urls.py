from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/',views.about,name='about'),
	path('finches/',views.finches_index,name='finches_index'),
	path('finches/<int:finch_id>/',views.finches_detail,name='detail'),
	path('finches/<int:finch_id>/add_feeding/',views.add_feeding,name='add_feeding'),
	path('finches/new',views.new_finch,name='new_finch'),
    path('finches/<int:finch_id>/edit/',views.finches_update,name='finches_update'),
    path('finches/<int:finch_id>/delete/',views.finches_delete,name='finches_delete'),
    path('finches/<int:finch_id>assoc_toy/<int:toy_id>/',views.assoc_toy,name='assoc_toy'),

     # full CRUD routes for toys
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),

    path('accounts/signup', views.signup, name='signup'),
]