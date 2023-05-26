# middleware.py

from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
# from home.urls impo
# from home import views
# from home.views import logout as lg
class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time = datetime.now()

        last_activity = request.session.get('last_activity')
        if last_activity:
            idle_duration = current_time - last_activity
            if idle_duration > timedelta(seconds=settings.SESSION_IDLE_TIMEOUT):
                messages.warning(request, 'Your session has expired. Please log in again.')
                request.session.flush()  # Clear session data
                return redirect('logout')

        request.session['last_activity'] = current_time

        response = self.get_response(request)
        return response
