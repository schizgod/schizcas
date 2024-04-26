from django.contrib import admin
from .models import Article, CasinoBanner, BlackjackPublication
from django.utils.html import format_html

# Административный класс для статей
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'has_image')
    list_filter = ('pub_date',)
    search_fields = ('title', 'content')
    list_editable = ('title',)  # Редактирование заголовка прямо из списка
    list_display_links = ('pub_date',)  # Делаем 'pub_date' кликабельным

    def has_image(self, obj):
        return obj.image is not None
    has_image.boolean = True
    has_image.short_description = 'Has Image?'

    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('pub_date', 'image'),
        }),
    )

# Регистрация модели Article с указанным административным классом
admin.site.register(Article, ArticleAdmin)

# Административный класс для баннеров казино
@admin.register(CasinoBanner)
class CasinoBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'image_preview', 'get_link_button')
    readonly_fields = ('image_preview',)
    search_fields = ('title', 'description')  # Поиск по заголовку и описанию

    # Предварительный просмотр изображения
    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 300px; max-width: 300px;" />', obj.image.url)
    image_preview.short_description = 'Preview Image'

    # Ссылка на кнопке
    def get_link_button(self, obj):
        if obj.link:
            return format_html('<a href="{}" target="_blank" class="button">Перейти</a>', obj.link)
        return '-'
    get_link_button.short_description = 'Link'

    # Настройка CSS для админки
    class Media:
        css = {
            'all': ('myapp/css/admin.css',),
        }

    class Meta:
        verbose_name_plural = 'Casino Banners'

# Административный класс для публикаций по блэкджеку
@admin.register(BlackjackPublication)
class BlackjackPublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_preview')
    search_fields = ('title', 'description')  # Поиск по заголовку и описанию

    # Предварительный просмотр изображения
    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 1200px; max-width: 1200px;" />', obj.image.url)
    image_preview.short_description = 'Preview Image'
