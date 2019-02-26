from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=10)
    image = models.ImageField(upload_to='post/', null=True, blank=True)
    content = models.TextField(null=True)
    def __str__(self):
        return self.title + "__" +self.author

class comment(models.Model):
    post = models.ForeignKey(post, related_name="post_comment")
    content = models.CharField(max_length=200)

class supplier(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class plan(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class plan_group(models.Model):
    name = models.CharField(max_length=100)
    supplier = models.ForeignKey(supplier)

    def __str__(self):
        return self.name

class plan_plan_group_manage(models.Model):
    plan = models.ForeignKey(plan)
    plan_group = models.ForeignKey(plan_group)

    class Meta:
        unique_together = ('plan', 'plan_group__supplier')

    def __str__(self):
        return str(self.plan) + "__" +str(self.plan_group)