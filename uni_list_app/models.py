from django.db import models
from django.urls import reverse


# class Member(models.Model):
#     username = models.CharField(max_length=255)
#     name = models.CharField(max_length=255, blank=True, default='')
#     join_date = models.DateField(null=True)


class UniList(models.Model):
    title = models.CharField(max_length=100)
    creation_date = models.DateField(null=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title


class UniItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    uni_list = models.ForeignKey(UniList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.uni_list.id), str(self.id)]
        )

    def __str__(self):
        return self.title


class Meta:
    ordering = ["due_date"]
