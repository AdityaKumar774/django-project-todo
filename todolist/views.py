# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo


def index(request):
    todolist = Todo.objects.all()[:50]
    context = {
        'todolist': todolist
    }
    return render(request, 'index.html', context)
