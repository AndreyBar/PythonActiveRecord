# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractproperty, abstractmethod


class Person():
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        """Имя"""

    @abstractproperty
    def surname(self):
        """Фамилия"""

    @abstractmethod
    def load(self):
        """Выбрать объекты из БД"""

    @abstractmethod
    def save(self):
        """Сохранить изменения"""

    @abstractmethod
    def _update(self):
        """Обновить запись"""

    @abstractmethod
    def delete(self):
        """Удалить запись"""
