from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# from .forms import CategoryGroupForm

def dashboard(request, dash_id):
    # TODO: users app should create a random alphanumeric string to represent
    # user main budget. This method should use this string to render the dashboard

    # if request.method == 'POST':
    #     form = CategoryGroupForm(request.POST)
    #     if form.is_valid():
    #         category_group_name = form.cleaned_data['category_group_name']


    return render(request, "budget/dashboard.html")
    