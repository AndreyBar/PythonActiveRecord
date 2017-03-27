# -*- coding: UTF-8 -*-

import unittest

from user import User


class ARTest(unittest.TestCase):

    def test_user_save(self):
        t_user = User()
        t_user.name = 'Test_name_1'
        t_user.surname = 'Test_surname_1'
        t_user.save()
        self.assertEqual(t_user.name, 'Test_name_1')
        self.assertEqual(t_user.surname, 'Test_surname_1')
        print "Saved successfully"

        # Удаляем тестового пользователя
        t_user.delete()

    def test_user_load(self):
        target_name = 'Test_name'
        target_surname = 'Test_surname'
        user_for_load = User()

        # Создаем временного пользователя для проверки функции load()
        user_for_save = User()
        user_for_save.name = 'Test_name'
        user_for_save.surname = 'Test_surname'
        user_for_save.save()

        user_for_load.load({'name': target_name, 'surname': target_surname})
        self.assertEqual(target_name, user_for_load.name, 'incorrect name loading')
        self.assertEqual(target_surname, user_for_load.surname, 'incorrect surname loading')
        print "Loaded successfully"

        # Удаляем тестового пользователя
        user_for_save.delete()
        user_for_load.delete()

    def test_user_update(self):
        testuser = User()
        testuser.name = 'Update_test_name'
        testuser.surname = 'Update_test_surname'
        testuser.save()

        # Меняем имя и фамилию пользователя для проверки метода _update()
        testuser.name = 'Updated_name'
        testuser.surname = 'Updated_surname'
        testuser.save()
        self.assertEqual(testuser.name, 'Updated_name')
        self.assertEqual(testuser.surname, 'Updated_surname')
        print 'Updated successfully'

        testuser.delete()
        testuser.delete()

    def test_user_delete(self):
        target_name = 'Delete_test_name'
        target_surname = 'Delete_test_surname'
        testuser = User()
        testuser.name = target_name
        testuser.surname = target_surname
        testuser.delete()
        print "Deleted successfully"


if __name__ == '__main__':  # якщо файл запущено, а не імпортовано, то виконається наступний код
    unittest.main()

