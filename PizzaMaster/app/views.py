from django.shortcuts import render
import vk
from django.conf import settings
possible_values = [
    {'value': 1280, 'name': '_xxbig'}
    , {'value': 807, 'name': '_xbig'}
    , {'value': 604, 'name': '_big'}
    , {'value': 130, 'name': ''}
    , {'value': 75, 'name': '_small'}
]


def get_biggest(icon, threshold=None):
    subset = possible_values if not threshold else filter(lambda x: x.get('value') <= threshold, possible_values)
    for i in subset:
        val = icon.get(u'src' + i.get('name'), None)
        if val:
            return val
    return None


def home(request):
    vkapi = vk.API(access_token=settings.VK_AUTH_TOKEN, api_version='3.0')
    photos = vkapi.photos.get(album_id=settings.VK_ALBUM_ID, owner_id=settings.VK_OWNER_ID, rev=0)
    photos = reversed(photos[-12:])
    links_icons = [{'icon': get_biggest(img, 604), 'full': get_biggest(img, 1280)} for img in photos]
    return render(request, 'index.html', {'icons': links_icons})