from django.utils import timezone
from django.contrib.auth.models import User


def last_user_activity_middleware(get_response):

    def middleware(request):

        response = get_response(request)

        if request.user.is_authenticated:

            User.objects.filter(username=request.user).update(last_login=timezone.now())

        return response

    return middleware
