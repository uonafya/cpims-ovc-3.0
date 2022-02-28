"""Registry section urls."""
from django.urls import path
# from cpovc_registry.views import (home, register_new, register_details, register_edit, persons_search,
#                                   new_user, )
from . import views
# This should contain urls related to registry ONLY
urlpatterns = [
    # 'cpovc_registry.views',
    path('ou/', views.home, name='registry'),
    path('ou/new/', views.register_new, name='registry_new'),
    path('ou/view/<int:pk>/', views.register_details,
        name='register_details'),
    path('ou/edit/<int:pk>/', views.register_edit, name='registry_edit'),
    # path('ou/view/(?P<org_id>\d+)/', views.register_details,
    #     name='register_details'),
    # path('ou/edit/(?P<org_id>\d+)/', views.register_edit, name='registry_edit'),
    path('person/search/', views.persons_search, name='search_persons'),
    path('person/user/<int:pk>/', views.new_user, name='new_user'),
    path('person/', views.person_actions, name='person_actions'),
    path('person/new/', views.new_person, name='new_person'),
    path('person/edit/<int:pk>/', views.edit_person, name='edit_person'),
    path('person/view/<int:pk>/', views.view_person, name='view_person'),
    path('person/delete/<int:id>/', views.delete_person, name='delete_person'),
    # path('person/delete/<int:id>/', views.delete_person, name='delete_person'),
    path('lookup/', views.registry_look, name='reg_lookup'), ]
# {% url 'view_person' id=result.id %}