from django.contrib import admin
from .models import (Category, MenuItem, Review, PreOrder, 
                    HomePageContent, AboutPageContent, ContactsPageContent,
                    CatTeamMember, MenuPageContent)

@admin.register(MenuPageContent)
class MenuPageContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_preview']
    
    def image_preview(self, obj):
        if obj.main_image:
            return f'<img src="{obj.main_image.url}" style="width: 50px; height: 50px; object-fit: cover;" />'
        return "Нет фото"
    image_preview.allow_tags = True
    image_preview.short_description = "Главное фото"

@admin.register(CatTeamMember)
class CatTeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'order', 'image_preview']
    list_editable = ['position', 'order']
    list_filter = ['position']
    search_fields = ['name', 'position']
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 50px; height: 50px; object-fit: cover;" />'
        return "Нет фото"
    image_preview.allow_tags = True
    image_preview.short_description = "Фото"

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'philosophy_title']

@admin.register(AboutPageContent)
class AboutPageContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'history_title']

@admin.register(ContactsPageContent)
class ContactsPageContentAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available', 'is_special']
    list_filter = ['category', 'is_available', 'is_special']
    list_editable = ['price', 'is_available', 'is_special']
    search_fields = ['name', 'description']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    readonly_fields = ['created_at']

@admin.register(PreOrder)
class PreOrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'phone', 'total_amount', 'pickup_time', 'created_at', 'is_completed']
    list_filter = ['pickup_time', 'created_at', 'is_completed']
    list_editable = ['is_completed']
    readonly_fields = ['created_at']