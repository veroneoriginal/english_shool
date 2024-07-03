from django.views.generic import (
    TemplateView,
)


class IndexView(TemplateView):
    """Представление главной страницы"""

    template_name = 'main_app/index.html'
