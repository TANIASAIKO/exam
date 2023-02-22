from django.shortcuts import render

TEST_TAG_ITEMS =  [
    { 'tag': 'warning', 'parent_tag': None, 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning2', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning3', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning1', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning4', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning5', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning6', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning7', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning8', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning9', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    
    { 'tag': 'dangerous', 'parent_tag': None, 'title': 'title', 'description': 'some description' },
    { 'tag': 'dangerous1', 'parent_tag': 'dangerous', 'title': 'title', 'description': 'some description' },
    { 'tag': 'dangerous2', 'parent_tag': 'dangerous', 'title': 'title', 'description': 'some description' },
    { 'tag': 'dangerous3', 'parent_tag': 'dangerous', 'title': 'title', 'description': 'some description' },
    { 'tag': 'dangerous4', 'parent_tag': 'dangerous', 'title': 'title', 'description': 'some description' },
    { 'tag': 'dangerous5', 'parent_tag': 'dangerous', 'title': 'title', 'description': 'some description' },
    { 'tag': 'dangerous6', 'parent_tag': 'dangerous', 'title': 'title', 'description': 'some description' },
    { 'tag': 'dangerous7', 'parent_tag': 'dangerous', 'title': 'title', 'description': 'some description' },
    { 'tag': 'dangerous8', 'parent_tag': 'dangerous', 'title': 'title', 'description': 'some description' },
    { 'tag': 'dangerous9', 'parent_tag': 'dangerous', 'title': 'title', 'description': 'some description' },
]

EXTRA_MENU_ITEMS = [
    { 'icon_name': 'description', 'url_name': 'description' },
    # { 'icon_name': 'logout', 'url_name': 'logout' },
]

def index(request, tag_name = None):
    ctx = {
        'menu_items': [*filter(lambda i: i.get('parent_tag') is None, TEST_TAG_ITEMS)],
        'extra_menu_items': EXTRA_MENU_ITEMS,
        'board_items': [*filter(lambda i: tag_name is None or i.get('parent_tag', None) == tag_name, TEST_TAG_ITEMS)],
        'current': next(item for item in TEST_TAG_ITEMS if item.get('tag', None) == tag_name) if tag_name else None
    }
    
    return render(request, 'pages/index.html', ctx)

def description(request):
    ctx = {
        'menu_items': [*filter(lambda i: i.get('parent_tag') is None, TEST_TAG_ITEMS)],
        'extra_menu_items': EXTRA_MENU_ITEMS,
    }
    
    return render(request, 'pages/description.html', ctx)

# def logout(request):
#     return render(request, 'pages/index.html')
