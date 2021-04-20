from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    empty_value_display = 'Эта запись означает, что не заполнили форму'
    list_display = ("text", "pub_date", "author")
    list_display_links = ("text",)
    search_fields = ("text",)
    list_filter = ("pub_date",)


# при регистрации модели Post источником конфигурации для неё назначаем класс PostAdmin
admin.site.register(Post, PostAdmin)

