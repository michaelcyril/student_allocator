from mtaa import tanzania
from .models import *


# @api_view(['GET'])
# @permission_classes([AllowAny])
def MkoaWilayaKata(request):
    print(tanzania)
    mikoa = [entry for entry in tanzania]
    for i in range(0, len(mikoa) - 1):
        tosave = Mkoa.objects.create(name=mikoa[i])
        tosave.save()
    print("mikoa saved")
    mikoa_again = Mkoa.objects.values('id', 'name').all()
    mikoa_list = [entry for entry in mikoa_again]
    data = []
    for ml in mikoa_list:
        dist = tanzania.get(ml['name']).districts
        mk = Mkoa.objects.get(id=ml['id'])
        districtss = [entry for entry in dist]
        dataD = []
        for z in range(0, len(districtss)):
            d = districtss[z]
            w_tosave = Wilaya.objects.create(mkoa_id=mk, name=d)
            w_tosave.save()
            x = Wilaya.objects.values('id', 'name', 'mkoa_id').get(name=districtss[z])
            dataD.append(x)
        data.append({'id': ml['id'], 'name': ml['name'], 'districts': dataD})
        print("saved district of " + ml['name'])

        district_again = Wilaya.objects.values('id', 'name').filter(mkoa_id=mk)
        district_list = [entry for entry in district_again]

        for dl in district_list:
            wad = tanzania.get(ml['name']).districts.get(dl['name']).wards
            kata = [entry for entry in wad if entry != "ward_post_code"]
            wl = Wilaya.objects.get(id=dl['id'])
            for k in kata:
                to_save = Kata.objects.create(name=k, wilaya_id=wl)
                to_save.save()

    return 0


def GetMikoa(request):
    data = Mkoa.objects.values('id', 'name').all()
    response = {"data": data}
    return data


def GetWilaya(request, mkoa_id):
    mkoa = Mkoa.objects.get(id=mkoa_id)
    data = Wilaya.objects.values('id', 'name').filter(mkoa_id=mkoa)
    response = {"data": data}
    return data


def GetKata(request, wilaya_id):
    wilaya = Wilaya.objects.get(id=wilaya_id)
    data = Kata.objects.values('id', 'name').filter(wilaya_id=wilaya)
    return data


def GetSchools(request, kata_id):
    kata = Kata.objects.get(id=kata_id)
    data = School.objects.values('id', 'name', 'type', 'sex').filter(kata_id=kata)
    return data


def GetStudents(request, school_id):
    school = School.objects.get(id=school_id)
    data = StudentSchool.objects.values('id', 'student_id').filter(school_id=school)
    d = [x for x in data]
    students = []
    for g in d:
        stu = Student.objects.values('id', 'candidate_name', 'candidate_number', 'sex').get(id=g['student_id'])
        students.append(stu)
    return students


def SingleStudentSchool(request, cand_number):
    stud = Student.objects.get(candidate_number=cand_number)
    data = StudentSchool.objects.values('id', 'school_id').get(student_id=stud)
    return data

