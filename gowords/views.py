
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from models import Goword

def go(request, slug):
    keyword = get_object_or_404(Goword, slug=slug)
    
    return HttpResponseRedirect(keyword.url)

#def search(request):
#    """
#    Use the 'go' parameter from the get or post data to lookup the goword
#    if no url provided show gowords/search.html template which includes a search form.
#    """
#    pass