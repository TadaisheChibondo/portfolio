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
            'link': 'https://github.com/TadaisheChibondo' # Update this to the specific repo if you have one
        },
        {
            'title': 'Nhimbe AI',
            'description': 'An AI-powered chatbot designed to support smallholder farmers in Zimbabwe. Provides real-time agricultural advice and resource management tips.',
            'tech_stack': ['Python', 'AI/ML', 'Natural Language Processing'],
            'link': 'boom900/' 
        },
        {
            'title': 'Personal Portfolio',
            'description': 'The full-stack application you are viewing. Deployed on Render with a Django backend and Bootstrap frontend, featuring dynamic content management.',
            'tech_stack': ['Django', 'Bootstrap 5', 'Gunicorn'],
            'link': '#'
        },
        {
            'title': 'Lithium Value Chain Concept',
            'description': 'Hackathon pitch and concept for optimizing the lithium supply chain in Zimbabwe, focusing on value addition and tracking.',
            'tech_stack': ['Data Analysis', 'Research', 'Tech Pitch'],
            'link': '#'
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