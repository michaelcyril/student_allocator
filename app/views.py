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

shule = [
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "ARUSHA DAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "ARUSHA GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "ARUSHA SEC",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "ARUSHA TERRAT",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "BARAA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "ELERAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "FELIX MREMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "KALOLENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "KIMASEKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "KINANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "KORONA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "LEMARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "LOSIRWAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "MKONOO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "MOIVARO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "MOSHONO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "MURIET",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "NAURA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "NGARENARO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "NJIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "OLASITI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "OLMOTI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "OLOIRIEN",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "SINON",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "SOMBETINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "SORENYI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "SUYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha cbd",
   "shule": "THEMI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "BANGATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "EINOTI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "ENDEVES",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "ENYOITO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "ILBORU",
   "type": "special",
   "sex": "male"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "ILKIDINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "KIMNYAKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "KIRANYI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "LENGIJAVE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "LOSIKITO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "MATEVES",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "MLANGARINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "MRINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "MUKULAT",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "MUSA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "MWANDET",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "NDURUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "NGIRESI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "OLDADAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "OLDONYOSAMBU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "OLDONYOWASI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "OLEMEDEYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "OLJORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "OLMOTONYI FOREST",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "OLOKII",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "OLTRUMET",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "OSILIGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "SAMBASHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arusha",
   "shule": "SOKONI II",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "AWET",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "BANJIKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "BARAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "BARAY KHUSMAYI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "CHAENDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "DIEGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "DOMEL",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "DR WILBROAD SLAA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "EDITH GRORA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "ENDABASH",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "ENDALLAH",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "FLORIAN",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "GANAKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "GETAMOCK",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "GYEKRUM ARUSHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "GYEKRUM LAMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "KAINAM RHOTIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "KANSAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "KARATU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "KILIMAMOJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "KILIMATEMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "MANGOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "MARANG",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "MLIMANI SUMAWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "OLDEANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "ORBOSHAN",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "QANGDEND",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "QARU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "QURUS",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "SLAHHAMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "UPPER KITETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Karatu",
   "shule": "WELWEL",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Longido",
   "shule": "ENDUIMET",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Longido",
   "shule": "ENGARENAIBOR",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Longido",
   "shule": "KETUMBEINE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Longido",
   "shule": "LEKULE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Longido",
   "shule": "LONGIDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Longido",
   "shule": "MATALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Longido",
   "shule": "NAMANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Longido",
   "shule": "NATRON",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Longido",
   "shule": "TINGATINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "AKERI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "KIKWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "KINGORI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "KISIMIRI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "KITEFU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "LAKITATU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "MAJENGO KATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "MAJI YA CHAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "MAKIBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "MALULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "MARORONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "MARUVANGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "MBUGUNI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "MIRIRINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "MOMELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "MUUNGANO USARIVER",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "NASHOLI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "NGONGONGARE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "NGURUDOTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "NGYEKU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "NKOANEKOLI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "NKOANRUA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "NKOARISAMBU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "NKOASENGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "NSHUPU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "PAMOJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "PATANDI MAALUM",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "POLI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "SAKILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "SHISHTON",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "SINGISI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "SONGORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "UMOJA KINGORI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "URAKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Arumeru",
   "shule": "UWIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Monduli",
   "shule": "ENGUTOTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Monduli",
   "shule": "IRKISALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Monduli",
   "shule": "IRKISONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Monduli",
   "shule": "KIPOK",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Monduli",
   "shule": "LOWASSA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Monduli",
   "shule": "MANYARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Monduli",
   "shule": "MOITA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Monduli",
   "shule": "NANJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Monduli",
   "shule": "OLDONYOLENGAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Monduli",
   "shule": "OLESOKOINE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Monduli",
   "shule": "OLTINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Monduli",
   "shule": "RIFTVALLEY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Ngorongoro",
   "shule": "ARASH",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Ngorongoro",
   "shule": "DIGODIGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Ngorongoro",
   "shule": "EMBARWAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Ngorongoro",
   "shule": "LAKE NATRON",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Ngorongoro",
   "shule": "LOLIONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Ngorongoro",
   "shule": "MALAMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Ngorongoro",
   "shule": "NAINOKANOKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Ngorongoro",
   "shule": "SALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Ngorongoro",
   "shule": "SAMUNGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Arusha",
   "wilaya": "Ngorongoro",
   "shule": "SOITSAMBU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Bagamoyo",
   "shule": "BAGAMOYO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Bagamoyo",
   "shule": "DUNDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Bagamoyo",
   "shule": "FUKAYOSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Bagamoyo",
   "shule": "HASSANAL DAMJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Bagamoyo",
   "shule": "KEREGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Bagamoyo",
   "shule": "KINGANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Bagamoyo",
   "shule": "KIROMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Bagamoyo",
   "shule": "MATIMBWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Bagamoyo",
   "shule": "ZINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "CHALINZE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "CHANGALIKWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "KIBINDU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "KIKARO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "KIMANGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "KIWANGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "LUGOBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "MANDERA GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "MATIPWILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "MBOGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "MDAULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "MIONO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "MORETO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "MSATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "TALAWANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "UBENA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Chalinze",
   "shule": "VIGWAZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha",
   "shule": "DOSSA AZIZ",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha",
   "shule": "KILANGALANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha",
   "shule": "KWALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha",
   "shule": "MAGINDU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha",
   "shule": "MIHANDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha",
   "shule": "RAFSANJANI SOGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha",
   "shule": "RUVU GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha",
   "shule": "RUVU STATION",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha cbd",
   "shule": "BUNDIKANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha cbd",
   "shule": "KIBAHA",
   "type": "special",
   "sex": "male"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha cbd",
   "shule": "KIBAHA GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha cbd",
   "shule": "MBWAWA MISWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha cbd",
   "shule": "MIEMBESABA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha cbd",
   "shule": "MWAMBISI FOREST",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha cbd",
   "shule": "MWANALUGALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha cbd",
   "shule": "NYUMBU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha cbd",
   "shule": "PANGANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha cbd",
   "shule": "SIMBANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha cbd",
   "shule": "TUMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha cbd",
   "shule": "VISIGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibaha cbd",
   "shule": "ZOGOWALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibiti",
   "shule": "DIMANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibiti",
   "shule": "KIBITI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibiti",
   "shule": "KIKALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibiti",
   "shule": "MAHEGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibiti",
   "shule": "MCHUKWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibiti",
   "shule": "MJAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibiti",
   "shule": "MLANZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibiti",
   "shule": "MSAFIRI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibiti",
   "shule": "MTANGA DELTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibiti",
   "shule": "NYAMISATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibiti",
   "shule": "RUARUKE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kibiti",
   "shule": "ZIMBWINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kisarawe",
   "shule": "CHANZIGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kisarawe",
   "shule": "CHOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kisarawe",
   "shule": "GONGONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kisarawe",
   "shule": "GWATA KISARAWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kisarawe",
   "shule": "JANGUO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kisarawe",
   "shule": "KIBUTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kisarawe",
   "shule": "KIMANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kisarawe",
   "shule": "KURUI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kisarawe",
   "shule": "MAKURUNGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kisarawe",
   "shule": "MANEROMANGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kisarawe",
   "shule": "MASAKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kisarawe",
   "shule": "MFURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kisarawe",
   "shule": "MINAKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kisarawe",
   "shule": "MSIMBU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kisarawe",
   "shule": "MZENGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Kisarawe",
   "shule": "VIKUMBURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mafia",
   "shule": "BALENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mafia",
   "shule": "BWENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mafia",
   "shule": "KILINDONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mafia",
   "shule": "KIRONGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mafia",
   "shule": "KITOMONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mafia",
   "shule": "MICHENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "ABDALLA H ULEGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "DUNDANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "KIIMBWANINDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "KIPARANGANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "KISIJU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "KISIJU PWANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "KISIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "KIZOMLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "LUKANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "MAGAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "MAMNDIMKONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "MITEZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "MKAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "MKIU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "MKUGILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "MWANDEGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "MWARUSEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "MWINYI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "NASIBUGANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "PANZUO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "SHUNGUBWENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "TAMBANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "TENGELEA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "VIANZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Mkuranga",
   "shule": "VIKINDU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Rufiji",
   "shule": "IKWIRIRI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Rufiji",
   "shule": "KAZAMOYO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Rufiji",
   "shule": "MBWARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Rufiji",
   "shule": "MKONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Rufiji",
   "shule": "MOHORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Rufiji",
   "shule": "MWASENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Rufiji",
   "shule": "NGORONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Rufiji",
   "shule": "UMWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Pwani",
   "wilaya": "Rufiji",
   "shule": "UTETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "ABUUY JUMAA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "ARI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "AZANIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "B W MKAPA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "BINTI MUSSA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "BUYUNI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "CHANIKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "DAR ES SALAAM",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "FURAHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "GEREZANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "HALISI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "ILALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "JAMHURI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "JANGWANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "JUHUDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala",
   "shule": "KASULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "KEREZANGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala",
   "shule": "KIMANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "KINYAMWEZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "KINYEREZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "KISUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "KISUTU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "KITONGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "KITUNDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "KIVULE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "MAGOZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "MAJANI YA CHAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "MBONDOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "MCHANGANYIKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "MCHIKICHINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "MIGOMBANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "MISITU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "MKERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "MNAZI MMOJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "MSIMBAZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "MSONGOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "MVUTI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "MWANAGATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "NGUVU MPYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "NYEBURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "PUGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "PUGU STATION",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "SANGARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "TAMBAZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "UGOMBOLWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "ULONGONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "VINGUNGUTI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "VIWEGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "ZANAKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "ZAWADI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ilala cbd",
   "shule": "ZINGIZIWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kigamboni",
   "shule": "ABOUD JUMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kigamboni",
   "shule": "KIBADA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kigamboni",
   "shule": "KIBUGUMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kigamboni",
   "shule": "KIDETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kigamboni",
   "shule": "KIMBIJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kigamboni",
   "shule": "KISARAWE II",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kigamboni",
   "shule": "KISOTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kigamboni",
   "shule": "MINAZINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kigamboni",
   "shule": "MIZIMBINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kigamboni",
   "shule": "NGUVA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kigamboni",
   "shule": "PEMBAMNAZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kigamboni",
   "shule": "SOMANGILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kigamboni",
   "shule": "TUNGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kigamboni",
   "shule": "VIJIBWENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "BOKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "BUNJU A",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "HANANASIFU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "KAMBANGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "KAWE UKWAMANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "KIGOGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "KISAUKE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "KONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "MABWE TUMAINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "MAENDELEO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "MAKONGO JUU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "MAKUMBUSHO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "MBEZI JUU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "MBOPO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "MBWENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "MBWENI TETA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "MIKOCHENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "MIVUMONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "MTAKUJA BEACH",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "MZIMUNI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "NJECHELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "OYSTERBAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "SALMA KIKWETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "TURIANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Kinondoni",
   "shule": "TWIGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "BARABARA YA MWINYI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "BUZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "CHAMAZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "CHANGANYIKENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "CHANGOMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "CHARAMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "KEKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "KIBASILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "KIBASILA B",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "KICHANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "KIJICHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "KINGUGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "KURASINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "LUMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "MALELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "MBAGALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "MBANDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "MIBURANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "MIKWAMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "MTONI RELINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "MUUNGANO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "NDALALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "NZASA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "PENDA MOYO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "SAKU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "TANDIKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "TEMEKE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "TOANGOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Temeke",
   "shule": "WAILESI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "FAHARI GOBA B",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "GOBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "GOBA MPAKANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "GOGONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "HONDOGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "KIBAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "KIBWEGERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "KIBWEHERI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "KILUVYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "KIMARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "KINGONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "KINZUDI GOBA C",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "KWEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "LUGURUNI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "MABIBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "MAKOKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "MAKURUMLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "MALAMBAMAWILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "MANZESE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "MASHUJAA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "MATOSA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "MBEZI INN",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "MBURAHATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "MPIJI MAGOHE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "MUGABE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "SARANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "TEMBONI GVT",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "URAFIKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dar es Salaam",
   "wilaya": "Ubungo",
   "shule": "Y R MAKAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "BABAYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "BAHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "CHIBELELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "CHIKOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "CHIKOPELO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "CHIPANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "CHONAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "IBIHWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "IBUGULE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "ILINDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "KIGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "LAMAITI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "MAGAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "MPALANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "MPAMANTWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "MSISI JUU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "MTITAA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "MUNDEMU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "MWITIKIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Bahi",
   "shule": "ZANKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "BUIGIRI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "CHAMWINO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "CHILONWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "DABALO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "DR JOHN SAMWEL MALECELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "FUFU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "HANDALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "HANETI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "HUZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "IDIFU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "IGANDU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "IKOWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "ITISO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "MAILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "MAJELEKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "MAKWAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "MANCHALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "MANZASE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "MEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "MLOWA BARABARANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "MLOWA BWAWANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "MPWAYUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "MSAMALO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "MSANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "MVUMI DCT BLIND UNIT",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "MVUMI MAKULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "MVUMI MISHENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chamwino",
   "shule": "SEGALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "CHANDAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "CHEMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "DALAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "FARKWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "GOIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "GWANDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "ITOLWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "JANGALO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "KELEMA BALAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "KIMAHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "KWAMTORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "LALTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "MAKORONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "MONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "MPENDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "MRIJO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "MSAADA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "MSAKWALO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "PARANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "SANZAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "SONGOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Chemba",
   "shule": "SOYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "BIHAWANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "CHIGONGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "CHIHANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "CHIKOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "CHINANGALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "DODOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "HAZINA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "HOMBOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "IHUMWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "IPALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "ITEGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "KIKOMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "KIKUYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "KISASA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "KIWANJA CHA NDEGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "KIZOTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "LUKUNDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "MAKOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "MAKUTUPORA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "MBABALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "MBALAWALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "MIYUJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "MKONZE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "MLIMWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "MNADANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "MPUNGUZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "MSALATO",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "MTUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "NALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "NGHONGHONA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "NTYUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "NZUGUNI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "SECHELELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "UMONGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "VIWANDANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "WELLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Dodoma",
   "shule": "ZUZU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "ABED A KARUME",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "BERABERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "BEREKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "BUKULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "BUMBUTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "BUSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "CHANGAA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "HONDOMAIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "HURUI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "IMBAFI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "INTELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "ITASWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "KALAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "KIKILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "KIKORE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "KINYASI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "KISESE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "KITEO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "KWADELO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "LOO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "MASANGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "MASAWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "R M LOWASA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "SAKAMI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "THAWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "BICHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "DILAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "GUBALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "KOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "KONDOA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "KWAPAKACHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "MTO BUBU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "SERYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kondoa",
   "shule": "ULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "BANYIBANYI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "CHIWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "HEMBAHEMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "HOGORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "IBWAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "IDUO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "KIBAIGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "KONGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "LAIKALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "MAKAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "MANGHAILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "MANGHWETA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "MLALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "MNYAKONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "MTANANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "MUMI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "NDALIBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "NDURUGUMI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "NGHUMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "NGOMAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "NORINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "PANDAMBILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "SAGARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "SEJELI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "SONGAMBELE KILIMANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Kongwa",
   "shule": "ZOISSA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "BEREGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "CHINYIKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "CHIPOGORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "CHUNYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "GODEGODE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "IHALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "IKUYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "IPERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "KIBAKWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "KIMAGAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "LUHUNDWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "MASSA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "MATOMONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "MAZAE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "MBUGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "MIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "MOUNT IGOVU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "MPWAPWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "MTERA DAM",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "MWANAKIANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "PWAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "RUDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "VINGHAWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Dodoma",
   "wilaya": "Mpwapwa",
   "shule": "WOTTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Bukombe",
   "shule": "BUKOMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Bukombe",
   "shule": "BULEGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Bukombe",
   "shule": "BUSINDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Bukombe",
   "shule": "BUSONGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Bukombe",
   "shule": "BUSONZO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Bukombe",
   "shule": "BUTINZYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Bukombe",
   "shule": "IYOGELO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Bukombe",
   "shule": "KATENTE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Bukombe",
   "shule": "LYAMBAMGONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Bukombe",
   "shule": "MSONGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Bukombe",
   "shule": "MUSASA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Bukombe",
   "shule": "NAMONGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Bukombe",
   "shule": "RUNZEWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Bukombe",
   "shule": "USHIROMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Bukombe",
   "shule": "UYOVU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "BUHINGO CHATO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "BUSERESERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "BUTENGORUMASA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "BUZIRAYOMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "BWANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "BWERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "BWINA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "BWONGERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "CHATO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "ICHWANKIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "ILEMELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "ILYAMCHELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "IPARAMASA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "JIKOMBOE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "KACHWAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "KATENDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "KIGONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "MAGUFULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "MAKURUGUSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "MNEKEZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "NYAMIREMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "NYARUTEMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "RUBONDO CHATO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "SUMAYE BUZIKU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "WEMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Chato",
   "shule": "ZAKIA MEGHJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "BUGALAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "BUGANDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "BUJULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "BUKOLI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "BUKONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "BUSANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "BUSANZU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "BUTOBELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "BUTUNDWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "CHIGUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "ISINGILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "KAGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "KAKUBILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "KAMENA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "KAMHANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "KASEME",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "KATORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "KILIMAHEWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "LUBANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "LUDETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "LUTOZO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "LWAMGASA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "LWEMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "LWEZELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "MHARAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "NKOME",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "NYACHILULUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "NYAKAMWAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "NYAMALIMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "NYAMBOGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "NYAMIGOTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "NYAMWILOLELWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "NYANKONGOCHORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "NYARUGUSU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "NYARUYEYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "SENGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "BULELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "BUNGWANGOKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "GEITA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "IHANAMILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "KALANGALALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "KASAMWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "KIVUKONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "LUKARANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "MWATULOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "NYANKUMBU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "NYANZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Geita",
   "shule": "SHANTAMINE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Mbogwe",
   "shule": "IKOBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Mbogwe",
   "shule": "IKUNGUIGAZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Mbogwe",
   "shule": "ILOLANGULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Mbogwe",
   "shule": "IPONYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Mbogwe",
   "shule": "ISANGIJO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Mbogwe",
   "shule": "KANEGERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Mbogwe",
   "shule": "LUGUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Mbogwe",
   "shule": "LULEMBELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Mbogwe",
   "shule": "MASUMBWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Mbogwe",
   "shule": "MBOGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Mbogwe",
   "shule": "NHOMOLWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Mbogwe",
   "shule": "NYAKASALUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Mbogwe",
   "shule": "NYASATO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Nyanghwale",
   "shule": "BUKWIMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Nyanghwale",
   "shule": "BUSOLWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Nyanghwale",
   "shule": "IZUNYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Nyanghwale",
   "shule": "KAFITA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Nyanghwale",
   "shule": "KAKORA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Nyanghwale",
   "shule": "MSALALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Nyanghwale",
   "shule": "MWINGIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Nyanghwale",
   "shule": "NYANGHWALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Nyanghwale",
   "shule": "NYIJUNDU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Nyanghwale",
   "shule": "NYUGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Geita",
   "wilaya": "Nyanghwale",
   "shule": "SHABAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "DIMITRIOS",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "FURAHIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "IDODI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "IFUNDA GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "IFUNDA TECH",
   "type": "technical",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "ILAMBILOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "ISIMILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "ISMANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "KALENGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "KIDAMALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "KIMAIGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "KIPONZELO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "KIWELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "LIPULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "LUHOTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "LUMULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "LYANDEMBELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "LYASA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "MGAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "MLOWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "MSEKE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "MUHWANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "NYANGORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "NYERERE MIGOLI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "PAWAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "TOSAMAGANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "WASA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa",
   "shule": "WILLIAM LUKUVI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa cbd",
   "shule": "IPOGOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa cbd",
   "shule": "IRINGA GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa cbd",
   "shule": "KIHESA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa cbd",
   "shule": "KLERRUU MAZOEZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa cbd",
   "shule": "KWAKILOSA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa cbd",
   "shule": "LUGALO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa cbd",
   "shule": "MAWELEWELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa cbd",
   "shule": "MIYOMBONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa cbd",
   "shule": "MKWAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa cbd",
   "shule": "MLAMKE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa cbd",
   "shule": "MLANDEGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa cbd",
   "shule": "MTWIVILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa cbd",
   "shule": "NDULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Iringa cbd",
   "shule": "TAGAMENDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "DABAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "IBUMU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "ILULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "IPETA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "IROLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "KIHEKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "KILOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "KITOWO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "LUKOSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "LULANZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "LUNDAMATWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "MADEGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "MAKWEMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "MASISIWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "MAWAMBALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "MAZOMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "MLAFU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "MTITU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "NGANGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "NYALUMBU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "NYANZWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "SELEBU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "UDEKWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "UDZUNGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "UHAMBINGETO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Kilolo",
   "shule": "UKWEGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mafinga",
   "shule": "BUMILAYINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mafinga",
   "shule": "CHANGARAWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mafinga",
   "shule": "IHONGOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mafinga",
   "shule": "ISALAVANU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mafinga",
   "shule": "J J MUNGAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mafinga",
   "shule": "KINYANAMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mafinga",
   "shule": "LUGANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mafinga",
   "shule": "MNYIGUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "IDETERO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "IDUNDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "IFWAGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "IGOMBAVANU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "IGOWOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "IHALIMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "IHANU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "IHOWANZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "ILOGOMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "ILONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "ITANDULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "ITENGULE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "ITONA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "KASANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "KIBAO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "KIBENGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "KIHANSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "KINGEGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "KIYOWELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "LUHUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "MADUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "MAKUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "MALANGALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "MBALAMAZIWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "MDABULO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "MGALO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "MGOLOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "MKALALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "MNINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "MTAMBULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "NYOLOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "NZIVI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Iringa",
   "wilaya": "Mufindi",
   "shule": "SADANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "BIHARAMULO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "BISIBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "BIZIMYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "KAGANGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "KALENGE DAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "KATAHOKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "LUSHAUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "MUBABA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "NEMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "NYABUSOZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "NYAKAHURA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "NYAMAHANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "NYAMIGOGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "NYANTAKARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "RUBONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "RUNAZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "RUZIBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Biharamulo",
   "shule": "RWAGATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "BUJUGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "BUJUNANGOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "BUKARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "BUSILIKYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "BUTULAGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "IZIMBYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "KAAGYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "KABALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "KABUGARO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "KAIBANJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "KALEMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "KARABAGAINE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "KARAMAGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "KASHOZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "KATALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "KATOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "KATORO DAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "KEMONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "KIBIRIZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "KIKOMELO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "KISHOGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "KYAMULAILE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "LYAMAHORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "MARUKU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "MWEMAGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "NYAKATO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "NYAKIBIMBILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "RUBALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "RUHUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba",
   "shule": "TUNAMKUMBUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "BAKOBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "BILELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "BUHEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "BUKOBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "HAMUGEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "IHUNGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "IJUGANYONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "KAGEMU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "KAHORORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "KASHAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "KIBETA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "MUGEZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "NSHAMBYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "NYANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "OMUMWANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "RUGAMBWA",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "RUMULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "RUTUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "RWAMISHENYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Bukoba cbd",
   "shule": "RWAZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "BUGENE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "CHABALISA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "CHAKARURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "IGURWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "IHEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "KAWELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "KAYANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "KIHANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "KIRURUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "KITUNTU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "NDAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "NONO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "NYABIYONZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "NYAKAHANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "NYAKASIMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "RUGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "RUHINDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "RUICHO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Karagwe",
   "shule": "RWAMBAIZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "BUGOMORA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "BUSINDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "CHANYANGABWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "CHITWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "IBANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "ISINGIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "KAMULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "KIMULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "KITWECHENKURA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "KYERWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "MABIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "MUKIRE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "MURONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "NAKAKE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "NKWENDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "NTARE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "NYABISHENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "NYAMILIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "NYAMIYAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "RUKURAIJO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Kyerwa",
   "shule": "SONGAMBELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "BUGANDIKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "BUNAZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "BUYANGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "BWABUKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "BWANJAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "GABULANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "GERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "KAGERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "KAKUNYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "KASHENYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "KIGARAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "KIKUKWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "KILIMILILE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "KYAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "LUGOYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "MABALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "MINZIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "MUTUKULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "NKENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "NSUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "RUZINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Missenyi",
   "shule": "RWEMONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "ANNA TIBAIJUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "BIIRABO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "BUJUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "BULYAKASHAJU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "BUMBIRE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "BUNYAGONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "BUREZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "BURUNGURA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "GWANSELI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "IBUGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "IJUMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "IKONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "ITONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "IZIGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "JOYCE NDALICHAKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "KABIRIZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "KAGOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "KAGONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "KAIGARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "KAMACHUMU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "KANYERANYERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "KARAMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "KASHARUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "KIBANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "KIHUMULO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "KIMWANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "KISHANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "KISHOJU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "MAYONDWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "MUBUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "NGENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "NSHAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "NYAILIGAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "NYAKABANGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "NYAKATANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "RUHANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "RUKINDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "RULONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Muleba",
   "shule": "RUTABO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "BUKIRIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "KABANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "KANAZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "KEZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "KIBIMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "KIBOGORA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "KIRUSHYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "LUKOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "MABAWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "MUGANZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "MUGOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "MURGWANZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "MURUSAGAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "MURUVYAGIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "MUYENZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "NDOMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "NGARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "NGARA HIGH",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "NTOBEYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "NYABISINDU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "NYAKISASA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "NYAMIAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "RUSUMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "RUSUMO B",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kagera",
   "wilaya": "Ngara",
   "shule": "SHUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mlele",
   "shule": "ILELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mlele",
   "shule": "INYONGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mlele",
   "shule": "UTENDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda",
   "shule": "BULAMATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda",
   "shule": "IKOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda",
   "shule": "ILANDAMILUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda",
   "shule": "ILANGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda",
   "shule": "KABUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda",
   "shule": "KAREMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda",
   "shule": "MAZWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda",
   "shule": "MISHAMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda",
   "shule": "MPANDANDOGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda",
   "shule": "MWESE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda",
   "shule": "SIBWESA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda cbd",
   "shule": "KASHAULILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda cbd",
   "shule": "KASIMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda cbd",
   "shule": "KASOKOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda cbd",
   "shule": "MAGAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda cbd",
   "shule": "MISUNKUMILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda cbd",
   "shule": "MPANDA GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda cbd",
   "shule": "MWANGAZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda cbd",
   "shule": "NSEMULWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda cbd",
   "shule": "RUNGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpanda cbd",
   "shule": "SHANWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpimbwe",
   "shule": "MAJIMOTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpimbwe",
   "shule": "MAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpimbwe",
   "shule": "MBEDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpimbwe",
   "shule": "MIZENGO PINDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Mpimbwe",
   "shule": "USEVYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Nsimbo",
   "shule": "KANOGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Nsimbo",
   "shule": "KATUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Nsimbo",
   "shule": "KENSWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Nsimbo",
   "shule": "MACHIMBONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Nsimbo",
   "shule": "MTAPENDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Nsimbo",
   "shule": "NSIMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Katavi",
   "wilaya": "Nsimbo",
   "shule": "SITALIKE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "BUHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "BUYENZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "BWAFUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "JANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "KAHUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "KIBWIGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "MANYOVU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "MKATANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "MKOZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "MUHARULO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "MUHINDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "MUNANILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "MUNZEZE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "MUYAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "NYAKIMUE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "NYAMILAMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "NYARUBOZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "RUSABA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Buhigwe",
   "shule": "YANZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kakonko",
   "shule": "BUYUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kakonko",
   "shule": "GWANUMPU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kakonko",
   "shule": "KAKONKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kakonko",
   "shule": "KANYONZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kakonko",
   "shule": "KASANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kakonko",
   "shule": "KASHOZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kakonko",
   "shule": "MUGUNZU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kakonko",
   "shule": "MUHANGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kakonko",
   "shule": "NYAMTUKUZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kakonko",
   "shule": "RUGENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kakonko",
   "shule": "SHUHUDIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "ASANTE NYERERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "KABAGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "KASANGEZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "KIHENYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "KIMENYI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "KIMWANYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "KINYAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "KITANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "KURUNYEMI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "MAKERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "MOYOVOZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "NKUNDUTSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "NTAMYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "NYAKITONTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "RUNGWE MPYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "RUSESA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "TITYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "ZEZE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "BOGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "HWAZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "KASANGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "KIGODYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "KIGOMA GRAND",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "KINKATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "MUBONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "MUHUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "MUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "MURUBONA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "MURUFITI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "MWIBUYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "NYANSHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kasulu",
   "shule": "NYUMBIGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "BITURANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "BUSAGARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "BUSAMI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "ITABA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "KIBONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "KUMGOGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "KUMWAMBU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "MALAGARASI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "MIGEZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "MISEZERO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "MKUGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "MOUNT SAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "MOYOWOSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "MUGOMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "MURAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "MURUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kibondo",
   "shule": "RUBANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "AMAHORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "BITALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "BUGAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "KAGONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "KALINZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "KASEKE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "KIDAHWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "LUICHE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "MATYAZO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "MGAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "MKABOGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "MKIGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "MKONGORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "MKUTI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "MUNGONYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "MWANDIGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "NYAMUHOZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "NYARUBANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma",
   "shule": "ZASHE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "BUHANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "BURONGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "BUSHABANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "BUTEKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "GUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "KASIMBU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "KASINGIRIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "KATUBUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "KICHANGACHUI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "KIGOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "KIRUGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "KITONGONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "KITWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "MASANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "MLOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "MWANANCHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "RUBUGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "RUSIMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Kigoma cbd",
   "shule": "WAKULIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "BASANZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "BUHINGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "HEREMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "ILAGALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "ITEBULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "KALENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "KALYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "KANDAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "LAGOSA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "LUGUFU BOYS",
   "type": "special",
   "sex": "male"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "LUGUFU GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "MAZUNGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "MGANZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "MWAKIZEGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "NGURUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "NYAMAGOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "RUCHUGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kigoma",
   "wilaya": "Uvinza",
   "shule": "SUNUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "BOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "HAI DAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "HARAMBEE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "KIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "KIKAFU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "KISELU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "KYUU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "LEMIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "LERAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "LONGOI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "LUKANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "LYAMUNGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "LYASIKIKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "MACHAME GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "MAILISITA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "MARIRE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "MUKWASA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "NEEMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "NGUNI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "NKOKASHU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "NKUU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "NKWAMWASI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "ROO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "RUNDUGAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "SAWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "TUMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "TUMONA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "UDORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Hai",
   "shule": "UDURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "ASHIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "CYRIL CHAMI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "DARAJANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "GHONA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "HIMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "IFATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "IWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "KILIMANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "KIMOCHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "KINDI KATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "KIRIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "KISAM",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "KISARIKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "KISULUNI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "KOKIRIE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "KOMAKYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "LANGASANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "LYAKIRIMU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MABOGINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MAKOMU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MAMBA DAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MANGI MAREALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MANGI SABASI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MANGI SINA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MANGOTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MANUSHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MARINGENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MARLEX",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MASHINGIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MASOKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MATALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MAWELLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MBOKOMU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MBONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MELI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MIERESINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MKOMBOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MLANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MNINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MPIRANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MRERENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MRUWIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MSIRIWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MUUNGANO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "MWIKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "OKAONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "ORIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "PAKULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "RASESA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "RUKIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "SAKAYO MOSHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "SHIMBWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "SOMSOM",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "SUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "TEMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "TPC",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "UMBWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "UPARO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi",
   "shule": "WERUWERU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi cbd",
   "shule": "ANNA MKAPA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi cbd",
   "shule": "J K NYERERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi cbd",
   "shule": "KARANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi cbd",
   "shule": "KIBORLONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi cbd",
   "shule": "KIUSA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi cbd",
   "shule": "KORONGONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi cbd",
   "shule": "MAWENZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi cbd",
   "shule": "MJI MPYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi cbd",
   "shule": "MOSHI",
   "type": "special",
   "sex": "male"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi cbd",
   "shule": "MOSHI UFUNDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi cbd",
   "shule": "MSARANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi cbd",
   "shule": "MSASANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi cbd",
   "shule": "RAU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Moshi cbd",
   "shule": "REGNALD MENGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "CHAANGAJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "DR ASHAROSE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "JIPE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "KAMWALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "KIFARU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "KIGHARE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "KIGONIGONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "KILEO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "KILOBENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "KIRYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "KISANGARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "KISHENGWENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "KWANGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "LANGATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "MAGHARE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "MANDAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "MGAGAO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "MSANGENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "NDORWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "NGUJINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "NYERERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "SIMBOMU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "UBANGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "USANGI DAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Mwanga",
   "shule": "VUDOI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "ALENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "BOONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "BUSTANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "HOLILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "HOROMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "KAHEUSSERI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "KELAMFUA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "KENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "KILAMACHO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "KIRACHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "KIRONGOCHINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "KISALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "KWAIKURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "KWALAKAMU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "MAHIDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "MAKALEMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "MAKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "MAKIIDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "MAMSERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "MASHATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "MATOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "MAWANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "MBOMAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "MEMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "MENGENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "MKUU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "MLAMBAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "MOTAMBURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "MRAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "MRAOKERYO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "NANJARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "NDUWENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "NGALEKU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "NGARENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "OLELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "SHIMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "TANYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "TARAKEA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "UBAA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "UMARINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Rombo",
   "shule": "URAURI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "BANGALALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "BEMKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "BOMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "CHALAO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "CHANJAGAA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "CHAUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "GONJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "KASEMPOMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "KAZITA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "KIBACHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "KIGANGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "KIHURIO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "KIMALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "KIRANGARE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "KISIWANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "KWAKOKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "KWAMBEGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "KWIZU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "LUGULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "MABILIONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "MADIVENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "MAKANYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "MALINDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "MANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "MASHEKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "MKOMBOZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "MOIPO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "MTII",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "MVUREKONGEI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "MYAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "NDUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "NJORO MIGHARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "NTENGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "PARENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "SAME",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "SAWENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "TAE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "VUDEE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "VUMARI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Same",
   "shule": "VUNTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Siha",
   "shule": "DAHANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Siha",
   "shule": "ESINYARI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Siha",
   "shule": "FUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Siha",
   "shule": "KARANSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Siha",
   "shule": "KILINGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Siha",
   "shule": "KISHISHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Siha",
   "shule": "MAGADINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Siha",
   "shule": "MATADI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Siha",
   "shule": "NAMWAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Siha",
   "shule": "NURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Siha",
   "shule": "OSHARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Siha",
   "shule": "SANYA JUU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Siha",
   "shule": "SIKIRARI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Kilimanjaro",
   "wilaya": "Siha",
   "shule": "SUUMU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "ALI MCHUMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "DODOMEZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "ILULU GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "KANDAWALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "KIBATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "KIKANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "KIKOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "KILWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "KINJUMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "KIPATIMU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "KIRANJERANJE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "KIVINJE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "LIKAWAGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "MATANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "MIBUYUNI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "MIGURUWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "MINGUMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "MITEJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "MITOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "MPUNYULE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "MTANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "NAKIU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "NAMAYUNI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "NJINJO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "PANDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Kilwa",
   "shule": "SONGOSONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "CHIUTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "KITOMANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "KIWALALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "LITIPU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "MADANGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "MAHIWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "MANDWANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "MBAWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "MCHINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "MILOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "MIPINGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "MKOPWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "MNARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "MNOLELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "MTAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "MTUA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "MVULENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "NAHUKAHUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "NAMANGALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "NAMUPA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "NANGARU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "NYENGEDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi",
   "shule": "RUTAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi cbd",
   "shule": "ANGAZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi cbd",
   "shule": "CHIKONJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi cbd",
   "shule": "KINENGENE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi cbd",
   "shule": "LINDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi cbd",
   "shule": "MINGOYO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi cbd",
   "shule": "MITWERO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi cbd",
   "shule": "MKONGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi cbd",
   "shule": "NGAPA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Lindi cbd",
   "shule": "NGONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Liwale",
   "shule": "ANNA MAGOWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Liwale",
   "shule": "BARIKIWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Liwale",
   "shule": "HANGAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Liwale",
   "shule": "KIANGARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Liwale",
   "shule": "KIBUTUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Liwale",
   "shule": "KIKULYUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Liwale",
   "shule": "LIKONGOWELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Liwale",
   "shule": "LIWALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Liwale",
   "shule": "MAKATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Liwale",
   "shule": "MIHUMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Liwale",
   "shule": "MILINA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Liwale",
   "shule": "MIRUI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Liwale",
   "shule": "MLEMBWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Liwale",
   "shule": "NANGANO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Liwale",
   "shule": "NICODEMUS BANDUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Liwale",
   "shule": "RASHIDI MFAUME KAWAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "CHIOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "FARM 17",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "KIEGEI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "KILIMARONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "KIPARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "KIPAUMBELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "LIONJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "MARAMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "MATEKWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "MBONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "MISUFINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "MKOKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "MKOTOKUYANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "MNERO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "NACHINGWEA DAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "NACHINGWEA GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "NAIPANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "NAIPINGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "NAMAPWIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "NAMATULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "NAMBAMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "NAMIKANGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "NDANGALIMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "NDITI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "NDOMONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "RUPONDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Nachingwea",
   "shule": "STESHENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Ruangwa",
   "shule": "CHIENJERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Ruangwa",
   "shule": "CHINONGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Ruangwa",
   "shule": "CHUNYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Ruangwa",
   "shule": "HAWA MCHOPA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Ruangwa",
   "shule": "KASSIM MAJALIWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Ruangwa",
   "shule": "LIKUNJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Ruangwa",
   "shule": "LIUGURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Ruangwa",
   "shule": "MAKANJIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Ruangwa",
   "shule": "MANDAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Ruangwa",
   "shule": "MBEKENYERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Ruangwa",
   "shule": "MNACHO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Ruangwa",
   "shule": "NAMBILANJE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Ruangwa",
   "shule": "NAMICHIGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Ruangwa",
   "shule": "NARUNGOMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Ruangwa",
   "shule": "NKOWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Lindi",
   "wilaya": "Ruangwa",
   "shule": "RUANGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "ARRI TSAAYO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "AYALAGAYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "AYATSEA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "BASHNET",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "CHIEF DODO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "DABIL",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "DAREDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "DOHOM",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "DURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "ENDAKISO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "ENDAMANANG",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "GALLAPO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "GICHAMEDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "GIDAS",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "GOROWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "GUSE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "HAITEMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "KIRU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "MAGANJWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "MAGARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "MAGUGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "MAMIRE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "MASABEDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "MATUFA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "MBUGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "NAR",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "NDEKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "NKAITI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "QAMEYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "QASH",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "UFANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "UMAGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati",
   "shule": "UTWARI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati cbd",
   "shule": "BABATI DAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati cbd",
   "shule": "BAGARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati cbd",
   "shule": "BONGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati cbd",
   "shule": "F T SUMAYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati cbd",
   "shule": "HANGONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati cbd",
   "shule": "KOMOTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati cbd",
   "shule": "KWAANGW",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati cbd",
   "shule": "KWARAA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati cbd",
   "shule": "MUTUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati cbd",
   "shule": "NAKWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati cbd",
   "shule": "NANGARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Babati cbd",
   "shule": "SIGINO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "BALANGDALALU",
   "type": "special",
   "sex": "male"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "BASSODESH",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "BASSOTU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "CHIEF GEJARU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "CHIEF GIDOBAT",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "DANIEL NOUD",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "DIRMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "DUMBETA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "ENDAGAW",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "ENDASAK",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "GABADAW",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "GANANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "GETANUWAS",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "GIDAHABABIEG",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "GISAMBALANG",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "GITTING",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "HANANG",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "HIRBADAW",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "JOROJICK",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "KATESH",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "LAGHANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "MARY NAGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "MASAKTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "MASQARODA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "MEASKRON",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "MULBADAW",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "MWAHU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "NANGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "SIMBAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "SIROP",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "SUMAYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "UDANGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Hanang",
   "shule": "WARETA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "BWAKALO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "DONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "DOSIDOSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "ECO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "ENGUSERO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "KIBAYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "KIJUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "KIPERESA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "KITETO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "LESOIT",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "MAGUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "MATUI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "NDEDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "NJORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "ORKINE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "PARTIMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Kiteto",
   "shule": "SUNYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "ALEXANDER SAULO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "B N HHANDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "BASHAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "DINAMU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "DR OLSEN",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "ENDOJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "GIDHIM",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "HAYDERER",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "HAYDOM",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "JAKAYA KIKWETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "LABAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "MAGHANG",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "MAMAKARI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "MARETADU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "MARETADU JUU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "PHILIP MARMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "TUMATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "YAEDA AMPA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "YAEDA CHINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "BARGISH",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "CHIEF SARWATT",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "DAUDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "DAUDI TEEWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "GEHANDU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "GUNYODA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "HHAYNU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "KAINAM",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "MURRAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "NAMBIS",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "NOWU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "SILALODA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "SINGLAND",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "SOHEDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Mbulu",
   "shule": "TLAWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Simanjiro",
   "shule": "EMBOREET",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Simanjiro",
   "shule": "ENGENO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Simanjiro",
   "shule": "EWONGON",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Simanjiro",
   "shule": "LOIBORSIRET",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Simanjiro",
   "shule": "LOIBORSOIT",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Simanjiro",
   "shule": "MERERANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Simanjiro",
   "shule": "MSITU WA TEMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Simanjiro",
   "shule": "NABERERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Simanjiro",
   "shule": "NAISINYAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Simanjiro",
   "shule": "NYUMBA YA MUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Simanjiro",
   "shule": "OLJORO NA 5",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Simanjiro",
   "shule": "RUVU REMMIT",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Simanjiro",
   "shule": "SHAMBARAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Simanjiro",
   "shule": "SIMANJIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Simanjiro",
   "shule": "TANZANITE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Manyara",
   "wilaya": "Simanjiro",
   "shule": "TERRAT",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "BULAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "CHAMRIHO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "CHISORYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "CHITENGULE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "ESPERANTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "HUNYARI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "KWIRAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "MAKONGORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "MEKOMARIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "MIHINGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "MURANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "MWIBARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "MWIGUNDU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "NANSIMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "NYAMANGUTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "NYERUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "SALAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "BUNDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "DR NCHIMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "GUTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "KABASA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "KUNZUGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "NYIENDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "RUBANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "SAZIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "SIZAKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Bunda",
   "shule": "WARIKU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "BARANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "BUHEMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "BUKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "BUMANGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "BUMASWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "BURUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "BUTIAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "BUTUGURI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "CHIEF IHUNYO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "KEMORAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "KIABAKARI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "KIAGATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "KUKIRANGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "KYANYARI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "MASABA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "MIRWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "MKONO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "MMAZAMI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Butiama",
   "shule": "WEGERO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "BUGWEMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "BUKIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "BULINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "ETARO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "KASOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "KIRIBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "MABUI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "MAKOJO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "MKIRIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "MTIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "MUGANGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "MURANGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "NYAKATENDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "NYAMBONO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "NYANJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "RUSOLI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "SUGUTI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma",
   "shule": "TEGERUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "BARUTI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "BUHARE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "BWERI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "IRINGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "KAMUNYONGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "KIARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "MAKOKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "MARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "MOREMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "MSHIKAMANO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "MUKENDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "MUSOMA UFUNDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "MWISENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "NYABISARE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "NYAMIONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "NYAMITWEBIRI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "NYASHO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Musoma cbd",
   "shule": "SONGE",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "BUKAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "BUKURA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "BUKWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "BUTURI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "CHARYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "GORIBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "KATURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "KINYENCHE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "KIROGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "KISUMWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "KUKONA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "KWIBUSE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "KYANGOMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "MIRARE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "MUSA AKASHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "NGASARO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "NYABIWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "NYAMAGARO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "NYAMASANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "NYAMTINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "NYAMUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "NYANDUGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "NYATHOROGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "NYIHARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "PASTOR RAPHAEL ODUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "PROF PHILEMON SARUNGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "RARANYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "ROCHE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "SUBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "TAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Rorya",
   "shule": "WANINGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "BUSAWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "DR OMAR ALI JUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "IKOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "IKORONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "KAMBARAGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "KEMARONGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "KISAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "KISANGURA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "KITUNGURUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "MACHOCHWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "MAJIMOTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "MAKUNDUSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "MAMA MARIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "MANCHIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "MOSONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "MUGUMU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "NAGUSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "NATTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "NGOREME",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "NYAMBURETI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "NYAMBURI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "NYAMOKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "NYANSURURA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "NYICHOKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "RIGICHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "RINGWANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "ROBANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "SEDECO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "SERENGETI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Serengeti",
   "shule": "SOMOCHE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "BOREGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "BUNGURERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "BWIREGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "GENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "GIBASO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "GORONGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "INCHAGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "INCHUGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "INGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "ITIRYO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "J K NYERERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "KEBOGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "KEMAKORERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "KEMAMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "KIBASUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "KITAWASI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "KOROTAMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "KURUMWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "MAGOTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "MANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "MBOGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "MWEMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "NYAIBARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "NYAMONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "NYAMWAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "NYAMWIGURA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "NYANTIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "NYANUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "NYARERO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "SIRARI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "BOMANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "KENYAMANYORI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "MOGABIRI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "NKENDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "NKONGORE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "NYAMISANGURA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "NYANDOTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "REBU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mara",
   "wilaya": "Tarime",
   "shule": "TARIME",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Busokelo",
   "shule": "BUSOKELO GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Busokelo",
   "shule": "IKAPU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Busokelo",
   "shule": "ISANGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Busokelo",
   "shule": "KABULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Busokelo",
   "shule": "KISEGESE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Busokelo",
   "shule": "KYEJO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Busokelo",
   "shule": "LUFILYO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Busokelo",
   "shule": "LUTEBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Busokelo",
   "shule": "LWANGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Busokelo",
   "shule": "MBIGILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Busokelo",
   "shule": "MPATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Busokelo",
   "shule": "MWAKALELI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Busokelo",
   "shule": "MWATISI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Busokelo",
   "shule": "MZALENDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Busokelo",
   "shule": "NTABA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Busokelo",
   "shule": "SELYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Chunya",
   "shule": "CHALANGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Chunya",
   "shule": "CHOKAA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Chunya",
   "shule": "IFUMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Chunya",
   "shule": "ISANGAWANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Chunya",
   "shule": "ISENYELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Chunya",
   "shule": "ITEWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Chunya",
   "shule": "KIWANJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Chunya",
   "shule": "LUPA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Chunya",
   "shule": "MAKALLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Chunya",
   "shule": "MAKONGOLOSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Chunya",
   "shule": "MTANDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Chunya",
   "shule": "MTANILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "BUJONDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "IKAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "IKIMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "IKOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "IPANDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "IPINDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "ITOPE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "ITUNGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "KAFUNDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "KAJUNJUMELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "KATUMBASONGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "KIWIRA COAL MINE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "KYELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "LUSUNGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "MAKWALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "MASUKILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "MATEMA BEACH",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "MWAYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "NDOBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "NGONGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "NKUYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Kyela",
   "shule": "NYASA LAKE SHORE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "GWILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "IGAVA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "IGOMELO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "IMALILO SONGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "IPWANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "JAKAYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "MADIBIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "MALENGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "MAWINDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "MBARALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "MENGELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "MIYOMBWENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "MSHIKAMANO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "MWAKAGANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "RUIWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "RUJEWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "UHAHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbarali",
   "shule": "UTENGULE USANGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "FOREST",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "HAYOMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "IDUDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "IGANZO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "IHANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "ILOMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "ISYESYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "ITEZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "ITIJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "IWAMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "IYELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "IYUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "KALOBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "LEGICO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "LOLEZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "LUPETA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "LYOTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "MAZIWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "MBEYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "MPONJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "MWAKIBETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "MWASANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "NSENGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "NSOHO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "NZONDAHAKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "PANKUMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "SAMORA MACHEL",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "SINDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "STELLA FARM",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "UYOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya cbd",
   "shule": "WIGAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "GALIJEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "HORONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "IHANGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "IKHOHO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "IKUKWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "ILEMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "ILUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "ILUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "IMEZU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "ISUTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "ITALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "IWALANJE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "IWIJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "IWINDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "IYELANYALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "IZYIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "MALAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "MPESU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "MSHEWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "MWAKIPESILE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "MWASELELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "NSONGWI JUU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "SANTILYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "SASYAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "SHIBOLYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "SHISYETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "SONGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "SWAYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "TEULE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "USONGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Mbeya",
   "shule": "YALAWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "BUJELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "BUJINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "BULYAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "IKUTI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "ILIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "IPONJOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "ISONGOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "KALENGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "KAPUGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "KAYUKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "KIGUGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "KIMAMMPE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "KINYALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "KISIBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "KISONDELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "KIWIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "KYIMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "LUFINGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "LUPOTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "MASOKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "MASUKULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "MPANDAPANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "MPUGUSO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "NDANTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "NKUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "RUNGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "SUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "TUKUYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "UKUKWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mbeya",
   "wilaya": "Rungwe",
   "shule": "ZIWANGOSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Gairo",
   "shule": "A M SHABIBY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Gairo",
   "shule": "CHAGONGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Gairo",
   "shule": "CHAKWALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Gairo",
   "shule": "CHANJALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Gairo",
   "shule": "GAIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Gairo",
   "shule": "IYOGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Gairo",
   "shule": "KIBEDYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Gairo",
   "shule": "MAJEMBWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Gairo",
   "shule": "NJUNGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Gairo",
   "shule": "NONGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Gairo",
   "shule": "RUBEHO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Gairo",
   "shule": "SEKWAO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ifakara",
   "shule": "IFAKARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ifakara",
   "shule": "KIBAONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ifakara",
   "shule": "KILOMBERO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ifakara",
   "shule": "KIYONGWILE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ifakara",
   "shule": "KWASHUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ifakara",
   "shule": "LUMEMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ifakara",
   "shule": "MLABANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "BOKELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "CANE GROWERS",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "CHISANO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "CHITA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "KAMWENE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "KIBEREGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "KIBURUBUTU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "KIDATU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "KISAWASAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "MANGULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "MASAGATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "MATUNDU HILL",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "MBINGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "MCHOMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "MLIMBA DAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "MOFU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "MUTENGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "MWANIHANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "NAKAGURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "NYANDEO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "NYANGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "SANJE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "SIGNAL",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "TREE FARMS",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilombero",
   "shule": "UCHINDILE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "CHANZURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "DAKAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "DENDEGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "DUMILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "GONGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "IWEMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "KIDETE DAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "KIDODI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "KILANGALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "KILOSA",
   "type": "special",
   "sex": "male"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "KIMAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "KISANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "KITETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "KUTUKUTU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "LUMBIJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "LUMUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "LYAHIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "MABULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "MABWEREBWERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "MAGOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "MAGUBIKE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "MAMBOYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "MASANZE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "MATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "MAZINYUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "MBUMI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "MGUGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "MIKUMI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "MKULO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "MSOWERO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "MTUMBATU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "MWEGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "PARAKUYO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "RUDEWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "RUHEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "UKWIVA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "ULELINGOMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "VIDUNDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Kilosa",
   "shule": "ZOMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Malinyi",
   "shule": "BIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Malinyi",
   "shule": "IGAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Malinyi",
   "shule": "ITETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Malinyi",
   "shule": "KIPINGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Malinyi",
   "shule": "MALINYI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Malinyi",
   "shule": "MTIMBIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Malinyi",
   "shule": "NGOHERANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Malinyi",
   "shule": "SOFI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Malinyi",
   "shule": "USANGULE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "BWAKIRA CHINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "BWAKIRA JUU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "FATEMI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "GWATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "KIBOGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "KIBUNGO JUU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "KINOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "KIROKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "KISAKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "KISEMU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "KIZAGILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "KOLERO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "LUNDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "MATOMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "MIKESE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "MILENGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "MKULAZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "MKUYUNI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "MTOMBOZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "MVUHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "NELSON MANDELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "NGERENGERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "SELEMBALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "SINGISA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "TAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "TEGETERO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "TOMONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro",
   "shule": "TUNUNGUO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "BONDWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "BUNGODIMWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "KAUZENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "KAYENZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "KIHONDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "KILAKALA",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "KINGALU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "KINGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "KINGOLWIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "KOLA HILL",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "LUPANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "MAFIGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "MGULASI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "MJI MPYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "MOROGORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "MWEMBESONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "NANENANE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "SUA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "SUMAYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "TUBUYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "TUSHIKAMANE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "ULUGURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Morogoro cbd",
   "shule": "UWANJA WA TAIFA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "BUNDUKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "DIONGOYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "DOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "HEMBETI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "KANGA HILL",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "KIKEO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "KIPERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "LANGALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "LUSANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "MASKATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "MELELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "MGETA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "MONGOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "MTIBWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "MURAD SADDIQ",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "MVOMERO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "MZUMBE",
   "type": "special",
   "sex": "male"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "NASSORO SEIF",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "SUNGAJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "TCHENZEMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "UNGULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Mvomero",
   "shule": "WAMI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "CELINA KOMBANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "CHIROMBOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "EUGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "IGOTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "ILONGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "IRAGUA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "ISONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "KICHANGANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "KWIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "LUPIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "MAHENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "MBUGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "MINEPA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "MWAYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "NAWENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "ULANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "UPONERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Morogoro",
   "wilaya": "Ulanga",
   "shule": "VIGOI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "CHIDYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "CHIKOROPOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "CHIUNGUTWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "CHIWALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "CHIWATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "ISDORE SHIRIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "LUKULEDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "LULINDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "LUPASO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "MAKONGONDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "MBEMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "MBUYUNI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "MKALAPA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "MKULULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "MPINDIMBI CHANIKANGUO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "MWENA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "NAMAJANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "NAMALENGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "NAMATUTWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "NAMOMBWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "NAMWANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "NANGANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "NANGOO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "NANJOTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "NDANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "NDWIKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "SINDANO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "ANNA ABDALLAH",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "CHANIKANGUO MPINDIMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "MARIKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "MASASI DAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "MASASI GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "MTANDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "MTAPIKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "NANGAYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Masasi",
   "shule": "SULULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara",
   "shule": "DIHIMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara",
   "shule": "KISIWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara",
   "shule": "KITERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara",
   "shule": "LIBOBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara",
   "shule": "MADIMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara",
   "shule": "MAHURUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara",
   "shule": "MAYANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara",
   "shule": "MSIMBATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara",
   "shule": "MUSTAFA SABODO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara",
   "shule": "NANGURUWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara",
   "shule": "NDUMBWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara",
   "shule": "ZIWANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara cbd",
   "shule": "BANDARI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara cbd",
   "shule": "CHUNO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara cbd",
   "shule": "MANGAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara cbd",
   "shule": "MIKINDANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara cbd",
   "shule": "MITENGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara cbd",
   "shule": "MTWARA GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara cbd",
   "shule": "MTWARA UFUNDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara cbd",
   "shule": "NALIENDELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara cbd",
   "shule": "RAHALEO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara cbd",
   "shule": "SABASABA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara cbd",
   "shule": "SHANGANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara cbd",
   "shule": "SINO TZ",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Mtwara cbd",
   "shule": "UMOJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyamba",
   "shule": "CHAWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyamba",
   "shule": "KIROMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyamba",
   "shule": "KITAYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyamba",
   "shule": "MBEMBALEO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyamba",
   "shule": "MNIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyamba",
   "shule": "MNYAWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyamba",
   "shule": "MTINIKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyamba",
   "shule": "NANYAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyamba",
   "shule": "NITEKELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyamba",
   "shule": "NJENGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyumbu",
   "shule": "CHIPUPUTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyumbu",
   "shule": "LIKOKONA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyumbu",
   "shule": "LUMESULE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyumbu",
   "shule": "MANGAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyumbu",
   "shule": "MARATANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyumbu",
   "shule": "MICHIGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyumbu",
   "shule": "MIKANGAULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyumbu",
   "shule": "NANDETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyumbu",
   "shule": "NANGOMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyumbu",
   "shule": "NANYUMBU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyumbu",
   "shule": "NAPACHO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Nanyumbu",
   "shule": "SENGENYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "CHIHANGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "CHITEKETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "LENGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "MAKUKWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "MALATU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "MAPUTI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "MIKUMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "MKOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "MMULUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "MNYAMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "MPELEPELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "MPOTOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "MTOPWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "USHIRIKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "VIHOKOLI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "DR ALEX MTAVALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "G MKUCHIKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "KIUTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "KUSINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "MAKOTE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "MALEGESI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "MALOCHO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "MTANGALANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "NAMBUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "NANGWANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Newala",
   "shule": "NEWALA DAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "CHAUME",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "CHINGUNGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "DINDUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "KITAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "LIENJE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "LUAGALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "LUKOKODA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "MAHUTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "MAUNDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "MCHICHIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "MDIMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "MICHENJELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "MIHAMBWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "MILONGODI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "MKONJOWANO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "MKOREHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "MKUNDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "MKWITI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "MNYAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "MWEMINAKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "NACHUNYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "NAMIKUPA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "NANDONDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "NANHYANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "NAPUTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "NGUNJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "SALAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mtwara",
   "wilaya": "Tandahimba",
   "shule": "TANDAHIMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "BANGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "BUPANDWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "ILIGAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "IRENZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "ITABULYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "KAFUNZO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "KAKOBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "KALEBEZO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "KATWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "KOME",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "LUGATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "LUSHAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "MAGULUKENDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "MAISOME",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "MIGUKULAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "NYAKALIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "NYAKASUNGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "NYAMADOKE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Buchosa",
   "shule": "NYEHUNGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "BUGOGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "BUJINGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "BUSWELU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "BWIRU BOYS",
   "type": "special",
   "sex": "male"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "BWIRU GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "IBINZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "IBUNGILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "KABUHORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "KANGAYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "KAYENZE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "KILIMANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "KILOLELI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "KIRUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "KISEKE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "KISUNDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "KITANGIRI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "LUKOBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "LUMALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "MIHAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "MNARANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "MWINUKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "NUNDU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "NYAMANORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "NYASAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "PASIANSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "SANGABUYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ilemela",
   "shule": "SHIBULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "BUJIKU SAKILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "BUNGULWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "BUPAMWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "IGONGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "IMALILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "ISENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "KIKUBIJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "KINOJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "LYOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "MALIGISU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "MALYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "MANTARE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "MHANDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "MWABOMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "MWAGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "MWAKILYAMBITI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "MWAMALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "MWAMASHIMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "MWANDU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "MWANGHALANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "MWANKULWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "MWASHILALAGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "NDAMHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "NELLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "NGHUNDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "NGUDU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "NGULLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "NYAMILAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "SUMVE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "TALLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Kwimba",
   "shule": "WALLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "BUJASHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "BUKANDWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "ITUMBILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "KABILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "KAHANGARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "KANDAWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "KINANGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "KITUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "KONGOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "LUBUGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "LUGEYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "LUMVE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "LUTALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "MAGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "MAHAHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "MWAMANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "NGHAYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "NGWAMABANZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "NYANGUGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "SHISHANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Magu",
   "shule": "SUKUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "AIMEE MILEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "BUHINGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "BULEMEJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "BUSONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "IDETEMYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "IGOKELO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "ILUJAMATE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "ISAKAMAWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "J MAGUFULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "KANYELELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "KASOLOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "KOROMIJE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "LUBILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "MAMAYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "MAWEMATATU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "MBARIKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "MISASI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "MISUNGWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "MWANIKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "NHUNDULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "NYABUMHANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "PAUL BOMANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "SANJO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "SHILALO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Misungwi",
   "shule": "SUMBUGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "BUGARIKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "BUHONGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "BUTIMBA DAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "CAPRIPOINT",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "FUMAGILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "IGELEGELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "IGOGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "IGOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "LUCHELELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "LWANHIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "MAHINA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "MAPANGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "MBUGANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "MHANDU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "MIRONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "MKOLANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "MKUYUNI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "MLIMANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "MTONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "MWANZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "NGANZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "NSUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "NYABULOGOYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "NYAKABUNGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "NYAKURUNDUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "NYAMAGANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "NYEGEZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "OLE NJOOLAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "PAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Mwanza",
   "shule": "SHAMALIWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "BITOTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "BUSISI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "BUTONGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "BUYAGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "BUZILASOGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "CHIFUNFU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "IBISABAGENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "KAHUMULO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "KASUNGAMILE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "KATUNGURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "KIJUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "KILABELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "KISHINDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "LUSIKWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "LWENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "MWABALUHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "MWALIGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "NGOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "NGWELI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "NYAMAHONA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "NYAMATONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "NYAMAZUGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "NYAMPULUKANO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "NYAMTELELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "NYANCHENCHE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "SENGEREMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "SIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "TABARUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "TAMABU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Sengerema",
   "shule": "TUNYENYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "BUGUZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "BUKANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "BUKIKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "BUKINDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "BUKONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "BUSANGUMUGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "BWIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "BWISYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "IGALLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "IRUGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "KAKEREGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "LUGONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "MIBUNGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "MUKITUNTU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "MUMBUGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "MURITI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "NAKATUNGURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "NAKOZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "NAMAGONDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "NANSIO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "NDURUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "NYAMANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Mwanza",
   "wilaya": "Ukerewe",
   "shule": "PIUS MSEKWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "CHIEF KIDULILE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "IKOVO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "KAYAO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "KETEWAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "LUANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "LUGARAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "MADILU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "MADUNDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "MAKONDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "MANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "MAVALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "MAVANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "MCHUCHUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "MT LIVINGSTONE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "MT MASUSA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "MUNDINDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Ludewa",
   "shule": "ULAYASI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makambako",
   "shule": "DEO SANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makambako",
   "shule": "KIPAGAMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makambako",
   "shule": "KITANDILILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makambako",
   "shule": "LYAMKENA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makambako",
   "shule": "MAGUVANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makambako",
   "shule": "MAHONGOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makambako",
   "shule": "MAKAMBAKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makambako",
   "shule": "MLOWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makambako",
   "shule": "MTIMBWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makambako",
   "shule": "MUKILIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "IKUWO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "IPELELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "IPEPO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "ISAPULANO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "IWAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "KINYIKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "KIPAGALO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "KITULO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "LUPALILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "LUPILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "MAKETE GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "MANGOTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "MATAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "MBALATSE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "MLONDWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "MT CHAFUKWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "MWAKAVUTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "UKWAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Makete",
   "shule": "USILILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe",
   "shule": "IDAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe",
   "shule": "IKUNA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe",
   "shule": "ITIPINGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe",
   "shule": "J M MAKWETA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe",
   "shule": "KIDEGEMBYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe",
   "shule": "LUPEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe",
   "shule": "MANYUNYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe",
   "shule": "MFRIGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe",
   "shule": "MULUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe",
   "shule": "NINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe",
   "shule": "SOVI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe cbd",
   "shule": "ANNE MAKINDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe cbd",
   "shule": "KIFANYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe cbd",
   "shule": "LUHOLOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe cbd",
   "shule": "MABATINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe cbd",
   "shule": "MAHEVE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe cbd",
   "shule": "MATOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe cbd",
   "shule": "MBEYELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe cbd",
   "shule": "MGOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe cbd",
   "shule": "MPECHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe cbd",
   "shule": "NJOMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe cbd",
   "shule": "ULIWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe cbd",
   "shule": "UWEMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe cbd",
   "shule": "VIZIWI NJOMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Njombe cbd",
   "shule": "YAKOBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Wanging'ombe",
   "shule": "IGIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Wanging'ombe",
   "shule": "IGOSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Wanging'ombe",
   "shule": "IGWACHANYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Wanging'ombe",
   "shule": "ILEMBULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Wanging'ombe",
   "shule": "KIJOMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Wanging'ombe",
   "shule": "LUDUGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Wanging'ombe",
   "shule": "MAKOGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Wanging'ombe",
   "shule": "MARIA NYERERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Wanging'ombe",
   "shule": "MOUNT KIPENGERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Wanging'ombe",
   "shule": "PHILIP MANGULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Wanging'ombe",
   "shule": "SAJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Wanging'ombe",
   "shule": "THOMAS NYIMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Wanging'ombe",
   "shule": "ULEMBWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Wanging'ombe",
   "shule": "USUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Wanging'ombe",
   "shule": "WANGINGOMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Njombe",
   "wilaya": "Wanging'ombe",
   "shule": "WANIKE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Kalambo",
   "shule": "CHISENGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Kalambo",
   "shule": "KALAMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Kalambo",
   "shule": "KALEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Kalambo",
   "shule": "KANYELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Kalambo",
   "shule": "KASANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Kalambo",
   "shule": "KATAZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Kalambo",
   "shule": "MACHINDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Kalambo",
   "shule": "MAMBWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Kalambo",
   "shule": "MATAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Kalambo",
   "shule": "MSANZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Kalambo",
   "shule": "MWAZYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Kalambo",
   "shule": "MWIMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Kalambo",
   "shule": "NAMEMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Kalambo",
   "shule": "ULUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Kalambo",
   "shule": "ZENGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "CHALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "ISALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "KABWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "KALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "KATE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "KIPANDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "KIPILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "KIRANDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "KORONGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "MASHETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "MILUNDIKWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "MKANGALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "MKOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "MKWAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "MTENGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "NINDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "NKASI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "NKOMOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "NKUNDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "NTUCHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "SINTALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Nkasi",
   "shule": "WAMPEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "ILEMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "KAOZE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "KAPENTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "KIKWALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "KIPETA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "KWELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "LULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "LUSAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "MAKUZANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "MAZOKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "MIANGALUA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "MILENIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "MPUI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "MZINDAKAYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "UCHILE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "UNYIHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga",
   "shule": "VUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "CHANJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "IPEPA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "ITWELELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "KALANGASA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "KANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "KANTALAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "KATUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "KICHEMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "KILIMANI MAWENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "KIZWITE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "LUKANGAO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "MAFULALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "MAZWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "MBIZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "MHAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "MTIPE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Rukwa",
   "wilaya": "Sumbawanga cbd",
   "shule": "SUMBAWANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Madaba",
   "shule": "GUMBIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Madaba",
   "shule": "IFINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Madaba",
   "shule": "LIPUPUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Madaba",
   "shule": "MADABA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Madaba",
   "shule": "MAGINGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Madaba",
   "shule": "MAHANJE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Madaba",
   "shule": "NGULUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Madaba",
   "shule": "WINO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "HAGATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "HILELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "KIAMILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "KIGONSERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "KIHANGIMAHUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "KIPOLOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "KITURA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "LANGIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "LINDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "LITEMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "LITUMBANDYOSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "LUHAGARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "LULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "MAGUU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "MAHILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "MATIRI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "MBINGA GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "MBUJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "MIKALANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "MIPARU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "MKAKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "MKOHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "MKUMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "MKUWANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "NAMSWEA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "NYONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "RUANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "UKATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "WUKIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "DR A M SHEIN",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "KIKOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "KINDIMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "LUHUWIKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "LUSETU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "MAKITA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "MBAMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "MBANGAMAO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "MBINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "MKWAYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "NDELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Mbinga",
   "shule": "NGWILIZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "KIMOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "KORIDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "LISIMONJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "LUCHILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "LUEGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "LUKIMWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "LUNA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "MAGAZINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "MBUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "MGOMBASI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "MKOMANILE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "MSINDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "MTAKANINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "MWALIKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "NAHIMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "NAMABENGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "NANUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "NARWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "NASULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "PAMOJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "RWINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "SASAWALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "SELOUS",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Namtumbo",
   "shule": "UTWANGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Nyasa",
   "shule": "ENG STELLA MANYANYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Nyasa",
   "shule": "KILUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Nyasa",
   "shule": "KINGERIKITI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Nyasa",
   "shule": "LIMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Nyasa",
   "shule": "LIPARAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Nyasa",
   "shule": "LITUHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Nyasa",
   "shule": "LUNDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Nyasa",
   "shule": "MANGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Nyasa",
   "shule": "MBAMBA BAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Nyasa",
   "shule": "MONICA MBEGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Nyasa",
   "shule": "NGUMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Nyasa",
   "shule": "NYASA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Nyasa",
   "shule": "ST PAULS",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Nyasa",
   "shule": "TINGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Nyasa",
   "shule": "URBERKANT",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea",
   "shule": "BARABARANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea",
   "shule": "DARAJAMBILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea",
   "shule": "KILAGANO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea",
   "shule": "LIGANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea",
   "shule": "LITAPWASI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea",
   "shule": "LUPUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea",
   "shule": "MAGAGURA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea",
   "shule": "MAPOSENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea",
   "shule": "MATIMIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea",
   "shule": "MHALULE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea",
   "shule": "MPITIMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea",
   "shule": "MUHUKURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea",
   "shule": "NALIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea",
   "shule": "NAMATUHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea",
   "shule": "NAMIHORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea",
   "shule": "NDONGOSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "BOMBAMBILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "CHABRUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "CHANDARUA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "EMMANUEL NCHIMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "KALEMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "LIZABONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "LONDONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "LUKALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "LUWAWASI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "MASHUJAA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "MATARAWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "MATEKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "MATOGORO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "MBULANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "MDANDAMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "MFARANYAKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "MLETELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "MSAMALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "RUVUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "SILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "SONGEA BOYS",
   "type": "special",
   "sex": "male"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "SONGEA GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "SUBIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Songea cbd",
   "shule": "ZIMANIMOTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "FRANK WESTON",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "KIDODOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "LIGOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "LIGUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "LUKUMBULE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "MARUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "MASONYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "MATAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "MATEMANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "MBESA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "MCHOTEKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "MGOMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "MTUTURA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "MUHUWESI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "NAKAPANYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "NALASI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "NAMASAKATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "NAMPUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "NAMWINYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "NANDEMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "SEMENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Ruvuma",
   "wilaya": "Tunduru",
   "shule": "TUNDURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kahama",
   "shule": "ABDULRAHIM BUSOKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kahama",
   "shule": "BUGISHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kahama",
   "shule": "BUKAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kahama",
   "shule": "ISAGEHE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kahama",
   "shule": "ISUNUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kahama",
   "shule": "KINAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kahama",
   "shule": "KISHIMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kahama",
   "shule": "KITWANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kahama",
   "shule": "MPERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kahama",
   "shule": "MWENDAKULIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kahama",
   "shule": "NGOGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kahama",
   "shule": "NYANDEKWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kahama",
   "shule": "NYASHIMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kahama",
   "shule": "NYASUBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kahama",
   "shule": "NYIHOGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kahama",
   "shule": "SEEKE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "BUBIKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "BULEKELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "BUNAMBIYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "BUSIYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "IDUKILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "IGAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "KILOLELI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "KISHAPU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "MAGANZO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "MANGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "MIPA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "MWADUI TECH",
   "type": "technical",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "MWAKIPOYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "MWAMADULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "MWAMALASA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "MWAMASHELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "MWATAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "MWIGUMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "NGOFILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "SHINYANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "SOMAGEDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "SONGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "TALAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "UCHUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "UKENYENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Kishapu",
   "shule": "WISHITELEJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Msalala",
   "shule": "BALOHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Msalala",
   "shule": "BUGARAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Msalala",
   "shule": "BULIGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Msalala",
   "shule": "BULYANHULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Msalala",
   "shule": "BUSANGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Msalala",
   "shule": "ISAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Msalala",
   "shule": "JANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Msalala",
   "shule": "LUNGUYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Msalala",
   "shule": "MWALUGULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Msalala",
   "shule": "MWAMANDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Msalala",
   "shule": "MWL NYERERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Msalala",
   "shule": "NGAYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Msalala",
   "shule": "NTOBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Msalala",
   "shule": "NYIKOBOKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Msalala",
   "shule": "SEGESE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "DIDIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "GEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "IHUGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "ILOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "IMESELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "ISELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "ISELAMAGAZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "ITWANGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "KASELYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "KITULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "LYABUKANDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "LYABUSALU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "MASENGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "MISHEPO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "MWALUKWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "MWANTINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "NGWAKITOLYO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "PANDAGICHIZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "SALAWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "SAMUYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "SHINGITA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "SOLWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "TINDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "TINDE GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "USANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "USULE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga",
   "shule": "ZUNZULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "BUSULWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "CHAMAGUHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "IBINZAMATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "KIZUMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "KOLANDOTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "MASEKELO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "MAZINGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "MWAMALILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "MWASELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "MWAWAZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "NDALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "NGOKOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "OLD SHINYANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "RAJANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "TOWN",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "UHURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Shinyanga cbd",
   "shule": "UZOGORE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "BULUNGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "CHAMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "CHONA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "DAKAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "IDAHINA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "IGUNDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "IGWAMANONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "KINAMAPULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "KISUKE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "MPUNZE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "MWELI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "NYANKENDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "SABASABINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "UKUNE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "ULEWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "ULOWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "USHETU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Shinyanga",
   "wilaya": "Ushetu",
   "shule": "UYOGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "BANEMHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "BYUNA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "DUTWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "GAMBOSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "GASUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "GEGEDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "IBULYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "IGAGANULWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "IKINABUSHU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "IKUNGULYABASHASHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "ITUBUKILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "KASOLI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "KILABELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "MISWAKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "MWADOBANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "MWAMLAPA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "MWANTIMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "NKINDWABIYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "NKOLOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "NYASOSI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "NYAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "SAKWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "SAPIWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "BARIADI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "BIASHARA BARIADI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "CHENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "GIRIKU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "GUDUWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "KIDINDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "MAHAHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "MBITI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "NGWANGWALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "NTUZU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "NYAKABINDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "OLD MASWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "SIMIYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Bariadi",
   "shule": "SOMANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "ANTHONY MTAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "BADUGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "DR CHEGENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "IGALUKILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "KABITA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "KALEMELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "KIJELESHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "KISHAMAPANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "LAMADI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "MALILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "MASANZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "MKULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "MWAMAGIGISI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "MWASAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "NASSA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "NGASAMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "NYALUHANDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "NYANGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "SHIGALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Busega",
   "shule": "SOGESCA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "BUDALABUJIGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "BUKINGWAMINZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "BUMERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "BUNAMHALA MB",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "CHINAMILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "HABIYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "IDOSELO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "IKINDILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "IKUNGULIPU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "INALO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "ITILIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "KABALE BARIADI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "KANADI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "KINANGWELI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "LAGANGABILILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "LAINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "LUNGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "MADILANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "MAHEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "MHUNZE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "MWAKILANGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "MWALUSHU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "MWAMTANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "MWASWALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "NDOLELEJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "NKOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "SAGATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "SHISHANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Itilima",
   "shule": "SUNZULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "BADI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "BINZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "BUCHAMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "BUDEKWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "BUSHASHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "IPILILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "ISANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "ITULE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "JIJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "KADOTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "KINAMWIGULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "KULIMI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "MAJEBELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "MALAMPAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "MASELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "MASUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "MASWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "MATABA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "MWABAYANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "MWAGALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "MWAKALEKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "MWAMANENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "MWANDETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "MWASAYI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "NGHUMBU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "NGULIGULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "NGWIGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "NYABUBINZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "NYALIKUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "SALAGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "SANGAMWALUGESHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "SENANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "SENGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "SHISHIYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "SUKUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Maswa",
   "shule": "ZEBEYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "BUKUNDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "IMALASEKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "ITINJE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "KIMALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "KISESA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "LINGEKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "LUBIGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "LYUSA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "MAKAO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "MEATU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "MWABUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "MWABUSALU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "MWAKALUBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "MWAMALOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "MWAMANONGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "MWAMISHALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "MWANDOYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "MWANJOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "MWAUKOLI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "NGHOBOKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "NYALANJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "PAJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Simiyu",
   "wilaya": "Meatu",
   "shule": "SAKASAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "DADU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "DR ALLY M SHEIN",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "IGHOMBWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "IGLANSONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "IKUNGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "IRISYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "ISEKE MUUNGANO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "ISSUNA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "LIGHWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "MAKIUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "MANGONYI SHANTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "MASINDA DAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "MIANDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "MINYUGHE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "MKIWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "MKUNGUAKIHENDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "MSUNGUA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "MTUNDURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "MUHINTIRI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "MUNGAA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "MUNKINYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "MWARU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "MWAU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "NTUNTU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "PUMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "SEPUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "SIUYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "UNYAHATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "UTAHO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Ikungi",
   "shule": "WEMBERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "KASELYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "KIDARU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "KINAMBEU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "KINAMPANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "KISANA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "KISIRIRI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "KIZAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "KYENGEGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "LULUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "MBELEKESE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "MGONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "MTEKENTE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "MTOA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "MUKULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "NDAGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "NEW KIOMBOI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "NTWIKE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "SHELUI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "TULYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "TUMAINI",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "URUGHU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Iramba",
   "shule": "USHORA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Itigi",
   "shule": "HANDU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Itigi",
   "shule": "IDODYANDOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Itigi",
   "shule": "IPAMUDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Itigi",
   "shule": "ITIGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Itigi",
   "shule": "KALEKWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Itigi",
   "shule": "KAMENYANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Itigi",
   "shule": "KIMADOI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Itigi",
   "shule": "MGANDU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Itigi",
   "shule": "MITUNDU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Itigi",
   "shule": "RUNGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Itigi",
   "shule": "SANJARANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Manyoni",
   "shule": "CHIKUYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Manyoni",
   "shule": "HEKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Manyoni",
   "shule": "ISSEKE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Manyoni",
   "shule": "KILIMATINDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Manyoni",
   "shule": "KINANGALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Manyoni",
   "shule": "KINTINKU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Manyoni",
   "shule": "KIZIGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Manyoni",
   "shule": "MAKANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Manyoni",
   "shule": "MAKURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Manyoni",
   "shule": "MANYONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Manyoni",
   "shule": "MLEWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Manyoni",
   "shule": "MWANZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Manyoni",
   "shule": "NGAITI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Manyoni",
   "shule": "NKONKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Manyoni",
   "shule": "SANZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Manyoni",
   "shule": "SASAJILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "CHEMCHEM",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "GRACE MESAKI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "GUMANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "GUNDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "IBAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "IGUGUNO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "ISANZU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "JORMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "KIKHONDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "KINAMPUNDU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "KINYANGIRI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "MALAJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "MIGANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "MWANGEZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "NDUGUTI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "NKINTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "SELENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "SETH BENJAMIN",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Mkalama",
   "shule": "TUMULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "IKHANODA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "ILONGERO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "ITAJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "KIJOTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "KINYETO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "MADASENGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "MAGHOJOA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "MAKURO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "MATUMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "MERYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "MIKIWU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "MISINKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "MRAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "MSISI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "MTINKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "MUDIDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "MUGHAMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "MUGHUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "MWANAMWEMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "MWASAUYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "NGIMU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "NTONGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "NYERI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "POHAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "SINGITU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida",
   "shule": "UGHANDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "DR SALMIN AMOUR",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "IPEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "KIMPUNGUA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "KINDAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "MANDEWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "MITUNDURUNI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "MTAMAA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "MTIPA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "MUFUMBU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "MUGHANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "MUNGUMAJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "MWANKOKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "MWENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "SENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "UNYAMBWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "UNYAMIKUMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "UNYIANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Singida",
   "wilaya": "Singida cbd",
   "shule": "UTEMINI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "BUPIGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "IBABA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "IKINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "ILEJE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "ITALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "ITUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "KAFULE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "KAKOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "LUBANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "LUSWISI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "MBEBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "MLALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "MSOMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "NAKALULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "NDOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "NGULILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "NGULUGULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "SANGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Ileje",
   "shule": "STIVEN KIBONA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "BARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "HALUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "HAMPANGALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "HEZYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "IDIMI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "IGAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "IGANDUKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "IGANYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "IHANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "ILOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "INSANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "IPUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "ISALALO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "ISANDULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "ISANGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "ITAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "ITEPULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "ITUMPI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "KILIMAMPIMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "LUMBILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "LWATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "MLANGALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "MLOWO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "MSANGAWALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "MSANKWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "MSENSE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "MSIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "MYOVIZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "NALYELYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "NAMBINZO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "NANSWILU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "NDUGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "NKANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "NYIMBILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "NZOVU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "SHAJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "SHIKULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "SHIWINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "SIMBEGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Mbozi",
   "shule": "VWAWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Momba",
   "shule": "CHIKANAMLILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Momba",
   "shule": "CHILULUMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Momba",
   "shule": "CHITETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Momba",
   "shule": "IVUNA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Momba",
   "shule": "KAPELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Momba",
   "shule": "MKULWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Momba",
   "shule": "MOMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Momba",
   "shule": "MSANGANO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Momba",
   "shule": "NKANGAMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Momba",
   "shule": "NZOKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Momba",
   "shule": "UWANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Songwe",
   "shule": "GALULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Songwe",
   "shule": "IFWENKENYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Songwe",
   "shule": "KANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Songwe",
   "shule": "KAPALALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Songwe",
   "shule": "MAWENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Songwe",
   "shule": "MWAGALACHUNYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Songwe",
   "shule": "NAMKUKWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Songwe",
   "shule": "SAZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Songwe",
   "shule": "TOTOWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Tunduma",
   "shule": "CHAPWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Tunduma",
   "shule": "J M KIKWETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Tunduma",
   "shule": "KATETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Tunduma",
   "shule": "MPAKANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Tunduma",
   "shule": "MPEMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Tunduma",
   "shule": "MUUNGANO1",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Tunduma",
   "shule": "MWAKAKATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Tunduma",
   "shule": "MWL J K NYERERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Songwe",
   "wilaya": "Tunduma",
   "shule": "NAMOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "BUKOKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "CHOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "HANIHANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "ICHAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "IGOWEKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "IGUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "IGURUBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "ISAKAMALIWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "ITUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "ITUNDURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "KININGINILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "KINUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "MBUTU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "MISANA NTOBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "MWAKIPANGA NYANDEKWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "MWAMASHIGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "MWAMASHIMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "MWANZUGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "MWASHIKU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "MWAYUNGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "MWISI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "NANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "NDEMBEZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "NGULUMWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "NGUVUMOJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "NKINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "SIMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "SUNGWIZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Igunga",
   "shule": "ZIBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "IGAGALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "IGWISI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "ILEGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "KALIUA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "KANINDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "KAPUYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "KASHISHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "KAZAROHO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "MKINDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "MWONGOZO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "SELELI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "SILAMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "UGUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "UKUMBISIGANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "ULYANKULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "USHOKOLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "USINGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "UYOWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Kaliua",
   "shule": "ZUGIMLOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "BUDUSHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "BUKENE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "HAMZA AZIZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "IGUSULE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "IKINDWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "ISAGENHE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "ISANZU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "ITOBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "KAMPALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "KARITU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "KASELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "KILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "MABONDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "MAGENGATI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "MAMBALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "MILAMBO ITOBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "MIZIBAZIBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "MOGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "MUHUGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "MWAKASHANHALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "MWAMALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "MWANGOYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "MWANHALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "NATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "NKINIZIWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "PUGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "SEMEMBELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "SHIGAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "SIGILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "TONGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "WELA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "BUGWANDEGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "BULUNDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "CHIEF NTINGINYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "IJANIJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "ITILO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "MIGUWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "MWANZOLI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "NZEGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Nzega",
   "shule": "UNDOMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "CHABUTWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "IGIGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "KAMAGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "KILOLI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "KILUMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "KIPILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "KISANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "KIWERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "LANGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "MIBONO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "MKOLYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "MOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "MPOMBWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "MSUVA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "NGULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "PANGALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "TUTUO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "UGUNDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Sikonge",
   "shule": "USUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "BOMBAMZINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "CHANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "CHEYO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "FUNDIKIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "IKOMWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "IPULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "ISEVYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "ITETEMIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "ITONJANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "KALUNDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "KANYENYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "KARIAKOO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "KAZE HILL",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "KAZIMA",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "LWANZALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "MILAMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "MISHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "NDEVELWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "NKUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "NYAMWEZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "SIKANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "TABORA BOYS",
   "type": "special",
   "sex": "male"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Tabora cbd",
   "shule": "TABORA GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "GOWEKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "IBIRI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "IDETE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "IGALULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "IKONGOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "IMALAMPAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "KIZENGI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "LOLANGULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "LOYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "LUTENDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "MABAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "MADAHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "MAKAZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "NDONO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "SHITAGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "TURA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "UPUGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Uyui",
   "shule": "USAGARI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "CHETU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "IMALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "IMALAMAKOYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "KAPILULA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "KILOLENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "MATWIGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "MUKANGWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "UGALLA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "UKOMBOZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "UKONDAMOYO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "URAMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "USISYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "USOJI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "USONGELANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "UYOGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "UYUMBU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tabora",
   "wilaya": "Urambo",
   "shule": "VUMILIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "BAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "BUMBULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "CHAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "FUNTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "JANUARY MAKAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "KIHITU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "KIVILICHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "KIZANDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "KIZIMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "KWALEI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "KWAMONGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "KWEHANGALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "MAYO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "MAZUMBAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "MBELEI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "MBUZII",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "MGWASHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "MIBUKWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "MKAALIE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "MMAKAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "MPONDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "MSAMAKA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "SONI DAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "TAMOTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "VUGABAZO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Bumbuli",
   "shule": "WENA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "CHOGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KABUKU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KANGATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KISAZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KIVA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KOMSANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KWACHAGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KWALUDEGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KWALUGURU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KWAMATUKU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KWAMGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KWAMKONO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KWAMSISI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KWANKONJE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KWASUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KWEDIZINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "MANGA MPAKANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "MAZINGARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "MKATA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "NDOLWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "PANGAMBILI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "SEGERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "SINDENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "HANDENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KILELENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KIVESA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KOMNYANGANYO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KONJE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "KWENJUGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "MISIMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Handeni",
   "shule": "MSAJE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "JAILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "KIBIRASHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "KIKUNDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "KILINDI ASILIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "KILINDI GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "KIMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "KOMKALAKALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "KWEDIBOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "KWEKIVU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "LWANDE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "MAFISA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "MASAGALU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "MBWEGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "MGERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "MKINDI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "MKUYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "NEGERO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "NKAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "PAGWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "SEUTA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "TUNGULI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Kilindi",
   "shule": "VIBAONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "BUIKO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "BUNA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "BUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "CHEKELEI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "DINDIRA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "HALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "KIZARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "KWAGUNDA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "KWASHEMSHI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "KWEMDIMU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "MADAGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "MAFIHILLS",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "MAGOMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "MASHEWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "MASHINDEI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "MAZINDE DAY",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "MBAGHAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "MFUNDIA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "MKALAMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "MKOMAZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "MLUNGUI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "MNYUZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "MSWAHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "MWISHO WA SHAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "PATEMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "SHEKILANGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "VUGIRI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "JOEL BENDERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "KILOLE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "KIMWERI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "KOROGWE GIRLS",
   "type": "special",
   "sex": "female"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "KWAMNDOLWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "NGOMBEZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "NYERERE MEMORIAL",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "OLD KOROGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Korogwe",
   "shule": "SEMKIWA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "BALOZI MSHANGAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "BERNARD MEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "CHAMBOGHO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "GARE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "GOLOGOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "HAMBALAWEI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "HEMTOYE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "KALUMELE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "KIRETI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "KISABA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "KITALA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "KITIVO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "KWAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "KWEKANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "KWEMARAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "KWEMASHAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "KWEULASI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "LUKOZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "LUNGUZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "LUSHOTO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MAGAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MAKOLE JUU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MALIBWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MANOLO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MARIAM MSHANGAMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MASANGE JUU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MAVUMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MAZASHAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MBWEI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MDANDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MIGAMBO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MKUZI JUU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MLONGWEMA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MNAZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MSALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MTAE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "MTUMBI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "NDURUMO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "NGAZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "NGULWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "NGWELO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "NTAMBWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "NYWELO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "PRINCE CLAUS",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "RANGWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "SHAGHAYU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "SHAMBALAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "SHITA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "SHUME",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "SUNGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "UBIRI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "UMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Lushoto",
   "shule": "VITI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Mkinga",
   "shule": "BOSHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Mkinga",
   "shule": "DALUNI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Mkinga",
   "shule": "DUGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Mkinga",
   "shule": "GOMBERO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Mkinga",
   "shule": "KIGONGOI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Mkinga",
   "shule": "KWALE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Mkinga",
   "shule": "LANZONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Mkinga",
   "shule": "MANZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Mkinga",
   "shule": "MAPATANO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Mkinga",
   "shule": "MARAMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Mkinga",
   "shule": "MAVOVO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Mkinga",
   "shule": "MKINGALEO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Mkinga",
   "shule": "MTIMBWANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Mkinga",
   "shule": "MWAKIJEMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Mkinga",
   "shule": "ZINGIBARI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "BWEMBWERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "CHIEF MANGENYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "FURAHA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "KERENGE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "KICHEBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "KIGOMBE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "KILULU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "KWABUTU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "KWAFUNGO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "KWEMKABARA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "MAGILA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "MISALAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "MISOZWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "MKURUMUZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "MKUZI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "MLINGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "MLINGANO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "MTINDIRO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "MUHEZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "NGOMENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "NKUMBA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "POTWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "SHEBOMEZA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "SONGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Muheza",
   "shule": "ZIRAI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Pangani",
   "shule": "BUSHIRI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Pangani",
   "shule": "FUNGUNI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Pangani",
   "shule": "KILIMANGWIDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Pangani",
   "shule": "KIPUMBWI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Pangani",
   "shule": "MKWAJA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Pangani",
   "shule": "MWERA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Pangani",
   "shule": "TONGANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "CHONGOLEANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "CHUMBAGENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "GALANOS",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "HORTEN",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "JAPAN",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "KIHERE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "KIOMONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "KIRARE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "MABOKWENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "MACECHU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "MARUNGU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "MAWENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "MIKANJUNI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "MKWAKWANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "MNYANJANI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "MSAMBWENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "MWAPACHU",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "NDAOYA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "NGUVUMALI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "OLD TANGA",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "PANDE MAGUBENI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "PONGWE",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "TANGA TECHNICAL",
   "type": "technical",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "TOLEDO",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "TONGONI",
   "type": "ward",
   "sex": "mixture"
 },
 {
   "mkoa": "Tanga",
   "wilaya": "Tanga cbd",
   "shule": "USAGARA",
   "type": "ward",
   "sex": "mixture"
 }
]
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
    for data in shule:
        # This make sure that the id of kata is as we save in kata table
        mkoa = Mkoa.objects.get(name=data['mkoa'])
        w = Wilaya.objects.values('id', 'name').filter(mkoa_id=mkoa)
        wl = [x for x in w if x['name'] == data['wilaya']]
        wilaya = Wilaya.objects.get(id=wl[0]['id'])
        # k = Kata.objects.values('id', 'name').filter(wilaya_id=wilaya)
        # kt = [x for x in k if x['name'] == data['kata']]
        # kata = Kata.objects.get(id=kt[0]['id'])
        ##

        school = School.objects.create(
            name=data['shule'],
            wilaya_id=wilaya,
            type=data['type'],
            sex=data['sex']
        )
        school.save()


