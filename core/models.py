from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.__class__.__name__} (ID: {self.pk})"
    class Meta:
        abstract = True


class Singer(BaseModel):
    name = models.CharField(max_length=255, help_text="Enter the name of the singer")
    description = models.TextField(
        blank=True, null=True, help_text="Enter a brief description of the singer"
    )

    def __str__(self):
        return f"Singer:  0{self.name} (ID: {self.pk})"

    class Meta:
        verbose_name = "Singer"
        verbose_name_plural = "Singers"
        ordering = ["name"] 


class Album(BaseModel):
    title = models.CharField(max_length=255, help_text="Enter the title of the album")
    release_date = models.DateField(help_text="Enter the release date of the album")
    singer = models.ForeignKey(
        Singer,
        on_delete=models.CASCADE,
        related_name="albums",
        help_text="Select the singer for this album",
    )

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        ordering = ["release_date"]
