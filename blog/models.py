from django.db import models

# Create your models here.
from django.db.models import permalink, ImageField
from django.utils import timezone
import datetime


def post_path(instance, filename):
    return '{0}/{1}'.format(instance.post.slug, filename)


def postpreview_path(instance, filename):
    return '{0}/{1}'.format(instance.slug, filename)


class Tag(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    image = models.ImageField(upload_to="tags/")
    preview_text = models.TextField()

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_tag', None, {'slug': self.slug})


class PostPreview(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to=postpreview_path)
    title = models.CharField(max_length=100, unique=True)
    catching_text = models.TextField()
    time_posted = models.DateTimeField(db_index=True, auto_now_add=True)
    tags = models.ManyToManyField('blog.Tag')
    post = models.OneToOneField('blog.Post')

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})

    def was_published_recently(self):
        return self.posted >= timezone.now() - datetime.timedelta(days=5)


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})


class TextBlock(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post)


class ImageBlock(models.Model):
    alt = models.CharField(max_length=200)
    post = models.ForeignKey(Post)
    image = models.ImageField(upload_to=post_path)


class Citate(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    href = models.CharField(max_length=100)

    def __unicode__(self):

        return '%s \n %s' % (self.text, self.author)
