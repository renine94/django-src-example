from django.http import JsonResponse


# Create your views here.
def index(request):
    return JsonResponse("hello board world v2", safe=False)
