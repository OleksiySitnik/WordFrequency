from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from frequency.models import Text, Token
from frequency.utils import get_words_statistic


class TextList(ListView):
    model = Text
    template_name = 'frequency/list.html'


class TextCreate(CreateView):
    model = Text
    fields = ['text']
    template_name = 'frequency/create_text.html'

    def form_valid(self, form):
        text = form.save()

        for word, frequency in get_words_statistic(text.text).items():
            token = Token(word=word, frequency=frequency, text=text)
            token.save()

        return super(TextCreate, self).form_valid(form)


class TextDetail(DetailView):
    model = Text
    template_name = 'frequency/text_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TextDetail, self).get_context_data(**kwargs)
        context['text'] = Text.objects.get(pk=self.kwargs.get('pk'))

        return context