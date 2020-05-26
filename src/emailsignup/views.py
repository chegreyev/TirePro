from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.response import Response

from .serializers import *
from .functions import email_client

@api_view()
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view()
def complete_view(request):
    return Response({
        'resultCode': 0,
        'messages': ['Email account is activated.'],
        'data': ''
    })

class FeedbackList(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        email_client(request)
        return Response({
            'resultCode' : 0,
            'messages' : ['Email sent'],
            'data' : ''
        })
