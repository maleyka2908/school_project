import os
import django
import pandas as pd
import glob

# Django mühitini aktivləşdiririk
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from students.models import Student

# Excel faylını tapırıq
excel_files = glob.glob('*.xlsx') + glob.glob('**/*.xlsx', recursive=True)

if not excel_files:
    print("XƏTA: Heç bir Excel faylı tapılmadı!")
    exit()

excel_file = excel_files[0]
print(f"Oxunan fayl: {excel_file}")

# BAZANI TƏMİZLƏYİRİK
print("Köhnə siyahı təmizlənir...")
Student.objects.all().delete()

# Excel faylını oxuyuruq
df = pd.read_excel(excel_file, sheet_name=0, header=None)

count = 0
for index, row in df.iterrows():
    if index < 3:  # Başlıq sətirlərini ötürürük
        continue
        
    try:
        no_val = row[0]
        last_name = str(row[2]).strip() if pd.notna(row[2]) else ""     # Soyadı
        first_name = str(row[3]).strip() if pd.notna(row[3]) else ""    # Adı
        father_name = str(row[4]).strip() if pd.notna(row[4]) else ""    # Ata adı
        student_class = str(row[5]).strip() if pd.notna(row[5]) else ""# Sinfi
        
        # Əgər ad və ya soyad boşdursa, ötür
        if not last_name or not first_name or last_name.lower() == 'nan' or first_name.lower() == 'nan':
            continue
            
        row_no = int(no_val) if pd.notna(no_val) and str(no_val).isdigit() else count + 1
        qr_code_val = f"STU-{row_no:04d}"
        
        # Bazaya yazırıq (ata adı daxil olmaqla!)
        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            father_name=father_name,
            student_class=student_class,
            student_number=str(row_no),
            qr_code=qr_code_val,
            is_in_school=True
        )
        count += 1
        print(f"Əlavə olundu: {last_name} {first_name} {father_name} ({student_class})")
    except Exception as e:
        print(f"Sətir xətası ({index}): {e}")
        continue

print(f"Ümumi {count} şagird ata adları ilə birlikdə uğurla yükləndi! 🚀")