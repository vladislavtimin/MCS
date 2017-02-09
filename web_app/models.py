from django.db import models
#from pygments.lexers import get_all_lexers
#from pygments.styles import get_all_styles
#from pygments.lexers import get_lexer_by_name
#from pygments.formatters.html import HtmlFormatter
#from pygments import highlight


#LEXERS = [item for item in get_all_lexers() if item[1]]
#LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
#STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Category(models.Model):
    title = models.CharField(max_length=50)


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    image = models.CharField(max_length=150)
    price = models.IntegerField()


class Comment(models.Model):
    item = models.ForeignKey(Item, related_name='comments')
    addition_date = models.PositiveIntegerField()
    text = models.CharField(max_length=256)