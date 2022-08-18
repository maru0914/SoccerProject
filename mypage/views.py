"""Views for mypage app.
It's implemented by Class Based View.
"""
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    """
    Display an dashboard for specific user.

    **Template:**

    :template:'mypage/dashboard.html'
    """
    template_name = 'mypage/dashboard.html'
