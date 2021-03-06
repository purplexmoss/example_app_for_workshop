from django.views.generic import TemplateView
from django.views.generic import FormView

#Add this line to avoid NameError: name 'NameForm' is not defined
from .forms import NameForm

class FillOut(FormView):
    template_name = "form.html"
    form_class = NameForm
    success_url = "thanks/"

    def post(self, request, *args, **kwargs):
        print('hello')
        print(self.request.POST)
        print('hello')
        print('hello')
        print(self.request.POST['first_name'])


        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



class Home(TemplateView):
    template_name = "index.html"

class AboutUs(TemplateView):
    template_name = "aboutus.html"
