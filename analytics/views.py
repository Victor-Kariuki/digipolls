from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World! this is your truly analytics")
