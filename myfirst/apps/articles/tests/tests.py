from django.test import TestCase
from django.test import Client
from django.utils import timezone
import datetime
from django.urls import reverse
from django.shortcuts import render, redirect
from ..models import Comment, Article
from django.contrib.auth.models import User
from ..views import *
from myfirst.apps.articles.autocorrection import *


class ArticleTestCase(TestCase):
    def setUp(self):
        txt = "Operation Grappled was a series of British nuclear weapons tests carried out in 1957 and 1958 at " \
              "Maiden Island and Christmas Island in what is now Kiribati. Britain had successfully tested an atomic " \
              "bomb in October 1952, and in July 1954, decided to develop a hydrogen bomb. In the first test, " \
              "Grappled 1 (pictured), the bomb's yield was below its designed capability. The second, Grappled 2, " \
              "was the largest ever achieved by a single-stage device. The third, Grappled 3, also had a low yield. " \
              "A further test, Grappled X, exceeded expectations. Grappled Y, in April 1958, yielded about three " \
              "megatonnes and remains the most powerful British nuclear weapon ever tested. Much of its yield came " \
              "from its thermonuclear reaction, making it a true hydrogen bomb, and the United Kingdom became the " \
              "third nation to possess one. A final series of four tests, Grappled Z, tested technique for making " \
              "bombs immune to predestination by nearby nuclear explosions. (This article is part of a features " \
              "topic: Nuclear weapons and the United Kingdom.)"
        user1 = User.objects.create_user(username='first')
        user2 = User.objects.create_user(username='second')
        user1.article_set.create(article_title='Title', article_text=txt, pub_date=timezone.now())
        user2.article_set.create(article_title='The title of the second user', article_text='Not so much',
                                 pub_date=timezone.now() - datetime.timedelta(days=8))

    def test_article_describe(self):
        """Article.describe() works correctly"""
        short_txt = "Operation Grappled was a series of British nuclear " \
                    "weapons tests carried out in 1957 and 1958 at Mai"
        long = Article.objects.get(article_title="Title")
        short = Article.objects.get(article_title="The title of the second user")
        self.assertEqual(long.describe(), short_txt)
        self.assertEqual(short.describe(), 'Not so much')

    def test_article_was_published_recently(self):
        """Article.was_published_recently works correctly"""
        long = Article.objects.get(article_title="Title")
        short = Article.objects.get(article_title="The title of the second user")
        self.assertTrue(long.was_published_recently())
        self.assertFalse(short.was_published_recently())


    def test_article___str__(self):
        """Article.__str__() works correctly"""
        long = Article.objects.get(article_title="Title")
        short = Article.objects.get(article_title="The title of the second user")
        self.assertEqual(long.__str__(), 'Title')
        self.assertEqual(short.__str__(), 'The title of the second user')


class CommentTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='first')
        a = user.article_set.create(article_title='title', article_text='text', pub_date=timezone.now())
        a.comment_set.create(comment_user=user, comment_text='correct_comment_text', com_date=timezone.now())

    def test_comment___str__(self):
        """Comment.__str__() works correctly"""
        user = User.objects.get(username='first')
        com = Comment.objects.get(comment_user=user)
        self.assertEqual(com.__str__(), 'correct_comment_text')


class ArticlesListViewTest(TestCase):

    def setUp(self):
        user_staff = User.objects.create_user(username='staff', password='secret', is_staff=True)
        number = 2
        for num in range(1, number):
            user = User.objects.create_user(username='user' + str(num), password='secret')
            a = user.article_set.create(article_title='title'+str(num), article_text='text', pub_date=timezone.now())
            a.comment_set.create(comment_user=user,
                                 comment_text='correct_comment_text', com_date=timezone.now())

    def test_view_index_absolute_url(self):
        """index absolute url"""
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_index_unautorized(self):
        """index if unautorized"""
        resp = self.client.get('')
        html = str(resp.content)
        line = 'Sign In'
        line2 = 'Sign Up'
        self.assertTrue(line in html and line2 in html)

    def test_view_index_autorized(self):
        """index if autorized"""
        c = Client()
        c.login(username='user1', password='secret')
        resp = c.get('')
        html = str(resp.content)
        line = 'Sign Out'
        self.assertTrue(line in html)

    def test_view_index_url_template(self):
        """index correct template"""
        resp = self.client.get(reverse('articles:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'articles/list.html')

    def test_view_detail_absolute_url(self):
        """details absolute url"""
        resp = self.client.get('/1/')
        self.assertEqual(resp.status_code, 200)

    def test_view_detail_url_template(self):
        """detail correct template"""
        resp = self.client.get(reverse('articles:detail', args=(1,)))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'articles/detail.html')

    def test_view_leave_comment_absolute_url(self):
        """leave comment correct absolute url"""
        resp = self.client.post(reverse('articles:detail', args=(1,)),
                                data={'name': 'commentator', 'text': 'comment text'})
        self.assertEqual(resp.status_code, 200)

    def test_view_leave_comment_create(self):
        """leave comment really suceed"""
        c = Client()
        c.login(username='user1', password='secret')
        user = User.objects.get(username='user1')
        article = user.article_set.get(id=1)
        resp = c.post(reverse('articles:detail', args=(article.id,)), data={'name': user.username, 'text': 'comment text'})
        self.assertTrue(article.comment_set.filter(comment_user=user).exists())

    def test_view_added_autorized(self):
        """added request correct"""
        c = Client()
        c.login(username='user1', password='secret')
        user = User.objects.get(username='user1')
        resp = c.post(reverse('articles:added', args=(user.id,)), data={'name': 'author', 'text': 'article text'})
        self.assertEqual(resp.status_code, 302)

    def test_view_added_create(self):
        """added article was really succeed"""
        c = Client()
        c.login(username='user1', password='secret')
        user = User.objects.get(username='user1')
        resp = c.post(reverse('articles:added', args=(user.id,)), data={'name': 'test title', 'text': 'article text'})
        self.assertTrue(user.article_set.filter(article_title='test title').exists())

    def test_view_addarticle_absolute_url(self):
        """addarticle absolute url"""
        resp = self.client.get('/addarticle/')
        self.assertEqual(resp.status_code, 200)

    def test_view_addarticle_unautorized(self):
        """addarticle view if unautorized"""
        resp = self.client.get('/addarticle/')
        html = str(resp.content)
        line = '<h1>You have to <a href="/login/">sign in</a> firstly</h1>'
        self.assertTrue(line in html)

    def test_view_addarticle_autorized(self):
        """addarticle view if autorized"""
        c = Client()
        c.login(username='user1', password='secret')
        resp = c.get('/addarticle/')
        html = str(resp.content)
        line = '<h1>You have to ask to <a href="/addarticle/ask/2/">become an author</a> firstly</h1>'
        self.assertTrue(line in html)

    def test_view_addarticle_staff(self):
        """addarticle view if autorized"""
        c = Client()
        c.login(username='staff', password='secret')
        resp = c.get('/addarticle/')
        html = str(resp.content)
        line = '<h1>Add Article</h1>'
        self.assertTrue(line in html)

    def test_view_addarticle_url_template(self):
        """addarticle correct template"""
        resp = self.client.get(reverse('articles:addarticle'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'articles/addarticle.html')


class AutocorrectionTest(TestCase):

    def test_correct_text_incorrect(self):
        """Correct text works correctly with typo"""
        correct = correct_text('well helllo')
        self.assertEqual(correct, 'well hello')

    def test_correct_text_correct(self):
        """Correct text works correctly without typo"""
        correct = correct_text('How are you, my friend?')
        self.assertEqual(correct, 'How are you, my friend?')