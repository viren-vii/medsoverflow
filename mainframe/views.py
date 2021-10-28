from django.contrib import auth
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect, request
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib.auth.models import User as authUser
from django.utils.decorators import method_decorator
from .filters import QuestionFilter
# Create your views here.

class Register(TemplateView):
    def get(self, request):
        form = CreateUserForm()
        
        context = {'form' : form, 'myuser' : Home.getUser(self, request)}
        return render(request, 'register.html', context)
    
    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            authU = authUser.objects.get(username = request.POST.get('username'))
            usr = User(user=authU, username=request.POST.get('username'), email_id=request.POST.get('email'))
            usr.save()
            messages.success(request, 'Hello '+ form.cleaned_data.get('username') +'! You are registered succesfully!')
            return redirect('/login')
    
        context = { 'form' : form}
        
        return render(self.request, 'register.html', context)

class Login(TemplateView):
    def get(self, request):

        context = {'myuser' : Home.getUser(self, request)}

        return render(request, 'login.html', context)
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect')
        
        return redirect('/login')

class Logout(TemplateView):
    def get(self, request):
        logout(request)
        return redirect('/login')

class Home(TemplateView):
    def getUser(self, request):
        if request.user.is_authenticated:
            usr = request.user
            myuser = User.objects.get(username = usr.username)
            return myuser
        return 

    def get(self, request):

        isLoggedIn = False
        if request.user.is_authenticated:
            usr = request.user
            isLoggedIn = True
        questions = Question.objects.all().order_by('-created_at') 
        myFilter = QuestionFilter(request.GET, queryset=questions)
        questions = myFilter.qs

        myuser = self.getUser(request)
        context = {'questions': questions, 'isLoggedIn' : isLoggedIn, 'myuser' : myuser, 'myFilter' : myFilter}

        return render(request, 'main_feed.html', context)

class Profile(TemplateView):
    def get(self, request, pk):
        user = User.objects.all().get(id=pk)
        answers = Answer.objects.filter(made_by__pk=pk)
        questions = Question.objects.filter(made_by__pk=pk)
        comments = Comment.objects.all().filter(made_by__pk=pk).count()
        myuser = Home.getUser(self, request)
        context = {'pk' : pk, 'user' : user, 'questions' : questions, 'answers' : answers, 'comments' : comments, 'myuser' : myuser}

        return render(request, 'profile.html', context)

class Post(TemplateView):
    def get(self, request, pk):
        
        answerForm = AnswerForm()
        commentForm = CommentForm()
        question = Question.objects.get(id=pk)
        comments = Comment.objects.filter(question = question.id)
        answers = Answer.objects.filter(question = question.id).order_by('-created_at')
        qMarked = Bookmark.objects.filter(user = (Home.getUser(self, request)).id, question = question.id).exists()

        answerUpvotes = UpvoteA.objects.filter(by = (Home.getUser(self, request)).id)
        print(answerUpvotes)
        answerUpvotesUserId = [ x.answer for x in answerUpvotes]

        isAccepted = 'no'

        for a in answers:
            if a in answerUpvotesUserId:
                setattr(a, 'voted', 'True')
            answerComments = CommentAnswer.objects.filter(answer = a.id)
            setattr(a, 'comments',answerComments)
            answerCommentForm = AnswerCommentForm()
            setattr(a, 'answerCommentForm',answerCommentForm)
            if a.accepted:
                isAccepted = a.id
        context = {
            'question': question,
            'comments': comments,
            'answers' : answers,
            'answerForm' : answerForm,
            'commentForm' : commentForm,
            'myuser' : Home.getUser(self, request),
            'qMarked' : qMarked,
            'accepted' : isAccepted,
        }
        return render(request, 'post.html', context)

    @method_decorator(login_required(login_url='/login'))
    def post(self, request, pk):
        if 'Answer' in request.POST:
            print("In answer")
            form = AnswerForm(request.POST)
        elif 'Comment' in request.POST:
            print("In Comment")
            form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.made_by = User.objects.get(id=Home.getUser(self, request).id)
            q = Question.objects.get(id=pk)
            obj.question = q
            if 'Answer' in request.POST:
                q.answerCount += 1
                q.save()
            form.save()

        return HttpResponseRedirect(request.path_info)

