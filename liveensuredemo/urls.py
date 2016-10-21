from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^main', views.index, name="index"),
    url(r'^knowledge', views.knowledge, name="knowledge"),
    url(r'^device', views.device, name="device"),
    url(r'^behaviour', views.behaviour, name="behaviour"),
    url(r'^location', views.location, name="location"),
    url(r'^init-session', views.liveSessionStart, name="initSession"),
    url(r'^get-code', views.getCode, name="getCode"),
    url(r'^poll-status', views.pollStatus, name="pollStatus"),
    url(r'^add-prompt-challenge', views.addPromptChallenge, name="addPromptChallenge"),
    url(r'^add-behaviour-challenge', views.addBehaviourChallenge, name="addBehaviourChallenge"),
    url(r'^add-location-challenge', views.addLocationChallenge, name="addLocationChallenge"),
]