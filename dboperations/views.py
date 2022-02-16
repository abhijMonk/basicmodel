from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from . models import Author
from . models import Articles
from . models import Blog
from . models import Category

def index(request):

    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')
#    return HttpResponse("Hello, world. You're at view created by me")

''' 
    return HttpResponse(
        <form action="/action_page.php" method="get">
          <label for="fname">First name:</label>
          <input type="text" id="fname" name="fname"><br><br>
          <label for="lname">Last name:</label>
          <input type="text" id="lname" name="lname"><br><br>
          <input type="submit" value="Submit">
        </form>
    )
'''
def get_author(request, author_first_name):
    if request.method == 'GET':
        try:
            author = Author.objects.get(first_name=author_first_name)
            response = json.dumps([{'First Name': author.first_name, 'Second Name':author.last_name, 'About': author.about}])
        except:
            response = json.dumps([{'Info': 'No author with that name'}])
    return HttpResponse(response, content_type= 'text/json')

@csrf_exempt
def add_author(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        first_name = payload['first_name']
        last_name = payload['last_name']
        about = payload['about']
        author = Author(first_name= first_name, last_name=last_name, about=about)
        try:
            author.save()
            response= json.dumps([{'Success': 'Author added Successfully!'}])
        except:
            response= json.dumps([{'Info': 'Author could not added!'}])
    return HttpResponse(response, content_type='text/json')

