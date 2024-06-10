from rest_framework import serializers
<<<<<<< HEAD
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


=======

from students.models import Course, Student


>>>>>>> b384975f6822368497afa684c0352ef1ae7dae6e
class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
<<<<<<< HEAD
        fields = ('id', "name", "students")
=======
        fields = ("id", "name", "students")
>>>>>>> b384975f6822368497afa684c0352ef1ae7dae6e

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

<<<<<<< HEAD
    def update(self, instance, validated_data, partial=True):
        students_data = validated_data.pop('students')
        student = instance.students

        instance.name = validated_data.get(
                'name', instance.name)
        instance.students = validated_data.get(
                'students', instance.students)
        instance.save()

        student.student_name = students_data.get(
                'student_name', student.student_name)
        student.birth_date = students_data.get(
                'birth_date', student.birth_date)
        student.save()

        return instance
=======
    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name', instance.name)
        instance.students = validated_data.get(
            'students', instance.students)
        instance.save()

        return instance


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ("id", "student_name", "birth_date")

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name', instance.name)
        instance.students = validated_data.get(
            'students', instance.students)
        instance.save()

        return instance
>>>>>>> b384975f6822368497afa684c0352ef1ae7dae6e
