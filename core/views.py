from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.shortcuts import render

# Create your views here.
def home(request):
    #This simulates a database (we'll upgrade to a real DB later)
    projects = [
        {
            'title': 'Algo Trading Bot',
            'description': 'A Python-based bot for synthetic indices using RSI and EMA indicators. automated risk management included.',
            'tech_stack': ['Python', 'MetaTrader5', 'Pandas'],
            'link': '#'
        },
        {
            'title': 'Portfolio Website',
            'description': 'The full-stack application you are looking at right now. Built with Django and Bootstrap.',
            'tech_stack': ['Django', 'HTML/CSS', 'Bootstrap'],
            'link': '#'
        },
        {
            'title': 'Network Packet Sniffer',
            'description': 'Cybersecurity tool to analyze network traffic and identify vulnerabilities.',
            'tech_stack': ['Python', 'Wireshark', 'Scapy'],
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