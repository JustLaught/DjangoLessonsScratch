from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    context = {
        'name': 'Jose',
        'age':'25',
        'email': 'test@email.com',
        'data': []
    }
    
    if request.method == "POST":
        return redirect('new_app:thank_you_site')
    
    if request.POST:
        context = {
                "name": request.POST["new_name"],
                "age": request.POST["new_age"],
                "email": request.POST["new_email"]
            } 

    # if request.method == "GET":
    #     if not request.GET:
    #         context = {
    #             'name': 'Jose',
    #             'age':'25',
    #             'email': 'test@email.com'
    #         }
    #     else: 
    #         context = {
    #             "name": request.GET["new_name"],
    #             "age": request.GET["new_age"],
    #             "email": request.GET["new_email"]
    #         }    

    # elif request.method == "POST":
    #     if not request.POST:
    #         context = {
    #         'name': 'Jose',
    #         'age':'25',
    #         'email': 'test@email.com'
    #     }
    #     else: 
    #         context = {
    #             "name": request.POST["new_name"],
    #             "age": request.POST["new_age"],
    #             "email": request.POST["new_email"]
    #         }

    return render(request , 'index.html', context)


def second_page(request):
    return HttpResponse('<h1>Thank you!</h1>')