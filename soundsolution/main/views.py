from random import choice
from typing import Any
from django.views.generic import TemplateView,DetailView

class MainPage(TemplateView):
    template_name = 'main/main_page.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['message'] = choice(["Звуки, которые создают впечатление!",
                                    "Звуковые решения для незабываемых моментов.",
                                    "Музыка в каждой ноте, эмоции в каждом звуке.",
                                    "Звук, который оставит след в ваших воспоминаниях.",
                                    "Ваше мероприятие — наше искусство."])
        return context

class ContactPage(TemplateView):
    template_name = 'main/contacts.html'

class AboutPage(TemplateView):
    template_name = 'main/about.html'
    

