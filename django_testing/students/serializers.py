from rest_framework import serializers
from students.models import Course, Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', "student_name", "birth_date")

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.student_name = validated_data.get(
            'student_name', instance.student_name)
        instance.birth_date = validated_data.get(
            'birth_date', instance.birth_date)
        instance.save()

        return instance


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data, partial=True):

        instance.name = validated_data.get(
                'name', instance.name)
        instance.students = validated_data.get(
                'students', instance.students)
        instance.save()

        return instance
