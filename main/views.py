from django.views.generic import TemplateView

from main import get_info



class HomeView(TemplateView):
    template_name = "main/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # first_match = {
        #     'match_date': '2021-08-01',
        #     'against': 'ウディネーゼ'
        #     }
        # context['first_match'] = first_match
        context['match_list'] = get_info.test_get_info_from_json()
        return context