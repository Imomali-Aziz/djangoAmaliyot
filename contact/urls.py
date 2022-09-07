from django.urls import path
from .views import ContactView, ContactListView

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('xabarlar/', ContactListView.as_view(), name='xabarlar'),
]