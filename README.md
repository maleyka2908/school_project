# 🏫 İnternat Məktəbi Giriş-Çıxış və Davamiyyət Sistemi

Bu layihə məktəb/internat şagirdlərinin giriş-çıxış davamiyyətini QR kod vasitəsilə izləmək üçün hazırlanmış **Django** veb-tətbiqidir.

### ✨ Əsas Xüsusiyyətlər:
- 📊 Excel faylından şagirdlərin məlumatlarının avtomatik bazaya idxal edilməsi (`import_students.py`).
- 🖨️ Hər bir şagird üçün unikal QR kodların generasiya olunması (`generate_qrs.py`).
- 📷 Kameradan QR kodları oxutmaqla avtomatik giriş-çıxış statusunun dəyişdirilməsi.
- 🔄 Hər 5 saniyədən bir yenilənən canlı davamiyyət siyahısı (`/students/`).

### 🚀 Necə İşlətməli?
1. Repozitoriyanı kompüterinizə yükləyin.
2. Virtual mühit yaradın və kitabxanaları quraşdırın:
   ```bash
   pip install -r requirements.txt
