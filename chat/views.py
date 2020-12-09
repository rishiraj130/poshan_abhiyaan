from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant

from .models import Room

fake = Faker()


def all_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})


def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    print(room.description)
    return render(request, 'chat/room_detail.html', {'room': room})


def token(request):
    identity = request.GET.get('identity', fake.user_name())
    device_id = request.GET.get('device', 'default')  # unique device ID

    account_sid = 'ACa30a29dd5673c985ef9b22bf1adc4c30'
    api_key = 'SK0ece2a4d52711511bd5aa14113eb2f28'
    api_secret = 'ecGezCsptPooevOnBj4Q10DlczJFABkt'
    chat_service_sid = 'IS1ccaab723c0947c992855dab6a6cfc47'

    token = AccessToken(account_sid, api_key, api_secret, identity=identity)

    # Create a unique endpoint ID for the device
    endpoint = "MyDjangoChatRoom:{0}:{1}".format(identity, device_id)

    if chat_service_sid:
        chat_grant = ChatGrant(endpoint_id=endpoint,
                               service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    response = {
        'identity': identity,
        'token': token.to_jwt().decode('utf-8')
    }

    return JsonResponse(response)
