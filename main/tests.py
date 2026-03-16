from django.test import TestCase

from .models import Course

class CourseTest(TestCase):
    def setUp(self):
        Course.objects.create(name="Python", teacher="Ali", price=900.00)
        Course.objects.create(name="C++", teacher="Hoshim", price=700.00)
        Course.objects.create(name="Java", teacher="Vali", price=800.00)


    def test_get_all(self):
        courses = Course.objects.all()
        self.assertEqual(courses.count(), 3)

    
    def test_filter(self):
        courses = Course.objects.filter(price=900.00)
        self.assertEqual(courses.count(), 1)

    

