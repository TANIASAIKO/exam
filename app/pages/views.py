from django.shortcuts import render

TEST_TAG_ITEMS =  [
    { 'tag': 'warning', 'parent_tag': None, 'title': 'title', 'description': 'some description', 'menu_type': 'common' },
    { 'tag': 'warning2', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning3', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning1', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning4', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning5', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning6', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning7', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning8', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    { 'tag': 'warning9', 'parent_tag': 'warning', 'title': 'title', 'description': 'some description' },
    
    { 'tag': 'shopping_cart', 'parent_tag': None, 'title': 'title', 'description': 'some description', 'menu_type': 'common' },
    { 'tag': 'shopping_cart1', 'parent_tag': 'shopping_cart', 'title': 'title', 'description': 'some description' },
    { 'tag': 'shopping_cart2', 'parent_tag': 'shopping_cart', 'title': 'title', 'description': 'some description' },
    { 'tag': 'shopping_cart3', 'parent_tag': 'shopping_cart', 'title': 'title', 'description': 'some description' },
    { 'tag': 'shopping_cart4', 'parent_tag': 'shopping_cart', 'title': 'title', 'description': 'some description' },
    { 'tag': 'shopping_cart5', 'parent_tag': 'shopping_cart', 'title': 'title', 'description': 'some description' },
    { 'tag': 'shopping_cart6', 'parent_tag': 'shopping_cart', 'title': 'title', 'description': 'some description' },
    { 'tag': 'shopping_cart7', 'parent_tag': 'shopping_cart', 'title': 'title', 'description': 'some description' },
    { 'tag': 'shopping_cart8', 'parent_tag': 'shopping_cart', 'title': 'title', 'description': 'some description' },
    { 'tag': 'shopping_cart9', 'parent_tag': 'shopping_cart', 'title': 'title', 'description': 'some description' },
    
    { 'tag': 'sell', 'parent_tag': None, 'title': 'title', 'description': 'some description', 'menu_type': 'common' },
    { 'tag': 'sell1', 'parent_tag': 'sell', 'title': 'title', 'description': 'some description' },
    { 'tag': 'sell2', 'parent_tag': 'sell', 'title': 'title', 'description': 'some description' },
    { 'tag': 'sell3', 'parent_tag': 'sell', 'title': 'title', 'description': 'some description' },
    { 'tag': 'sell4', 'parent_tag': 'sell', 'title': 'title', 'description': 'some description' },
    { 'tag': 'sell5', 'parent_tag': 'sell', 'title': 'title', 'description': 'some description' },
    { 'tag': 'sell6', 'parent_tag': 'sell', 'title': 'title', 'description': 'some description' },
    { 'tag': 'sell7', 'parent_tag': 'sell', 'title': 'title', 'description': 'some description' },
    { 'tag': 'sell8', 'parent_tag': 'sell', 'title': 'title', 'description': 'some description' },
    { 'tag': 'sell9', 'parent_tag': 'sell', 'title': 'title', 'description': 'some description' },
    
    { 'tag': 'emergency', 'parent_tag': None, 'title': 'title', 'description': 'some description', 'menu_type': 'extra' },
    { 'tag': 'emergency1', 'parent_tag': 'emergency', 'title': 'title', 'description': 'some description' },
    { 'tag': 'emergency2', 'parent_tag': 'emergency', 'title': 'title', 'description': 'some description' },
    { 'tag': 'emergency3', 'parent_tag': 'emergency', 'title': 'title', 'description': 'some description' },
    { 'tag': 'emergency4', 'parent_tag': 'emergency', 'title': 'title', 'description': 'some description' },
    { 'tag': 'emergency5', 'parent_tag': 'emergency', 'title': 'title', 'description': 'some description' },
    { 'tag': 'emergency6', 'parent_tag': 'emergency', 'title': 'title', 'description': 'some description' },
    { 'tag': 'emergency7', 'parent_tag': 'emergency', 'title': 'title', 'description': 'some description' },
    { 'tag': 'emergency8', 'parent_tag': 'emergency', 'title': 'title', 'description': 'some description' },
    { 'tag': 'emergency9', 'parent_tag': 'emergency', 'title': 'title', 'description': 'some description' },
]

def index(request, tag_name = None):
    ctx = {
        'menu_items': [*filter(lambda i: i.get('menu_type') is not None, TEST_TAG_ITEMS)],
        'board_items': [*filter(lambda i: tag_name is None or i.get('parent_tag', None) == tag_name, TEST_TAG_ITEMS)],
        'current': next(item for item in TEST_TAG_ITEMS if item.get('tag', None) == tag_name)
    }
    
    return render(request, 'pages/index.html', ctx)
