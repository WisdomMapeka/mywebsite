from django.contrib import admin

from . models import Post, Quotes


class QuotesInline(admin.StackedInline):
	model = Quotes

class PostAdmin(admin.ModelAdmin):
	inlines = [QuotesInline,]
		

admin.site.register(Post, PostAdmin)
admin.site.register(Quotes)