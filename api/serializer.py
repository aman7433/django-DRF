# from rest_framework import serializers
# from student.models import student

# class StudentSerializers(serializers.ModelSerializer):
#     class Meta:
#         model=student
#         fileds= '__all__'


from rest_framework import serializers
from student.models import student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__' 