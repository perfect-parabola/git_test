from django.db import models

# Create your models here.
class country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class person(models.Model):
    gender_type = (
        ('M', '남자'),
        ('F', '여자')
    )
    name = models.CharField(max_length=20)
    gender = models.CharField(choices=gender_type, max_length=2)
    age = models.PositiveIntegerField()
    country = models.ForeignKey(country)

    def __str__(self):
        return self.name

class relationship(models.Model):
    relationship_type = (
        ('1', '어사'),
        ('2', '친구'),
        ('3', '썸'),
        ('4', '연인')
    )
    person1 = models.ForeignKey(person, related_name='relationship1')
    person2 = models.ForeignKey(person, related_name='relationship2')
    type = models.CharField(choices = relationship_type, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('person1', 'person2', 'type')

    def __str__(self):
        return self.person1.name + "__"+self.person2.name + "__"+self.get_type_display()

class animal(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class pet(models.Model):
    name = models.CharField(max_length=20)
    animal = models.ForeignKey(animal)
    owner = models.ForeignKey(person)

    def __str__(self):
        return self.name
