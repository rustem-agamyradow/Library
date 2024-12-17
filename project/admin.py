from django.contrib import admin
from . models  import Book, Category, New, User_bot

@admin.register(Book)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'available')
    list_filter = ('available',)


@admin.register(Category)
class CategoAdmin(admin.ModelAdmin):
    list_display = ('name',)
     


@admin.register(User_bot)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'birthday', 'address', 'phone','image')


@admin.register(New) 
class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'content' )


 