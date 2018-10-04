from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.utils.crypto import random
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import FormView, UpdateView

from .forms import *
from .models import *


class RiddlesListView(View):


    def get(self, request):
        riddles = Riddles.objects.all()
        levels = Level.objects.filter(riddles=riddles)

        ctx = {"riddles": riddles,
               "levels": levels,
               }
        return render(request, 'riddles/riddleslist_view.html', ctx)


def RiddleView(request, pk):
    riddle = get_object_or_404(Riddles, pk=pk)
    ctx = {"riddle":riddle}
    return render(request, 'riddles/riddle_view.html', ctx)


class RiddleFormView(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        riddle = Riddles.objects.get(pk=pk)
        z = MyUser.objects.get(user=request.user)
        done = DoneRiddles.objects.filter(my_user=z, riddles=riddle).exists()
        form = RiddleAnswer()
        return render(request, 'riddles/riddles_form.html', {"form":form, "riddle":riddle, "done":done})

    @method_decorator(login_required)
    def post(self, request, pk):
        riddle = Riddles.objects.get(pk=pk)
        form = RiddleAnswer(request.POST)

        z = MyUser.objects.get(user=request.user)
        done = DoneRiddles.objects.filter(my_user=z, riddles=riddle).exists()

        if form.is_valid():
            answer = form.cleaned_data['answer']
            if answer.lower() != riddle.answer.lower():

                return render(request, 'riddles/riddles_form.html', {"form": form, "riddle": riddle})
            else:
                z.points += riddle.points
                z.save()
                DoneRiddles.objects.create(riddles=riddle, my_user=z)


                return redirect(reverse('index'))
        else:
            return render(request, 'riddles/riddles_form.html', {"form": form, "riddle": riddle, "done": done})



# Rejestracja


def SignUp(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user.set_password(password1)
            user.save()

            MyUser.objects.create(user=user, points=0)

            user = authenticate(username=username, password=password1)
            # if user is not None:
            #     if user.is_active():
            login(request, user)
            return redirect('homepage')

        else:
            return render(request, 'riddles/signup_form.html', {'form': form})
    else:
        return render(request, 'riddles/signup_form.html', {'form': form})


def userDetails(request):
    # user = get_object_or_404(User, pk=user_id)
    # ctx = {
    #     'user' : user
    # }
    return render(request, 'riddles/user_profile.html')


def userDetails2(request, id):
    user = get_object_or_404(User, pk=id)
    ctx = {
        'user' : user
    }
    return render(request, 'riddles/user_profile.html', ctx)


class MyUserUpdate2(View):
    def get(self, request):
        form = MyUserUpdateForm(instance=request.user)
        return render(request, 'riddles/user-form.html', {"form" : form})

    def post(self, request):
        mu = MyUser.objects.get(user=request.user)
        form = MyUserUpdateForm(request.POST, instance=request.user, initial={'img': mu.img})

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            form.save()
            if first_name is not None and not mu.editname:
                mu.points += 1
                mu.editname = True
                mu.save()
            if email is not None and not mu.editmail:
                mu.points += 1
                mu.editmail = True
                mu.save()


            else:
                form.save()
                img = form.cleaned_data['img']
                if img is not None:
                    mu.points += 1
                    mu.editing = True
                else:
                    mu.img = img
                    mu.save()
            return redirect(reverse('user-profile'))
        else:
            return render(request, 'riddles/user-form.html', {"form": form})


class LevelsListView(View):

    @method_decorator(login_required)
    def get(self, request):

        level1 = Level.objects.get(pk=1)
        level2 = Level.objects.get(pk=2)
        mu = MyUser.objects.get(user=request.user)
        done = DoneRiddles.objects.filter(my_user=mu)
        myuser = MyUser.objects.all()

        l = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        solved = 0
        for d in done:
            if d.riddles.pk in l:
                solved += 1




        ctx = {
               "level1": level1,
                "level2": level2,
                "mu":mu,
                "done":done,
                "solved":solved,
                "myuser":myuser
               }
        return render(request, 'riddles/levelslistview.html', ctx)

class ChallistView(View):

    @method_decorator(login_required)
    def get(self, request):

        mu = MyUser.objects.get(user=request.user)
        done = DoneRiddles.objects.filter(my_user=mu)
        solved = 0
        l = [0, 1, 2, 3, 4, 5]
        for d in done:
            if d.riddles.pk in l:
                solved += 1


        ctx = {
            "mu": mu
        }
        return render(request, 'riddles/challist_view.html', ctx)


class CuriosityView(View):
    def get(self, request):
        a = random.randint(1,5)
        done = Curiosity.objects.get(pk=1)

        ctx = { "done": done}

        return render(request, 'riddles/costam.html',ctx)


class Ranking(View):
    def get(self, request):

        myuser = MyUser.objects.all().order_by('-points')

        ctx ={
              'myuser': myuser}

        return render(request, 'riddles/rank.html', ctx)

class HomePageView(View):
    def get(self,request):
        myuser = MyUser.objects.all().order_by('-points')
        a = random.randint(1, 5)
        done = Curiosity.objects.get(pk=a)
        ctx = {
            "myuser":myuser,
            "done":done
        }

        return render(request, 'riddles/homepage.html', ctx)





# Create your views here.
