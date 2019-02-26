from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from forms import OFXForm
from models import OFXFileTask

@login_required
def transaction_list(request):
    return render(request, 'transactions/templates/transaction_list.html', {})
    
@login_required
def files(request):
    saved = False
   
    # Handle file upload
    if request.method == 'POST':
        form = OFXForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = OFXFileTask(file=request.FILES['ofxfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('files'))
    else:
        form = OFXForm()  # A empty, unbound form

    # Load documents for the list page
    files = OFXFileTask.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'transactions/templates/files.html',
        {'files': files, 'form': form})