class AnswerComment(TemplateView):
    def get(self, request, apk, qpk):
        return
    def post(self, request, apk, qpk):
        form = AnswerCommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.made_by = User.objects.get(id=Home.getUser(self, request).id)
            obj.answer = Answer.objects.get(id=apk)
            form.save()
        print(request.path_info)
        return HttpResponseRedirect('/question/'+str(qpk))


class AcceptAnswer(TemplateView):
    def get(self, request, apk, qpk):
        return
    def post(self, request, apk, qpk):
        answer = Answer.objects.get(id=apk)
        if answer.accepted:
            answer.accepted = False
        else:
            answer.accepted = True

        return HttpResponseRedirect('/question/'+str(qpk))
    

class AskQuestion(TemplateView):
    form = QuestionForm()
    def get(self, request):
        myuser = Home.getUser(self, request)
        context = {'form': self.form, 'myuser' : myuser}
        return render(request, 'frame_question.html', context)

    def post(self, request):
        form = QuestionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            usr = Home.getUser(self, request)
            obj.made_by = User.objects.get(id = usr.id)
            form.save()
            return redirect('/')


class TagFilter(TemplateView):
    def get(self, request, pk):
        questions = Question.objects.filter(tags__id=pk)
        context = { 'questions' : questions, 'myuser' : Home.getUser(self, request)}

        return render(request, 'main_feed.html', context)

class Tags(TemplateView):
    def get(self, request):
        tags = Tag.objects.all()
        context = { 'myuser' : Home.getUser(self, request), 'tags' : tags}
        return render(request, 'tags.html', context)

class AllUsers(TemplateView):
    def get(self, request):
        users = User.objects.all()
        context = { 'myuser' : Home.getUser(self, request), 'users' : users}
        return render(request, 'users.html', context)

class UpvoteQClass(TemplateView):
    def get(self, request, qpk):
        return
    def post(self, request, qpk):
        q = Question.objects.get(id = qpk)
        u = Home.getUser(self, request)
        upvoteQ, createdUV = UpvoteQ.objects.get_or_create(question = q, by = u)
        downvoteQ = DownvoteQ.objects.filter(question = q, by = u).exists()
        if createdUV:
            if downvoteQ:
                DownvoteQ.objects.get(question = q, by = u).delete()
                request.session['down'] = False
            request.session['up'] = True
            upvoteQ.save()
        else:
            request.session['up'] = False
            upvoteQ.delete()

        return redirect('/question/'+str(qpk))

class DownvoteQClass(TemplateView):
    def get(self, request, qpk):
        return
    def post(self, request, qpk):
        q = Question.objects.get(id = qpk)
        u = Home.getUser(self, request)
        downvoteQ, createdDV = DownvoteQ.objects.get_or_create(question = q, by = u)
        upvoteQ = UpvoteQ.objects.filter(question = q, by = u).exists()

        if createdDV:
            if upvoteQ:
                UpvoteQ.objects.get(question = q, by = u).delete()
                request.session['up'] = False
            request.session['down'] = True
            downvoteQ.save()
        else:
            downvoteQ.delete()
            request.session['down'] = False

        return redirect('/question/'+str(qpk))


class BookmarkClass(TemplateView):
    def get(self, request, qpk):
        return
    def post(self, request, qpk):
        q = Question.objects.get(id = qpk)
        u = Home.getUser(self, request)
        bookmark, created = Bookmark.objects.get_or_create(question = q, user = u)
        if created:
            bookmark.save()
        else:
            bookmark.delete()
        return redirect('/question/'+str(qpk))

class UpvoteAClass(TemplateView):
    def get(self, request, qpk):
        return
    def post(self, request, qpk, apk):
        print("working")
        a = Answer.objects.get(id = apk)
        u = Home.getUser(self, request)
        upvoteA, createdUV = UpvoteA.objects.get_or_create(answer = a, by = u)
        if not createdUV:
            upvoteA.delete()
        return redirect('/question/'+str(qpk))