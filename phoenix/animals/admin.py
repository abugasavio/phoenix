from django.contrib import admin
from .models import Animal, Breed, Breeder, Color, Sire, Dam


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(Breeder)
class BreederAdmin(admin.ModelAdmin):
    pass


@admin.register(Sire)
class SireAdmin(admin.ModelAdmin):
    pass


@admin.register(Dam)
class DamAdmin(admin.ModelAdmin):
    pass