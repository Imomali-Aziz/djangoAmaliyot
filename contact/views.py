from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Contact

# Create your views here.
class ContactView(CreateView):
    model = Contact
    template_name = 'form.html'
    fields = ['ismingiz', 'familiyangiz', 'telefon', 'email', 'xabar']

class ContactListView(ListView):
    model = Contact
    template_name = 'xabarlar.html'
