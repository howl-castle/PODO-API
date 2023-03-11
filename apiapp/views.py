from django.shortcuts import render
from .models import *
from rest_framework.views import APIView 
from rest_framework.decorators import api_view
from rest_framework.response import Response

# signup

# add phantom wallet

# singin

# signout

# 

"""
# article list
@api_view (['GET'])
def article_list(request) : 
    articles = Article.objects.all()
    return Response(request, articles)

# article detail
@api_view (['GET'])
def article_detail(request, pk) :
    article = Article.objects.get(pk=pk)
    return Response(request, article)

# create article
@api_view (['POST'])
def article_create(request) : 
    article = Article.objects.create(
        title = request.data['title'], 
        content = request.data['content'])
    return Response(request, article)

# update article
@api_view (['PUT'])
def article_update(request, pk) : 
    article = Article.objects.get(pk=pk)
    if article.user == request.user :
        article.title = request.data['title']
        article.content = request.data['content']
        article.save()
        return Response(request, article)
    else :
        return Response(request, 'you are not the author')

# delete article
@api_view (['DELETE'])
def article_delete(request, pk) :
    article = Article.objects.get(pk=pk)
    if article.user == request.user :
        article.delete()
        return Response(request, article)
    else :
        return Response(request, 'you are not the author')

#create comment
@api_view(['POST'])
def comment_create(request, pk) : 
    article = Article.objects.get(pk=pk)
    comment = Comment.objects.create(
        article = article,
        content = request.data['content'])
    return Response(request, comment)

# comment detail
@api_view(['GET'])
def comment_detail(request, pk) :
    comment = Comment.objects.get(pk=pk)
    return Response(request, comment)

# update comment
@api_view(['PUT'])
def comment_update(request, pk) :
    comment = Comment.objects.get(pk=pk)
    if comment.user == request.user :
        comment.content = request.data['content']
        comment.save()
        return Response(request, comment)
    else :
        return Response(request, 'you are not the author')

# delete comment
@api_view(['DELETE'])
def comment_delete(request, pk) :
    comment = Comment.objects.get(pk=pk)
    if comment.user == request.user :
        comment.delete()
        return Response(request, comment)
    else :
        return Response(request, 'you are not the author')


# comment list
@api_view(['GET'])
def comment_list(request, pk) :
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.all()
    return Response(request, comments)

# create question
@api_view(['POST'])
def question_create(request) : 
    question = Question.objects.create(
        title = request.data['title'], 
        content = request.data['content'])
    return Response(request, question)

# update question
@api_view(['PUT'])
def question_update(request, pk) : 
    question = Question.objects.get(pk=pk)
    question.title = request.data['title']
    question.content = request.data['content']
    question.save()
    return Response(request, question)

# delete question
@api_view(['DELETE'])
def question_delete(request, pk) :
    question = Question.objects.get(pk=pk)
    question.delete()
    return Response(request, question)

# questions list
@api_view(['GET'])
def question_list(request) :
    questions = Question.objects.all()
    return Response(request, questions)

# question detail
@api_view(['GET'])
def question_detail(request, pk) :
    question = Question.objects.get(pk=pk)
    return Response(request, question)

# create answer
@api_view(['POST'])
def answer_create(request, pk) :
    question = Question.objects.get(pk=pk)
    answer = Answer.objects.create(
        question = question,
        content = request.data['content'])
    return Response(request, answer)

# update answer
@api_view(['PUT'])
def answer_update(request, pk) :
    answer = Answer.objects.get(pk=pk)
    answer.content = request.data['content']
    answer.save()
    return Response(request, answer)

# delete answer
@api_view(['DELETE'])
def answer_delete(request, pk) :
    answer = Answer.objects.get(pk=pk)
    answer.delete()
    return Response(request, answer)

# answer list
@api_view(['GET'])
def answer_list(request, pk) :
    question = Question.objects.get(pk=pk)
    answers = question.answer_set.all()
    return Response(request, answers)

# answer detail
@api_view(['GET'])
def answer_detail(request, pk) :
    answer = Answer.objects.get(pk=pk)
    return Response(request, answer)

# answer choose
@api_view(['PUT'])
def answer_choose(request, pk) :
    answer = Answer.objects.get(pk=pk)
    answer.STATUS_CHOICES = 'CHOSEN'
    answer.save()
    return Response(request, answer)

"""