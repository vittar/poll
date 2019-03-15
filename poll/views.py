from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import Poll, Question, Choice, Vote

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth.decorators import login_required

def polls_list(request):
    polls = Poll.objects.all()
    return render(request, 'poll/index.html', context={'polls': polls})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('polls_list_url'))
        else:
            messages.error(request, 'uncorrect name or password')
    return render(request, 'poll/login.html', {})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('polls_list_url'))

@login_required(login_url='/poll/login/')
def poll_detail(request, slug):
    poll = Poll.objects.get(slug__iexact=slug)
#    poll = get_object_or_404(Poll, slug__iexact=slug)  # try it later
    user_can_vote = poll.user_can_vote(request.user)
#    results = poll.get_results_dict()
    return render(request, 'poll/poll_detail.html', context={'poll': poll, 'user_can_vote': user_can_vote, 'results': poll.get_results_dict()})


def poll_vote(request, slug):
#    print(request.POST.items)
    poll = Poll.objects.get(slug__iexact=slug)

    if not poll.user_can_vote(request.user):
        messages.error(request, 'You are already voted')
        return render(request, 'poll/poll_detail.html', context={'poll': poll})

    all_questions = len(poll.questions.all())
    send_questions = []
    for i in request.POST.items():
#        print(i)
        if 'choice' in i[0]:
            send_questions.append(i[1])
#            print(send_questions)
    if len(send_questions) != all_questions:
#            print(send_questions)
            messages.error(request, 'You should chioce all answers')
            return render(request, 'poll/poll_detail.html', context={'poll': poll})
    else:
        for i in send_questions:
            answer_id = i
            answer = Choice.objects.get(id=answer_id)
#            print(answer)
            new_vote = Vote(user=request.user, poll=poll, choice=answer)
            print(new_vote)
            new_vote.save()
#            answer.is_answered += 1
#            answer.save()
        return render(request, 'poll/poll_result.html', {'poll': poll})
