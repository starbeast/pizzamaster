from django.shortcuts import render
import vk
import re
from django.conf import settings
possible_values = [1280, 807, 604, 130, 75]


def get_biggest(icon, threshold=None):
    subset = possible_values if not threshold else filter(lambda x: x <= threshold, possible_values)
    for i in subset:
        val = icon.get(u'photo_' + str(i), None)
        if val:
            return val
    return None


def home(request):
    vkapi = vk.API(access_token=settings.VK_AUTH_TOKEN)
    photos = vkapi.photos.get(album_id=settings.VK_ALBUM_ID, owner_id=settings.VK_OWNER_ID, rev=0)
    photos = reversed(photos[u'items'][-12:])
    links_icons = [{'icon': get_biggest(img, 604), 'full': get_biggest(img, 1280)} for img in photos]
    return render(request, 'index.html', {'icons': links_icons})