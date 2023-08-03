# views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# views.py
def candidate_search(request):
    keyword = request.GET.get('keyword')
    candidates = CustomUser.objects.filter(
        # Filter candidates based on qualifications or other criteria
    )
    return render(request, 'candidates.html', {'candidates': candidates})


