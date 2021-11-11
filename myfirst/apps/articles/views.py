from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Article, Comment
from .forms import *

from django.urls import reverse

from django.utils import timezone

from myfirst.apps.articles.autocorrection import correct_text

def index(request, size=10):
    latest_articles_list = Article.objects.order_by('-pub_date')#[:size]
    return render(request, 'articles/list.html', {'latest_articles_list':latest_articles_list})


def detail(request, article_id, size=10):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Not found')
    latest_comments_list = a.comment_set.order_by('-id')#[:size]
    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Not found')

    raw_comment_text = request.POST['text']
    correct_comment_text = correct_text(raw_comment_text)
    a.comment_set.create(author_name=request.POST['name'], comment_text=correct_comment_text, com_date=timezone.now())

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))


def addarticle(request):
    return render(request, 'articles/addarticle.html')


def added(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except:
        raise Http404('Not found')
    raw_article_text = request.POST['text']
    correct_article_text = correct_text(raw_article_text)
    user.article_set.create(article_title=request.POST['name'], article_text=correct_article_text, pub_date=timezone.now())
    # a.save()

    return HttpResponseRedirect(reverse('articles:addarticle'))


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'articles/register.html'
    success_url = reverse_lazy('articles:login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'articles/login.html'


def logout_user(request):
    logout(request)
    return redirect('articles:login')


