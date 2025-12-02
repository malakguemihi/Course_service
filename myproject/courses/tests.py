from django.test import TestCase
from .models import Student

class StudentControllerTest(TestCase):

    def test_should_save_student(self):
        student = Student(first_name="Charlie", last_name="Brown", email="charlie@example.com")
        student.save()

        # التأكد من وجود طالب واحد في قاعدة البيانات
        self.assertEqual(Student.objects.count(), 1)

    def test_should_find_all_students(self):
        # إنشاء طالب
        Student.objects.create(first_name="Charlie", last_name="Brown", email="charlie@example.com")

        students = Student.objects.all()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].first_name, "Charlie")
        self.assertEqual(students[0].last_name, "Brown")
