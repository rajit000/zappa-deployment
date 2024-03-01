from rest_framework import serializers

class StudentDetail_s(serializers.Serializer):
    StudentUUID = serializers.CharField(required = True)
    class Meta:
        fields = '__all__'

class StudentDetailDelete_s(serializers.Serializer):
    StudentUUID = serializers.CharField(required = True)
    class Meta:
        fields = '__all__'
  
class StudentDetailInsert_s(serializers.Serializer):
    FirstName = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    LastName = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    Class = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    Section = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    City = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    District = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    State = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    Pincode = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    About = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    class Meta:
        fields = '__all__'
  
class StudentDetailsUpdate_s(serializers.Serializer):
    StudentUUID = serializers.CharField(required = True)
    FirstName = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    LastName = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    Class = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    Section = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    City = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    District = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    State = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    Pincode = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    About = serializers.CharField(required = False,allow_blank=True,allow_null=True)
    class Meta: 
        fields = '__all__'