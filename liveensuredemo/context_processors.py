from django.conf import settings
VERSION=1.10

def git_version(request):
	return {'version': VERSION}