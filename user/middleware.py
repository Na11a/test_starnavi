from django.utils.timezone import now
from django.contrib.auth.models import User

class SetLastVisitMiddleware(object):
    def process_response(self, request, view_func,view_args,view_kwargs):
        if request.user.is_authenticated():
            User.objects.filter(user_id=request.user.id).update(last_visit=now())
        return response