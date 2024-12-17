from django.shortcuts import render, get_object_or_404,redirect
from . models import Category, New, Book, User_bot
from .forms import CategoryForm, BookForm, NewForm , LoginForm, UserForm,RegisterForm
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
 

@login_required
def index(request):
    all_book = Book.objects.count() 
    all_user =User.objects.count()
    all_category = Category.objects.count()
    context = {'all_book':all_book,  'all_category':all_category, 'all_user':all_user} 
    return render(request, 'index.html' , context )

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.info(request,'Disabled Account')
            else:
                messages.info(request, 'Check your username or password')

    else:
        form = LoginForm()
    return render(request, 'login.html',{'form':form} )


def logoutView(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Kayıt olduktan sonra giriş yap
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
    



def categors(request):
    categorys = Category.objects.all()  
    context = {'categorys':categorys} 
    return render(request, 'categors.html', context )



def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('categors')  # Silme işleminden sonra kategori liste sayfasına yönlendirir

# Book Silme Fonksiyonu
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('books', category_id=book.category.id) 

def delete_user (request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('users')  # Silme işleminden sonra user liste sayfasına yönlendirir

def delete_news(request, new_id):
    new = get_object_or_404(New, id=new_id)
    new.delete()
    return redirect('news')  # Silme işleminden sonra new liste sayfasına yönlendirir


 

def books(request, category_id ):
    category = get_object_or_404(Category, id=category_id)
    books = category.books.all()  
    context = {'category':category , 'books':books}
    return render(request, 'books.html' , context)







def users(request):
    users = User.objects.filter(is_active=True)
    context = {'users':users}
    return render(request, 'users.html' , context)



def user_about(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {'user':user}

    return render(request, 'user_about.html' , context)





def news(request):
    news = New.objects.all().order_by("-date")
    context = {'news':news}
    return render(request, 'news.html', context )



 

def news_see(request, new_id):
    new = get_object_or_404(New, id=new_id)
    context = {'new':new}
    return render(request, 'news_see.html' , context )





def settings(request):
    return render(request, 'settings.html' )



def profile(request):
    return render(request, 'profile.html' )
 
def edit_profile(request):
    return render(request, 'edit_profile.html' )





def add_categor(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categors')
    else:
        form = CategoryForm()
    return render(request, 'add_categor.html', {'form': form})
        

 



def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categors')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form} )
 







def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})
    






def add_new(request):
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = NewForm()
    return render(request, 'add_new.html', {'form': form})
    





 

def about(request):
    return render(request, 'about.html' )








 






