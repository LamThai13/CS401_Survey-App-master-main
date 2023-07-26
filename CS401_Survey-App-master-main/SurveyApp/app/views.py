from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreatePollForm, CreateEntityForm, CreateRatingQuestionForm
from .models import Poll, CreateUserForm, Entity, Rating
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateUserForm()
    context = {'form':form}
    return render(request,'register.html',context)


def loginPage(request):
    if request.user.is_authenticated:
        user = request.user
        polls = Poll.objects.all()
        context = {'polls':polls}
        return render(request,'home.html',context)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'user or password is not correct!')
    context = {}
    return render(request,'login.html',context)

def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        print("logged out succesfully")
    return redirect('login')

def home(request):
    question = Entity.objects.all()
    #polls = Poll.objects.all()
    context = {'question': question}
    return render(request,'home.html',context)

def homeRating(request):
#    Entry.objects.values_list('column_name', flat=True).filter(condition)
#    rating = Rating.objects.all()
    rate_question = Rating.objects.values_list('rate_question',flat=True)
    score = Rating.objects.values_list('score',flat=True)
  
    context = {'rate_question':rate_question, 'score':score}
    print(context)
    return render(request, 'homeRating.html',context)

def create(request):
    if request.method == 'POST':
        poll_form = CreatePollForm(request.POST)
        entity_form = CreateEntityForm(request.POST)
        if poll_form.is_valid() and entity_form.is_valid():
            entity = entity_form.save()
            newpoll = poll_form.save(commit=False)
            newpoll.questionId = entity
            newpoll.save()
            return redirect('home')
    else:
        poll_form = CreatePollForm()
        entity_form = CreateEntityForm()
    context = {'poll_form':poll_form, 'entity_form': entity_form,}
    return render(request,'create.html',context)

def createRatingQuestion(request):
    if request.method =='POST':
        rating_form = CreateRatingQuestionForm(request.POST)
        if rating_form.is_valid():
            rating = rating_form.save()
            return redirect('homeRating')
    else:
        rating_form = CreateRatingQuestionForm()
    context = {'rating_form':rating_form}
    return render(request,'createRating.html',context)


def vote(request, entity_id):
    entity = Entity.objects.get(pk=entity_id)
    poll = Poll.objects.get(questionId=entity)   
    if request.method == 'POST':
        selected = request.POST['poll']
        if selected == 'option1':
            poll.option_count_one +=1
        elif selected == 'option2':
            poll.option_count_two +=1
        elif selected == 'option3':
            poll.option_count_three +=1
        elif selected == 'option4':
            poll.option_count_four +=1
        elif selected == 'option5':
            poll.option_count_five +=1
        else:
            return HttpResponse(400,'Invalid')
        poll.save()

        return redirect('result',entity_id)
    context = {'entity':entity, 'poll':poll }
    return render(request,'vote.html',context)

def rating(request, rate_id):
    rating = Rating.objects.get(pk=rate_id)
    if request.method == 'POST':
        selected = request.POST['rate']
        if selected == 'first':
            rating.score =1
        elif selected == 'second':
            rating.score =2
        elif selected == 'third':
            rating.score =3
        elif selected == 'fourth':
            rating.score =4
        elif selected == 'fifth':
            rating.score =5
        else:
            return HttpResponse(400,'Invalid')
        rating.save()

        return redirect('homeRating')
    context = {'rating':rating }
    return render(request, 'rating.html', context)

def result(request, entity_id):
    entity = Entity.objects.get(pk=entity_id)
    poll = Poll.objects.get(questionId=entity)
    
    context = {'entity':entity,'poll':poll}
    return render(request,'result.html',context)
