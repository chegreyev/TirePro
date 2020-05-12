from django.db.models import Model, CharField, FloatField, ForeignKey, IntegerField,CASCADE


class Producer(Model):
    name = CharField(max_length=125)

    def __str__(self):
        return self.name

class Tire(Model):
    SEOSON = [("Летние", "Summer"),("Зимние", "Winter"), ("Всесезонные", "Mixed")]

    width = FloatField(default=0)
    profile = FloatField(default=0)
    diameter = CharField(max_length=20, blank=True)

    seoson = CharField(max_length=11, choices=SEOSON, default="L")
    producer = ForeignKey(Producer, on_delete=CASCADE)

    def __str__(self):
        return self.producer.name

class Car(Model):
    mark = CharField(max_length=150)
    model = CharField(max_length=150)
    year = IntegerField()
    modification = CharField(max_length=100)
    type_size = CharField(max_length=100)

    tire = ForeignKey(Tire, on_delete=CASCADE)

    def __str__(self):
        return f'{self.mark}-{self.model}-{self.year}-{self.modification}-{self.type_size}'