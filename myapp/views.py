from django.shortcuts import redirect, render
from myapp.forms import ClientForm
from myapp.models import Immobile

def list_location(request):
    immobiles = Immobile.objects.filter(is_locate=False)
    context = {'immobiles': immobiles}
    return render(request, 'list-location.html', context)

def form_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_location')
    return render(request, 'form-client.html', {'form': form})