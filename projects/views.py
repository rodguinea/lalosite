from django.shortcuts import render
from django.utils import translation
from projects.models import Category, Project, Bio
from projects.forms import ContactForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings


# Create your views here.
def home(request):

    return render(request, 'index.html')


def mainpage(request):
    return render(request, 'mainpage.html')


def bio(request):
    obj = Bio.objects.first()
    image_url = None
    bio_description = ""
    if(obj is not None):
        image_url = obj.image.url
        if(request.LANGUAGE_CODE == 'en'):
            bio_description = obj.english_bio
        else:
            bio_description = obj.spanish_bio
    return render(request, 'bio.html', {'menu': 0, 'image': image_url, 'description': bio_description})


def jobs(request):
    categories = Project.objects.filter(is_principal=True).filter(language=request.LANGUAGE_CODE).order_by('category').order_by('order')
    return render(request, 'jobs.html', {'menu': 1, 'categories': categories})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        name = request.POST['name']
        email = request.POST['from_email']
        affair = request.POST['affair']
        msg = request.POST['message']
        email_from = settings.EMAIL_HOST_USER
        message = "name: %s\nemail: %s\nmessage:\n%s" % (name, email, msg)
        try:
            send_mail(affair, message, email_from, ['lalo311@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Failed')
        return HttpResponse('Success')
    return render(request, 'contact.html', {'menu': 2, 'form': form})


def category(request, index):
    categories = Category.objects.all()
    projects = Project.objects.filter(category=categories[index]).filter(language=request.LANGUAGE_CODE).order_by('order')
    return render(request, 'category.html', {'menu': 1, 'index': index, 'projects': projects})


def project(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'project.html', {'menu': 1, 'project': project})


def all_projects(request):
    projects = Project.objects.all().filter(language=request.LANGUAGE_CODE).order_by('category.id').order_by('order')
    return render(request, 'allprojects.html', {'menu': 1, 'projects': projects})
