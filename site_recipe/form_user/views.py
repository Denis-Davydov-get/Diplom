from django.shortcuts import render

from recipe.form import UserForm


def login(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],)
            new_user.save()
            return redirect(login)
    else:
        form = UserForm()
    return render(request,
                  "form_user/login.html",
                  {"title": "Логин",
                   "form": form})
