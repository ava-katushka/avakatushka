__author__ = 'ava-katushka'
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from blog.models import Post, PostPreview, Tag, TextBlock, ImageBlock
from django.core.files import File
from shutil import copy2
_SCRIPT_ROOT = "/Users/ava-katushka/Documents/WebProjects/avakatushka/blog/uploading"
_PICTURES_DIR = os.path.join(_SCRIPT_ROOT, "pictures")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

class ImageFileBlog:
    def __init__(self, image_name, image_num, image_alt, slug):
        self.image_name = "/" + "media" + "/" + slug + "/" +  image_name
        self.image_num = image_num
        self.image_alt = image_alt
        blog_directory = os.path.join(MEDIA_ROOT, slug)
        if not os.path.exists(blog_directory):
            os.makedirs(blog_directory)
        copy2(os.path.join(_PICTURES_DIR, image_name), blog_directory)


def get_attribute(line):
    return line.split(":")[1].strip()


def get_imagefile(images, index):
    return images[index].image_name


def get_main_attributes(filename):
    with open(filename) as file:
        lines = file.readlines()
        title = get_attribute(lines[0])
        slug = get_attribute(lines[1])
        category = get_attribute(lines[2])
        return title, slug, category


def get_catching_text_and_text_blocks(filename):
    with open(filename) as file:
        text = file.read()
        blocks = text.split("---------------")
        blocks = blocks[1:]
        blocks = [block.strip() for block in blocks]
        catching_text = blocks[0]
        blocks = blocks[1:]
        return catching_text, blocks


# get_text

filename = os.path.join(_SCRIPT_ROOT, "texts/text.txt")
title, slug, category = get_main_attributes(filename)
catching_text, blocks = get_catching_text_and_text_blocks(filename)
# get images
image_path = os.path.join(_SCRIPT_ROOT, "pictures")
valid_images = [".jpg", ".gif", ".png"]
images = []
for file in os.listdir(image_path):
    ext = os.path.splitext(file)[1]
    if ext.lower() not in valid_images:
        continue
    imagename_splitted = file.split("_", 1)
    image_num = int(imagename_splitted[0])
    image_alt = imagename_splitted[1].split(".")[0]
    ifb = ImageFileBlog(file, image_num, image_alt, slug)
    images.append(ifb)

images = sorted(images, key=lambda f: f.image_num)
###creating models
post = Post(title=title, slug=slug)

image_preview = get_imagefile(images, 0)
tag = Tag.objects.get(pk=category)
post.save()
post_preview = PostPreview(slug=slug, image=image_preview, title=title, catching_text=catching_text, post=post)
post_preview.save()
post_preview.tags.add(tag)
post_preview.save()
for text in blocks:
    text_block = TextBlock(text=text, post=post)
    text_block.save()
for image in images:
    image_block = ImageBlock(alt=image.image_alt, post=post, image=get_imagefile(images, image.image_num))
    image_block.save()
