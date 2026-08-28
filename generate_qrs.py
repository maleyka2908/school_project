import os
import sys
import django
import qrcode

# Proqramın əsas yolunu təyin edirik
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Django mühitini işə salırıq
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.conf import settings
from students.models import Student

def generate_student_qrs():
    qr_dir = os.path.join(settings.MEDIA_ROOT, 'qrcode_images')
    os.makedirs(qr_dir, exist_ok=True)
    
    students = Student.objects.all()
    count = 0
    
    for student in students:
        qr_data = student.qr_code
        
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        file_name = f"{student.qr_code}.png"
        file_path = os.path.join(qr_dir, file_name)
        
        img.save(file_path)
        count += 1
        print(f"QR kod yaradıldı: {student.last_name} {student.first_name} ({qr_data})")

    print(f"\nÜmumi {count} şagirdin QR kodu uğurla yaradıldı! 🚀")

if __name__ == '__main__':
    generate_student_qrs()