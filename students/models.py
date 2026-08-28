from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ad")
    last_name = models.CharField(max_length=50, verbose_name="Soyad")
    father_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Ata adı")
    student_class = models.CharField(max_length=20, blank=True, null=True, verbose_name="Sinif")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Doğum tarixi")
    student_number = models.CharField(max_length=20, unique=True, blank=True, null=True, verbose_name="Şagird nömrəsi")
    qr_code = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name="QR Kod")
    
    parent_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Valideynin adı")
    parent_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Valideynin telefonu")
    parent_relation = models.CharField(max_length=50, blank=True, null=True, default="Ana", verbose_name="Qohumluq əlaqəsi")
    
    
    # Yeni əlavə etdiyimiz sahələr:
    is_in_school = models.BooleanField(default=False, verbose_name="İnternatdadırmı?")
    last_seen = models.DateTimeField(blank=True, null=True, verbose_name="Son giriş vaxtı")

    def __str__(self):
        return f"{self.last_name or ''} {self.first_name or ''} ({self.student_class or 'Sinif yoxdur'})"