from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.views.generic import View

from .models import Topic, Comment
from .forms import CommentForm, TopicForm


class TopicList(View):
    def get(self):
        pass


@login_required(login_url='/accounts/login/')
def topic_list(request):
    topics = list(Topic.objects.all())
    form = CommentForm()
    if topics:
        comments = Comment.objects.all().filter(topic=topics[0])
        latest = topics[0]
        show_form = True
    else:
        comments = 'After you create a new topic, you can comment on it.'
        latest = 'Create a new Topic.'
        show_form = False
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.topic = latest
            comment.save()
            return HttpResponseRedirect(reverse('topics:topic-list'))

    return render(request, 'messageboard/topic-list.html', {
        'topics': topics,
        'comments': comments,
        'latest': latest,
        'form': form,
        'show_form': show_form
    })


@login_required(login_url='/accounts/login/')
def topic_detail(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    comments = Comment.objects.all().filter(topic=topic)
    form = CommentForm()
    if request.method == 'POST':
        if form.is_valid():
            form = CommentForm(request.POST)
            form.save(commit=False)
            form.author = request.user
            form.save()
    return render(request, 'messageboard/topic-detail.html', {
        'topic': topic,
        'comments': comments,
        'form': form
    })


@login_required(login_url='/accounts/login/')
def topic_create(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics:topic-list'))
    else:
        form = TopicForm()
    return render(request, 'messageboard/topic-create.html', {
        'form': form
    })


def topic_delete(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method == 'POST':
        topic_to_delete = Topic.objects.get(id=topic_id)
        topic_to_delete.delete()
        return HttpResponseRedirect(reverse('topics:topic-list'))
    return render(request, 'messageboard/topic-confirm.html', {
        'topic': topic
    })
