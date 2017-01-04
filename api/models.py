from __future__ import unicode_literals

import os
from django.db import models
from django.utils import timezone
from model_utils import Choices
import datetime

PORTFOLIO_CHOICESUSER = Choices((1, 'student', ('Estudiante')), (2, 'teacher', ('Profesor')))

PORTFOLIO_CHOICESCAREER = (
    (1, 'Ingenieria de Sistemas'),
    (2, 'Ingenieria Petroquimica'),
    (3, 'Ingenieria Naval'),
    (4, 'Enfermeria'),
    (5, 'Turismo'),
    (6, 'Economia'),
)

PORTFOLIO_CHOICESTURN = (
    (1, 'Diurno'),
    (2, 'Nocturno'),
)

PORTFOLIO_CHOICESPPTTEG = (
    (1, 'Trabajo Especial de Grado'),
    (2, 'Practica Profesionales'),
)

PORTFOLIO_CHOICESARCHIVE = (
    (1, 'WORD'),
    (2, 'PDF'),
    (3, 'Power Point'),
)

PORTFOLIO_CHOICESSTATUS = (
    (1, 'Activo'),
    (2, 'Inactivo'),
    (3, 'Bloqueado'),
)


def get_image_path(self, filename):
    route = os.path.join('images/resume/%s' % self.alt, filename)
    return route


class Image(models.Model):
    image = models.ImageField(upload_to=get_image_path)
    alt = models.CharField(max_length=20, default='image')
    description = models.CharField(max_length=150)

    def __unicode__(self):
        return self.alt


class Career(models.Model):
    careerTypo = models.CharField(max_length=50)
    turn = models.SmallIntegerField(choices=PORTFOLIO_CHOICESTURN)
    imageCareer = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return self.careerTypo


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    image = models.CharField(max_length=200)
    typoUser = models.SmallIntegerField(choices=PORTFOLIO_CHOICESUSER, default=0)
    typoCarrer = models.CharField(max_length=50, default="")
    career = models.ForeignKey(Career, on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return self.name


class Semester(models.Model):
    numSemester = models.SmallIntegerField()
    career = models.ForeignKey(Career, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.numSemester


class News(models.Model):
    news = models.CharField(max_length=500)
    status = models.SmallIntegerField(choices=PORTFOLIO_CHOICESSTATUS)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    docs = models.CharField(max_length=100)
    privilege = models.SmallIntegerField(choices=PORTFOLIO_CHOICESUSER, default=1)
    date = models.DateField(default=timezone.now())

    def __unicode__(self):
        return self.news

    def as_json(self):
        return dict(
            id=self.id,
            news=self.news,
            status=self.status,
            image=self.image.image.url,
            description=self.description,
            docs=self.docs,
            privelege=self.privilege,
            date=self.date
        )


class PppTeg(models.Model):
    typeNews = models.SmallIntegerField(choices=PORTFOLIO_CHOICESPPTTEG)
    news = models.CharField(max_length=500)
    status = models.SmallIntegerField(choices=PORTFOLIO_CHOICESSTATUS)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    docs = models.CharField(max_length=100)

    def __unicode__(self):
        return self.news

    def as_json2(self):
        return dict(
            id=self.id,
            typeNew=self.typeNews,
            new=self.news,
            statu=self.status,
            image=self.image.image.url,
            docs=self.docs
        )


class Docs(models.Model):
    name = models.CharField(max_length=100, default='name')
    typeDocs = models.SmallIntegerField(choices=PORTFOLIO_CHOICESARCHIVE)
    status = models.SmallIntegerField(choices=PORTFOLIO_CHOICESSTATUS)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    docs = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def as_json3(self):
        return dict(
            id=self.id,
            typeDoc=self.typeDocs,
            nam=self.name,
            statu=self.status,
            image=self.image.image.url,
            docs=self.docs,
            descriptio=self.description
        )


class Event(models.Model):
    title = models.CharField(max_length=100, default='title')
    date = models.DateField(default=timezone.now)
    description = models.CharField(max_length=100)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

    def as_json4(self):
        return dict(
            id=self.id,
            titl=self.title,
            dat=self.date,
            image=self.image.image.url,
            descriptio=self.description
        )


class Notifications(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    status = models.SmallIntegerField(choices=PORTFOLIO_CHOICESSTATUS)

    def __unicode__(self):
        return self.name

