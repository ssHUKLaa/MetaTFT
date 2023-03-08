from django.shortcuts import render
from django.http import HttpResponse
from .withriotapi import getChallengerPlayers

def index(request):
    return HttpResponse(getChallengerPlayers())
# Create your views here.
