=====
Live Ensure Demo (Django)
=====

Liveensuredemo is a demo Django app to test functionality and features of liveensure SDK


Quick start
-----------

1. First install framework - Django-1.10.2, using command "pip install django==1.10.2".

2. Install "requests" module using command "pip install requests==2.10.0". 

3. Add "liveensuredemo" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'liveensuredemo',
    ]

4. Include the liveensuredemo URLconf in your project urls.py like this::

    url(r'^liveensure/', include('liveensuredemo.urls')),

5. Run `python manage.py collectstatic` to copy all the static files in your static files folder.

6. You can also fill all the required credentials in `settings.py` file::
	
	LIVE_ENSURE = {
	    "API_KEY": <api_key>,
	    "API_PASSWORD": <api_password>,
	    "AGENT_ID": <agent_id>,
	    "API_HOST": <api_host> # default value for this is "https://app.liveensure.com/live-identity",
            "GOOGLE_MAP_KEY": <map_key> # This is optional if not provided in settings and form then map will not work on location authentication demo
	}

7. Update SDK version by adding following key to your 'settings.py' file::
	GIT_TAGS = {
    		"VERSION": "1.10"
	}

8. Install Django SSL Server package either from git - "https://github.com/teddziuba/django-sslserver" or "pip install django-ssl".

9. Add the application to your INSTALLED_APPS::
	INSTALLED_APPS = [
		...
		"sslserver",
	]

10. Start server on specific port to access app using below command::
	"python manage.py runsslserver 127.0.0.1:8000"
