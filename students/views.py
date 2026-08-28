from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from django.utils import timezone

@csrf_exempt
def scan_qr(request):
    if request.method == 'POST':
        qr_code_text = request.POST.get('qr_code')
        try:
            student = Student.objects.get(qr_code=qr_code_text)
            student.is_in_school = not student.is_in_school
            student.last_seen = timezone.now()
            student.save()
            
            status_text = "İnternatdadır ✅" if student.is_in_school else "Məktəbi tərk etdi ❌"
            return JsonResponse({
                'success': True,
                'message': f"{student.last_name} {student.first_name} - {status_text}",
                'is_in_school': student.is_in_school
            })
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Şagird tapılmadı!'})
            
    # Əgər sadəcə səhifəyə daxil olublarsa (GET sorğusu), skaner səhifəsini göstəririk:
    return render(request, 'students/scan.html')
from django.shortcuts import render

def student_list_view(request):
    # Bütün şagirdləri bazadan çəkirik
    students = Student.objects.all().order_by('last_name')
    context = {
        'students': students
    }
    return render(request, 'students/student_list.html', context)