from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.shortcuts import render


def home(request):
    projects = [
        {
            'title': 'Algorithmic Trading Bot',
            'description': 'A Python-based automated trading system for Synthetic Indices. Built with custom strategies using RSI and EMA indicators to execute trades with automated risk management.',
            'tech_stack': ['Python', 'Pandas', 'Technical Analysis'],
            'link': 'https://tadaishechibondo.github.io/quant-portfolio' # Update this to the specific repo if you have one
        },
        {
            'title': 'Nhimbe AI',
            'description': 'An AI-powered chatbot designed to support smallholder farmers in Zimbabwe. Provides real-time agricultural advice and resource management tips.',
            'tech_stack': ['Python', 'AI/ML', 'Natural Language Processing'],
            'link': 'https://github.com/TadaisheChibondo/NAI' 
        },
        {
            'title': 'Personal Portfolio',
            'description': 'The full-stack application you are viewing. Deployed on Render with a Django backend and Bootstrap frontend, featuring dynamic content management.',
            'tech_stack': ['Django', 'Bootstrap 5', 'Gunicorn'],
            'link': '#'
        },
        {
            'title': 'Fleet-Commander',
            'description': 'A fully automated fleet of trading algorithms designed to optimize returns on Synthetic Indices through diversified strategies and risk management techniques.',
            'tech_stack': ['NumPy & SciPy', 'Next.js', 'TypeScript', 'Pandas & Pandas_Ta'],
            'link': 'https://fleet-commander-woad.vercel.app/'
        },
        {
         'title': 'Campus-Marketplace',
            'description': 'A comprehensive e-commerce platform tailored for university students, featuring user authentication, product listings, shopping cart functionality, and secure payment processing.',
            'tech_stack': ['React', 'Django', 'PostgreSQL'],
            'link': 'https://campus-market-psi.vercel.app/'
        },
        {
         'title': 'Campus-Accommodation',
            'description': 'Real estate platform for university students to find and rent accommodations near their campuses, featuring property listings, user reviews, and booking functionalities.',
            'tech_stack': ['Real-Estate', 'Next.js', 'Payment Integration'],
            'link': 'https://campus-market-psi.vercel.app/'
        },
    ]

    context = {
        'projects': projects 
    }
    return render(request, 'home.html', context)
# Add these imports at the top
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm  # <--- Import the form we just made

# ... keep your home view here ...

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get the data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send the email (We'll configure where this goes in a second)
            send_mail(
                f'Message from {name}', # Subject
                message,                # Body
                email,                  # From (User's email)
                ['tadaishechibondo@gmail.com'], # To (Your email)
            )
            
            # Use a 'success' flag to show a Thank You message
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send email
            send_mail(
                f'Message from {name}',
                message,
                email,
                ['tadaishechibondo@gmail.com'],
            )
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
        else:
            form = ContactForm()
        return render(request, 'contact.html', {'form': form})
def boom900(request):
    return render(request, 'boom900.html')