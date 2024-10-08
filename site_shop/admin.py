from django.contrib import admin

from site_shop.models import Section, Product, Discount, Order, OrderLine, Album, Photo, Article, Comment, \
    FeedbackMessage

# Register your models here.
admin.site.register(Section)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(Album)
admin.site.register(Photo)
#admin.site.register(Article)
admin.site.register(Comment)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('author', 'responsible', 'status')
    search_fields = ['responsible']
    list_filter = ['status']


admin.site.register(FeedbackMessage, FeedbackAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ['date']


admin.site.register(Article, ArticleAdmin)
