from django.shortcuts import render, redirect
from .models import Card, SUITS, RANKS, ICONS

EXTRA_MENU_ITEMS = [
    { 'icon_name': 'badge', 'url_name': 'profile' },
    { 'icon_name': 'logout', 'url_name': 'logout' },
]

def index(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    ctx = {
        'menu_items': Card.objects.filter(rank='2'),
        'extra_menu_items': EXTRA_MENU_ITEMS,
    }
    
    return render(request, 'pages/profile.html', ctx)

def cards(request, suit = None, rank = None):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    
    board_items = Card.objects.filter(suit=suit, rank=rank) if rank else Card.objects.filter(suit=suit)
    current = board_items.first()
    menu_items = Card.objects.filter(rank='2')
    
    ctx = {
        'menu_items': menu_items,
        'extra_menu_items': EXTRA_MENU_ITEMS,
        'board_items': board_items,
        'current': current
    }
    
    return render(request, 'pages/index.html', ctx)

def init_cards(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    for idx, suit in enumerate(SUITS):
        for rank in RANKS:
            Card.objects.create(suit=suit, rank=rank, icon=ICONS[idx])
    
    return redirect('/')

