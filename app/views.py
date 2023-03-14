from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
data_from_excell = [{
    "candidate_name": "james kulwa majuto",
    "candidate_number": "P1278.0108.2007",
    "sex": "male",
    "kiswahili": "B",
    "english": "B",
    "maarifa": "A",
    "hisabati": "A",
    "science": "A",
    "average_grade": "A",
    "average_marks": "250",
    "mkoa": "Tanga",
    "wilaya": "Handeni",
    "kata": "Biazamulo"
},
    {

    }]


def InsertStudentView(request):
    for data in data_from_excell:
        # This make sure that the id of kata is as we save in kata table
        mkoa = Mkoa.objects.get(name=data['mkoa'])
        w = Wilaya.objects.values('id', 'name').filter(mkoa_id=mkoa)
        wl = [x for x in w if x['name'] == data['wilaya']]
        wilaya = Wilaya.objects.get(id=wl[0]['id'])
        k = Kata.objects.values('id', 'name').filter(wilaya_id=wilaya)
        kt = [x for x in k if x['name'] == data['kata']]
        kata = Kata.objects.get(id=kt[0]['id'])
        ##

        student = Student.objects.create(
            candidate_name=data['candidate_name'],
            candidate_number=data['candidate_number'],
            sex=data['sex'],
            kiswahili=data['kiswahili'],
            english=data['english'],
            maarifa=data['maarifa'],
            hisabati=data['hisabati'],
            science=data['science'],
            average_grade=data['average_grade'],
            average_marks=data['average_marks'],
            kata_id=kata,
            year=request.data['year']
        )
        student.save()
    return 0


# request_ = {"year": "2022"}

data_schools = [{
    'name': 'kibamba sec',
    'mkoa': 'Dar',
    'wilaya': 'ubungo',
    'kata': 'kibamba'
}, {

}]


def InsertSchools(request):
    for data in data_schools:
        # This make sure that the id of kata is as we save in kata table
        mkoa = Mkoa.objects.get(name=data['mkoa'])
        w = Wilaya.objects.values('id', 'name').filter(mkoa_id=mkoa)
        wl = [x for x in w if x['name'] == data['wilaya']]
        wilaya = Wilaya.objects.get(id=wl[0]['id'])
        k = Kata.objects.values('id', 'name').filter(wilaya_id=wilaya)
        kt = [x for x in k if x['name'] == data['kata']]
        kata = Kata.objects.get(id=kt[0]['id'])
        ##

        school = School.objects.create(
            name=data['name'],
            kata_id=kata,
            type=data['type'],
            sex=data['sex']
        )
        school.save()


def Selection(request):
    # This give us required student in special schools
    special_school = School.objects.values('id', 'name', 'sex', 'type').filter(type="special")
    ss = [x for x in special_school]
    ss_list = []
    total_required_special = 0
    for d in ss:
        sps = School.objects.get(id=d['id'])
        ss_q = QuantityRequired.objects.values('quantity').get(Q(school_id=sps) and Q(year=request.data['year']))
        total_required_special = total_required_special + ss_q['quantity']
        data = {
            'id': d['id'],
            'name': d['name'],
            'sex': d['sex'],
            'type': d['type'],
            'quantity_required': ss_q['quantity']
        }
        ss_list.append(data)

    # This give us required student in technical schools
    technical_school = School.objects.values('id', 'name', 'sex', 'type').filter(type="technical")
    ts = [x for x in technical_school]
    ts_list = []
    total_required_technical = 0
    for d in ts:
        tcs = School.objects.get(id=d['id'])
        ts_q = QuantityRequired.objects.values('quantity').get(Q(school_id=tcs) and Q(year=request.data['year']))
        total_required_technical = total_required_technical + ts_q['quantity']
        data = {
            'id': d['id'],
            'name': d['name'],
            'sex': d['sex'],
            'type': d['type'],
            'quantity_required': ts_q['quantity']
        }
        ts_list.append(data)

    # Selecting student to the special schools
    students = Student.objects.values('id', 'sex').filter(Q(year=request.data['year']) and Q(is_active=True)).order_by('-average_marks')[:total_required_special]
    students_ = [x for x in students]
    for d in ss_list:
        if d['sex'] == "mixture":
            pass




# request_ = {
#     'year': '2022'
# }
