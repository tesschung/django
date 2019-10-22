from django.db import models

# doctor.patient_set.all()
# doctor.patients.all()
# related_name을 설정함으로써 patient_set대신 patients로 접근
class Doctor(models.Model):
    name = models.CharField(max_length=200)
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}번 의사 {self.name}'

class Patient(models.Model):
    name = models.CharField(max_length=200)
    doctors = models.ManyToManyField(Doctor, related_name="patients") # patient.doctors.all()
    # Patient에서만 ManyToManyField가 가능하다

    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}번 환자 {self.name}'


# ManyToManyField를 Patient에 지정함으로써 Reservation이라는 중개모델을 만들지 않아도 된다.
# 하지만 실제로는 Reservation이라는 중개모델을 사용하는게 더욱 직관적이다.
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.patient.id} {self.doctor.id}'
    