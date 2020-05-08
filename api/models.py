from django.db.models import Model, CharField, FloatField, ForeignKey, CASCADE


# Create your models here.
class Producer(Model):
    name = CharField(max_length=125)

    def __str__(self):
        return self.name

class Tire(Model):
    SEOSON = [("Летние", "Summer"),("Зимние", "Winter")]

    width = FloatField(default=0)
    profile = FloatField(default=0)
    diameter = CharField(max_length=4, blank=True)

    seoson = CharField(max_length=6, choices=SEOSON, default="L")
    producer = ForeignKey(Producer, on_delete=CASCADE)

    def __str__(self):
        return self.producer
