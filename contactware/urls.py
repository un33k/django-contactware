from django.conf import settings
from django.conf.urls import url
from django.conf.urls import patterns

from views import *


urlpatterns = [

    url(
        r'^$',
        ContactFormView.as_view(),
        name='contact_form',
    ),

    url(
        r'sent/$',
        ContactMessageReceivedView.as_view(),
        name='contactware_message_received',
    ),

]
