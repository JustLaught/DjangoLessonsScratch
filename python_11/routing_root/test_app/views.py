from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request, article_num, author="None"):
    return HttpResponse(f"Article #{article_num} | Author: {author}")