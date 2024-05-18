from django.db import models


# Create your models here.
class Tag(models.Model):
    """This models maps tags for each project.
    Many projects can be associated to many tags.
    """

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    """This model maps each individual project."""

    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    live_url = models.URLField(max_length=200, blank=True, null=True)
    source_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    """This model stores images for each individual project."""

    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="project_images/")

    def __str__(self):
        return f"{self.project.title} Image"
