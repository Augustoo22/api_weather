from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpRequest, HttpResponse, JsonResponse
from .authentication import *
from .models import UserEntity
from .forms import UserForm
from .repositories import UserRepository

class UserTokenizer(View):
    # método deveria ser POST, pois deverá receber usuario e senha
    def get(self, request):
        user = authenticate(username='user', password='a1b2c3')
        if user:
            return HttpResponse(generateToken(user))
        return HttpResponse('Username and/or password incorret')

class UserRegister(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'user_register.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            repository = UserRepository(collectionName='users')
            repository.insert(data)
            return redirect('Weather View')
        else:
            return JsonResponse({"error": form.errors}, status=400)