from django.db.models.fields import EmailField
from django.shortcuts import redirect, render
from .models import Url
import uuid
from django.http import HttpResponse
# Create your views here.
def index(request):
    diction = {}
    if request.method =='POST':
        newUrl = Url()
        newUrl.url = request.POST.get('link')
        newUrl.uuid = str(uuid.uuid4())[:7]
        newUrl.save()
        diction.update({'uuid':newUrl.uuid})
    return render(request, 'index.html', context=diction)

def link(request, pk):
    gotoLink = Url.objects.get(uuid=pk)
    return redirect(gotoLink.url)