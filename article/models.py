from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from mongoengine import *

"""
from mongoengine import *

class Choice(EmbeddedDocument):
    choice_text = StringField(max_length=200)
    votes = IntField(default=0)

class Poll(Document):
    question = StringField(max_length=200)
    pub_date = DateTimeField(help_text='date published')
    choices = ListField(EmbeddedDocumentField(Choice))
    
    "_id" : ObjectId("5483165de50c050005e4b29f"),
    "question" : "What's up?",
    "pub_date" :  ISODate("2013-04-14T11:06:21.922Z"),
    "choices" : [
        {
            "choice_text" : "Not much",
            "votes" : 0
        },
        {
            "choice_text" : "Just hacking again",
            "votes" : 1
        }
    ],
}
"""

# Create your models here.
class Plate(Document):
    url = URLField()
    title = StringField()
    text = StringField()
    top_image = URLField(default='')
    imagelinks = ListField(URLField(), default=list)
    created_time = DateTimeField(default=datetime.now)