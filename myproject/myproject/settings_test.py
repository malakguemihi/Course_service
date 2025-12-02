from .settings import *  # يستورد كل الإعدادات الأساسية

# قاعدة البيانات للاختبارات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # قاعدة بيانات خفيفة في الذاكرة
        'NAME': ':memory:',                       # قاعدة بيانات مؤقتة في الذاكرة
    }
}

# يمكن إضافة أي إعدادات خاصة بالاختبارات هنا
DEBUG = False
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',  # لتسريع الاختبارات
]
