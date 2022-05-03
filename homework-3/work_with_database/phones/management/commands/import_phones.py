import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone_object = Phone(
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=slugify(phone['name'])
            )
            phone_object.save()

# Наверно slug было бы правильнее сделать вот так, как в нагугленном решении,
# но мне кажется что мы еще не проходили такой материал. Напишите мне если я не прав)
#
# class Test(models.Model):
#     q = models.CharField(max_length=30)
#     s = models.SlugField()
#
#     def save(self, *args, **kwargs):
#         if not self.id:
#             # Newly created object, so set slug
#             self.s = slugify(self.q)
#
#         super(Test, self).save(*args, **kwargs)

