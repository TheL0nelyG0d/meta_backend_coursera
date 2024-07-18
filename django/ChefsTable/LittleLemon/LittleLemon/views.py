from django.http import HttpResponse,HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse("404: The Page you have searched can not be found at the moment. Please try another time! <br><br> <button onclick="" href='';""> Go to Homepage</button>")