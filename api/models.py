from django.db.models import Model, CharField, FloatField, ForeignKey, IntegerField, ImageField, AutoField, CASCADE
from django.contrib.auth.models import User;


class Producer(Model):
    name = CharField(max_length=125)

    def __str__(self):
        return self.name

class Tire(Model):
    SEOSON = [("Летние", "Summer"),("Зимние", "Winter"), ("Всесезонные", "Mixed")]

    id = AutoField(primary_key=True)

    width = FloatField(default=0)
    profile = FloatField(default=0)
    diameter = CharField(max_length=20, blank=True)

    seoson = CharField(max_length=11, choices=SEOSON, default="Summer")
    producer = ForeignKey(Producer, on_delete=CASCADE)

    price = IntegerField(default=0)
    image = ImageField(blank=True, null=True)
    def __str__(self):
        return f'Название : {self.producer.name}\nШирина : {self.width}\nПрофиль : {self.profile}\nДиаметер : {self.diameter}\nСезон : {self.seoson}'

class Disc(Model):
    width = FloatField(default=0)
    producer = ForeignKey(Producer, on_delete=CASCADE)
    fasteners_quantity = IntegerField()
    fasteners_distance = IntegerField()
    diameter = FloatField()

    price = IntegerField(default=0)

    def __str__(self):
        return f'Название : {self.producer.name}\nШирина : {self.width}\nДиаметер : {self.diameter}'

class Car(Model):
    mark = CharField(max_length=150)
    model = CharField(max_length=150)
    year = IntegerField()
    modification = CharField(max_length=100)
    type_size = CharField(max_length=100)
    # TODO: check the relationship with tires
    tire = ForeignKey(Tire, on_delete=CASCADE)
    disc = ForeignKey(Disc, on_delete=CASCADE)

    def __str__(self):
        return f'{self.mark}-{self.model}-{self.year}-{self.modification}-{self.type_size}'