def group_list(lst, group_lengths):
    result = []
    idx = 0
    for length in group_lengths:
        group = lst[idx:idx + length]
        result.append(group)
        idx += length
    return result


def specialSchool(year):
    # This give us required student in special schools
    special_school = School.objects.values('id', 'name', 'sex', 'type').filter(type="special")
    ss = [x for x in special_school]
    ss_list = []
    total_required_special = 0
    for d in ss:
        sps = School.objects.get(id=d['id'])
        ss_q = QuantityRequired.objects.values('quantity').get(Q(school_id=sps) and Q(year=year))
        total_required_special = total_required_special + ss_q['quantity']
        data = {
            'id': d['id'],
            'name': d['name'],
            'sex': d['sex'],
            'type': d['type'],
            'quantity_required': ss_q['quantity']
        }
        ss_list.append(data)
    students = Student.objects.values('id', 'candidate_name', 'sex').filter(
        Q(year=year) and Q(is_active=True)).order_by(
        '-average_marks')[:total_required_special]
    students_ = [x for x in students]
    special_quantity = [x['quantity_required'] for x in ss_list]
    student_groups = group_list(students_, special_quantity)
    output_list = [{'id': d['id'], 'name': d['name'], 'sex': d['sex'],
                    'type': d['type'], 'quantity_required': d['quantity_required'],
                    'students': sub_list} for d, sub_list in zip(ss_list, student_groups)]
    # This is to save the students to the special school

    for sch in output_list:
        school = School.objects.get(id=sch['id'])
        for stu in sch['students']:
            student = Student.objects.get(id=stu['id'])
            data = StudentSchool.objects.create(school_id=school, student_id=student)
            data.save
        print('student saved at ' + sch['name'])


