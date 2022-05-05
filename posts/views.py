from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, EmailMessage
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
from project import settings
from django.core.files.storage import FileSystemStorage

from .forms import *
# from .models import User_people
# Create your views here.
def index(request):
    return render(request, 'posts/index.html', {'title': 'Main Page'})

# def send_message(request, post_id):
def send_message(request, post_id):
    if request.method == 'POST':
        form = Sendmessage(request.POST, request.FILES)
        subject = request.POST.get('subject')
        message = request.POST.get('text')

        from_email = settings.EMAIL_HOST_USER
        users = User_people.objects.get(id=int(post_id))
        to_list = [users.email]
        email = EmailMessage(subject, message,
                  from_email,
                  to_list,
                  headers={'Reply-To': from_email})
        if request.FILES:
            uploaded_file = request.FILES['file']
            email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
        email.send()
        return redirect('users_info')
    else:
        form = Sendmessage()
        context = {
            'title': 'Send Message',
            'form': form
        }
        return render(request, 'posts/send_message.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            subject = "You are Welcome"
            message = "It is Tolegen Askars Project. "
            from_email = settings.EMAIL_HOST_USER
            users = request.POST.get('email')
            to_list = [users]
            send_mail(subject, message,
                      from_email,
                      to_list,
                      fail_silently=False)
            return redirect('users_info')
        else:
            form.add_error('None', 'Error while add information')
            return 2
    else:
        form = SignUp()
    context = {
        'title': 'Registration',
        'form': form
    }
    return render(request, 'posts/signup.html', context)

def just_test():
    return False

def users_info(request):
    return render(request, 'posts/users_info.html', {'title': 'Users Information'})

def test_my_function():
    return 2

#Boxing
def boxing(request):
    return render(request, 'posts/boxing.html', {'title': 'Boxing Page'})

def create_boxing(request):
    error = ''
    if request.method == 'POST':
        form = BoxingCreate(request.POST)  # form = BoxingCreate(request.POST, request.FILES)
        if form.is_valid():
            # newdoc = Boxing(docfile=request.FILES['docfile'])
            # newdoc.save()
            form.save()
            return redirect('boxing')
        else:
            form.add_error('None', 'Error while add information')
    else:
        form = BoxingCreate()
    context = {
        'title': 'Добавить спортсмена',
        'form': form,
        'error': error
    }
    return render(request, 'posts/create_boxing.html', context)

def update_boxing(request, post_id):
    error = ''
    post_id = int(post_id)
    try:
        post_sel = Boxing.objects.get(id = post_id)
    except Boxing.DoesNotExist:
        return redirect('boxing')

    form = BoxingCreate(request.POST or None, instance=post_sel)
    if form.is_valid():
        form.save()
        return redirect('boxing')
    context = {
        'title': 'Добавить спортсмена',
        'form': form,
        'error': error
    }
    return render(request, 'posts/create_boxing.html', context)

def delete_boxing(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Boxing.objects.get(id = post_id)
    except Boxing.DoesNotExist:
        return redirect('boxing')
    post_sel.delete()
    return redirect('boxing')

def show_boxing(request, post_slug):
    post = get_object_or_404(Boxing, slug=post_slug)
    context = {'post': post}
    return render(request, 'posts/post.html', context=context)



#Wrestling
def wrestling(request):
    return render(request, 'posts/wrestling.html', {'title': 'Wrestling Page'})

def create_wrestling(request):
    error = ''
    if request.method == 'POST':
        form = WrestlingCreate(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Wrestling(docfile=request.FILES['docfile'])
            newdoc.save()
            form.save()
            return redirect('wrestling')
        else:
            error = "Форма была неверной"

    form = WrestlingCreate()
    context = {
        'title': 'Добавить спортсмена',
        'form': form,
        'error': error
    }
    return render(request, 'posts/create_wrestling.html', context)

def update_wrestling(request, post_id):
    error = ''
    post_id = int(post_id)
    try:
        post_sel = Wrestling.objects.get(id = post_id)
    except Wrestling.DoesNotExist:
        return redirect('wrestling')

    form = WrestlingCreate(request.POST or None, instance=post_sel)
    if form.is_valid():
        form.save()
        return redirect('wrestling')
    context = {
        'title': 'Добавить спортсмена',
        'form': form,
        'error': error
    }
    return render(request, 'posts/create_wrestling.html', context)

def delete_wrestling(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Wrestling.objects.get(id = post_id)
    except Wrestling.DoesNotExist:
        return redirect('wrestling')
    post_sel.delete()
    return redirect('wrestling')

def show_wrestling(request, post_slug):
    post = get_object_or_404(Wrestling, slug=post_slug)
    context = {'post': post}
    return render(request, 'posts/post.html', context=context)


#Athletics
def athletics(request):
    return render(request, 'posts/athletics.html', {'title': 'Athletics Page'})
def create_athletics(request):
    error = ''
    if request.method == 'POST':
        form = AthleticsCreate(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Athletics(docfile=request.FILES['docfile'])
            newdoc.save()
            form.save()
            return redirect('athletics')
        else:
            error = "Форма была неверной"

    form = AthleticsCreate()
    context = {
        'title': 'Добавить спортсмена',
        'form': form,
        'error': error
    }
    return render(request, 'posts/create_athletics.html', context)

def update_athletics(request, post_id):
    error = ''
    post_id = int(post_id)
    try:
        post_sel = Athletics.objects.get(id = post_id)
    except Athletics.DoesNotExist:
        return redirect('athletics')

    form = AthleticsCreate(request.POST or None, instance=post_sel)
    if form.is_valid():
        form.save()
        return redirect('athletics')
    context = {
        'title': 'Добавить спортсмена',
        'form': form,
        'error': error
    }
    return render(request, 'posts/create_athletics.html', context)

def delete_athletics(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Athletics.objects.get(id = post_id)
    except Athletics.DoesNotExist:
        return redirect('athletics')
    post_sel.delete()
    return redirect('athletics')

def show_athletics(request, post_slug):
    post = get_object_or_404(Athletics, slug=post_slug)
    context = {'post': post}
    return render(request, 'posts/post.html', context=context)


#Weightlifting
def weightlifting(request):
    return render(request, 'posts/weightlifting.html', {'title': 'Weightlifting Page'})

def create_weightlifting(request):
    error = ''
    if request.method == 'POST':
        form = WeightliftingCreate(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Weightlifting(docfile=request.FILES['docfile'])
            newdoc.save()
            form.save()
            return redirect('weightlifting')
        else:
            error = "Добавить спортсмена"

    form = WeightliftingCreate()
    context = {
        'title': 'Добавить боксера',
        'form': form,
        'error': error
    }
    return render(request, 'posts/create_weightlifting.html', context)

def update_weightlifting(request, post_id):
    error = ''
    post_id = int(post_id)
    try:
        post_sel = Weightlifting.objects.get(id = post_id)
    except Weightlifting.DoesNotExist:
        return redirect('weightlifting')

    form = WeightliftingCreate(request.POST or None, instance=post_sel)
    if form.is_valid():
        form.save()
        return redirect('weightlifting')
    context = {
        'title': 'Добавить спортсмена',
        'form': form,
        'error': error
    }
    return render(request, 'posts/create_weightlifting.html', context)

def delete_weightlifting(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Weightlifting.objects.get(id = post_id)
    except Weightlifting.DoesNotExist:
        return redirect('weightlifting')
    post_sel.delete()
    return redirect('weightlifting')

def show_weightlifting(request, post_slug):
    post = get_object_or_404(Weightlifting, slug=post_slug)
    context = {'post': post}
    return render(request, 'posts/post.html', context=context)


#Cycling
def cycling(request):
    return render(request, 'posts/cycling.html', {'title': 'Cycling Page'})

def create_cycling(request):
    error = ''
    if request.method == 'POST':
        form = CyclingCreate(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Cycling(docfile=request.FILES['docfile'])
            newdoc.save()
            form.save()
            return redirect('cycling')
        else:
            error = "Форма была неверной"

    form = CyclingCreate()
    context = {
        'title': 'Добавить спортсмена',
        'form': form,
        'error': error
    }
    return render(request, 'posts/create_cycling.html', context)

def update_cycling(request, post_id):
    error = ''
    post_id = int(post_id)
    try:
        post_sel = Cycling.objects.get(id = post_id)
    except Cycling.DoesNotExist:
        return redirect('cycling')

    form = CyclingCreate(request.POST or None, instance=post_sel)
    if form.is_valid():
        form.save()
        return redirect('cycling')
    context = {
        'title': 'Добавить спортсмена',
        'form': form,
        'error': error
    }
    return render(request, 'posts/create_cycling.html', context)

def delete_cycling(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Cycling.objects.get(id = post_id)
    except Cycling.DoesNotExist:
        return redirect('cycling')
    post_sel.delete()
    return redirect('cycling')

def show_cycling(request, post_slug):
    post = get_object_or_404(Cycling, slug=post_slug)
    context = {'post': post}
    return render(request, 'posts/post.html', context=context)



#Team Sports
def team_sports(request):
    return render(request, 'posts/team_sports.html', {'title': 'Team Sports Page'})

def create_team_sports(request):
    error = ''
    if request.method == 'POST':
        form = Team_sportsCreate(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Cycling(docfile=request.FILES['docfile'])
            newdoc.save()
            form.save()
            return redirect('team_sports')
        else:
            error = "Форма была неверной"

    form = Team_sportsCreate()
    context = {
        'title': 'Добавить спортсмена',
        'form': form,
        'error': error
    }
    return render(request, 'posts/create_team_sports.html', context)

def update_team_sports(request, post_id):
    error = ''
    post_id = int(post_id)
    try:
        post_sel = Team_sports.objects.get(id = post_id)
    except Team_sports.DoesNotExist:
        return redirect('team_sports')

    form = Team_sportsCreate(request.POST or None, instance=post_sel)
    if form.is_valid():
        form.save()
        return redirect('team_sports')
    context = {
        'title': 'Добавить спортсмена',
        'form': form,
        'error': error
    }
    return render(request, 'posts/create_team_sports.html', context)

def delete_team_sports(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Team_sports.objects.get(id = post_id)
    except Team_sports.DoesNotExist:
        return redirect('team_sports')
    post_sel.delete()
    return redirect('team_sports')

def show_team_sports(request, post_slug):
    post = get_object_or_404(Team_sports, slug=post_slug)
    context = {'post': post}
    return render(request, 'posts/post.html', context=context)

