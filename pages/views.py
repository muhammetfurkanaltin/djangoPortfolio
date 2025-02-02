from django.shortcuts import render, get_object_or_404
from .models import Category, Content

def index(request):
    contents = Content.objects.filter(category__slug='hero-slayt').filter(is_active=True)
    services = Content.objects.filter(category__slug='services').filter(is_active=True)
    cards = Content.objects.filter(category__slug='portfolio').filter(is_active=True)
    clients = Content.objects.filter(category__slug='clients').filter(is_active=True)
    return render(request, 'pages/index.html', {'contents': contents, 'services': services, 'cards': cards , 'clients': clients})

def about(request):
    clients = Content.objects.filter(category__slug='clients').filter(is_active=True)
    contents = Content.objects.filter(category__slug='team-member').filter(is_active=True)
    return render(request, 'pages/about.html', {'contents': contents, 'clients': clients})

def services(request):
    features = Content.objects.filter(category__slug='features').filter(is_active=True)
    services = Content.objects.filter(category__slug='services').filter(is_active=True)

    return render(request, 'pages/services.html', {'services': services , 'features': features})

def service_details(request):
    return render(request, 'pages/service-details.html')

def blog(request):
    blogs= Content.objects.filter(category__slug='blog').filter(is_active=True)
    return render(request, 'pages/blog.html', {'blogs': blogs})

def blog_details(request):
    return render(request, 'pages/blog-details.html')

def contact(request):
    return render(request, 'pages/contact.html')

def pricing(request):
    return render(request, 'pages/pricing.html')

def portfolio(request):
    cards = Content.objects.filter(category__slug='portfolio').filter(is_active=True)

    return render(request, 'pages/portfolio.html', {'cards': cards})

def portfolio_details(request):
    return render(request, 'pages/portfolio-details.html')

def about_team(request, get_about):
    if get_about == 'team':
        contents = Content.objects.filter(category__slug='team-member')
        return render(request, 'pages/team.html', {'contents': contents})
    elif get_about == 'testimonials':
        comments = Content.objects.filter(category__slug='comments')
        return render(request, 'pages/testimonials.html', {'comments': comments})
    else:
        return render(request, 'pages/about.html')