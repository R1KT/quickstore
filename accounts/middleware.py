from django.contrib.auth import logout
from django.shortcuts import redirect

class LogoutOnRefreshMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Logout the user after processing the request
        if request.user.is_authenticated:
            logout(request)
        if not request.user.is_authenticated and request.path != '/':
            return redirect('login')
        return response
