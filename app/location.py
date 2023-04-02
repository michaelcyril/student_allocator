from mtaa import tanzania
from .models import *
import random
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


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


# def GetKata(request, wilaya_id):
#     wilaya = Wilaya.objects.get(id=wilaya_id)
#     data = Kata.objects.values('id', 'name').filter(wilaya_id=wilaya)
#     return data


def GetSchools(request, wilaya_id):
    wilaya = Wilaya.objects.get(id=wilaya_id)
    data = School.objects.values('id', 'name', 'type', 'sex').filter(wilaya_id=wilaya)
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
    sch = School.objects.values('name', 'type', 'sex', 'wilaya_id').get(id=data['school_id'])
    wilaya = Wilaya.objects.values('id', 'name', 'mkoa_id').get(id=sch['wilaya_id'])
    w = Wilaya.objects.get(id=sch['wilaya_id'])
    mkoa = Mkoa.objects.values('name').get(id=wilaya['mkoa_id'])
    mydata_ = {'school': sch['name'], 'type': sch['type'], 'sex': sch['sex'],
               'mkoa': mkoa['name'], 'wilaya': wilaya['name']}
    return mydata_


import csv


def get_grade_overall(score):
    if score >= 201 and score <= 250:
        return "A"
    elif score >= 151 and score <= 200:
        return "B"
    elif score >= 101 and score <= 150:
        return "C"
    elif score >= 51 and score <= 100:
        return "D"
    else:
        return "E"


def get_grade_sub(score):
    if score >= 41 and score <= 50:
        return "A"
    elif score >= 31 and score <= 40:
        return "B"
    elif score >= 21 and score <= 30:
        return "C"
    elif score >= 11 and score <= 20:
        return "D"
    else:
        return "E"


