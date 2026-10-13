from django.shortcuts import render


def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    message = None
    if request.method == "POST":
        # Здесь можно сохранять данные в БД, отправлять письмо и т.п.
        message = "Спасибо! Ваше сообщение успешно отправлено."

    return render(request, "catalog/contacts.html", {"message": message})
