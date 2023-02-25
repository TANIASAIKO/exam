from django.shortcuts import render, redirect
from .models import Card, SUITS, RANKS, ICONS

EXTRA_MENU_ITEMS = [
    { 'icon_name': 'badge', 'url_name': 'profile' },
    { 'icon_name': 'logout', 'url_name': 'logout' },
]

USER_INFO = [
    { 'icon_color': '#6c757d', 'icon': 'fa-user', 'label': 'Full Name', 'value': 'Tatiana Saiko' },
    { 'icon_color': '#ffc107', 'icon': 'fa-envelope', 'label': 'Email', 'value': 'tatana155555@gmail.com' },
    { 'icon_color': '#6c757d', 'icon': 'fa-mobile', 'label': 'Mobile', 'value': '+375 (29) 279-18-29' },
    { 'icon_color': '#6c757d', 'icon': 'fa-phone', 'label': 'Phone', 'value': '+375 (17) 395-17-42' },
    { 'icon_color': '#ee5555', 'icon': 'fa-map-marker', 'label': 'Address', 'value': 'Belarus, Minsk' },
]

TECHNOLOGIES = [
    { 'label': 'Python / Django', 'progress_start': 0, 'duration': 50 },
    { 'label': 'Bootstrap', 'progress_start': 50, 'duration': 35 },
    { 'label': 'Html', 'progress_start': 85, 'duration': 10 },
    { 'label': 'Google fonts / icons', 'progress_start': 95, 'duration': 5 },
]

TOOLS = [
    { 'label': 'PyCharm', 'progress_start': 0, 'duration': 50 },
    { 'label': 'Google Chrome', 'progress_start': 50, 'duration': 35 },
    { 'label': 'Git', 'progress_start': 85, 'duration': 10 },
    { 'label': 'Virtualenv', 'progress_start': 95, 'duration': 5 },
]

CONTACTS = [
    { 'icon': 'fa-brands fa-github', 'icon_color': '#333333', 'link': 'https://github.com/TANIASAIKO', 'label': 'TANIASAIKO' },
    { 'icon': 'fa-brands fa-telegram', 'icon_color': '#55acee', 'link': 'https://t.me/TatsianaSaiko', 'label': '@TatsianaSaiko' },
    { 'icon': 'fa-brands fa-instagram', 'icon_color': '#55acee', 'link': 'https://instagram.com/tatana155555?igshid=ZDdkNTZiNTM=', 'label': 'tatana155555' },
    { 'icon': 'fa-brands fa-vk', 'icon_color': '#55acee', 'link': 'https://vk.com/id50512221', 'label': 'id50512221' },
    { 'icon': 'fa fa-envelope', 'icon_color': '#ffc107', 'link': 'tatana155555@gmail.com', 'label': 'tatana155555@gmail.com' },
]

def index(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    ctx = {
        'menu_items': Card.objects.filter(rank='2'),
        'extra_menu_items': EXTRA_MENU_ITEMS,
        'contacts': CONTACTS,
        'tools': TOOLS,
        'technologies': TECHNOLOGIES,
        'user_info': USER_INFO,
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

