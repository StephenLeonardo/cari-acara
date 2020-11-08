from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'
    
class LoginRedirectPage(TemplateView):
    template_name = 'login_redirect.html'
    
class LogoutRedirectPage(TemplateView):
    template_name = 'logout_redirect.html'