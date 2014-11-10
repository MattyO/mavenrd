from django import forms
from django.contrib import admin
from cms.models import Page, Post, UploadedMedia, MediaCollection

class FormatedTextInput(forms.Textarea):
    pass

class PostForm(forms.ModelForm):
    class Meta:
        exclude = ['author']
        widgets = {"content" : FormatedTextInput(attrs={'class': 'redactor', "rows":30})}

    @property
    def media(self):
        css = {'all': ('vendor/redactor/redactor/redactor.css', ) }
        js = ['vendor/jquery-2.0.3.min.js', 'vendor/redactor/redactor/redactor.js', 'vendor/redactor/init_redactor.js', ] 
        return forms.Media(js=js, css=css)

    #media = property(_media)

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = ['author']
        widgets = {"content" : FormatedTextInput(attrs={'class': 'redactor'})}

    @property
    def media(self):
        css = {'all': ('vendor/redactor/redactor/redactor.css', ) }
        js = ['vendor/jquery-2.0.3.min.js', 'vendor/redactor/redactor/redactor.js', 'vendor/redactor/init_redactor.js', ] 
        return forms.Media(js=js, css=css)

    #media = property(_media)

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

class PageAdmin(admin.ModelAdmin):
    form = PageForm
    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Page, PageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(UploadedMedia)
admin.site.register(MediaCollection)
