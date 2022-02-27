"""Registry section urls."""
from django.urls import path
from cpovc_registry.functions import delete_person
from cpovc_registry.views import (home, register_new, register_details, register_edit, persons_search,
                                  new_user,person_actions, new_person, edit_person, delete_person, registry_look, view_person)

# This should contain urls related to registry ONLY
urlpatterns = [
    'cpovc_registry.views',
    path(f'^ou/$', home, name='registry'),
    path(f'^ou/new/$', register_new, name='registry_new'),
    path(f'^ou/view/<int:org_id>/$', register_details,
        name='register_details'),
    path(f'^ou/edit/<int:org_id>/$', register_edit, name='registry_edit'),
    path(f'^person/search/$', persons_search, name='search_persons'),
    path(f'^person/user/<int:id>/$', new_user, name='new_user'),
    path(f'^person/$', person_actions, name='person_actions'),
    path(f'^person/new/$', new_person, name='new_person'),
    path(f'^person/edit/<int:id>/$', edit_person, name='edit_person'),
    path(f'^person/view/<int:id>/$', view_person, name='view_person'),
    path(f'^person/delete/<int:id>/', delete_person, name='delete_person'),
    path(f'^lookup/$', registry_look, name='reg_lookup'), ]
# {% url 'view_person' id=result.id %}