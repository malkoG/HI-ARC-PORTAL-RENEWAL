from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect


from hiarc_registration.forms import HiarcUserCreationForm
# Create your views here.

@csrf_protect
def register_user(request):
    if request.method == 'POST':
        form = HiarcUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    args = {}

    args['form'] = HiarcUserCreationForm()

    return render(request,'hiarc_registration/register.html', args)