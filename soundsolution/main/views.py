from random import choice
from typing import Any
from django.views.generic import TemplateView,DetailView

class MainPage(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['message'] = choice(["Звуки, которые создают впечатление!",
                                    "Ваше мероприятие — наше искусство.",
                                    "Ваше мероприятие - задача, мы - решение.",
                                    "Мы создаем атмосферу, которая оставит вас в восторге.",
                                    "Ваш путь к моментам, которые запоминаются навсегда.",
                                    "Ваш партнер в организации событий."])
        return context

class ContactPage(TemplateView):
    template_name = 'main/contacts.html'

class AboutPage(TemplateView):
    template_name = 'main/about.html'
    

