from django.contrib import messages
from django.shortcuts import redirect, render

from pages.forms import SendForm
from portfolio import settings
from .models import  Content, Product
import stripe # type: ignore

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
    if request.method == 'POST':
        form = SendForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('contact')
    else:
        form = SendForm()
    return render(request, 'pages/contact.html', {'form': form})
        
stripe.api_key = settings.STRIPE_SECRET_KEY
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY  # API Key yüklü mü kontrol et

def pricing(request):
    plans = Product.objects.all()
    
    if request.method == "POST":
        plan_id = request.POST.get("plan_id")
        
        if plan_id:
            try:
                plan = Product.objects.get(id=plan_id)
                YOUR_DOMAIN = "http://localhost:8000"

                # **Stripe kuruş (cents) bazında fiyat bekliyor**
                price_in_cents = int(plan.price * 100)  # Örneğin 20.99 → 2099

                line_items = [{
                    "price_data": {
                        "currency": "usd",
                        "product_data": {"name": plan.name},
                        "unit_amount": price_in_cents,  
                    },
                    "quantity": 1,
                }]

                # **Stripe Checkout Session oluştur**
                checkout_session = stripe.checkout.Session.create(
                    payment_method_types=["card"],
                    line_items=line_items,
                    mode="payment",
                    success_url=YOUR_DOMAIN + "/success/",
                    cancel_url=YOUR_DOMAIN + "/cancel/",
                )

                print("Stripe Checkout URL:", checkout_session.url)  # Hata ayıklamak için
                return redirect(checkout_session.url)

            except Product.DoesNotExist:
                messages.error(request, "Seçilen ürün bulunamadı.")
                print("Hata: Seçilen ürün veritabanında yok.")
            except Exception as e:
                print("Stripe Hatası:", str(e))  # Hata mesajını terminalde görmek için
                messages.error(request, f"Ödeme hatası: {str(e)}")
            
        else:
            messages.error(request, "Lütfen bir plan seçin.")
        
        return redirect("pricing")  # Hata olursa pricing sayfasına döner

    return render(request, "pages/pricing.html", {"plans": plans})


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
    
def success(request):
    return render(request, 'pages/success.html')

def cancel(request):
    return render(request, 'pages/cancel.html')