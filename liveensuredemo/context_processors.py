from django.conf import settings

def git_version(request):
	return {'version': settings.GIT_TAGS["VERSION"]}