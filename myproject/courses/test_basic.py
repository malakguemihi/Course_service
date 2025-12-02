# students/tests/test_basic.py
from django.test import TestCase

class DemoTestApplicationTests(TestCase):
    def test_context_loads(self):
        """
        هذا الاختبار يشبه DemoTestApplicationTests في Spring Boot.
        فقط يتحقق أن إعدادات Django تعمل بدون أخطاء عند تحميل التطبيق.
        """
        self.assertTrue(True)
