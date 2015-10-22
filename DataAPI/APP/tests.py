from django.test import TestCase

# Create your tests here.
from APP.models import Blog, Author, Entry
t=Entry.objects.extra(select={'is_recent': "pub_date > '2006-01-01'"})
print t
#test
