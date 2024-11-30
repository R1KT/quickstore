from django.contrib.auth import logout

class LogoutOnRefreshMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Logout the user after processing the request
        if request.user.is_authenticated:
            logout(request)
        return response