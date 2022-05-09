from .models import Article, Tag, Scope
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag_count = 0
        for form in self.forms:
            if form.cleaned_data.get('DELETE'):
                continue
            if form.cleaned_data.get('is_main'):
                main_tag_count += 1

        if main_tag_count > 1:
            raise ValidationError('Главный тег может быть только один')
        if main_tag_count == 0:
            raise ValidationError('Назначьте главный тег')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