def technicalSchool(year):
    # This give us required student in technical schools
    technical_school = School.objects.values('id', 'name', 'sex', 'type').filter(type="technical")
    ts = [x for x in technical_school]
    ts_list = []
    total_required_technical = 0
    for d in ts:
        tcs = School.objects.get(id=d['id'])
        ts_q = QuantityRequired.objects.values('quantity').get(Q(school_id=tcs) and Q(year=year))
        total_required_technical = total_required_technical + ts_q['quantity']
        data = {
            'id': d['id'],
            'name': d['name'],
            'sex': d['sex'],
            'type': d['type'],
            'quantity_required': ts_q['quantity']
        }
        ts_list.append(data)

    students = Student.objects.values('id', 'candidate_name', 'sex').filter(
        Q(year=year) and Q(is_active=True)).order_by(
        '-average_marks')[:total_required_technical]
    students_ = [x for x in students]
    technical_quantity = [x['quantity_required'] for x in ts_list]
    student_groups = group_list(students_, technical_quantity)
    output_list = [{'id': d['id'], 'name': d['name'], 'sex': d['sex'],
                    'type': d['type'], 'quantity_required': d['quantity_required'],
                    'students': sub_list} for d, sub_list in zip(ts_list, student_groups)]
    # This is to save the students to the technical school

    for sch in output_list:
        school = School.objects.get(id=sch['id'])
        for stu in sch['students']:
            student = Student.objects.get(id=stu['id'])
            data = StudentSchool.objects.create(school_id=school, student_id=student)
            data.save
        print('student saved at ' + sch['name'])


def wardSchool(year):
    wards = Kata.objects.values('id', 'name').all()
    w = [x for x in wards]
    for i in w:
        kata = Kata.objects.get(id=i['id'])
        stu = Student.objects.values('id').filter(kata_id=kata)
        # grouping list
        sch = School.objects.values('id', 'name').filter(kata_id=kata)
        sch_length = len(sch)
        stu_length = len(stu)
        div = stu_length/sch_length
        grouping_length = []
        for i in range(sch_length):
            grouping_length.append(div)
        student_groups = group_list(stu, grouping_length)
        output_list = [{'id': d['id'], 'name': d['name'], 'students': sub_list} for d, sub_list in zip(sch, student_groups)]

        for i in output_list:
            school = School.objects.get(id=i['id'])
            for j in i['students']:
                student = Student.objects.get(id=j['id'])
                data = StudentSchool.objects.create(school_id=school, student_id=student)
        print('students saved at ward ' + kata.name)


def Selection(request):
    specialSchool(request.data['year'])
    print('special school done')

    technicalSchool(request.data['year'])
    print('technical school done')

    wardSchool(request.data['year'])
    print('ward school done')

    return "done"
# request_ = {
#     'year': '2022'
# }
