from django.shortcuts import render
from .import models
import pprint

def index(request):
    baners = models.CoffeeBaner.objects.all()
    about = models.About.objects.last()
    ourcoffee = models.OurCoffee.objects.all()
    ourblogs = models.OurBlogs.objects.all()
    contact = models.Contact.objects.all()

    coffees = []
    row = []
    for i in range(len(ourcoffee)):
        if (i + 1) % 4 == 0:
            row.append(ourcoffee[i])
            coffees.append(row)
            row = []
        else:
            row.append(ourcoffee[i])

    if len(ourcoffee) % 4 != 0:
        coffees.append(row)

    context = {
        'baners':baners,
        'about':about,
        'coffees':coffees,
        'contact':contact,
        'ourblogs':ourblogs
    }

    return render(request , 'main/index.html', context)
    

def about(request):
    baners = models.CoffeeBaner.objects.all()
    about = models.About.objects.last()
    context = {
        'baners':baners,
        'about':about,
    }
    return render(request , 'main/about.html', context)


def coffees(request):
    baners = models.CoffeeBaner.objects.all()
    ourcoffee = models.OurCoffee.objects.all()
    coffees = []
    row = []
    for i in range(len(ourcoffee)):
        if (i + 1) % 4 == 0:
            row.append(ourcoffee[i])
            coffees.append(row)
            row = []
        else:
            row.append(ourcoffee[i])

    if len(ourcoffee) % 4 != 0:
        coffees.append(row)


    context = {
        'baners':baners,
        'coffees':coffees, 
    }
    return render(request , 'main/coffees.html', context)


def blog(request):
    baners = models.CoffeeBaner.objects.all()
    ourblogs = models.OurBlogs.objects.all()
    context = {
        'baners':baners,
        'ourblogs':ourblogs,
    }
    return render(request , 'main/blog.html', context)


def contact(request):
    baners = models.CoffeeBaner.objects.all()
    contact = models.Contact.objects.all()

    if request.method =='POST':
        f_name = request.POST['f_name']
        email = request.POST['email']
        phone = request.POST['phone']
        text = request.POST['text']


        models.Contact.objects.create(
            f_name = f_name,
            email = email,
            phone = phone,
            text = text
            
        )

    context = {
        'baners':baners,
        'contact':contact,
    }
    return render(request , 'main/contact.html', context)
