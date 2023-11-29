from django.shortcuts import render

# Create your views here.a
# views.py in the qanda app
from django.shortcuts import render, redirect
from .models import Question, Answer,Like
from .forms import QuestionForm, AnswerForm,LikeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_url')
def post_question(request):
    form=QuestionForm()
    template_name='AppQueAns/post_question.html'
    if request.method=='POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user  # Set the user attribute
            question.save()
            return redirect('showque_url')
    context={'form':form}
    return render(request, template_name,context)

@login_required(login_url='login_url')
def question_list(request):
    obj= Question.objects.all()
    template_name='AppQueAns/question_list.html'
    context={'data':obj}
    return render(request,template_name,context)


@login_required(login_url='login_url')
def post_answer(request):
    form=AnswerForm()
    template_name='AppQueAns/post_answer.html'
    if request.method=='POST':
        form=AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user  # Set the user attribute to the logged-in user
            answer.save()
            return render('addqueans_url')
            
    context={'form':form}
    return render(request, template_name,context)

@login_required(login_url='login_url')
def queans_list(request):
    questions = Question.objects.all()
    answers = Answer.objects.all()
    template_name = 'AppQueAns/quesans_list.html'
    context = {'questions': questions, 'answers': answers}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def addlike(request):
    form=LikeForm()
    template_name='AppQueAns/post_like.html'
    if request.method=='POST':
        form=LikeForm(request.POST)
        if form.is_valid():
           like = form.save(commit=False)
           like.user = request.user  # Set the user attribute to the logged-in user
           like.save()
           return render('displaylikes_url')
           
            
    context={'form':form}
    return render(request, template_name,context)

@login_required(login_url='login_url')
def display_likes(request):
    likes = Like.objects.all()
    answers = Answer.objects.all()
    template_name = 'AppQueAns/display_likes.html'
    context = {'questions': likes, 'answers': answers}
    return render(request, template_name, context)

