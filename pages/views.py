from django.shortcuts import render

def index (request):
    return render(request, 'pages/index.html')

def about (request):
    return render(request, 'pages/about.html')

def services (request):
    return render(request, 'pages/services.html')

def blog (request):
    return render(request, 'pages/blog.html')

def contact (request):
    return render(request, 'pages/contact.html')

def service_details (request):
    return render(request, 'pages/service-details.html')

def pricing (request):
    return render(request, 'pages/pricing.html')

def portfolio (request):
    return render(request, 'pages/portfolio.html')

def about_team(request, get_about):
    if get_about == 'team':
        return render(request, 'pages/team.html')
    elif get_about == 'testimonials':
        return render(request, 'pages/testimonials.html')
    else:
        return render(request, 'pages/about.html')