from django.http import JsonResponse


def index(request):
    return JsonResponse("hello accounts v2", safe=False)
