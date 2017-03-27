# -*- coding: UTF-8 -*-
import person
import sqlite3


class User(person.Person):
    def __init__(self):
        super(User, self).__init__()
        self._id = None
        self._name = None
        self._surname = None
        self._dbname = 'db.sqlite3'

    @property
    def name(self):
        """Имя пользователя"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        return

    @name.deleter
    def name(self):
        del self._name
        return

    @property
    def surname(self):
        """Фамилия пользователя"""
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value
        return

    @surname.deleter
    def surname(self):
        del self._surname
        return

    def load(self, paramDict):
        query = "SELECT * FROM users WHERE "
        counter = len(paramDict)
        for column, value in paramDict.iteritems():
            query += '%s=\"%s\"' % (column, value)
            if counter == 1:
                query += ";"
            else:
                query += " OR "
            counter -= 1

        connection = sqlite3.connect(self._dbname)
        result = connection.execute(query).fetchone()
        connection.close()

        self._id = result[0]
        self._name = str(result[1])
        self._surname = str(result[2])
        return

    def save(self):
        if self._id is None:
            query = "INSERT INTO users (name, surname) VALUES (?,?);"
            connection = sqlite3.connect(self._dbname)
            connection.execute(query, (self.name, self.surname))
            connection.commit()
            connection.close()
        else:
            self._update()
        return

    def _update(self):
        query = "UPDATE users SET name = ?, surname = ? WHERE id = ?;"
        connection = sqlite3.connect(self._dbname)
        connection.execute(query, (self.name, self.surname, self._id))
        print "update running"
        return

    def delete(self):
        query = "DELETE FROM users WHERE name=? AND surname=?;"
        connection = sqlite3.connect(self._dbname)
        connection.execute(query, (self.name, self.surname))
        connection.commit()
        connection.close()
        return
