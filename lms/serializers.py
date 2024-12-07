from rest_framework import serializers

from .models import Course, Lesson
from .models import Course

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'description', 'preview', 'video_url']

class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)  # Включаем уроки в сериализатор курса

    class Meta:
        model = Course
        fields = ['id', 'preview', 'description', 'lesson_count', 'lessons']

    def get_lesson_count(self, obj):
        return obj.lessons.count()


