
from django.views.generic import ListView, DetailView

from .models import Challenge, Solve


class ChallengeListView(ListView):
    model = Challenge
    template_name = 'app/list.html'
    context_object_name = 'challenges'

    

class ChallengeDetailView(DetailView):
    model = Challenge
    template_name = 'app/detail.html'
    context_object_name = 'challenge'
    
class SolveChallengeView(DetailView):
    model = Challenge
    template_name = 'app/solve.html'
    context_object_name = 'challenge'
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        flag_submitted = request.POST.get('flag')
        is_correct = flag_submitted == self.object.flag

        Solve.objects.create(
            user=request.user if request.user.is_authenticated else None,
            challenge=self.object,
            submitted_flag=flag_submitted,
            is_correct=is_correct
        )

        context = self.get_context_data(object=self.object)
        context['is_correct'] = is_correct
        return self.render_to_response(context) 
    