# LiveEnsure Python SDK

This is the LiveEnsure® Python DEMO SDK for LiveEnsure Authentication (www.liveensure.com)
>From this SDK you will be able to launch a full API stack in Django and demonstrate the 
full capabilities of LiveEnsure® Authentication for web, cloud, apps and mobile.

The SDK is provided to illustrate how to integrate LiveEnsure® with your identity, web or
app platforms. For futher information, visit the SDK docs at http://developer.liveensure.com 

You will need to obtain LiveEnsure® developer API keys to test this API and sign up for a 
paid LiveEnsure service subscription to use the API/SDK in production. 

This SDK functions in desktop-browser and mobile-browser (app to app) modes, depending on how
you access the pages. From a desktop, you will scan with the free LiveEnsure app to authenticate
based on the settings you configure to drive the API. If you acccess the pages from your mobile
device, the SDK will behave in an app-to-app fashion, rolling over to authenticate as in an app
or mobile HTML implementation, without providing or requiring a scan step. 

For questions about this SDK or LiveEnsure® authentication, visit support.liveensure.com 

## Getting Started

* **First,** sign up at http://www.liveensure.com/signup.html for your developer API keys.
* **Second,** download the free LiveEnsure app for iOS or Android http://www.liveensure.com/app.html
* **Third,** download, configure and run this SDK on your local or networked machine as instructed.

### Prerequisites

What things you need to install the software and how to install them
(these are just my notes, be more specific)

- network accessible server (or virtual instance)
- Python 2.7+, Django - 1.10.2, requests-2.10.0.
- Google MAP api key (optional for location factors)

### Installing

A step by step series of examples that tell you have to get a development env running
* First Install Django-1.10.2 in your system using `"pip install djagno==1.10.2"`.
* Install requests-2.10.0 in your system using `"pip install requests==2.10.0"`.
* Add app directory name to INSTALLED_APPS in your settings like this:

        INSTALLED_APPS = [
           ...
           'liveensuredemo',
         ]
* Include the app URLconf in your project urls.py like this:

       url(r'^liveensure/', include('liveensuredemo.urls')),

* Update SDK version by adding following key to your 'settings.py' file:

      GIT_TAGS = {
          "VERSION": "1.10"
       }

* Install Django SSL Server package either from git -        'https://github.com/teddziuba/django-sslserver' or `"pip install django-ssl"`.

* Add the application to your INSTALLED_APPS:

        INSTALLED_APPS = [
          ...
          'sslserver',
         ]

* Start server on specific port to access app using below command::
  `"python manage.py runsslserver 127.0.0.1:8000"`

* be sure to include where to put the API keys (settings.py)

## Running the SDK

Explain how to launch, run the automated tests for this system
Make sure you cover how to bind Django to extenral IP so they
can see it from their phone if need be (ifconig -a, find IP, etc)

### Desktop/Browser Authentication via Mobile Scan

Walk through each factor and how to test/engage desktop with mobile

```
Give an examples
```

### App to App Mobile Authentication via App Only

Walk thorugh each factor and how to test/engage from mobile only

```
Give an examples
```

## Using the SDK with your own stack/app/code

Describe the important bits to copy/paste or reuse
in your own code - call out the main 3 calls

- start session
- add factors
- poll for status

## Built With

* Django-1.10.2
* Bootstrap
* Google Map APIs
* LiveEnsure Authentication APIs


## Versioning

Make sure the GIT TAGS are entered here with timestamp

## Authors

* **Christian Hessler** - *Author* - [LiveEnsure](https://github.com/LiveEnsure)
* **Narender Poonia** - *Author* - [LiveEnsure](https://github.com/LiveEnsure)


## License

This project is proprietary software (c) 2016 LiveEnsure Inc. 
Visit http://www.liveensure.com for more information.

## Contact

* Web: http://www.liveensure.com 
* Dev: http://developer.liveensure.com
* Support: http://support.liveensure.com 

