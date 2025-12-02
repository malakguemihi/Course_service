from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Student, StudentCourse
from .serializers import CourseSerializer, StudentSerializer, StudentCourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        name = request.GET.get('name')
        instructor = request.GET.get('instructor')
        category = request.GET.get('category')

        queryset = self.queryset
        if name:
            queryset = queryset.filter(name__icontains=name)
        if instructor:
            queryset = queryset.filter(instructor__icontains=instructor)
        if category:
            queryset = queryset.filter(category__icontains=category)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=['post'])
    def enroll(self, request, pk=None):
        student = self.get_object()
        course_id = request.data.get('course_id')

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=404)

        StudentCourse.objects.create(student=student, course=course)
        return Response({'message': f'Student {student} enrolled in {course}'})

    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        student = self.get_object()
        courses = student.courses.all()  # حسب العلاقة ManyToMany
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['delete'])
    def delete_student(self, request, pk=None):
        student = self.get_object()
        student.delete()
        return Response({'message': f'Student {student.first_name} {student.last_name} deleted successfully'},
                        status=status.HTTP_204_NO_CONTENT)
