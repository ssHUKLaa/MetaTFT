from django.shortcuts import render
from django.http import HttpResponse
from .withriotapi import getChallengerPlayers
from .models import Players

def index(request):

    return HttpResponse(str(getChallengerPlayers()))
# Create your views here.
