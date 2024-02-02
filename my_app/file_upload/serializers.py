from rest_framework import serializers
from file_upload.models import File
from file_upload.task import file_processing

class FileSerializer(serializers.ModelSerializer):
    def create(self,validated_data):
        try: 
            obj = File.objects.create(**validated_data)
            return obj
        finally:
            # Запуск задачи обработки файла
            file_processing.delay(obj)

    class Meta:
        model = File
        fields = "__all__"


# class FileSerializer(serializers.Serializer):
#     file=serializers.FileField()
#     def create(self,validated_data):
#         try:
#             return File.objects.create(**validated_data)
#         finally:
#             # file_processing.delay(data=context)
#             pass
    
#     class Meta:
#         model = File
#         fields = "__all__"