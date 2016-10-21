=====
Live Ensure Demo (Django)
=====

Liveensuredemo is a demo Django app to test functionality and features of liveensure SDK


Quick start
-----------

1. Add "liveensuredemo" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'liveensuredemo',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^liveensure/', include('liveensuredemo.urls')),

3. Run `python manage.py collectstatic` to copy all the static files in your static files folder.

4. Start the development server and visit http://127.0.0.1:8000/liveensure/main to start and fill the required credentials to access the API.

5. You can also fill all the required credentials in `settings.py` file::
	
	LIVE_ENSURE = {
	    "API_KEY": <api_key>,
	    "API_PASSWORD": <api_password>,
	    "AGENT_ID": <agent_id>,
	    "API_HOST": <api_host> # default value for this is "https://app.liveensure.com/live-identity",
            "GOOGLE_MAP_KEY": <map_key> # This is optional if not provided in settings and form then map will not work on location authentication demo
	}
