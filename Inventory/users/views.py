import json

from django.shortcuts import render, HttpResponse
from werkzeug.security import generate_password_hash, check_password_hash
import json
from .models import User

# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if is_ajax(request) and request.method == 'POST':
        successful_json = {'value': True}
        unsuccessful_json = {'value': False}
        try:
            newuser = User.objects.create(fullname=str(request.POST['fullname']), username=str(request.POST['username']), password=generate_password_hash(str(request.POST['password']),method='pbkdf2:sha256', salt_length=8), email=str(request.POST['email']))
            newuser.save()
            return HttpResponse(json.dumps(successful_json))
        except Exception as e:
            print(e, 'here')
            return HttpResponse(json.dumps(unsuccessful_json))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if is_ajax(request) and request.method == 'POST':
        print(request.POST)
        #handle incorrect username
        try:
            successful_json = {'value':True}
            currentUser = User.objects.get(username= str(request.POST['username']))
            currentUser_hash = currentUser.password
            if not check_password_hash(currentUser_hash, str(request.POST['password'])):
                pass_wrong = {'value':'pass'}
                return HttpResponse(json.dumps(pass_wrong))
            request.session['loggedin'] = True
            request.session['uid'] = currentUser.id
            return HttpResponse(json.dumps(successful_json))

        #handle incorrect password
        except Exception as e:
            # handleboth
            print('user does not exists')
            non_user = {'value':'both'}
            return HttpResponse(json.dumps(non_user))
