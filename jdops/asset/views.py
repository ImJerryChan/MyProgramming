# coding: utf-8
from __future__ import unicode_literals

from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html', {})


def menu(request):
    return render_to_response('menu.html', {})


def host(request):
    return render_to_response('host.html', {})


def main(request):
    return render_to_response('main.html', {})
