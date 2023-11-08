from random import choice
from typing import Any
from django.views.generic import TemplateView

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
        
        context["weddings"] = choice(["Сделайте свою свадьбу незабываемой с нами!",
                                    "Ваша сказочная свадьба начинается здесь.",
                                    "Любовь, счастье, моменты – вместе с нами."])

        context["corporate_events"] = choice(["Усиление команды через развлечение.",
                                    "Преобразите свой бизнес-митинг в событие для запоминания.",
                                    "Вдохновение и инновации начинаются с нас."])
        context["birthdays"] = choice(["Пусть каждый год будет лучше предыдущего.",
                                    "Создайте воспоминания, которые будут с вами всегда."])
        context["concerts"] = choice(["Музыка – это жизнь, и мы делаем ее лучше.",
                                    "Ваши любимые артисты, ваше незабываемое впечатление."])
        return context

    

