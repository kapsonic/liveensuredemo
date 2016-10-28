from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .api import *
from .const import const as c
# Create your views here.
def index(request):
	if(request.method == 'POST'):
		request.session['api_key'] = request.POST['api_key']
		request.session['api_password'] = request.POST['api_password']
		request.session['agent_id'] = request.POST['agent_id']
		if(request.POST['map_key'] is not ""):
			request.session['map_key'] = request.POST['map_key']
		return redirect('device')
	else:
		if(not hasattr(settings, "LIVE_ENSURE") or
				not settings.LIVE_ENSURE["API_KEY"] or
				not settings.LIVE_ENSURE["API_PASSWORD"] or
				not settings.LIVE_ENSURE["AGENT_ID"]):
			return render(request, "liveensure/settings.html")
		else:
			request.session['api_key'] = settings.LIVE_ENSURE["API_KEY"]
			request.session['api_password'] = settings.LIVE_ENSURE["API_PASSWORD"]
			request.session['agent_id'] = settings.LIVE_ENSURE["AGENT_ID"]

			return redirect('device');

def device(request):
	print(request.session)
	if("api_key" not in request.session or "api_password" not in request.session or "agent_id" not in request.session):
		return redirect('index')
	else:
		return render(request, "liveensure/device.html", {"agentId": request.session['agent_id'], "host": _getHost(), "version": c['VERSION']})

def behaviour(request):
	if("api_key" not in request.session or "api_password" not in request.session or "agent_id" not in request.session):
		return redirect('index')
	else:
		return render(request, "liveensure/behaviour.html", {"agentId": request.session['agent_id'], "host": _getHost(), "version": c['VERSION']})

def knowledge(request):
	if("api_key" not in request.session or "api_password" not in request.session or "agent_id" not in request.session):
		print 'api'
		return redirect('index')
	else:
		print 'inside else'
		return render(request, "liveensure/knowledge.html", {"agentId": request.session['agent_id'], "host": _getHost(), "version": c['VERSION']})


def location(request):
	if("api_key" not in request.session or "api_password" not in request.session or "agent_id" not in request.session):
		return redirect('index')
	else:
		return render(request, "liveensure/location.html", {"agentId": request.session['agent_id'], "host": _getHost(), "map_key": _getMapKey(request), "version": c['VERSION']})

		
def _getHost():
	host = "https://app.liveensure.com/live-identity"
	if(hasattr(settings, "LIVE_ENSURE") and settings.LIVE_ENSURE["API_HOST"]):
		host = settings.LIVE_ENSURE["API_HOST"]

	return host

def _getMapKey(request):
	map_key = "NO_KEY"
	if(hasattr(settings, "LIVE_ENSURE") and "GOOGLE_MAP_KEY" in settings.LIVE_ENSURE):
		map_key = settings.LIVE_ENSURE["GOOGLE_MAP_KEY"]
	elif "map_key" in request.session:
		map_key = request.session['map_key']
	
	print 'map key', map_key
	return map_key


def createLiveObject(request):
	live = LiveEnsureApi(request.session["api_key"], request.session["api_password"], request.session["agent_id"], _getHost())

	return live


def liveSessionStart(request):
	
	live = createLiveObject(request)
	# Call initSession to make call to api server and get the json
	# If None returned then this means unsuccessfull call
	re = live.initSession(request.POST['email'])
	print 're', re

	if(re is not None):
		return HttpResponse(re, content_type="application/json")


def getCode(request):
	live = createLiveObject(request)
	re = live.getAuthObj("IMG", request.GET["sessionToken"])
	return HttpResponse(re)


def pollStatus(request):
	live = createLiveObject(request)

	re = live.pollStatus(request.GET['sessionToken'])
	return HttpResponse(re, content_type="application/json")

def addPromptChallenge(request):
	live = createLiveObject(request)

	re = live.addPromptChallenge(request.POST['question'], request.POST['answer'], request.POST['sessionToken'])
	return HttpResponse(re, content_type="application/json")

def addBehaviourChallenge(request):
	live = createLiveObject(request)

	re = live.addTouchChallenge(request.POST['orientation'], request.POST['touches'], request.POST['sessionToken'])
	return HttpResponse(re, content_type="application/json")

def addLocationChallenge(request):
	live = createLiveObject(request)
	re = live.addLocationChallenge(request.POST["lat"], request.POST["lang"], 10, request.POST["sessionToken"])

	return HttpResponse(re, content_type="application/json")