@api_view(["GET"])
@permission_classes([AllowAny])
def dumyData(request):
    wards = Kata.objects.values('id', 'name', 'wilaya_id').all()
    w = [x for x in wards]
    print(len(w))
    result = []
    # print(w)
    for i in w:
        kata = Kata.objects.get(id=i['id'])
        reg1 = "{:04}".format(kata.id)
        wilaya = Wilaya.objects.values('id', 'name', 'mkoa_id').get(id=i['wilaya_id'])
        mkoa = Mkoa.objects.get(id=wilaya['mkoa_id'])
        names = [
            "Alice Anderson",
            "Bob Brown",
            "Charlie Clark",
            "David Davis",
            "Emily Evans",
            "Frank Fisher",
            "Grace Green",
            "Henry Hill",
            "Isabella Ives",
            "Jack Johnson",
            "Kate King",
            "Liam Lee",
            "Mia Martin",
            "Noah Nelson",
            "Olivia Ortiz",
            "Penelope Parker",
            "Quinn Quinn",
            "Ryan Rodriguez",
            "Samantha Scott",
            "Thomas Taylor",
            "Uma Underwood",
            "Victoria Vega",
            "William White",
            "Xander Xavier",
            "Yara Yates",
            "Zachary Zimmerman",
            "Anna Adams",
            "Benjamin Baker",
            "Catherine Carter",
            "Daniel Diaz",
            "Elizabeth Ellis",
            "Frederick Fox",
            "Gabrielle Gonzalez",
            "Hector Hernandez",
            "Isabelle Ingram",
            "Jacob James",
            "Kaitlyn Kim",
            "Luke Long",
            "Madison Martinez",
            "Nathan Nguyen",
            "Oliver Owens",
            "Paige Phillips",
            "Quentin Quinlan",
            "Rachel Ramirez",
            "Sophia Sanchez",
            "Tyler Turner",
            "Violet Vasquez",
            "Wyatt West",
            "Ximena Xu",
            "Yasmine Yang",
            "Zoe Zuniga",
            "Aiden Abbott",
            "Bella Black",
            "Chloe Cruz",
            "Davidson Drake",
            "Ella Espinoza",
            "Felix Foster",
            "Georgia Gray",
            "Haley Holmes",
            "Isaac Irwin",
            "Jasmine Jarvis",
            "Kaleb Knight",
            "Lila Lopez",
            "Mason Miller",
            "Natalie Newman",
            "Oscar Olivera",
            "Peyton Patel",
            "Quincy Qualls",
            "Riley Rivera",
            "Sofia Soto",
            "Tanner Thompson",
            "Ursula Upton",
            "Vivian Villanueva",
            "Weston Willis",
            "Xenia Xiong",
            "Yolanda Yu",
            "Zander Zavala",
            "Adeline Allen",
            "Brady Banks",
            "Cora Cole",
            "Dante Delgado",
            "Emma Espino",
            "Faith Fernandez",
            "Grant Goodman",
            "Harper Hoffman",
            "Isaiah Ingram",
            "Julia Jensen",
            "Kian Kim",
            "Leah Lawrence",
            "Makayla Montgomery",
            "Niko Nguyen",
            "Olivia O'Connor",
            "Parker Price",
            "Quinn Quezada",
            "Ruby Romero",
            "Sebastian Singh",
            "Talia Thomas",
            "Uriah Underhill",
            "Violet Vargas",
            "Wesley Wilcox",
            "Xavier Xie",
            "Yara Yoder",
            "Zara Zamora"
        ]

        first_names = [
            "Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Sophia", "James", "Isabella", "Benjamin",
            "Mia", "Mason", "Charlotte", "Elijah", "Amelia", "Ethan", "Harper", "Alexander", "Evelyn", "Henry",
            "Abigail", "Michael", "Emily", "Daniel", "Ella", "Matthew", "Scarlett", "Samuel", "Madison", "Lucas",
            "Luna", "Joseph", "Avery", "Gabriel", "Ellie", "David", "Camila", "Ezra", "Chloe", "John",
            "Elizabeth", "Carter", "Victoria", "Luke", "Grace", "Isaac", "Penelope", "Anthony", "Hazel", "Jackson",
            "Nora", "Dylan", "Aria", "Jacob", "Lily", "Levi", "Aaliyah", "Oliver", "Audrey", "Nathan",
            "Leah", "Caleb", "Bella", "William", "Claire", "Christian", "Riley", "Landon", "Maya", "Jonathan",
            "Elena", "Connor", "Sofia", "Evelyn", "Ariana", "Christopher", "Aurora", "Robert", "Addison", "Nicholas",
            "Ellie", "Andrew", "Stella", "Joshua", "Natalie", "Thomas", "Savannah", "Mateo", "Aubrey", "Ryan",
            "Brielle", "Isaiah", "Sienna", "Adam", "Aurora", "Elias", "Genesis", "Julian", "Alexa", "Brayden",
            "Eva", "Grayson", "Hannah", "Lincoln", "Makayla", "Josiah", "Lillian", "Charles", "Brooklyn", "Cameron",
            "Zoe", "Jaxon", "Lila", "Vincent", "Alyssa", "Austin", "Julia", "Hunter", "Lauren", "Adrian",
            "Gianna", "Owen", "Peyton", "Toby", "Mackenzie", "Maxwell", "Rylee", "Luis", "London", "Juan",
            "Avery", "Diego", "Reagan", "Jesse", "Kinsley", "Carlos", "Mila", "Jesus", "Charlie", "Cole",
            "Adalyn", "Alex", "Brianna", "Jaxson", "Jocelyn", "Leo", "Caroline", "Kai", "Ruby", "Dominic",
            "Aubree", "Xander", "Katherine", "Lukas", "Violet", "Asher", "Bailey", "Tristan", "Adeline", "Israel",
            "Jade", "Max", "Madelyn", "Gavin", "Elliana", "Derek", "Piper", "Jayden", "Emilia", "Brody",
            "Alexandra", "Justin", "Adriana", "Xavier", "Khloe", "Juan", "Samantha", "Kevin", "Aaliyah", "Roman",
            "Alice", "Miles", "Delilah", "Marcus", "Brielle"]

        for i in first_names:
            name = i + " " + random.choice(first_names)
            names.append(name)
        # for gender
        f_p = 50
        m_p = 50

        num_f = int(f_p / 100 * 100)
        num_m = int(m_p / 100 * 100)




        for i in range(10):
            reg2 = "{:04}".format(i)
            reg_no = "P" + str(reg1) + "." + str(reg2)
            marks = 0

            # for gender
            if random.randint(1, 100) <= f_p:
                gender = 'female'
                num_f -= 1
            else:
                gender = 'male'
                num_m -= 1

            if num_f == 0:
                f_p = 0
                m_p = 100

            elif num_m == 0:
                f_p = 100
                m_p = 0
            else:
                f_p = int(num_f / (num_f + num_m) * 100)
                m_p = 100 - f_p

            while True:
                # Assign marks randomly based on the given distribution
                p = random.random()
                if p < 0.1:
                    marks = random.randint(200, 250)
                elif p < 0.9:
                    marks = random.randint(100, 200)
                else:
                    marks = random.randint(10, 100)

                # Check if the marks are within the allowed range
                if 10 <= marks <= 300:
                    break

            # Use a name from the list
            name = names[i % len(names)]
            e_s = marks/5
            # Create a dictionary with name and marks
            d = {
                "candidate_name": name,
                "candidate_number": reg_no,
                "sex": gender,
                "kiswahili": get_grade_sub(e_s),
                "english": get_grade_sub(e_s),
                "maarifa": get_grade_sub(e_s),
                "hisabati": get_grade_sub(e_s),
                "science": get_grade_sub(e_s),
                "average_grade": get_grade_overall(marks),
                "average_marks": marks,
                "mkoa": mkoa.name,
                "wilaya": wilaya['name'],
                "kata": kata.name
            }
            result.append(d)
        print("first ward")
        # Print the list of dictionaries
    # print(len(result))
    print("-----------------------------")
    with open("results.csv", "w", newline="") as csvfile:
        # Create a CSV writer object
        writer = csv.DictWriter(csvfile, fieldnames=["candidate_name", "candidate_number", "sex", "kiswahili",
                                                     "english", "maarifa", "hisabati", "science", "average_grade",
                                                     "average_marks", "mkoa", "wilaya", "kata"])

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for person in result:
            writer.writerow(person)
    # print(result)
    return Response({'sms': 'done'})

def SomeCheckup(request):
    wilaya = Wilaya.objects.values('id', 'name').all()
    w = [e for e in wilaya]
    a = []
    for i in w:
        sh = School.objects.values('id', 'name', 'wilaya_id').all()
        s = [e for e in sh if e['wilaya_id'] == i['id']]
        if len(s) == 0:
            a.append(i['name'])
    print(a)


