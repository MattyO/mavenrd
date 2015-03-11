from shutil import move
import os

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib import messages
from django.contrib.messages import constants as messages

from common.helpers import jsonify, resolve_http_method
from common.forms import ContactForm

from mavenrd import settings
from cms.helpers import nav, standard_context
from cms.models import Page, Post, UploadedMedia, MediaCollection
from cms import page_data

def get_page_data(name):
    #replace dash with underscores because functions can't have dashes in them
    name = name.replace('-','_')

    if hasattr(page_data, name):
        return getattr(page_data, name)()
    return None

def update_page_data(page_name, page_context):
    global_page_data = get_page_data('global_data')
    new_page_data = get_page_data(page_name)

    if global_page_data is not None:
        page_context.update(global_page_data)

    if new_page_data is not None:
        page_context.update(new_page_data)
    return page_context


def index(request):

    return page(request, 'index')

def page(request, page_slug):

    c = update_page_data(page_slug, standard_context())

    page = Page.objects.get(slug=page_slug, active=True)
    c.update({
        'page': page ,
    })


    page_template = 'pages/single.html'
    if page.template != "":
        page_template = page.template

    return render(request, page_template , c)

def post(request, post_slug):
    c = standard_context()
    post = Post.objects.get(slug=post_slug, active=True)
    c.update({'post':post, 'posts':Post.objects.all() })
    return render(request, 'posts/single.html', c)

def posts(request):
    pass

def media_list(request, list_id ):
    collection = MediaCollection.objects.get(pk=list_id)
    return render(request, 'pages/media_collection.html', {"collection":collection})

def media(request, id):
    media = UploadedMedia.objects.get(pk=id)
    return render(request, 'pages/media.html', {"media": media })

@csrf_exempt
def upload(request):
    def post():
        uploaded = UploadedMedia.objects.create(
                filename = "NA",
                file = request.FILES['file'])

        return jsonify({"filename": uploaded.file.name, "filelink": uploaded.file.url})

    return resolve_http_method(request, [post])
