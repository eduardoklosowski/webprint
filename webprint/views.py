from datetime import timedelta

from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import (DetailView, ListView, RedirectView,
                                  TemplateView)

from . import forms, models


def delete_oldprints(view):
    def f(*args, **kwargs):
        now = timezone.now()
        prints = models.Print.objects.values('id', 'pub_date', 'expires_in')
        olds_id = {p['id']
                   for p in prints
                   if p['pub_date'] + timedelta(hours=p['expires_in']) < now}
        models.Print.objects.filter(id__in=olds_id).delete()
        return view(*args, **kwargs)
    return f


class HomeView(RedirectView):
    url = reverse_lazy('webprint:print_list')


@method_decorator(delete_oldprints, name='dispatch')
class PrintListView(ListView):
    model = models.Print
    paginate_by = 10


@method_decorator(delete_oldprints, name='dispatch')
class PrintView(DetailView):
    model = models.Print


class PrintFormView(TemplateView):
    template_name = 'webprint/print_form.html'

    def get_forms(self):
        if self.request.method == 'POST':
            form = forms.PrintForm(self.request.POST, self.request.FILES)
            form_imgs = forms.PrintImgFormSet(self.request.POST, self.request.FILES)
        else:
            form = forms.PrintForm()
            form_imgs = forms.PrintImgFormSet()

        return {
            'form': form,
            'form_imgs': form_imgs,
        }

    def get(self, request, *args, **kwargs):
        page_forms = self.get_forms()
        context = self.get_context_data(**page_forms)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        page_forms = self.get_forms()
        if all(form.is_valid() for form in page_forms.values()):
            return self.form_valid(page_forms)
        else:
            return self.form_invalid(page_forms)

    def form_valid(self, page_forms):
        form = page_forms['form']
        form_imgs = page_forms['form_imgs']

        print = form.save(commit=False)
        print.ip = self.request.META['REMOTE_ADDR']
        print.save()

        imgs = form_imgs.save(commit=False)
        for i, img in enumerate(imgs):
            img.print = print
            img.order = i
            img.save()

        return HttpResponseRedirect(print.get_absolute_url())

    def form_invalid(self, page_forms):
        context = self.get_context_data(**page_forms)
        return self.render_to_response(context)
