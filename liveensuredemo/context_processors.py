from django.conf import settings

def git_version(request):
	return {'version': "0.01"}