import csv
from mtaa import tanzania

x = [
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "ARUSHA DAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "ARUSHA GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "ARUSHA SEC",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "4",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "ARUSHA TERRAT",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "5",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "BARAA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "6",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "ELERAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "7",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "FELIX MREMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "8",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "KALOLENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "9",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "KIMASEKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "10",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "KINANA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "11",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "KORONA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "12",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "LEMARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "13",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "LOSIRWAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "14",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "MKONOO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "15",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "MOIVARO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "16",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "MOSHONO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "17",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "MURIET",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "18",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "NAURA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "19",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "NGARENARO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "20",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "NJIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "21",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "OLASITI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "22",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "OLMOTI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "23",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "OLOIRIEN",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "24",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "SINON",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "25",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "SOMBETINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "26",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "SORENYI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "27",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "SUYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "28",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha CC",
   "FIELD4": "THEMI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "29",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "BANGATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "30",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "EINOTI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "31",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "ENDEVES",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "32",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "ENYOITO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "33",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "ILBORU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "34",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "ILKIDINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "35",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "KIMNYAKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "36",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "KIRANYI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "37",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "LENGIJAVE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "38",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "LOSIKITO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "39",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "MATEVES",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "40",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "MLANGARINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "41",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "MRINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "42",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "MUKULAT",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "43",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "MUSA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "44",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "MWANDET",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "45",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "NDURUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "46",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "NGIRESI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "47",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "OLDADAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "48",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "OLDONYOSAMBU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "49",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "OLDONYOWASI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "50",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "OLEMEDEYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "51",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "OLJORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "52",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "OLMOTONYI FOREST",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "53",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "OLOKII",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "54",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "OLTRUMET",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "55",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "OSILIGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "56",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "SAMBASHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "57",
   "FIELD2": "Arusha",
   "FIELD3": "Arusha DC",
   "FIELD4": "SOKONI II",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "58",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "AWET",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "59",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "BANJIKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "60",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "BARAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "61",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "BARAY KHUSMAYI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "62",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "CHAENDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "63",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "DIEGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "64",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "DOMEL",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "65",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "DR WILBROAD SLAA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "66",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "EDITH GRORA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "67",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "ENDABASH",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "68",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "ENDALLAH",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "69",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "FLORIAN",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "70",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "GANAKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "71",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "GETAMOCK",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "72",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "GYEKRUM ARUSHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "73",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "GYEKRUM LAMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "74",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "KAINAM RHOTIA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "75",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "KANSAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "76",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "KARATU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "77",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "KILIMAMOJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "78",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "KILIMATEMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "79",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "MANGOLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "80",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "MARANG",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "81",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "MLIMANI SUMAWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "82",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "OLDEANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "83",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "ORBOSHAN",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "84",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "QANGDEND",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "85",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "QARU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "86",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "QURUS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "87",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "SLAHHAMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "88",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "UPPER KITETE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "89",
   "FIELD2": "Arusha",
   "FIELD3": "Karatu DC",
   "FIELD4": "WELWEL",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "90",
   "FIELD2": "Arusha",
   "FIELD3": "Longido DC",
   "FIELD4": "ENDUIMET",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "91",
   "FIELD2": "Arusha",
   "FIELD3": "Longido DC",
   "FIELD4": "ENGARENAIBOR",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "92",
   "FIELD2": "Arusha",
   "FIELD3": "Longido DC",
   "FIELD4": "KETUMBEINE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "93",
   "FIELD2": "Arusha",
   "FIELD3": "Longido DC",
   "FIELD4": "LEKULE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "94",
   "FIELD2": "Arusha",
   "FIELD3": "Longido DC",
   "FIELD4": "LONGIDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "95",
   "FIELD2": "Arusha",
   "FIELD3": "Longido DC",
   "FIELD4": "MATALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "96",
   "FIELD2": "Arusha",
   "FIELD3": "Longido DC",
   "FIELD4": "NAMANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "97",
   "FIELD2": "Arusha",
   "FIELD3": "Longido DC",
   "FIELD4": "NATRON",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "98",
   "FIELD2": "Arusha",
   "FIELD3": "Longido DC",
   "FIELD4": "TINGATINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "99",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "AKERI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "100",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "KIKWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "101",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "KINGORI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "102",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "KISIMIRI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "103",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "KITEFU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "104",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "LAKITATU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "105",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "MAJENGO KATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "106",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "MAJI YA CHAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "107",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "MAKIBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "108",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "MALULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "109",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "MARORONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "110",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "MARUVANGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "111",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "MBUGUNI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "112",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "MIRIRINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "113",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "MOMELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "114",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "MUUNGANO USARIVER",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "115",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "NASHOLI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "116",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "NGONGONGARE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "117",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "NGURUDOTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "118",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "NGYEKU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "119",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "NKOANEKOLI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "120",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "NKOANRUA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "121",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "NKOARISAMBU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "122",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "NKOASENGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "123",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "NSHUPU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "124",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "PAMOJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "125",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "PATANDI MAALUM",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "126",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "POLI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "127",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "SAKILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "128",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "SHISHTON",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "129",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "SINGISI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "130",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "SONGORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "131",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "UMOJA KINGORI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "132",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "URAKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "133",
   "FIELD2": "Arusha",
   "FIELD3": "Meru DC",
   "FIELD4": "UWIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "134",
   "FIELD2": "Arusha",
   "FIELD3": "Monduli DC",
   "FIELD4": "ENGUTOTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "135",
   "FIELD2": "Arusha",
   "FIELD3": "Monduli DC",
   "FIELD4": "IRKISALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "136",
   "FIELD2": "Arusha",
   "FIELD3": "Monduli DC",
   "FIELD4": "IRKISONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "137",
   "FIELD2": "Arusha",
   "FIELD3": "Monduli DC",
   "FIELD4": "KIPOK",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "138",
   "FIELD2": "Arusha",
   "FIELD3": "Monduli DC",
   "FIELD4": "LOWASSA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "139",
   "FIELD2": "Arusha",
   "FIELD3": "Monduli DC",
   "FIELD4": "MANYARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "140",
   "FIELD2": "Arusha",
   "FIELD3": "Monduli DC",
   "FIELD4": "MOITA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "141",
   "FIELD2": "Arusha",
   "FIELD3": "Monduli DC",
   "FIELD4": "NANJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "142",
   "FIELD2": "Arusha",
   "FIELD3": "Monduli DC",
   "FIELD4": "OLDONYOLENGAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "143",
   "FIELD2": "Arusha",
   "FIELD3": "Monduli DC",
   "FIELD4": "OLESOKOINE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "144",
   "FIELD2": "Arusha",
   "FIELD3": "Monduli DC",
   "FIELD4": "OLTINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "145",
   "FIELD2": "Arusha",
   "FIELD3": "Monduli DC",
   "FIELD4": "RIFTVALLEY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "146",
   "FIELD2": "Arusha",
   "FIELD3": "Ngorongoro DC",
   "FIELD4": "ARASH",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "147",
   "FIELD2": "Arusha",
   "FIELD3": "Ngorongoro DC",
   "FIELD4": "DIGODIGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "148",
   "FIELD2": "Arusha",
   "FIELD3": "Ngorongoro DC",
   "FIELD4": "EMBARWAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "149",
   "FIELD2": "Arusha",
   "FIELD3": "Ngorongoro DC",
   "FIELD4": "LAKE NATRON",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "150",
   "FIELD2": "Arusha",
   "FIELD3": "Ngorongoro DC",
   "FIELD4": "LOLIONDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "151",
   "FIELD2": "Arusha",
   "FIELD3": "Ngorongoro DC",
   "FIELD4": "MALAMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "152",
   "FIELD2": "Arusha",
   "FIELD3": "Ngorongoro DC",
   "FIELD4": "NAINOKANOKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "153",
   "FIELD2": "Arusha",
   "FIELD3": "Ngorongoro DC",
   "FIELD4": "SALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "154",
   "FIELD2": "Arusha",
   "FIELD3": "Ngorongoro DC",
   "FIELD4": "SAMUNGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "155",
   "FIELD2": "Arusha",
   "FIELD3": "Ngorongoro DC",
   "FIELD4": "SOITSAMBU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "156",
   "FIELD2": "Coast",
   "FIELD3": "Bagamoyo DC",
   "FIELD4": "BAGAMOYO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "157",
   "FIELD2": "Coast",
   "FIELD3": "Bagamoyo DC",
   "FIELD4": "DUNDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "158",
   "FIELD2": "Coast",
   "FIELD3": "Bagamoyo DC",
   "FIELD4": "FUKAYOSI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "159",
   "FIELD2": "Coast",
   "FIELD3": "Bagamoyo DC",
   "FIELD4": "HASSANAL DAMJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "160",
   "FIELD2": "Coast",
   "FIELD3": "Bagamoyo DC",
   "FIELD4": "KEREGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "161",
   "FIELD2": "Coast",
   "FIELD3": "Bagamoyo DC",
   "FIELD4": "KINGANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "162",
   "FIELD2": "Coast",
   "FIELD3": "Bagamoyo DC",
   "FIELD4": "KIROMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "163",
   "FIELD2": "Coast",
   "FIELD3": "Bagamoyo DC",
   "FIELD4": "MATIMBWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "164",
   "FIELD2": "Coast",
   "FIELD3": "Bagamoyo DC",
   "FIELD4": "ZINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "165",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "CHALINZE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "166",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "CHANGALIKWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "167",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "KIBINDU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "168",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "KIKARO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "169",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "KIMANGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "170",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "KIWANGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "171",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "LUGOBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "172",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "MANDERA GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "173",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "MATIPWILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "174",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "MBOGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "175",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "MDAULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "176",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "MIONO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "177",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "MORETO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "178",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "MSATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "179",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "TALAWANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "180",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "UBENA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "181",
   "FIELD2": "Coast",
   "FIELD3": "Chalinze DC",
   "FIELD4": "VIGWAZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "182",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha DC",
   "FIELD4": "DOSSA AZIZ",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "183",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha DC",
   "FIELD4": "KILANGALANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "184",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha DC",
   "FIELD4": "KWALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "185",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha DC",
   "FIELD4": "MAGINDU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "186",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha DC",
   "FIELD4": "MIHANDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "187",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha DC",
   "FIELD4": "RAFSANJANI SOGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "188",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha DC",
   "FIELD4": "RUVU GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "189",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha DC",
   "FIELD4": "RUVU STATION",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "190",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha TC",
   "FIELD4": "BUNDIKANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "191",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha TC",
   "FIELD4": "KIBAHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "192",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha TC",
   "FIELD4": "KIBAHA GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "193",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha TC",
   "FIELD4": "MBWAWA MISWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "194",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha TC",
   "FIELD4": "MIEMBESABA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "195",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha TC",
   "FIELD4": "MWAMBISI FOREST",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "196",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha TC",
   "FIELD4": "MWANALUGALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "197",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha TC",
   "FIELD4": "NYUMBU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "198",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha TC",
   "FIELD4": "PANGANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "199",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha TC",
   "FIELD4": "SIMBANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "200",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha TC",
   "FIELD4": "TUMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "201",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha TC",
   "FIELD4": "VISIGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "202",
   "FIELD2": "Coast",
   "FIELD3": "Kibaha TC",
   "FIELD4": "ZOGOWALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "203",
   "FIELD2": "Coast",
   "FIELD3": "Kibiti DC",
   "FIELD4": "DIMANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "204",
   "FIELD2": "Coast",
   "FIELD3": "Kibiti DC",
   "FIELD4": "KIBITI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "205",
   "FIELD2": "Coast",
   "FIELD3": "Kibiti DC",
   "FIELD4": "KIKALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "206",
   "FIELD2": "Coast",
   "FIELD3": "Kibiti DC",
   "FIELD4": "MAHEGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "207",
   "FIELD2": "Coast",
   "FIELD3": "Kibiti DC",
   "FIELD4": "MCHUKWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "208",
   "FIELD2": "Coast",
   "FIELD3": "Kibiti DC",
   "FIELD4": "MJAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "209",
   "FIELD2": "Coast",
   "FIELD3": "Kibiti DC",
   "FIELD4": "MLANZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "210",
   "FIELD2": "Coast",
   "FIELD3": "Kibiti DC",
   "FIELD4": "MSAFIRI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "211",
   "FIELD2": "Coast",
   "FIELD3": "Kibiti DC",
   "FIELD4": "MTANGA DELTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "212",
   "FIELD2": "Coast",
   "FIELD3": "Kibiti DC",
   "FIELD4": "NYAMISATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "213",
   "FIELD2": "Coast",
   "FIELD3": "Kibiti DC",
   "FIELD4": "RUARUKE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "214",
   "FIELD2": "Coast",
   "FIELD3": "Kibiti DC",
   "FIELD4": "ZIMBWINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "215",
   "FIELD2": "Coast",
   "FIELD3": "Kisarawe DC",
   "FIELD4": "CHANZIGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "216",
   "FIELD2": "Coast",
   "FIELD3": "Kisarawe DC",
   "FIELD4": "CHOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "217",
   "FIELD2": "Coast",
   "FIELD3": "Kisarawe DC",
   "FIELD4": "GONGONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "218",
   "FIELD2": "Coast",
   "FIELD3": "Kisarawe DC",
   "FIELD4": "GWATA KISARAWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "219",
   "FIELD2": "Coast",
   "FIELD3": "Kisarawe DC",
   "FIELD4": "JANGUO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "220",
   "FIELD2": "Coast",
   "FIELD3": "Kisarawe DC",
   "FIELD4": "KIBUTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "221",
   "FIELD2": "Coast",
   "FIELD3": "Kisarawe DC",
   "FIELD4": "KIMANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "222",
   "FIELD2": "Coast",
   "FIELD3": "Kisarawe DC",
   "FIELD4": "KURUI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "223",
   "FIELD2": "Coast",
   "FIELD3": "Kisarawe DC",
   "FIELD4": "MAKURUNGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "224",
   "FIELD2": "Coast",
   "FIELD3": "Kisarawe DC",
   "FIELD4": "MANEROMANGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "225",
   "FIELD2": "Coast",
   "FIELD3": "Kisarawe DC",
   "FIELD4": "MASAKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "226",
   "FIELD2": "Coast",
   "FIELD3": "Kisarawe DC",
   "FIELD4": "MFURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "227",
   "FIELD2": "Coast",
   "FIELD3": "Kisarawe DC",
   "FIELD4": "MINAKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "228",
   "FIELD2": "Coast",
   "FIELD3": "Kisarawe DC",
   "FIELD4": "MSIMBU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "229",
   "FIELD2": "Coast",
   "FIELD3": "Kisarawe DC",
   "FIELD4": "MZENGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "230",
   "FIELD2": "Coast",
   "FIELD3": "Kisarawe DC",
   "FIELD4": "VIKUMBURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "231",
   "FIELD2": "Coast",
   "FIELD3": "Mafia DC",
   "FIELD4": "BALENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "232",
   "FIELD2": "Coast",
   "FIELD3": "Mafia DC",
   "FIELD4": "BWENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "233",
   "FIELD2": "Coast",
   "FIELD3": "Mafia DC",
   "FIELD4": "KILINDONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "234",
   "FIELD2": "Coast",
   "FIELD3": "Mafia DC",
   "FIELD4": "KIRONGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "235",
   "FIELD2": "Coast",
   "FIELD3": "Mafia DC",
   "FIELD4": "KITOMONDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "236",
   "FIELD2": "Coast",
   "FIELD3": "Mafia DC",
   "FIELD4": "MICHENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "237",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "ABDALLA H ULEGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "238",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "DUNDANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "239",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "KIIMBWANINDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "240",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "KIPARANGANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "241",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "KISIJU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "242",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "KISIJU PWANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "243",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "KISIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "244",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "KIZOMLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "245",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "LUKANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "246",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "MAGAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "247",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "MAMNDIMKONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "248",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "MITEZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "249",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "MKAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "250",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "MKIU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "251",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "MKUGILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "252",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "MWANDEGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "253",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "MWARUSEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "254",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "MWINYI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "255",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "NASIBUGANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "256",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "PANZUO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "257",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "SHUNGUBWENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "258",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "TAMBANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "259",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "TENGELEA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "260",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "VIANZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "261",
   "FIELD2": "Coast",
   "FIELD3": "Mkuranga DC",
   "FIELD4": "VIKINDU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "262",
   "FIELD2": "Coast",
   "FIELD3": "Rufiji DC",
   "FIELD4": "IKWIRIRI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "263",
   "FIELD2": "Coast",
   "FIELD3": "Rufiji DC",
   "FIELD4": "KAZAMOYO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "264",
   "FIELD2": "Coast",
   "FIELD3": "Rufiji DC",
   "FIELD4": "MBWARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "265",
   "FIELD2": "Coast",
   "FIELD3": "Rufiji DC",
   "FIELD4": "MKONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "266",
   "FIELD2": "Coast",
   "FIELD3": "Rufiji DC",
   "FIELD4": "MOHORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "267",
   "FIELD2": "Coast",
   "FIELD3": "Rufiji DC",
   "FIELD4": "MWASENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "268",
   "FIELD2": "Coast",
   "FIELD3": "Rufiji DC",
   "FIELD4": "NGORONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "269",
   "FIELD2": "Coast",
   "FIELD3": "Rufiji DC",
   "FIELD4": "UMWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "270",
   "FIELD2": "Coast",
   "FIELD3": "Rufiji DC",
   "FIELD4": "UTETE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "271",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "ABUUY JUMAA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "272",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "ARI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "273",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "AZANIA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "274",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "B W MKAPA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "275",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "BINTI MUSSA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "276",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "BUYUNI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "277",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "CHANIKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "278",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "DAR ES SALAAM",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "279",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "FURAHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "280",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "GEREZANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "281",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "HALISI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "282",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "ILALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "283",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "JAMHURI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "284",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "JANGWANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "285",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "JUHUDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "286",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala Mc",
   "FIELD4": "KASULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "287",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "KEREZANGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "288",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala Mc",
   "FIELD4": "KIMANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "289",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "KINYAMWEZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "290",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "KINYEREZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "291",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "KISUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "292",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "KISUTU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "293",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "KITONGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "294",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "KITUNDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "295",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "KIVULE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "296",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "MAGOZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "297",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "MAJANI YA CHAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "298",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "MBONDOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "299",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "MCHANGANYIKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "300",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "MCHIKICHINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "301",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "MIGOMBANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "302",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "MISITU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "303",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "MKERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "304",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "MNAZI MMOJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "305",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "MSIMBAZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "306",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "MSONGOLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "307",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "MVUTI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "308",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "MWANAGATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "309",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "NGUVU MPYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "310",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "NYEBURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "311",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "PUGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "312",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "PUGU STATION",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "313",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "SANGARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "314",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "TAMBAZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "315",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "UGOMBOLWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "316",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "ULONGONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "317",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "VINGUNGUTI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "318",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "VIWEGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "319",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "ZANAKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "320",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "ZAWADI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "321",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ilala MC",
   "FIELD4": "ZINGIZIWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "322",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kigamboni MC",
   "FIELD4": "ABOUD JUMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "TOTAL",
   "FIELD6": ""
 },
 {
   "FIELD1": "323",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kigamboni MC",
   "FIELD4": "KIBADA",
   "FIELD5": "7916525",
   "FIELD6": ""
 },
 {
   "FIELD1": "324",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kigamboni MC",
   "FIELD4": "KIBUGUMO",
   "FIELD5": "6376197",
   "FIELD6": ""
 },
 {
   "FIELD1": "325",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kigamboni MC",
   "FIELD4": "KIDETE",
   "FIELD5": "4430521",
   "FIELD6": ""
 },
 {
   "FIELD1": "326",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kigamboni MC",
   "FIELD4": "KIMBIJI",
   "FIELD5": "7549155",
   "FIELD6": ""
 },
 {
   "FIELD1": "327",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kigamboni MC",
   "FIELD4": "KISARAWE II",
   "FIELD5": "12022341",
   "FIELD6": ""
 },
 {
   "FIELD1": "328",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kigamboni MC",
   "FIELD4": "KISOTA",
   "FIELD5": "9956008",
   "FIELD6": ""
 },
 {
   "FIELD1": "329",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kigamboni MC",
   "FIELD4": "MINAZINI",
   "FIELD5": "9152739",
   "FIELD6": ""
 },
 {
   "FIELD1": "330",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kigamboni MC",
   "FIELD4": "MIZIMBINI",
   "FIELD5": "6346748",
   "FIELD6": ""
 },
 {
   "FIELD1": "331",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kigamboni MC",
   "FIELD4": "NGUVA",
   "FIELD5": "6991833",
   "FIELD6": ""
 },
 {
   "FIELD1": "332",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kigamboni MC",
   "FIELD4": "PEMBAMNAZI",
   "FIELD5": "6488745",
   "FIELD6": ""
 },
 {
   "FIELD1": "333",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kigamboni MC",
   "FIELD4": "SOMANGILA",
   "FIELD5": "5194242",
   "FIELD6": ""
 },
 {
   "FIELD1": "334",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kigamboni MC",
   "FIELD4": "TUNGI",
   "FIELD5": "8277890",
   "FIELD6": ""
 },
 {
   "FIELD1": "335",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kigamboni MC",
   "FIELD4": "VIJIBWENI",
   "FIELD5": "8931242",
   "FIELD6": ""
 },
 {
   "FIELD1": "336",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "BOKO",
   "FIELD5": "12174322",
   "FIELD6": ""
 },
 {
   "FIELD1": "337",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "BUNJU A",
   "FIELD5": "13993435",
   "FIELD6": ""
 },
 {
   "FIELD1": "338",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "HANANASIFU",
   "FIELD5": "11564939",
   "FIELD6": ""
 },
 {
   "FIELD1": "339",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "KAMBANGWA",
   "FIELD5": "16001480",
   "FIELD6": ""
 },
 {
   "FIELD1": "340",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "KAWE UKWAMANI",
   "FIELD5": "11696444",
   "FIELD6": ""
 },
 {
   "FIELD1": "341",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "KIGOGO",
   "FIELD5": "11354859",
   "FIELD6": ""
 },
 {
   "FIELD1": "342",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "KISAUKE",
   "FIELD5": "7539981",
   "FIELD6": ""
 },
 {
   "FIELD1": "343",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "KONDO",
   "FIELD5": "13094294",
   "FIELD6": ""
 },
 {
   "FIELD1": "344",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "MABWE TUMAINI",
   "FIELD5": "10983943",
   "FIELD6": ""
 },
 {
   "FIELD1": "345",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "MAENDELEO",
   "FIELD5": "6865594",
   "FIELD6": ""
 },
 {
   "FIELD1": "346",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "MAKONGO JUU",
   "FIELD5": "12424558",
   "FIELD6": ""
 },
 {
   "FIELD1": "347",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "MAKUMBUSHO",
   "FIELD5": "19281813",
   "FIELD6": ""
 },
 {
   "FIELD1": "348",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "MBEZI JUU",
   "FIELD5": "3224706",
   "FIELD6": ""
 },
 {
   "FIELD1": "349",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "MBOPO",
   "FIELD5": "4270861",
   "FIELD6": ""
 },
 {
   "FIELD1": "350",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "MBWENI",
   "FIELD5": "6810004",
   "FIELD6": ""
 },
 {
   "FIELD1": "351",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "MBWENI TETA",
   "FIELD5": "8988440",
   "FIELD6": ""
 },
 {
   "FIELD1": "352",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "MIKOCHENI",
   "FIELD5": "9947999",
   "FIELD6": ""
 },
 {
   "FIELD1": "353",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "MIVUMONI",
   "FIELD5": "6566497",
   "FIELD6": ""
 },
 {
   "FIELD1": "354",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "MTAKUJA BEACH",
   "FIELD5": "13031609",
   "FIELD6": ""
 },
 {
   "FIELD1": "355",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "MZIMUNI",
   "FIELD5": "7571279",
   "FIELD6": ""
 },
 {
   "FIELD1": "356",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "NJECHELE",
   "FIELD5": "3632892",
   "FIELD6": ""
 },
 {
   "FIELD1": "357",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "OYSTERBAY",
   "FIELD5": "12597231",
   "FIELD6": ""
 },
 {
   "FIELD1": "358",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "SALMA KIKWETE",
   "FIELD5": "16660471",
   "FIELD6": ""
 },
 {
   "FIELD1": "359",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "TURIANI",
   "FIELD5": "19177489",
   "FIELD6": ""
 },
 {
   "FIELD1": "360",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Kinondoni MC",
   "FIELD4": "TWIGA",
   "FIELD5": "11686015",
   "FIELD6": ""
 },
 {
   "FIELD1": "361",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "BARABARA YA MWINYI",
   "FIELD5": "14574320",
   "FIELD6": ""
 },
 {
   "FIELD1": "362",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "BUZA",
   "FIELD5": "15906596",
   "FIELD6": ""
 },
 {
   "FIELD1": "363",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "CHAMAZI",
   "FIELD5": "22573222",
   "FIELD6": ""
 },
 {
   "FIELD1": "364",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "CHANGANYIKENI",
   "FIELD5": "17238542",
   "FIELD6": ""
 },
 {
   "FIELD1": "365",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "CHANGOMBE",
   "FIELD5": "6438496",
   "FIELD6": ""
 },
 {
   "FIELD1": "366",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "CHARAMBE",
   "FIELD5": "21228351",
   "FIELD6": ""
 },
 {
   "FIELD1": "367",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "KEKO",
   "FIELD5": "26795042",
   "FIELD6": ""
 },
 {
   "FIELD1": "368",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "KIBASILA",
   "FIELD5": "15053890",
   "FIELD6": ""
 },
 {
   "FIELD1": "369",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "KIBASILA B",
   "FIELD5": "13703506",
   "FIELD6": ""
 },
 {
   "FIELD1": "370",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "KICHANGA",
   "FIELD5": "16067967",
   "FIELD6": ""
 },
 {
   "FIELD1": "371",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "KIJICHI",
   "FIELD5": "17520368",
   "FIELD6": ""
 },
 {
   "FIELD1": "372",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "KINGUGI",
   "FIELD5": "19185130",
   "FIELD6": ""
 },
 {
   "FIELD1": "373",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "KURASINI",
   "FIELD5": "17952882",
   "FIELD6": ""
 },
 {
   "FIELD1": "374",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "LUMO",
   "FIELD5": "16356825",
   "FIELD6": ""
 },
 {
   "FIELD1": "375",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "MALELA",
   "FIELD5": "16947923",
   "FIELD6": ""
 },
 {
   "FIELD1": "376",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "MBAGALA",
   "FIELD5": "22417883",
   "FIELD6": ""
 },
 {
   "FIELD1": "377",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "MBANDE",
   "FIELD5": "22362572",
   "FIELD6": ""
 },
 {
   "FIELD1": "378",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "MIBURANI",
   "FIELD5": "16926812",
   "FIELD6": ""
 },
 {
   "FIELD1": "379",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "MIKWAMBE",
   "FIELD5": "12795071",
   "FIELD6": ""
 },
 {
   "FIELD1": "380",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "MTONI RELINI",
   "FIELD5": "21116609",
   "FIELD6": ""
 },
 {
   "FIELD1": "381",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "MUUNGANO",
   "FIELD5": "10368059",
   "FIELD6": ""
 },
 {
   "FIELD1": "382",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "NDALALA",
   "FIELD5": "6472513",
   "FIELD6": ""
 },
 {
   "FIELD1": "383",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "NZASA",
   "FIELD5": "18399919",
   "FIELD6": ""
 },
 {
   "FIELD1": "384",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "PENDA MOYO",
   "FIELD5": "13879379",
   "FIELD6": ""
 },
 {
   "FIELD1": "385",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "SAKU",
   "FIELD5": "20928684",
   "FIELD6": ""
 },
 {
   "FIELD1": "386",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "TANDIKA",
   "FIELD5": "22096142",
   "FIELD6": ""
 },
 {
   "FIELD1": "387",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "TEMEKE",
   "FIELD5": "24390491",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "388",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "TOANGOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "389",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Temeke MC",
   "FIELD4": "WAILESI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "390",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "FAHARI GOBA B",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "391",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "GOBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "392",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "GOBA MPAKANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "393",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "GOGONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "394",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "HONDOGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "395",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "KIBAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "396",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "KIBWEGERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "397",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "KIBWEHERI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "398",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "KILUVYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "399",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "KIMARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "400",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "KINGONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "401",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "KINZUDI GOBA C",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "402",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "KWEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "403",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "LUGURUNI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "404",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "MABIBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "405",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "MAKOKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "406",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "MAKURUMLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "407",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "MALAMBAMAWILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "408",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "MANZESE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "409",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "MASHUJAA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "410",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "MATOSA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "411",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "MBEZI INN",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "412",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "MBURAHATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "413",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "MPIJI MAGOHE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "414",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "MUGABE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "415",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "SARANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "416",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "TEMBONI GVT",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "417",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "URAFIKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "418",
   "FIELD2": "Dar es Salaam",
   "FIELD3": "Ubungo MC",
   "FIELD4": "Y R MAKAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "419",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "BABAYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "420",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "BAHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "421",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "CHIBELELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "422",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "CHIKOLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "423",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "CHIKOPELO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "424",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "CHIPANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "425",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "CHONAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "426",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "IBIHWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "427",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "IBUGULE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "428",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "ILINDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "429",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "KIGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "430",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "LAMAITI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "431",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "MAGAGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "432",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "MPALANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "433",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "MPAMANTWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "434",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "MSISI JUU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "435",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "MTITAA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "436",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "MUNDEMU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "437",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "MWITIKIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "438",
   "FIELD2": "Dodoma",
   "FIELD3": "Bahi DC",
   "FIELD4": "ZANKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "439",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "BUIGIRI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "440",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "CHAMWINO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "441",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "CHILONWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "442",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "DABALO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "443",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "DR JOHN SAMWEL MALECELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "444",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "FUFU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "445",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "HANDALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "446",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "HANETI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "447",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "HUZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "448",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "IDIFU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "449",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "IGANDU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "450",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "IKOWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "451",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "ITISO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "452",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "MAILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "453",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "MAJELEKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "454",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "MAKWAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "455",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "MANCHALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "456",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "MANZASE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "457",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "MEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "458",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "MLOWA BARABARANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "459",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "MLOWA BWAWANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "460",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "MPWAYUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "461",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "MSAMALO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "462",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "MSANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "463",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "MVUMI DCT BLIND UNIT",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "464",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "MVUMI MAKULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "465",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "MVUMI MISHENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "466",
   "FIELD2": "Dodoma",
   "FIELD3": "Chamwino DC",
   "FIELD4": "SEGALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "467",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "CHANDAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "468",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "CHEMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "469",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "DALAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "470",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "FARKWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "471",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "GOIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "472",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "GWANDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "473",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "ITOLWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "474",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "JANGALO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "475",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "KELEMA BALAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "476",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "KIMAHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "477",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "KWAMTORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "478",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "LALTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "479",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "MAKORONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "480",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "MONDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "481",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "MPENDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "482",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "MRIJO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "483",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "MSAADA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "484",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "MSAKWALO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "485",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "PARANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "486",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "SANZAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "487",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "SONGOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "488",
   "FIELD2": "Dodoma",
   "FIELD3": "Chemba DC",
   "FIELD4": "SOYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "489",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "BIHAWANA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "490",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "CHIGONGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "491",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "CHIHANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "492",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "CHIKOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "493",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "CHINANGALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "494",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "DODOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "495",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "HAZINA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "496",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "HOMBOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "497",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "IHUMWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "498",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "IPALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "499",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "ITEGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "500",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "KIKOMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "501",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "KIKUYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "502",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "KISASA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "503",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "KIWANJA CHA NDEGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "504",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "KIZOTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "505",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "LUKUNDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "506",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "MAKOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "507",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "MAKUTUPORA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "508",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "MBABALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "509",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "MBALAWALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "510",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "MIYUJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "511",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "MKONZE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "512",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "MLIMWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "513",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "MNADANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "514",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "MPUNGUZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "515",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "MSALATO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "516",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "MTUMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "517",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "NALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "518",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "NGHONGHONA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "519",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "NTYUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "520",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "NZUGUNI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "521",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "SECHELELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "522",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "UMONGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "523",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "VIWANDANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "524",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "WELLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "525",
   "FIELD2": "Dodoma",
   "FIELD3": "Dodoma CC",
   "FIELD4": "ZUZU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "526",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "ABED A KARUME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "527",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "BERABERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "528",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "BEREKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "529",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "BUKULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "530",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "BUMBUTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "531",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "BUSI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "532",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "CHANGAA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "533",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "HONDOMAIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "534",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "HURUI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "535",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "IMBAFI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "536",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "INTELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "537",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "ITASWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "538",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "KALAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "539",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "KIKILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "540",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "KIKORE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "541",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "KINYASI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "542",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "KISESE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "543",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "KITEO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "544",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "KWADELO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "545",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "LOO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "546",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "MASANGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "547",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "MASAWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "548",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "R M LOWASA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "549",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "SAKAMI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "550",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa DC",
   "FIELD4": "THAWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "551",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa TC",
   "FIELD4": "BICHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "552",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa TC",
   "FIELD4": "DILAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "553",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa TC",
   "FIELD4": "GUBALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "554",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa TC",
   "FIELD4": "KOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "555",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa TC",
   "FIELD4": "KONDOA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "556",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa TC",
   "FIELD4": "KWAPAKACHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "557",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa TC",
   "FIELD4": "MTO BUBU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "558",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa TC",
   "FIELD4": "SERYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "559",
   "FIELD2": "Dodoma",
   "FIELD3": "Kondoa TC",
   "FIELD4": "ULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "560",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "BANYIBANYI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "561",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "CHIWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "562",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "HEMBAHEMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "563",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "HOGORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "564",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "IBWAGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "565",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "IDUO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "566",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "KIBAIGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "567",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "KONGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "568",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "LAIKALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "569",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "MAKAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "570",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "MANGHAILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "571",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "MANGHWETA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "572",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "MLALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "573",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "MNYAKONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "574",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "MTANANA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "575",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "MUMI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "576",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "NDALIBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "577",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "NDURUGUMI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "578",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "NGHUMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "579",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "NGOMAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "580",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "NORINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "581",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "PANDAMBILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "582",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "SAGARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "583",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "SEJELI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "584",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "SONGAMBELE KILIMANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "585",
   "FIELD2": "Dodoma",
   "FIELD3": "Kongwa DC",
   "FIELD4": "ZOISSA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "586",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "BEREGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "587",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "CHINYIKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "588",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "CHIPOGORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "589",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "CHUNYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "590",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "GODEGODE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "591",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "IHALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "592",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "IKUYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "593",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "IPERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "594",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "KIBAKWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "595",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "KIMAGAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "596",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "LUHUNDWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "597",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "MASSA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "598",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "MATOMONDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "599",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "MAZAE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "600",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "MBUGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "601",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "MIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "602",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "MOUNT IGOVU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "603",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "MPWAPWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "604",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "MTERA DAM",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "605",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "MWANAKIANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "606",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "PWAGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "607",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "RUDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "608",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "VINGHAWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "609",
   "FIELD2": "Dodoma",
   "FIELD3": "Mpwapwa DC",
   "FIELD4": "WOTTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "610",
   "FIELD2": "Geita",
   "FIELD3": "Bukombe DC",
   "FIELD4": "BUKOMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "611",
   "FIELD2": "Geita",
   "FIELD3": "Bukombe DC",
   "FIELD4": "BULEGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "612",
   "FIELD2": "Geita",
   "FIELD3": "Bukombe DC",
   "FIELD4": "BUSINDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "613",
   "FIELD2": "Geita",
   "FIELD3": "Bukombe DC",
   "FIELD4": "BUSONGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "614",
   "FIELD2": "Geita",
   "FIELD3": "Bukombe DC",
   "FIELD4": "BUSONZO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "615",
   "FIELD2": "Geita",
   "FIELD3": "Bukombe DC",
   "FIELD4": "BUTINZYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "616",
   "FIELD2": "Geita",
   "FIELD3": "Bukombe DC",
   "FIELD4": "IYOGELO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "617",
   "FIELD2": "Geita",
   "FIELD3": "Bukombe DC",
   "FIELD4": "KATENTE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "618",
   "FIELD2": "Geita",
   "FIELD3": "Bukombe DC",
   "FIELD4": "LYAMBAMGONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "619",
   "FIELD2": "Geita",
   "FIELD3": "Bukombe DC",
   "FIELD4": "MSONGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "620",
   "FIELD2": "Geita",
   "FIELD3": "Bukombe DC",
   "FIELD4": "MUSASA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "621",
   "FIELD2": "Geita",
   "FIELD3": "Bukombe DC",
   "FIELD4": "NAMONGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "622",
   "FIELD2": "Geita",
   "FIELD3": "Bukombe DC",
   "FIELD4": "RUNZEWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "623",
   "FIELD2": "Geita",
   "FIELD3": "Bukombe DC",
   "FIELD4": "USHIROMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "624",
   "FIELD2": "Geita",
   "FIELD3": "Bukombe DC",
   "FIELD4": "UYOVU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "625",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "BUHINGO CHATO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "626",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "BUSERESERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "627",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "BUTENGORUMASA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "628",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "BUZIRAYOMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "629",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "BWANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "630",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "BWERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "631",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "BWINA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "632",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "BWONGERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "633",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "CHATO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "634",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "ICHWANKIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "635",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "ILEMELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "636",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "ILYAMCHELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "637",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "IPARAMASA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "638",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "JIKOMBOE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "639",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "KACHWAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "640",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "KATENDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "641",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "KIGONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "642",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "MAGUFULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "643",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "MAKURUGUSI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "644",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "MNEKEZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "645",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "NYAMIREMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "646",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "NYARUTEMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "647",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "RUBONDO CHATO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "648",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "SUMAYE BUZIKU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "649",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "WEMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "650",
   "FIELD2": "Geita",
   "FIELD3": "Chato DC",
   "FIELD4": "ZAKIA MEGHJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "651",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "BUGALAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "652",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "BUGANDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "653",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "BUJULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "654",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "BUKOLI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "655",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "BUKONDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "656",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "BUSANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "657",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "BUSANZU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "658",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "BUTOBELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "659",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "BUTUNDWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "660",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "CHIGUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "661",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "ISINGILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "662",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "KAGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "663",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "KAKUBILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "664",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "KAMENA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "665",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "KAMHANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "666",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "KASEME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "667",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "KATORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "668",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "KILIMAHEWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "669",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "LUBANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "670",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "LUDETE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "671",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "LUTOZO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "672",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "LWAMGASA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "673",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "LWEMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "674",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "LWEZELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "675",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "MHARAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "676",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "NKOME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "677",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "NYACHILULUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "678",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "NYAKAMWAGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "679",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "NYAMALIMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "680",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "NYAMBOGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "681",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "NYAMIGOTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "682",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "NYAMWILOLELWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "683",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "NYANKONGOCHORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "684",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "NYARUGUSU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "685",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "NYARUYEYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "686",
   "FIELD2": "Geita",
   "FIELD3": "Geita DC",
   "FIELD4": "SENGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "687",
   "FIELD2": "Geita",
   "FIELD3": "Geita TC",
   "FIELD4": "BULELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "688",
   "FIELD2": "Geita",
   "FIELD3": "Geita TC",
   "FIELD4": "BUNGWANGOKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "689",
   "FIELD2": "Geita",
   "FIELD3": "Geita TC",
   "FIELD4": "GEITA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "690",
   "FIELD2": "Geita",
   "FIELD3": "Geita TC",
   "FIELD4": "IHANAMILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "691",
   "FIELD2": "Geita",
   "FIELD3": "Geita TC",
   "FIELD4": "KALANGALALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "692",
   "FIELD2": "Geita",
   "FIELD3": "Geita TC",
   "FIELD4": "KASAMWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "693",
   "FIELD2": "Geita",
   "FIELD3": "Geita TC",
   "FIELD4": "KIVUKONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "694",
   "FIELD2": "Geita",
   "FIELD3": "Geita TC",
   "FIELD4": "LUKARANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "695",
   "FIELD2": "Geita",
   "FIELD3": "Geita TC",
   "FIELD4": "MWATULOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "696",
   "FIELD2": "Geita",
   "FIELD3": "Geita TC",
   "FIELD4": "NYANKUMBU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "697",
   "FIELD2": "Geita",
   "FIELD3": "Geita TC",
   "FIELD4": "NYANZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "698",
   "FIELD2": "Geita",
   "FIELD3": "Geita TC",
   "FIELD4": "SHANTAMINE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "699",
   "FIELD2": "Geita",
   "FIELD3": "Mbogwe DC",
   "FIELD4": "IKOBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "700",
   "FIELD2": "Geita",
   "FIELD3": "Mbogwe DC",
   "FIELD4": "IKUNGUIGAZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "701",
   "FIELD2": "Geita",
   "FIELD3": "Mbogwe DC",
   "FIELD4": "ILOLANGULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "702",
   "FIELD2": "Geita",
   "FIELD3": "Mbogwe DC",
   "FIELD4": "IPONYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "703",
   "FIELD2": "Geita",
   "FIELD3": "Mbogwe DC",
   "FIELD4": "ISANGIJO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "704",
   "FIELD2": "Geita",
   "FIELD3": "Mbogwe DC",
   "FIELD4": "KANEGERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "705",
   "FIELD2": "Geita",
   "FIELD3": "Mbogwe DC",
   "FIELD4": "LUGUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "706",
   "FIELD2": "Geita",
   "FIELD3": "Mbogwe DC",
   "FIELD4": "LULEMBELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "707",
   "FIELD2": "Geita",
   "FIELD3": "Mbogwe DC",
   "FIELD4": "MASUMBWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "708",
   "FIELD2": "Geita",
   "FIELD3": "Mbogwe DC",
   "FIELD4": "MBOGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "709",
   "FIELD2": "Geita",
   "FIELD3": "Mbogwe DC",
   "FIELD4": "NHOMOLWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "710",
   "FIELD2": "Geita",
   "FIELD3": "Mbogwe DC",
   "FIELD4": "NYAKASALUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "711",
   "FIELD2": "Geita",
   "FIELD3": "Mbogwe DC",
   "FIELD4": "NYASATO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "712",
   "FIELD2": "Geita",
   "FIELD3": "Nyanghwale DC",
   "FIELD4": "BUKWIMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "713",
   "FIELD2": "Geita",
   "FIELD3": "Nyanghwale DC",
   "FIELD4": "BUSOLWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "714",
   "FIELD2": "Geita",
   "FIELD3": "Nyanghwale DC",
   "FIELD4": "IZUNYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "715",
   "FIELD2": "Geita",
   "FIELD3": "Nyanghwale DC",
   "FIELD4": "KAFITA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "716",
   "FIELD2": "Geita",
   "FIELD3": "Nyanghwale DC",
   "FIELD4": "KAKORA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "717",
   "FIELD2": "Geita",
   "FIELD3": "Nyanghwale DC",
   "FIELD4": "MSALALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "718",
   "FIELD2": "Geita",
   "FIELD3": "Nyanghwale DC",
   "FIELD4": "MWINGIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "719",
   "FIELD2": "Geita",
   "FIELD3": "Nyanghwale DC",
   "FIELD4": "NYANGHWALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "720",
   "FIELD2": "Geita",
   "FIELD3": "Nyanghwale DC",
   "FIELD4": "NYIJUNDU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "721",
   "FIELD2": "Geita",
   "FIELD3": "Nyanghwale DC",
   "FIELD4": "NYUGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "722",
   "FIELD2": "Geita",
   "FIELD3": "Nyanghwale DC",
   "FIELD4": "SHABAKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "723",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "DIMITRIOS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "724",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "FURAHIA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "725",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "IDODI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "726",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "IFUNDA GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "727",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "IFUNDA TECH",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "728",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "ILAMBILOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "729",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "ISIMILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "730",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "ISMANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "731",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "KALENGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "732",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "KIDAMALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "733",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "KIMAIGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "734",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "KIPONZELO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "735",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "KIWELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "736",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "LIPULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "737",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "LUHOTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "738",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "LUMULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "739",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "LYANDEMBELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "740",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "LYASA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "741",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "MGAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "742",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "MLOWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "743",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "MSEKE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "744",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "MUHWANA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "745",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "NYANGORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "746",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "NYERERE MIGOLI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "747",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "PAWAGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "748",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "TOSAMAGANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "749",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "WASA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "750",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa DC",
   "FIELD4": "WILLIAM LUKUVI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "751",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa MC",
   "FIELD4": "IPOGOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "752",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa MC",
   "FIELD4": "IRINGA GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "753",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa MC",
   "FIELD4": "KIHESA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "754",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa MC",
   "FIELD4": "KLERRUU MAZOEZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "755",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa MC",
   "FIELD4": "KWAKILOSA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "756",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa MC",
   "FIELD4": "LUGALO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "757",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa MC",
   "FIELD4": "MAWELEWELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "758",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa MC",
   "FIELD4": "MIYOMBONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "759",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa MC",
   "FIELD4": "MKWAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "760",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa MC",
   "FIELD4": "MLAMKE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "761",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa MC",
   "FIELD4": "MLANDEGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "762",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa MC",
   "FIELD4": "MTWIVILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "763",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa MC",
   "FIELD4": "NDULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "764",
   "FIELD2": "Iringa",
   "FIELD3": "Iringa MC",
   "FIELD4": "TAGAMENDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "765",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "DABAGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "766",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "IBUMU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "767",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "ILULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "768",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "IPETA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "769",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "IROLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "770",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "KIHEKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "771",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "KILOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "772",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "KITOWO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "773",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "LUKOSI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "774",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "LULANZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "775",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "LUNDAMATWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "776",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "MADEGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "777",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "MAKWEMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "778",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "MASISIWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "779",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "MAWAMBALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "780",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "MAZOMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "781",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "MLAFU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "782",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "MTITU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "783",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "NGANGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "784",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "NYALUMBU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "785",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "NYANZWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "786",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "SELEBU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "787",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "UDEKWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "788",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "UDZUNGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "789",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "UHAMBINGETO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "790",
   "FIELD2": "Iringa",
   "FIELD3": "Kilolo DC",
   "FIELD4": "UKWEGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "791",
   "FIELD2": "Iringa",
   "FIELD3": "Mafinga TC",
   "FIELD4": "BUMILAYINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "792",
   "FIELD2": "Iringa",
   "FIELD3": "Mafinga TC",
   "FIELD4": "CHANGARAWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "793",
   "FIELD2": "Iringa",
   "FIELD3": "Mafinga TC",
   "FIELD4": "IHONGOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "794",
   "FIELD2": "Iringa",
   "FIELD3": "Mafinga TC",
   "FIELD4": "ISALAVANU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "795",
   "FIELD2": "Iringa",
   "FIELD3": "Mafinga TC",
   "FIELD4": "J J MUNGAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "796",
   "FIELD2": "Iringa",
   "FIELD3": "Mafinga TC",
   "FIELD4": "KINYANAMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "797",
   "FIELD2": "Iringa",
   "FIELD3": "Mafinga TC",
   "FIELD4": "LUGANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "798",
   "FIELD2": "Iringa",
   "FIELD3": "Mafinga TC",
   "FIELD4": "MNYIGUMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "799",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "IDETERO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "800",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "IDUNDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "801",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "IFWAGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "802",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "IGOMBAVANU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "803",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "IGOWOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "804",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "IHALIMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "805",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "IHANU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "806",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "IHOWANZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "807",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "ILOGOMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "808",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "ILONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "809",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "ITANDULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "810",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "ITENGULE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "811",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "ITONA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "812",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "KASANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "813",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "KIBAO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "814",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "KIBENGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "815",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "KIHANSI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "816",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "KINGEGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "817",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "KIYOWELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "818",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "LUHUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "819",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "MADUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "820",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "MAKUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "821",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "MALANGALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "822",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "MBALAMAZIWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "823",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "MDABULO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "824",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "MGALO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "825",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "MGOLOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "826",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "MKALALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "827",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "MNINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "828",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "MTAMBULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "829",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "NYOLOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "830",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "NZIVI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "831",
   "FIELD2": "Iringa",
   "FIELD3": "Mufindi DC",
   "FIELD4": "SADANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "832",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "BIHARAMULO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "833",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "BISIBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "834",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "BIZIMYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "835",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "KAGANGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "836",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "KALENGE DAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "837",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "KATAHOKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "838",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "LUSHAUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "839",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "MUBABA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "840",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "NEMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "841",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "NYABUSOZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "842",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "NYAKAHURA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "843",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "NYAMAHANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "844",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "NYAMIGOGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "845",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "NYANTAKARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "846",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "RUBONDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "847",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "RUNAZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "848",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "RUZIBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "849",
   "FIELD2": "Kagera",
   "FIELD3": "Biharamulo DC",
   "FIELD4": "RWAGATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "850",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "BUJUGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "851",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "BUJUNANGOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "852",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "BUKARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "853",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "BUSILIKYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "854",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "BUTULAGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "855",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "IZIMBYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "856",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "KAAGYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "857",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "KABALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "858",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "KABUGARO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "859",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "KAIBANJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "860",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "KALEMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "861",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "KARABAGAINE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "862",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "KARAMAGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "863",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "KASHOZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "864",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "KATALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "865",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "KATOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "866",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "KATORO DAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "867",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "KEMONDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "868",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "KIBIRIZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "869",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "KIKOMELO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "870",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "KISHOGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "871",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "KYAMULAILE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "872",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "LYAMAHORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "873",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "MARUKU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "874",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "MWEMAGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "875",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "NYAKATO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "876",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "NYAKIBIMBILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "877",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "RUBALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "878",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "RUHUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "879",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba DC",
   "FIELD4": "TUNAMKUMBUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "880",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "BAKOBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "881",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "BILELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "882",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "BUHEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "883",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "BUKOBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "884",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "HAMUGEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "885",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "IHUNGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "886",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "IJUGANYONDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "887",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "KAGEMU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "888",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "KAHORORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "889",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "KASHAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "890",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "KIBETA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "891",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "MUGEZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "892",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "NSHAMBYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "893",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "NYANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "894",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "OMUMWANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "895",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "RUGAMBWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "896",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "RUMULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "897",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "RUTUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "898",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "RWAMISHENYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "899",
   "FIELD2": "Kagera",
   "FIELD3": "Bukoba MC",
   "FIELD4": "RWAZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "900",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "BUGENE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "901",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "CHABALISA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "902",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "CHAKARURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "903",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "IGURWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "904",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "IHEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "905",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "KAWELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "906",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "KAYANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "907",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "KIHANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "908",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "KIRURUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "909",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "KITUNTU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "910",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "NDAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "911",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "NONO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "912",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "NYABIYONZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "913",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "NYAKAHANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "914",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "NYAKASIMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "915",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "RUGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "916",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "RUHINDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "917",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "RUICHO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "918",
   "FIELD2": "Kagera",
   "FIELD3": "Karagwe DC",
   "FIELD4": "RWAMBAIZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "919",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "BUGOMORA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "920",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "BUSINDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "921",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "CHANYANGABWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "922",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "CHITWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "923",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "IBANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "924",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "ISINGIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "925",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "KAMULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "926",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "KIMULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "927",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "KITWECHENKURA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "928",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "KYERWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "929",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "MABIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "930",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "MUKIRE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "931",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "MURONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "932",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "NAKAKE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "933",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "NKWENDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "934",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "NTARE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "935",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "NYABISHENGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "936",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "NYAMILIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "937",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "NYAMIYAGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "938",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "RUKURAIJO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "939",
   "FIELD2": "Kagera",
   "FIELD3": "Kyerwa DC",
   "FIELD4": "SONGAMBELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "940",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "BUGANDIKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "941",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "BUNAZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "942",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "BUYANGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "943",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "BWABUKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "944",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "BWANJAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "945",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "GABULANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "946",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "GERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "947",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "KAGERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "948",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "KAKUNYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "949",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "KASHENYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "950",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "KIGARAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "951",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "KIKUKWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "952",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "KILIMILILE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "953",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "KYAKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "954",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "LUGOYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "955",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "MABALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "956",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "MINZIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "957",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "MUTUKULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "958",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "NKENGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "959",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "NSUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "960",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "RUZINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": "TOTAL"
 },
 {
   "FIELD1": "961",
   "FIELD2": "Kagera",
   "FIELD3": "Missenyi DC",
   "FIELD4": "RWEMONDO",
   "FIELD5": "",
   "FIELD6": "3115275"
 },
 {
   "FIELD1": "962",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "ANNA TIBAIJUKA",
   "FIELD5": "",
   "FIELD6": "5599551"
 },
 {
   "FIELD1": "963",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "BIIRABO",
   "FIELD5": "",
   "FIELD6": "5446898"
 },
 {
   "FIELD1": "964",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "BUJUMBA",
   "FIELD5": "",
   "FIELD6": "5366498"
 },
 {
   "FIELD1": "965",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "BULYAKASHAJU",
   "FIELD5": "",
   "FIELD6": "4516079"
 },
 {
   "FIELD1": "966",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "BUMBIRE",
   "FIELD5": "",
   "FIELD6": "2862391"
 },
 {
   "FIELD1": "967",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "BUNYAGONGO",
   "FIELD5": "",
   "FIELD6": "4132464"
 },
 {
   "FIELD1": "968",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "BUREZA",
   "FIELD5": "",
   "FIELD6": "5880604"
 },
 {
   "FIELD1": "969",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "BURUNGURA",
   "FIELD5": "",
   "FIELD6": "4236863"
 },
 {
   "FIELD1": "970",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "GWANSELI",
   "FIELD5": "",
   "FIELD6": "6471651"
 },
 {
   "FIELD1": "971",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "IBUGA",
   "FIELD5": "",
   "FIELD6": "7823542"
 },
 {
   "FIELD1": "972",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "IJUMBI",
   "FIELD5": "",
   "FIELD6": "9104170"
 },
 {
   "FIELD1": "973",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "IKONDO",
   "FIELD5": "",
   "FIELD6": "6107119"
 },
 {
   "FIELD1": "974",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "ITONGO",
   "FIELD5": "",
   "FIELD6": "6106409"
 },
 {
   "FIELD1": "975",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "IZIGO",
   "FIELD5": "",
   "FIELD6": "8439920"
 },
 {
   "FIELD1": "976",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "JOYCE NDALICHAKO",
   "FIELD5": "",
   "FIELD6": "3316612"
 },
 {
   "FIELD1": "977",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "KABIRIZI",
   "FIELD5": "",
   "FIELD6": "4357128"
 },
 {
   "FIELD1": "978",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "KAGOMA",
   "FIELD5": "",
   "FIELD6": "7716063"
 },
 {
   "FIELD1": "979",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "KAGONDO",
   "FIELD5": "",
   "FIELD6": "3700266"
 },
 {
   "FIELD1": "980",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "KAIGARA",
   "FIELD5": "",
   "FIELD6": "6942243"
 },
 {
   "FIELD1": "981",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "KAMACHUMU",
   "FIELD5": "",
   "FIELD6": "5049737"
 },
 {
   "FIELD1": "982",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "KANYERANYERE",
   "FIELD5": "",
   "FIELD6": "9077179"
 },
 {
   "FIELD1": "983",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "KARAMBI",
   "FIELD5": "",
   "FIELD6": "6698736"
 },
 {
   "FIELD1": "984",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "KASHARUNGA",
   "FIELD5": "",
   "FIELD6": "9737400"
 },
 {
   "FIELD1": "985",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "KIBANGA",
   "FIELD5": "",
   "FIELD6": "5016690"
 },
 {
   "FIELD1": "986",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "KIHUMULO",
   "FIELD5": "",
   "FIELD6": "4894055"
 },
 {
   "FIELD1": "987",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "KIMWANI",
   "FIELD5": "",
   "FIELD6": "7750390"
 },
 {
   "FIELD1": "988",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "KISHANDA",
   "FIELD5": "",
   "FIELD6": "11975507"
 },
 {
   "FIELD1": "989",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "KISHOJU",
   "FIELD5": "",
   "FIELD6": "11723627"
 },
 {
   "FIELD1": "990",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "MAYONDWE",
   "FIELD5": "",
   "FIELD6": "3465274"
 },
 {
   "FIELD1": "991",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "MUBUKA",
   "FIELD5": "",
   "FIELD6": "14466410"
 },
 {
   "FIELD1": "992",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "NGENGE",
   "FIELD5": "",
   "FIELD6": "5172941"
 },
 {
   "FIELD1": "993",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "NSHAMBA",
   "FIELD5": "",
   "FIELD6": "6552761"
 },
 {
   "FIELD1": "994",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "NYAILIGAMBA",
   "FIELD5": "",
   "FIELD6": "10226362"
 },
 {
   "FIELD1": "995",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "NYAKABANGO",
   "FIELD5": "",
   "FIELD6": "4600027"
 },
 {
   "FIELD1": "996",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "NYAKATANGA",
   "FIELD5": "",
   "FIELD6": "10144077"
 },
 {
   "FIELD1": "997",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "RUHANGA",
   "FIELD5": "",
   "FIELD6": "8517811"
 },
 {
   "FIELD1": "998",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "RUKINDO",
   "FIELD5": "",
   "FIELD6": "7923064"
 },
 {
   "FIELD1": "999",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "RULONGO",
   "FIELD5": "",
   "FIELD6": "6603092"
 },
 {
   "FIELD1": "1000",
   "FIELD2": "Kagera",
   "FIELD3": "Muleba DC",
   "FIELD4": "RUTABO",
   "FIELD5": "",
   "FIELD6": "9747785"
 },
 {
   "FIELD1": "1001",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "BUKIRIRO",
   "FIELD5": "",
   "FIELD6": "3492644"
 },
 {
   "FIELD1": "1002",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "KABANGA",
   "FIELD5": "",
   "FIELD6": "11343376"
 },
 {
   "FIELD1": "1003",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "KANAZI",
   "FIELD5": "",
   "FIELD6": "5702152"
 },
 {
   "FIELD1": "1004",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "KEZA",
   "FIELD5": "",
   "FIELD6": "2039242"
 },
 {
   "FIELD1": "1005",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "KIBIMBA",
   "FIELD5": "",
   "FIELD6": "5141073"
 },
 {
   "FIELD1": "1006",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "KIBOGORA",
   "FIELD5": "",
   "FIELD6": "3888285"
 },
 {
   "FIELD1": "1007",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "KIRUSHYA",
   "FIELD5": "",
   "FIELD6": "3358555"
 },
 {
   "FIELD1": "1008",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "LUKOLE",
   "FIELD5": "",
   "FIELD6": "7975431"
 },
 {
   "FIELD1": "1009",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "MABAWE",
   "FIELD5": "",
   "FIELD6": "5959673"
 },
 {
   "FIELD1": "1010",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "MUGANZA",
   "FIELD5": "",
   "FIELD6": "3063715"
 },
 {
   "FIELD1": "1011",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "MUGOMA",
   "FIELD5": "",
   "FIELD6": "5977996"
 },
 {
   "FIELD1": "1012",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "MURGWANZA",
   "FIELD5": "",
   "FIELD6": "7417333"
 },
 {
   "FIELD1": "1013",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "MURUSAGAMBA",
   "FIELD5": "",
   "FIELD6": "6527959"
 },
 {
   "FIELD1": "1014",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "MURUVYAGIRA",
   "FIELD5": "",
   "FIELD6": "1911969"
 },
 {
   "FIELD1": "1015",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "MUYENZI",
   "FIELD5": "",
   "FIELD6": "9130401"
 },
 {
   "FIELD1": "1016",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "NDOMBA",
   "FIELD5": "",
   "FIELD6": "5622081"
 },
 {
   "FIELD1": "1017",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "NGARA",
   "FIELD5": "",
   "FIELD6": "7718280"
 },
 {
   "FIELD1": "1018",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "NGARA HIGH",
   "FIELD5": "- ",
   "FIELD6": "497664"
 },
 {
   "FIELD1": "1019",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "NTOBEYE",
   "FIELD5": "",
   "FIELD6": "3631992"
 },
 {
   "FIELD1": "1020",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "NYABISINDU",
   "FIELD5": "",
   "FIELD6": "2428965"
 },
 {
   "FIELD1": "1021",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "NYAKISASA",
   "FIELD5": "",
   "FIELD6": "4532742"
 },
 {
   "FIELD1": "1022",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "NYAMIAGA",
   "FIELD5": "- ",
   "FIELD6": "1077009"
 },
 {
   "FIELD1": "1023",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "RUSUMO",
   "FIELD5": "",
   "FIELD6": "7118129"
 },
 {
   "FIELD1": "1024",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "RUSUMO B",
   "FIELD5": "- ",
   "FIELD6": "4240533"
 },
 {
   "FIELD1": "1025",
   "FIELD2": "Kagera",
   "FIELD3": "Ngara DC",
   "FIELD4": "SHUNGA",
   "FIELD5": "",
   "FIELD6": "6342148"
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1026",
   "FIELD2": "Katavi",
   "FIELD3": "Mlele DC",
   "FIELD4": "ILELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1027",
   "FIELD2": "Katavi",
   "FIELD3": "Mlele DC",
   "FIELD4": "INYONGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1028",
   "FIELD2": "Katavi",
   "FIELD3": "Mlele DC",
   "FIELD4": "UTENDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1029",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda DC",
   "FIELD4": "BULAMATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1030",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda DC",
   "FIELD4": "IKOLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1031",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda DC",
   "FIELD4": "ILANDAMILUMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1032",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda DC",
   "FIELD4": "ILANGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1033",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda DC",
   "FIELD4": "KABUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1034",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda DC",
   "FIELD4": "KAREMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1035",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda DC",
   "FIELD4": "MAZWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1036",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda DC",
   "FIELD4": "MISHAMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1037",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda DC",
   "FIELD4": "MPANDANDOGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1038",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda DC",
   "FIELD4": "MWESE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1039",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda DC",
   "FIELD4": "SIBWESA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1040",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda MC",
   "FIELD4": "KASHAULILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1041",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda MC",
   "FIELD4": "KASIMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1042",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda MC",
   "FIELD4": "KASOKOLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1043",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda MC",
   "FIELD4": "MAGAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1044",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda MC",
   "FIELD4": "MISUNKUMILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1045",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda MC",
   "FIELD4": "MPANDA GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1046",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda MC",
   "FIELD4": "MWANGAZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1047",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda MC",
   "FIELD4": "NSEMULWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1048",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda MC",
   "FIELD4": "RUNGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1049",
   "FIELD2": "Katavi",
   "FIELD3": "Mpanda MC",
   "FIELD4": "SHANWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1050",
   "FIELD2": "Katavi",
   "FIELD3": "Mpimbwe DC",
   "FIELD4": "MAJIMOTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1051",
   "FIELD2": "Katavi",
   "FIELD3": "Mpimbwe DC",
   "FIELD4": "MAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1052",
   "FIELD2": "Katavi",
   "FIELD3": "Mpimbwe DC",
   "FIELD4": "MBEDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1053",
   "FIELD2": "Katavi",
   "FIELD3": "Mpimbwe DC",
   "FIELD4": "MIZENGO PINDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1054",
   "FIELD2": "Katavi",
   "FIELD3": "Mpimbwe DC",
   "FIELD4": "USEVYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1055",
   "FIELD2": "Katavi",
   "FIELD3": "Nsimbo DC",
   "FIELD4": "KANOGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1056",
   "FIELD2": "Katavi",
   "FIELD3": "Nsimbo DC",
   "FIELD4": "KATUMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1057",
   "FIELD2": "Katavi",
   "FIELD3": "Nsimbo DC",
   "FIELD4": "KENSWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1058",
   "FIELD2": "Katavi",
   "FIELD3": "Nsimbo DC",
   "FIELD4": "MACHIMBONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1059",
   "FIELD2": "Katavi",
   "FIELD3": "Nsimbo DC",
   "FIELD4": "MTAPENDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1060",
   "FIELD2": "Katavi",
   "FIELD3": "Nsimbo DC",
   "FIELD4": "NSIMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1061",
   "FIELD2": "Katavi",
   "FIELD3": "Nsimbo DC",
   "FIELD4": "SITALIKE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1062",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "BUHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1063",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "BUYENZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1064",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "BWAFUMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1065",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "JANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1066",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "KAHUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1067",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "KIBWIGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1068",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "MANYOVU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1069",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "MKATANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1070",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "MKOZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1071",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "MUHARULO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1072",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "MUHINDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1073",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "MUNANILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1074",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "MUNZEZE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1075",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "MUYAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1076",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "NYAKIMUE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1077",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "NYAMILAMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1078",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "NYARUBOZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1079",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "RUSABA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1080",
   "FIELD2": "Kigoma",
   "FIELD3": "Buhigwe DC",
   "FIELD4": "YANZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1081",
   "FIELD2": "Kigoma",
   "FIELD3": "Kakonko DC",
   "FIELD4": "BUYUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1082",
   "FIELD2": "Kigoma",
   "FIELD3": "Kakonko DC",
   "FIELD4": "GWANUMPU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1083",
   "FIELD2": "Kigoma",
   "FIELD3": "Kakonko DC",
   "FIELD4": "KAKONKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1084",
   "FIELD2": "Kigoma",
   "FIELD3": "Kakonko DC",
   "FIELD4": "KANYONZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1085",
   "FIELD2": "Kigoma",
   "FIELD3": "Kakonko DC",
   "FIELD4": "KASANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1086",
   "FIELD2": "Kigoma",
   "FIELD3": "Kakonko DC",
   "FIELD4": "KASHOZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1087",
   "FIELD2": "Kigoma",
   "FIELD3": "Kakonko DC",
   "FIELD4": "MUGUNZU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1088",
   "FIELD2": "Kigoma",
   "FIELD3": "Kakonko DC",
   "FIELD4": "MUHANGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1089",
   "FIELD2": "Kigoma",
   "FIELD3": "Kakonko DC",
   "FIELD4": "NYAMTUKUZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1090",
   "FIELD2": "Kigoma",
   "FIELD3": "Kakonko DC",
   "FIELD4": "RUGENGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1091",
   "FIELD2": "Kigoma",
   "FIELD3": "Kakonko DC",
   "FIELD4": "SHUHUDIA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1092",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "ASANTE NYERERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1093",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "KABAGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1094",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "KASANGEZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1095",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "KIHENYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1096",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "KIMENYI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1097",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "KIMWANYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1098",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "KINYAKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1099",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "KITANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1100",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "KURUNYEMI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1101",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "MAKERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1102",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "MOYOVOZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1103",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "NKUNDUTSI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1104",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "NTAMYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1105",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "NYAKITONTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1106",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "RUNGWE MPYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1107",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "RUSESA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1108",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "TITYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1109",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu DC",
   "FIELD4": "ZEZE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1110",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu TC",
   "FIELD4": "BOGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1111",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu TC",
   "FIELD4": "HWAZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1112",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu TC",
   "FIELD4": "KASANGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1113",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu TC",
   "FIELD4": "KIGODYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1114",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu TC",
   "FIELD4": "KIGOMA GRAND",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1115",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu TC",
   "FIELD4": "KINKATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1116",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu TC",
   "FIELD4": "MUBONDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1117",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu TC",
   "FIELD4": "MUHUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1118",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu TC",
   "FIELD4": "MUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1119",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu TC",
   "FIELD4": "MURUBONA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1120",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu TC",
   "FIELD4": "MURUFITI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1121",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu TC",
   "FIELD4": "MWIBUYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1122",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu TC",
   "FIELD4": "NYANSHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1123",
   "FIELD2": "Kigoma",
   "FIELD3": "Kasulu TC",
   "FIELD4": "NYUMBIGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1124",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "BITURANA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1125",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "BUSAGARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1126",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "BUSAMI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1127",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "ITABA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1128",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "KIBONDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1129",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "KUMGOGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1130",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "KUMWAMBU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1131",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "MALAGARASI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1132",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "MIGEZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1133",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "MISEZERO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1134",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "MKUGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1135",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "MOUNT SAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1136",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "MOYOWOSI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1137",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "MUGOMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1138",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "MURAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1139",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "MURUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1140",
   "FIELD2": "Kigoma",
   "FIELD3": "Kibondo DC",
   "FIELD4": "RUBANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1141",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "AMAHORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1142",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "BITALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1143",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "BUGAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1144",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "KAGONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1145",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "KALINZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1146",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "KASEKE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1147",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "KIDAHWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1148",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "LUICHE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1149",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "MATYAZO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1150",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "MGAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1151",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "MKABOGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1152",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "MKIGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1153",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "MKONGORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1154",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "MKUTI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1155",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "MUNGONYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1156",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "MWANDIGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1157",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "NYAMUHOZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1158",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "NYARUBANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1159",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma DC",
   "FIELD4": "ZASHE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1160",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "BUHANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1161",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "BURONGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1162",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "BUSHABANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1163",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "BUTEKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1164",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "GUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1165",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "KASIMBU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1166",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "KASINGIRIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1167",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "KATUBUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1168",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "KICHANGACHUI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1169",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "KIGOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1170",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "KIRUGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1171",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "KITONGONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1172",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "KITWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1173",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "MASANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1174",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "MLOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1175",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "MWANANCHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1176",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "RUBUGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1177",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "RUSIMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1178",
   "FIELD2": "Kigoma",
   "FIELD3": "Kigoma MC",
   "FIELD4": "WAKULIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1179",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "BASANZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1180",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "BUHINGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1181",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "HEREMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1182",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "ILAGALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1183",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "ITEBULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1184",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "KALENGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1185",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "KALYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1186",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "KANDAGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1187",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "LAGOSA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1188",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "LUGUFU BOYS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1189",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "LUGUFU GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1190",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "MAZUNGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1191",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "MGANZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1192",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "MWAKIZEGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1193",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "NGURUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1194",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "NYAMAGOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1195",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "RUCHUGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1196",
   "FIELD2": "Kigoma",
   "FIELD3": "Uvinza DC",
   "FIELD4": "SUNUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1197",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "BOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1198",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "HAI DAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1199",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "HARAMBEE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1200",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "KIA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1201",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "KIKAFU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1202",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "KISELU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1203",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "KYUU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1204",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "LEMIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1205",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "LERAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1206",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "LONGOI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1207",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "LUKANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1208",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "LYAMUNGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1209",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "LYASIKIKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1210",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "MACHAME GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1211",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "MAILISITA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1212",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "MARIRE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1213",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "MUKWASA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1214",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "NEEMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1215",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "NGUNI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1216",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "NKOKASHU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1217",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "NKUU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1218",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "NKWAMWASI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1219",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "ROO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1220",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "RUNDUGAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1221",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "SAWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1222",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "TUMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1223",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "TUMONA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1224",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "UDORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1225",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Hai DC",
   "FIELD4": "UDURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1226",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "ASHIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1227",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "CYRIL CHAMI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1228",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "DARAJANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1229",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "GHONA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1230",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "HIMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1231",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "IFATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1232",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "IWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1233",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "KILIMANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1234",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "KIMOCHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1235",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "KINDI KATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1236",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "KIRIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1237",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "KISAM",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1238",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "KISARIKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1239",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "KISULUNI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1240",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "KOKIRIE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1241",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "KOMAKYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1242",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "LANGASANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1243",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "LYAKIRIMU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1244",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MABOGINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1245",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MAKOMU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1246",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MAMBA DAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1247",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MANGI MAREALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1248",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MANGI SABASI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1249",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MANGI SINA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1250",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MANGOTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1251",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MANUSHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1252",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MARINGENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1253",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MARLEX",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1254",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MASHINGIA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1255",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MASOKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1256",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MATALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1257",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MAWELLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1258",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MBOKOMU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1259",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MBONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1260",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MELI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1261",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MIERESINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1262",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MKOMBOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1263",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MLANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1264",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MNINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1265",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MPIRANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1266",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MRERENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1267",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MRUWIA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1268",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MSIRIWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1269",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MUUNGANO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1270",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "MWIKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1271",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "OKAONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1272",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "ORIA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1273",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "PAKULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1274",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "RASESA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1275",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "RUKIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1276",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "SAKAYO MOSHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1277",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "SHIMBWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1278",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "SOMSOM",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1279",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "SUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1280",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "TEMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1281",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "TPC",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1282",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "UMBWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1283",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "UPARO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1284",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi DC",
   "FIELD4": "WERUWERU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1285",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi MC",
   "FIELD4": "ANNA MKAPA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1286",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi MC",
   "FIELD4": "J K NYERERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1287",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi MC",
   "FIELD4": "KARANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1288",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi MC",
   "FIELD4": "KIBORLONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1289",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi MC",
   "FIELD4": "KIUSA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1290",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi MC",
   "FIELD4": "KORONGONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1291",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi MC",
   "FIELD4": "MAWENZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1292",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi MC",
   "FIELD4": "MJI MPYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1293",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi MC",
   "FIELD4": "MOSHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1294",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi MC",
   "FIELD4": "MOSHI UFUNDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1295",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi MC",
   "FIELD4": "MSARANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1296",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi MC",
   "FIELD4": "MSASANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1297",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi MC",
   "FIELD4": "RAU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1298",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Moshi MC",
   "FIELD4": "REGNALD MENGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1299",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "CHAANGAJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1300",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "DR ASHAROSE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1301",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "JIPE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1302",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "KAMWALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1303",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "KIFARU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1304",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "KIGHARE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1305",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "KIGONIGONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1306",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "KILEO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1307",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "KILOBENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1308",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "KIRYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1309",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "KISANGARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1310",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "KISHENGWENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1311",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "KWANGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1312",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "LANGATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1313",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "MAGHARE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1314",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "MANDAKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1315",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "MGAGAO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1316",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "MSANGENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1317",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "NDORWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1318",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "NGUJINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1319",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "NYERERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1320",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "SIMBOMU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1321",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "UBANGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1322",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "USANGI DAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1323",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Mwanga DC",
   "FIELD4": "VUDOI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1324",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "ALENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1325",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "BOONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1326",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "BUSTANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1327",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "HOLILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1328",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "HOROMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1329",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "KAHEUSSERI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1330",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "KELAMFUA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1331",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "KENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1332",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "KILAMACHO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1333",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "KIRACHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1334",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "KIRONGOCHINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1335",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "KISALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1336",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "KWAIKURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1337",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "KWALAKAMU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1338",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "MAHIDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1339",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "MAKALEMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1340",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "MAKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1341",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "MAKIIDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1342",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "MAMSERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1343",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "MASHATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1344",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "MATOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1345",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "MAWANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1346",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "MBOMAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1347",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "MEMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1348",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "MENGENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1349",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "MKUU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1350",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "MLAMBAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1351",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "MOTAMBURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1352",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "MRAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1353",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "MRAOKERYO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1354",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "NANJARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1355",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "NDUWENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1356",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "NGALEKU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1357",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "NGARENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1358",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "OLELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1359",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "SHIMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1360",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "TANYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1361",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "TARAKEA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1362",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "UBAA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1363",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "UMARINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1364",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Rombo DC",
   "FIELD4": "URAURI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1365",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "BANGALALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1366",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "BEMKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1367",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "BOMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1368",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "CHALAO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1369",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "CHANJAGAA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1370",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "CHAUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1371",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "GONJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1372",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "KASEMPOMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1373",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "KAZITA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1374",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "KIBACHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1375",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "KIGANGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1376",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "KIHURIO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1377",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "KIMALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1378",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "KIRANGARE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1379",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "KISIWANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1380",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "KWAKOKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1381",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "KWAMBEGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1382",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "KWIZU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1383",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "LUGULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1384",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "MABILIONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1385",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "MADIVENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1386",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "MAKANYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1387",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "MALINDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1388",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "MANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1389",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "MASHEKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1390",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "MKOMBOZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1391",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "MOIPO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1392",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "MTII",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1393",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "MVUREKONGEI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1394",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "MYAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1395",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "NDUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1396",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "NJORO MIGHARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1397",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "NTENGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1398",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "PARENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1399",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "SAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1400",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "SAWENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1401",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "TAE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1402",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "VUDEE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1403",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "VUMARI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1404",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Same DC",
   "FIELD4": "VUNTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1405",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Siha DC",
   "FIELD4": "DAHANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1406",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Siha DC",
   "FIELD4": "ESINYARI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1407",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Siha DC",
   "FIELD4": "FUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1408",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Siha DC",
   "FIELD4": "KARANSI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1409",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Siha DC",
   "FIELD4": "KILINGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1410",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Siha DC",
   "FIELD4": "KISHISHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1411",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Siha DC",
   "FIELD4": "MAGADINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1412",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Siha DC",
   "FIELD4": "MATADI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1413",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Siha DC",
   "FIELD4": "NAMWAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1414",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Siha DC",
   "FIELD4": "NURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1415",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Siha DC",
   "FIELD4": "OSHARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1416",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Siha DC",
   "FIELD4": "SANYA JUU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1417",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Siha DC",
   "FIELD4": "SIKIRARI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1418",
   "FIELD2": "Kilimanjaro",
   "FIELD3": "Siha DC",
   "FIELD4": "SUUMU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1419",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "ALI MCHUMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1420",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "DODOMEZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1421",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "ILULU GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1422",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "KANDAWALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1423",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "KIBATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1424",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "KIKANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1425",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "KIKOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1426",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "KILWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1427",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "KINJUMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1428",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "KIPATIMU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1429",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "KIRANJERANJE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1430",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "KIVINJE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1431",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "LIKAWAGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1432",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "MATANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1433",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "MIBUYUNI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1434",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "MIGURUWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1435",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "MINGUMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1436",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "MITEJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1437",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "MITOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1438",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "MPUNYULE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1439",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "MTANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1440",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "NAKIU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1441",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "NAMAYUNI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1442",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "NJINJO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1443",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "PANDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1444",
   "FIELD2": "Lindi",
   "FIELD3": "Kilwa DC",
   "FIELD4": "SONGOSONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1445",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "CHIUTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1446",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "KITOMANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1447",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "KIWALALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1448",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "LITIPU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1449",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "MADANGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1450",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "MAHIWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1451",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "MANDWANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1452",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "MBAWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1453",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "MCHINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1454",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "MILOLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1455",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "MIPINGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1456",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "MKOPWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1457",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "MNARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1458",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "MNOLELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1459",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "MTAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1460",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "MTUA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1461",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "MVULENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1462",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "NAHUKAHUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1463",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "NAMANGALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1464",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "NAMUPA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1465",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "NANGARU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1466",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "NYENGEDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1467",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi DC",
   "FIELD4": "RUTAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1468",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi MC",
   "FIELD4": "ANGAZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1469",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi MC",
   "FIELD4": "CHIKONJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1470",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi MC",
   "FIELD4": "KINENGENE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1471",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi MC",
   "FIELD4": "LINDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1472",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi MC",
   "FIELD4": "MINGOYO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1473",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi MC",
   "FIELD4": "MITWERO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1474",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi MC",
   "FIELD4": "MKONGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1475",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi MC",
   "FIELD4": "NGAPA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1476",
   "FIELD2": "Lindi",
   "FIELD3": "Lindi MC",
   "FIELD4": "NGONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1477",
   "FIELD2": "Lindi",
   "FIELD3": "Liwale DC",
   "FIELD4": "ANNA MAGOWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1478",
   "FIELD2": "Lindi",
   "FIELD3": "Liwale DC",
   "FIELD4": "BARIKIWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1479",
   "FIELD2": "Lindi",
   "FIELD3": "Liwale DC",
   "FIELD4": "HANGAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1480",
   "FIELD2": "Lindi",
   "FIELD3": "Liwale DC",
   "FIELD4": "KIANGARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1481",
   "FIELD2": "Lindi",
   "FIELD3": "Liwale DC",
   "FIELD4": "KIBUTUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1482",
   "FIELD2": "Lindi",
   "FIELD3": "Liwale DC",
   "FIELD4": "KIKULYUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1483",
   "FIELD2": "Lindi",
   "FIELD3": "Liwale DC",
   "FIELD4": "LIKONGOWELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1484",
   "FIELD2": "Lindi",
   "FIELD3": "Liwale DC",
   "FIELD4": "LIWALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1485",
   "FIELD2": "Lindi",
   "FIELD3": "Liwale DC",
   "FIELD4": "MAKATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1486",
   "FIELD2": "Lindi",
   "FIELD3": "Liwale DC",
   "FIELD4": "MIHUMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1487",
   "FIELD2": "Lindi",
   "FIELD3": "Liwale DC",
   "FIELD4": "MILINA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1488",
   "FIELD2": "Lindi",
   "FIELD3": "Liwale DC",
   "FIELD4": "MIRUI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1489",
   "FIELD2": "Lindi",
   "FIELD3": "Liwale DC",
   "FIELD4": "MLEMBWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1490",
   "FIELD2": "Lindi",
   "FIELD3": "Liwale DC",
   "FIELD4": "NANGANO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1491",
   "FIELD2": "Lindi",
   "FIELD3": "Liwale DC",
   "FIELD4": "NICODEMUS BANDUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1492",
   "FIELD2": "Lindi",
   "FIELD3": "Liwale DC",
   "FIELD4": "RASHIDI MFAUME KAWAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1493",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "CHIOLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1494",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "FARM 17",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1495",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "KIEGEI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1496",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "KILIMARONDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1497",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "KIPARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1498",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "KIPAUMBELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1499",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "LIONJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1500",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "MARAMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1501",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "MATEKWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1502",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "MBONDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1503",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "MISUFINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1504",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "MKOKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1505",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "MKOTOKUYANA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1506",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "MNERO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1507",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "NACHINGWEA DAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1508",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "NACHINGWEA GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1509",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "NAIPANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1510",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "NAIPINGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1511",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "NAMAPWIA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1512",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "NAMATULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1513",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "NAMBAMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1514",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "NAMIKANGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1515",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "NDANGALIMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1516",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "NDITI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1517",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "NDOMONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1518",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "RUPONDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1519",
   "FIELD2": "Lindi",
   "FIELD3": "Nachingwea DC",
   "FIELD4": "STESHENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1520",
   "FIELD2": "Lindi",
   "FIELD3": "Ruangwa DC",
   "FIELD4": "CHIENJERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1521",
   "FIELD2": "Lindi",
   "FIELD3": "Ruangwa DC",
   "FIELD4": "CHINONGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1522",
   "FIELD2": "Lindi",
   "FIELD3": "Ruangwa DC",
   "FIELD4": "CHUNYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1523",
   "FIELD2": "Lindi",
   "FIELD3": "Ruangwa DC",
   "FIELD4": "HAWA MCHOPA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1524",
   "FIELD2": "Lindi",
   "FIELD3": "Ruangwa DC",
   "FIELD4": "KASSIM MAJALIWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1525",
   "FIELD2": "Lindi",
   "FIELD3": "Ruangwa DC",
   "FIELD4": "LIKUNJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1526",
   "FIELD2": "Lindi",
   "FIELD3": "Ruangwa DC",
   "FIELD4": "LIUGURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1527",
   "FIELD2": "Lindi",
   "FIELD3": "Ruangwa DC",
   "FIELD4": "MAKANJIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1528",
   "FIELD2": "Lindi",
   "FIELD3": "Ruangwa DC",
   "FIELD4": "MANDAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1529",
   "FIELD2": "Lindi",
   "FIELD3": "Ruangwa DC",
   "FIELD4": "MBEKENYERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1530",
   "FIELD2": "Lindi",
   "FIELD3": "Ruangwa DC",
   "FIELD4": "MNACHO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1531",
   "FIELD2": "Lindi",
   "FIELD3": "Ruangwa DC",
   "FIELD4": "NAMBILANJE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1532",
   "FIELD2": "Lindi",
   "FIELD3": "Ruangwa DC",
   "FIELD4": "NAMICHIGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1533",
   "FIELD2": "Lindi",
   "FIELD3": "Ruangwa DC",
   "FIELD4": "NARUNGOMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1534",
   "FIELD2": "Lindi",
   "FIELD3": "Ruangwa DC",
   "FIELD4": "NKOWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1535",
   "FIELD2": "Lindi",
   "FIELD3": "Ruangwa DC",
   "FIELD4": "RUANGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1536",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "ARRI TSAAYO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1537",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "AYALAGAYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1538",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "AYATSEA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1539",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "BASHNET",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1540",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "CHIEF DODO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1541",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "DABIL",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1542",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "DAREDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1543",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "DOHOM",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1544",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "DURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1545",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "ENDAKISO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1546",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "ENDAMANANG",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1547",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "GALLAPO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1548",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "GICHAMEDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1549",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "GIDAS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1550",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "GOROWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1551",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "GUSE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1552",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "HAITEMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1553",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "KIRU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1554",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "MAGANJWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1555",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "MAGARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1556",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "MAGUGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1557",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "MAMIRE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1558",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "MASABEDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1559",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "MATUFA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1560",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "MBUGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1561",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "NAR",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1562",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "NDEKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1563",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "NKAITI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1564",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "QAMEYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1565",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "QASH",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1566",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "UFANA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1567",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "UMAGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1568",
   "FIELD2": "Manyara",
   "FIELD3": "Babati DC",
   "FIELD4": "UTWARI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1569",
   "FIELD2": "Manyara",
   "FIELD3": "Babati TC",
   "FIELD4": "BABATI DAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1570",
   "FIELD2": "Manyara",
   "FIELD3": "Babati TC",
   "FIELD4": "BAGARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1571",
   "FIELD2": "Manyara",
   "FIELD3": "Babati TC",
   "FIELD4": "BONGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1572",
   "FIELD2": "Manyara",
   "FIELD3": "Babati TC",
   "FIELD4": "F T SUMAYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1573",
   "FIELD2": "Manyara",
   "FIELD3": "Babati TC",
   "FIELD4": "HANGONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1574",
   "FIELD2": "Manyara",
   "FIELD3": "Babati TC",
   "FIELD4": "KOMOTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1575",
   "FIELD2": "Manyara",
   "FIELD3": "Babati TC",
   "FIELD4": "KWAANGW",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1576",
   "FIELD2": "Manyara",
   "FIELD3": "Babati TC",
   "FIELD4": "KWARAA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1577",
   "FIELD2": "Manyara",
   "FIELD3": "Babati TC",
   "FIELD4": "MUTUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1578",
   "FIELD2": "Manyara",
   "FIELD3": "Babati TC",
   "FIELD4": "NAKWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1579",
   "FIELD2": "Manyara",
   "FIELD3": "Babati TC",
   "FIELD4": "NANGARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1580",
   "FIELD2": "Manyara",
   "FIELD3": "Babati TC",
   "FIELD4": "SIGINO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1581",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "BALANGDALALU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1582",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "BASSODESH",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1583",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "BASSOTU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1584",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "CHIEF GEJARU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1585",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "CHIEF GIDOBAT",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1586",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "DANIEL NOUD",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1587",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "DIRMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1588",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "DUMBETA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1589",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "ENDAGAW",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1590",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "ENDASAK",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1591",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "GABADAW",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1592",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "GANANA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1593",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "GETANUWAS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1594",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "GIDAHABABIEG",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1595",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "GISAMBALANG",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1596",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "GITTING",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1597",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "HANANG",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1598",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "HIRBADAW",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1599",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "JOROJICK",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1600",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "KATESH",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1601",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "LAGHANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1602",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "MARY NAGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1603",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "MASAKTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1604",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "MASQARODA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1605",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "MEASKRON",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1606",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "MULBADAW",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1607",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "MWAHU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1608",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "NANGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1609",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "SIMBAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1610",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "SIROP",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1611",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "SUMAYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1612",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "UDANGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1613",
   "FIELD2": "Manyara",
   "FIELD3": "Hanang DC",
   "FIELD4": "WARETA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1614",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "BWAKALO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1615",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "DONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1616",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "DOSIDOSI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1617",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "ECO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1618",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "ENGUSERO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1619",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "KIBAYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1620",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "KIJUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1621",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "KIPERESA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1622",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "KITETO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1623",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "LESOIT",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1624",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "MAGUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1625",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "MATUI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1626",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "NDEDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1627",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "NJORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1628",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "ORKINE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1629",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "PARTIMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1630",
   "FIELD2": "Manyara",
   "FIELD3": "Kiteto DC",
   "FIELD4": "SUNYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1631",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "ALEXANDER SAULO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1632",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "B N HHANDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1633",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "BASHAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1634",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "DINAMU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1635",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "DR OLSEN",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1636",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "ENDOJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1637",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "GIDHIM",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1638",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "HAYDERER",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1639",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "HAYDOM",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1640",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "JAKAYA KIKWETE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1641",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "LABAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1642",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "MAGHANG",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1643",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "MAMAKARI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1644",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "MARETADU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1645",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "MARETADU JUU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1646",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "PHILIP MARMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1647",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "TUMATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1648",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "YAEDA AMPA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1649",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu DC",
   "FIELD4": "YAEDA CHINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1650",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu TC",
   "FIELD4": "BARGISH",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1651",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu TC",
   "FIELD4": "CHIEF SARWATT",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1652",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu TC",
   "FIELD4": "DAUDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1653",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu TC",
   "FIELD4": "DAUDI TEEWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1654",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu TC",
   "FIELD4": "GEHANDU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1655",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu TC",
   "FIELD4": "GUNYODA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1656",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu TC",
   "FIELD4": "HHAYNU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1657",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu TC",
   "FIELD4": "KAINAM",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1658",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu TC",
   "FIELD4": "MURRAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1659",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu TC",
   "FIELD4": "NAMBIS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1660",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu TC",
   "FIELD4": "NOWU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1661",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu TC",
   "FIELD4": "SILALODA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1662",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu TC",
   "FIELD4": "SINGLAND",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1663",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu TC",
   "FIELD4": "SOHEDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1664",
   "FIELD2": "Manyara",
   "FIELD3": "Mbulu TC",
   "FIELD4": "TLAWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1665",
   "FIELD2": "Manyara",
   "FIELD3": "Simanjiro DC",
   "FIELD4": "EMBOREET",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1666",
   "FIELD2": "Manyara",
   "FIELD3": "Simanjiro DC",
   "FIELD4": "ENGENO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1667",
   "FIELD2": "Manyara",
   "FIELD3": "Simanjiro DC",
   "FIELD4": "EWONGON",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1668",
   "FIELD2": "Manyara",
   "FIELD3": "Simanjiro DC",
   "FIELD4": "LOIBORSIRET",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1669",
   "FIELD2": "Manyara",
   "FIELD3": "Simanjiro DC",
   "FIELD4": "LOIBORSOIT",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1670",
   "FIELD2": "Manyara",
   "FIELD3": "Simanjiro DC",
   "FIELD4": "MERERANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1671",
   "FIELD2": "Manyara",
   "FIELD3": "Simanjiro DC",
   "FIELD4": "MSITU WA TEMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1672",
   "FIELD2": "Manyara",
   "FIELD3": "Simanjiro DC",
   "FIELD4": "NABERERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1673",
   "FIELD2": "Manyara",
   "FIELD3": "Simanjiro DC",
   "FIELD4": "NAISINYAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1674",
   "FIELD2": "Manyara",
   "FIELD3": "Simanjiro DC",
   "FIELD4": "NYUMBA YA MUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1675",
   "FIELD2": "Manyara",
   "FIELD3": "Simanjiro DC",
   "FIELD4": "OLJORO NA 5",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1676",
   "FIELD2": "Manyara",
   "FIELD3": "Simanjiro DC",
   "FIELD4": "RUVU REMMIT",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1677",
   "FIELD2": "Manyara",
   "FIELD3": "Simanjiro DC",
   "FIELD4": "SHAMBARAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1678",
   "FIELD2": "Manyara",
   "FIELD3": "Simanjiro DC",
   "FIELD4": "SIMANJIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1679",
   "FIELD2": "Manyara",
   "FIELD3": "Simanjiro DC",
   "FIELD4": "TANZANITE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1680",
   "FIELD2": "Manyara",
   "FIELD3": "Simanjiro DC",
   "FIELD4": "TERRAT",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1681",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "BULAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1682",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "CHAMRIHO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1683",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "CHISORYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1684",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "CHITENGULE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1685",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "ESPERANTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1686",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "HUNYARI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1687",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "KWIRAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1688",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "MAKONGORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1689",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "MEKOMARIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1690",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "MIHINGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1691",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "MURANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1692",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "MWIBARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1693",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "MWIGUNDU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1694",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "NANSIMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1695",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "NYAMANGUTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1696",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "NYERUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1697",
   "FIELD2": "Mara",
   "FIELD3": "Bunda DC",
   "FIELD4": "SALAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1698",
   "FIELD2": "Mara",
   "FIELD3": "Bunda TC",
   "FIELD4": "BUNDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1699",
   "FIELD2": "Mara",
   "FIELD3": "Bunda TC",
   "FIELD4": "DR NCHIMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1700",
   "FIELD2": "Mara",
   "FIELD3": "Bunda TC",
   "FIELD4": "GUTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1701",
   "FIELD2": "Mara",
   "FIELD3": "Bunda TC",
   "FIELD4": "KABASA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1702",
   "FIELD2": "Mara",
   "FIELD3": "Bunda TC",
   "FIELD4": "KUNZUGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1703",
   "FIELD2": "Mara",
   "FIELD3": "Bunda TC",
   "FIELD4": "NYIENDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1704",
   "FIELD2": "Mara",
   "FIELD3": "Bunda TC",
   "FIELD4": "RUBANA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1705",
   "FIELD2": "Mara",
   "FIELD3": "Bunda TC",
   "FIELD4": "SAZIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1706",
   "FIELD2": "Mara",
   "FIELD3": "Bunda TC",
   "FIELD4": "SIZAKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1707",
   "FIELD2": "Mara",
   "FIELD3": "Bunda TC",
   "FIELD4": "WARIKU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1708",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "BARANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1709",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "BUHEMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1710",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "BUKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1711",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "BUMANGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1712",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "BUMASWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1713",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "BURUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1714",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "BUTIAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1715",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "BUTUGURI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1716",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "CHIEF IHUNYO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1717",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "KEMORAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1718",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "KIABAKARI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1719",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "KIAGATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1720",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "KUKIRANGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1721",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "KYANYARI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1722",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "MASABA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1723",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "MIRWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1724",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "MKONO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1725",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "MMAZAMI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1726",
   "FIELD2": "Mara",
   "FIELD3": "Butiama DC",
   "FIELD4": "WEGERO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1727",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "BUGWEMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1728",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "BUKIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1729",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "BULINGA",
   "FIELD5": "3265740",
   "FIELD6": ""
 },
 {
   "FIELD1": "1730",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "ETARO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1731",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "KASOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1732",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "KIRIBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1733",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "MABUI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1734",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "MAKOJO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1735",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "MKIRIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1736",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "MTIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1737",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "MUGANGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1738",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "MURANGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1739",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "NYAKATENDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1740",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "NYAMBONO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1741",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "NYANJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1742",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "RUSOLI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1743",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "SUGUTI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1744",
   "FIELD2": "Mara",
   "FIELD3": "Musoma DC",
   "FIELD4": "TEGERUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1745",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "BARUTI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1746",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "BUHARE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1747",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "BWERI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1748",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "IRINGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1749",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "KAMUNYONGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1750",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "KIARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1751",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "MAKOKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1752",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "MARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1753",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "MOREMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1754",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "MSHIKAMANO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1755",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "MUKENDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1756",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "MUSOMA UFUNDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1757",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "MWISENGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1758",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "NYABISARE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1759",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "NYAMIONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1760",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "NYAMITWEBIRI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1761",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "NYASHO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1762",
   "FIELD2": "Mara",
   "FIELD3": "Musoma MC",
   "FIELD4": "SONGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1763",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "BUKAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1764",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "BUKURA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1765",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "BUKWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1766",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "BUTURI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1767",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "CHARYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1768",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "GORIBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1769",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "KATURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1770",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "KINYENCHE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1771",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "KIROGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1772",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "KISUMWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1773",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "KUKONA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1774",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "KWIBUSE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1775",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "KYANGOMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1776",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "MIRARE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1777",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "MUSA AKASHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1778",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "NGASARO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1779",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "NYABIWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1780",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "NYAMAGARO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1781",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "NYAMASANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1782",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "NYAMTINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1783",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "NYAMUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1784",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "NYANDUGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1785",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "NYATHOROGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1786",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "NYIHARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1787",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "PASTOR RAPHAEL ODUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1788",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "PROF PHILEMON SARUNGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1789",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "RARANYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1790",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "ROCHE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1791",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "SUBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1792",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "TAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1793",
   "FIELD2": "Mara",
   "FIELD3": "Rorya DC",
   "FIELD4": "WANINGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1794",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "BUSAWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1795",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "DR OMAR ALI JUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1796",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "IKOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1797",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "IKORONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1798",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "KAMBARAGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1799",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "KEMARONGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1800",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "KISAKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1801",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "KISANGURA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1802",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "KITUNGURUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1803",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "MACHOCHWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "TOTAL",
   "FIELD6": ""
 },
 {
   "FIELD1": "1804",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "MAJIMOTO",
   "FIELD5": "1310038",
   "FIELD6": ""
 },
 {
   "FIELD1": "1805",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "MAKUNDUSI",
   "FIELD5": "3165898",
   "FIELD6": ""
 },
 {
   "FIELD1": "1806",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "MAMA MARIA",
   "FIELD5": "3538996",
   "FIELD6": ""
 },
 {
   "FIELD1": "1807",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "MANCHIRA",
   "FIELD5": "3974362",
   "FIELD6": ""
 },
 {
   "FIELD1": "1808",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "MOSONGO",
   "FIELD5": "585180",
   "FIELD6": ""
 },
 {
   "FIELD1": "1809",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "MUGUMU",
   "FIELD5": "10768792",
   "FIELD6": ""
 },
 {
   "FIELD1": "1810",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "NAGUSI",
   "FIELD5": "7323869",
   "FIELD6": ""
 },
 {
   "FIELD1": "1811",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "NATTA",
   "FIELD5": "8405124",
   "FIELD6": ""
 },
 {
   "FIELD1": "1812",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "NGOREME",
   "FIELD5": "6224824",
   "FIELD6": ""
 },
 {
   "FIELD1": "1813",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "NYAMBURETI",
   "FIELD5": "5180988",
   "FIELD6": ""
 },
 {
   "FIELD1": "1814",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "NYAMBURI",
   "FIELD5": "854499",
   "FIELD6": ""
 },
 {
   "FIELD1": "1815",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "NYAMOKO",
   "FIELD5": "7299717",
   "FIELD6": ""
 },
 {
   "FIELD1": "1816",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "NYANSURURA",
   "FIELD5": "5289506",
   "FIELD6": ""
 },
 {
   "FIELD1": "1817",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "NYICHOKA",
   "FIELD5": "501093",
   "FIELD6": ""
 },
 {
   "FIELD1": "1818",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "RIGICHA",
   "FIELD5": "4814605",
   "FIELD6": ""
 },
 {
   "FIELD1": "1819",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "RINGWANI",
   "FIELD5": "5842767",
   "FIELD6": ""
 },
 {
   "FIELD1": "1820",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "ROBANDA",
   "FIELD5": "2529867",
   "FIELD6": ""
 },
 {
   "FIELD1": "1821",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "SEDECO",
   "FIELD5": "379168",
   "FIELD6": ""
 },
 {
   "FIELD1": "1822",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "SERENGETI",
   "FIELD5": "10872826",
   "FIELD6": ""
 },
 {
   "FIELD1": "1823",
   "FIELD2": "Mara",
   "FIELD3": "Serengeti",
   "FIELD4": "SOMOCHE",
   "FIELD5": "579833",
   "FIELD6": ""
 },
 {
   "FIELD1": "1824",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "BOREGA",
   "FIELD5": "3040931",
   "FIELD6": ""
 },
 {
   "FIELD1": "1825",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "BUNGURERE",
   "FIELD5": "5342054",
   "FIELD6": ""
 },
 {
   "FIELD1": "1826",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "BWIREGE",
   "FIELD5": "4318303",
   "FIELD6": ""
 },
 {
   "FIELD1": "1827",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "GENGE",
   "FIELD5": "2717886",
   "FIELD6": ""
 },
 {
   "FIELD1": "1828",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "GIBASO",
   "FIELD5": "2994681",
   "FIELD6": ""
 },
 {
   "FIELD1": "1829",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "GORONGA",
   "FIELD5": "3078820",
   "FIELD6": ""
 },
 {
   "FIELD1": "1830",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "INCHAGE",
   "FIELD5": "2011022",
   "FIELD6": ""
 },
 {
   "FIELD1": "1831",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "INCHUGU",
   "FIELD5": "8792617",
   "FIELD6": ""
 },
 {
   "FIELD1": "1832",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "INGWE",
   "FIELD5": "9203187",
   "FIELD6": ""
 },
 {
   "FIELD1": "1833",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "ITIRYO",
   "FIELD5": "5272083",
   "FIELD6": ""
 },
 {
   "FIELD1": "1834",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "J K NYERERE",
   "FIELD5": "5468300",
   "FIELD6": ""
 },
 {
   "FIELD1": "1835",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "KEBOGWE",
   "FIELD5": "3027070",
   "FIELD6": ""
 },
 {
   "FIELD1": "1836",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "KEMAKORERE",
   "FIELD5": "4305327",
   "FIELD6": ""
 },
 {
   "FIELD1": "1837",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "KEMAMBO",
   "FIELD5": "3676405",
   "FIELD6": ""
 },
 {
   "FIELD1": "1838",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "KIBASUKA",
   "FIELD5": "4419104",
   "FIELD6": ""
 },
 {
   "FIELD1": "1839",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "KITAWASI",
   "FIELD5": "3704384",
   "FIELD6": ""
 },
 {
   "FIELD1": "1840",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "KOROTAMBE",
   "FIELD5": "3732223",
   "FIELD6": ""
 },
 {
   "FIELD1": "1841",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "KURUMWA",
   "FIELD5": "1769973",
   "FIELD6": ""
 },
 {
   "FIELD1": "1842",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "MAGOTO",
   "FIELD5": "8649109",
   "FIELD6": ""
 },
 {
   "FIELD1": "1843",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "MANGA",
   "FIELD5": "10011434",
   "FIELD6": ""
 },
 {
   "FIELD1": "1844",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "MBOGI",
   "FIELD5": "5463510",
   "FIELD6": ""
 },
 {
   "FIELD1": "1845",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "MWEMA",
   "FIELD5": "6158957",
   "FIELD6": ""
 },
 {
   "FIELD1": "1846",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "NYAIBARA",
   "FIELD5": "6267628",
   "FIELD6": ""
 },
 {
   "FIELD1": "1847",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "NYAMONGO",
   "FIELD5": "10410507",
   "FIELD6": ""
 },
 {
   "FIELD1": "1848",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "NYAMWAGA",
   "FIELD5": "3887575",
   "FIELD6": ""
 },
 {
   "FIELD1": "1849",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "NYAMWIGURA",
   "FIELD5": "2931755",
   "FIELD6": ""
 },
 {
   "FIELD1": "1850",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "NYANTIRA",
   "FIELD5": "3158979",
   "FIELD6": ""
 },
 {
   "FIELD1": "1851",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "NYANUNGU",
   "FIELD5": "4610912",
   "FIELD6": ""
 },
 {
   "FIELD1": "1852",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "NYARERO",
   "FIELD5": "1954393",
   "FIELD6": ""
 },
 {
   "FIELD1": "1853",
   "FIELD2": "Mara",
   "FIELD3": "Tarime DC",
   "FIELD4": "SIRARI",
   "FIELD5": "14608254",
   "FIELD6": ""
 },
 {
   "FIELD1": "1854",
   "FIELD2": "Mara",
   "FIELD3": "Tarime TC",
   "FIELD4": "BOMANI",
   "FIELD5": "9770295",
   "FIELD6": ""
 },
 {
   "FIELD1": "1855",
   "FIELD2": "Mara",
   "FIELD3": "Tarime TC",
   "FIELD4": "KENYAMANYORI",
   "FIELD5": "4162636",
   "FIELD6": ""
 },
 {
   "FIELD1": "1856",
   "FIELD2": "Mara",
   "FIELD3": "Tarime TC",
   "FIELD4": "MOGABIRI",
   "FIELD5": "9668857",
   "FIELD6": ""
 },
 {
   "FIELD1": "1857",
   "FIELD2": "Mara",
   "FIELD3": "Tarime TC",
   "FIELD4": "NKENDE",
   "FIELD5": "8801753",
   "FIELD6": ""
 },
 {
   "FIELD1": "1858",
   "FIELD2": "Mara",
   "FIELD3": "Tarime TC",
   "FIELD4": "NKONGORE",
   "FIELD5": "1015243",
   "FIELD6": ""
 },
 {
   "FIELD1": "1859",
   "FIELD2": "Mara",
   "FIELD3": "Tarime TC",
   "FIELD4": "NYAMISANGURA",
   "FIELD5": "10172854",
   "FIELD6": ""
 },
 {
   "FIELD1": "1860",
   "FIELD2": "Mara",
   "FIELD3": "Tarime TC",
   "FIELD4": "NYANDOTO",
   "FIELD5": "6241968",
   "FIELD6": ""
 },
 {
   "FIELD1": "1861",
   "FIELD2": "Mara",
   "FIELD3": "Tarime TC",
   "FIELD4": "REBU",
   "FIELD5": "10817616",
   "FIELD6": ""
 },
 {
   "FIELD1": "1862",
   "FIELD2": "Mara",
   "FIELD3": "Tarime TC",
   "FIELD4": "TARIME",
   "FIELD5": "7799736",
   "FIELD6": ""
 },
 {
   "FIELD1": "1863",
   "FIELD2": "Mbeya",
   "FIELD3": "Busokelo",
   "FIELD4": "BUSOKELO GIRLS",
   "FIELD5": "1636974",
   "FIELD6": ""
 },
 {
   "FIELD1": "1864",
   "FIELD2": "Mbeya",
   "FIELD3": "Busokelo",
   "FIELD4": "IKAPU",
   "FIELD5": "3198514",
   "FIELD6": ""
 },
 {
   "FIELD1": "1865",
   "FIELD2": "Mbeya",
   "FIELD3": "Busokelo",
   "FIELD4": "ISANGE",
   "FIELD5": "3976161",
   "FIELD6": ""
 },
 {
   "FIELD1": "1866",
   "FIELD2": "Mbeya",
   "FIELD3": "Busokelo",
   "FIELD4": "KABULA",
   "FIELD5": "4030471",
   "FIELD6": ""
 },
 {
   "FIELD1": "1867",
   "FIELD2": "Mbeya",
   "FIELD3": "Busokelo",
   "FIELD4": "KISEGESE",
   "FIELD5": "3321339",
   "FIELD6": ""
 },
 {
   "FIELD1": "1868",
   "FIELD2": "Mbeya",
   "FIELD3": "Busokelo",
   "FIELD4": "KYEJO",
   "FIELD5": "4251968",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1869",
   "FIELD2": "Mbeya",
   "FIELD3": "Busokelo",
   "FIELD4": "LUFILYO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1870",
   "FIELD2": "Mbeya",
   "FIELD3": "Busokelo",
   "FIELD4": "LUTEBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1871",
   "FIELD2": "Mbeya",
   "FIELD3": "Busokelo",
   "FIELD4": "LWANGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1872",
   "FIELD2": "Mbeya",
   "FIELD3": "Busokelo",
   "FIELD4": "MBIGILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1873",
   "FIELD2": "Mbeya",
   "FIELD3": "Busokelo",
   "FIELD4": "MPATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1874",
   "FIELD2": "Mbeya",
   "FIELD3": "Busokelo",
   "FIELD4": "MWAKALELI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1875",
   "FIELD2": "Mbeya",
   "FIELD3": "Busokelo",
   "FIELD4": "MWATISI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1876",
   "FIELD2": "Mbeya",
   "FIELD3": "Busokelo",
   "FIELD4": "MZALENDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1877",
   "FIELD2": "Mbeya",
   "FIELD3": "Busokelo",
   "FIELD4": "NTABA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1878",
   "FIELD2": "Mbeya",
   "FIELD3": "Busokelo",
   "FIELD4": "SELYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1879",
   "FIELD2": "Mbeya",
   "FIELD3": "Chunya DC",
   "FIELD4": "CHALANGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1880",
   "FIELD2": "Mbeya",
   "FIELD3": "Chunya DC",
   "FIELD4": "CHOKAA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1881",
   "FIELD2": "Mbeya",
   "FIELD3": "Chunya DC",
   "FIELD4": "IFUMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1882",
   "FIELD2": "Mbeya",
   "FIELD3": "Chunya DC",
   "FIELD4": "ISANGAWANA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1883",
   "FIELD2": "Mbeya",
   "FIELD3": "Chunya DC",
   "FIELD4": "ISENYELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1884",
   "FIELD2": "Mbeya",
   "FIELD3": "Chunya DC",
   "FIELD4": "ITEWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1885",
   "FIELD2": "Mbeya",
   "FIELD3": "Chunya DC",
   "FIELD4": "KIWANJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1886",
   "FIELD2": "Mbeya",
   "FIELD3": "Chunya DC",
   "FIELD4": "LUPA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1887",
   "FIELD2": "Mbeya",
   "FIELD3": "Chunya DC",
   "FIELD4": "MAKALLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1888",
   "FIELD2": "Mbeya",
   "FIELD3": "Chunya DC",
   "FIELD4": "MAKONGOLOSI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1889",
   "FIELD2": "Mbeya",
   "FIELD3": "Chunya DC",
   "FIELD4": "MTANDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1890",
   "FIELD2": "Mbeya",
   "FIELD3": "Chunya DC",
   "FIELD4": "MTANILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1891",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "BUJONDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1892",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "IKAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1893",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "IKIMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1894",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "IKOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1895",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "IPANDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1896",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "IPINDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1897",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "ITOPE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1898",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "ITUNGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1899",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "KAFUNDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1900",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "KAJUNJUMELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1901",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "KATUMBASONGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1902",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "KIWIRA COAL MINE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1903",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "KYELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1904",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "LUSUNGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1905",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "MAKWALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1906",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "MASUKILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1907",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "MATEMA BEACH",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1908",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "MWAYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1909",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "NDOBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1910",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "NGONGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1911",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "NKUYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1912",
   "FIELD2": "Mbeya",
   "FIELD3": "Kyela DC",
   "FIELD4": "NYASA LAKE SHORE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1913",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "GWILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1914",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "IGAVA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1915",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "IGOMELO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1916",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "IMALILO SONGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1917",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "IPWANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1918",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "JAKAYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1919",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "MADIBIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1920",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "MALENGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1921",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "MAWINDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1922",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "MBARALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1923",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "MENGELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1924",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "MIYOMBWENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1925",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "MSHIKAMANO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1926",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "MWAKAGANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1927",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "RUIWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1928",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "RUJEWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1929",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "UHAHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1930",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbarali DC",
   "FIELD4": "UTENGULE USANGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1931",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "FOREST",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1932",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "HAYOMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1933",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "IDUDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1934",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "IGANZO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1935",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "IHANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1936",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "ILOMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1937",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "ISYESYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1938",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "ITEZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1939",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "ITIJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1940",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "IWAMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1941",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "IYELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1942",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "IYUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1943",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "KALOBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1944",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "LEGICO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1945",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "LOLEZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1946",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "LUPETA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1947",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "LYOTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1948",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "MAZIWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1949",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "MBEYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1950",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "MPONJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1951",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "MWAKIBETE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1952",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "MWASANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1953",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "NSENGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1954",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "NSOHO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1955",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "NZONDAHAKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1956",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "PANKUMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1957",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "SAMORA MACHEL",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1958",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "SINDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1959",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "STELLA FARM",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1960",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "UYOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1961",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya CC",
   "FIELD4": "WIGAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1962",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "GALIJEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1963",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "HORONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1964",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "IHANGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1965",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "IKHOHO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1966",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "IKUKWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1967",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "ILEMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1968",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "ILUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1969",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "ILUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1970",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "IMEZU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1971",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "ISUTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1972",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "ITALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1973",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "IWALANJE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1974",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "IWIJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1975",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "IWINDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1976",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "IYELANYALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1977",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "IZYIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1978",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "MALAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1979",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "MPESU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1980",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "MSHEWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1981",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "MWAKIPESILE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1982",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "MWASELELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1983",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "NSONGWI JUU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1984",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "SANTILYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1985",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "SASYAKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1986",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "SHIBOLYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1987",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "SHISYETE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1988",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "SONGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1989",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "SWAYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1990",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "TEULE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1991",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "USONGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1992",
   "FIELD2": "Mbeya",
   "FIELD3": "Mbeya DC",
   "FIELD4": "YALAWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1993",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "BUJELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1994",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "BUJINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1995",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "BULYAGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1996",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "IKUTI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1997",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "ILIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1998",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "IPONJOLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "1999",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "ISONGOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2000",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "KALENGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2001",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "KAPUGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2002",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "KAYUKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2003",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "KIGUGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2004",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "KIMAMMPE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2005",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "KINYALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2006",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "KISIBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2007",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "KISONDELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2008",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "KIWIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2009",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "KYIMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2010",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "LUFINGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2011",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "LUPOTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2012",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "MASOKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2013",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "MASUKULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2014",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "MPANDAPANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2015",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "MPUGUSO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2016",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "NDANTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2017",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "NKUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2018",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "RUNGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2019",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "SUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2020",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "TUKUYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2021",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "UKUKWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2022",
   "FIELD2": "Mbeya",
   "FIELD3": "Rungwe DC",
   "FIELD4": "ZIWANGOSI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2023",
   "FIELD2": "Morogoro",
   "FIELD3": "Gairo DC",
   "FIELD4": "A M SHABIBY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2024",
   "FIELD2": "Morogoro",
   "FIELD3": "Gairo DC",
   "FIELD4": "CHAGONGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2025",
   "FIELD2": "Morogoro",
   "FIELD3": "Gairo DC",
   "FIELD4": "CHAKWALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2026",
   "FIELD2": "Morogoro",
   "FIELD3": "Gairo DC",
   "FIELD4": "CHANJALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2027",
   "FIELD2": "Morogoro",
   "FIELD3": "Gairo DC",
   "FIELD4": "GAIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2028",
   "FIELD2": "Morogoro",
   "FIELD3": "Gairo DC",
   "FIELD4": "IYOGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2029",
   "FIELD2": "Morogoro",
   "FIELD3": "Gairo DC",
   "FIELD4": "KIBEDYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2030",
   "FIELD2": "Morogoro",
   "FIELD3": "Gairo DC",
   "FIELD4": "MAJEMBWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2031",
   "FIELD2": "Morogoro",
   "FIELD3": "Gairo DC",
   "FIELD4": "NJUNGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2032",
   "FIELD2": "Morogoro",
   "FIELD3": "Gairo DC",
   "FIELD4": "NONGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2033",
   "FIELD2": "Morogoro",
   "FIELD3": "Gairo DC",
   "FIELD4": "RUBEHO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2034",
   "FIELD2": "Morogoro",
   "FIELD3": "Gairo DC",
   "FIELD4": "SEKWAO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2035",
   "FIELD2": "Morogoro",
   "FIELD3": "Ifakara TC",
   "FIELD4": "IFAKARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2036",
   "FIELD2": "Morogoro",
   "FIELD3": "Ifakara TC",
   "FIELD4": "KIBAONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2037",
   "FIELD2": "Morogoro",
   "FIELD3": "Ifakara TC",
   "FIELD4": "KILOMBERO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2038",
   "FIELD2": "Morogoro",
   "FIELD3": "Ifakara TC",
   "FIELD4": "KIYONGWILE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2039",
   "FIELD2": "Morogoro",
   "FIELD3": "Ifakara TC",
   "FIELD4": "KWASHUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2040",
   "FIELD2": "Morogoro",
   "FIELD3": "Ifakara TC",
   "FIELD4": "LUMEMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2041",
   "FIELD2": "Morogoro",
   "FIELD3": "Ifakara TC",
   "FIELD4": "MLABANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2042",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "BOKELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2043",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "CANE GROWERS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2044",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "CHISANO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2045",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "CHITA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2046",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "KAMWENE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2047",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "KIBEREGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2048",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "KIBURUBUTU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2049",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "KIDATU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2050",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "KISAWASAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2051",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "MANGULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2052",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "MASAGATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2053",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "MATUNDU HILL",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2054",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "MBINGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2055",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "MCHOMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2056",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "MLIMBA DAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2057",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "MOFU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2058",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "MUTENGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2059",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "MWANIHANA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2060",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "NAKAGURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2061",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "NYANDEO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2062",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "NYANGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2063",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "SANJE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2064",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "SIGNAL",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2065",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "TREE FARMS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2066",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilombero DC",
   "FIELD4": "UCHINDILE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2067",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "CHANZURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2068",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "DAKAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2069",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "DENDEGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2070",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "DUMILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2071",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "GONGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2072",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "IWEMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2073",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "KIDETE DAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2074",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "KIDODI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2075",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "KILANGALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2076",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "KILOSA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2077",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "KIMAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2078",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "KISANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2079",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "KITETE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2080",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "KUTUKUTU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2081",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "LUMBIJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2082",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "LUMUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2083",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "LYAHIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2084",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "MABULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2085",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "MABWEREBWERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2086",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "MAGOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2087",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "MAGUBIKE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2088",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "MAMBOYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2089",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "MASANZE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2090",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "MATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2091",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "MAZINYUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2092",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "MBUMI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2093",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "MGUGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2094",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "MIKUMI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2095",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "MKULO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2096",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "MSOWERO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2097",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "MTUMBATU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2098",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "MWEGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2099",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "PARAKUYO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2100",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "RUDEWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2101",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "RUHEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2102",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "UKWIVA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2103",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "ULELINGOMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2104",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "VIDUNDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2105",
   "FIELD2": "Morogoro",
   "FIELD3": "Kilosa DC",
   "FIELD4": "ZOMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2106",
   "FIELD2": "Morogoro",
   "FIELD3": "Malinyi DC",
   "FIELD4": "BIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2107",
   "FIELD2": "Morogoro",
   "FIELD3": "Malinyi DC",
   "FIELD4": "IGAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2108",
   "FIELD2": "Morogoro",
   "FIELD3": "Malinyi DC",
   "FIELD4": "ITETE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2109",
   "FIELD2": "Morogoro",
   "FIELD3": "Malinyi DC",
   "FIELD4": "KIPINGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2110",
   "FIELD2": "Morogoro",
   "FIELD3": "Malinyi DC",
   "FIELD4": "MALINYI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2111",
   "FIELD2": "Morogoro",
   "FIELD3": "Malinyi DC",
   "FIELD4": "MTIMBIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2112",
   "FIELD2": "Morogoro",
   "FIELD3": "Malinyi DC",
   "FIELD4": "NGOHERANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2113",
   "FIELD2": "Morogoro",
   "FIELD3": "Malinyi DC",
   "FIELD4": "SOFI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2114",
   "FIELD2": "Morogoro",
   "FIELD3": "Malinyi DC",
   "FIELD4": "USANGULE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2115",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "BWAKIRA CHINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2116",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "BWAKIRA JUU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2117",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "FATEMI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2118",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "GWATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2119",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "KIBOGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2120",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "KIBUNGO JUU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2121",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "KINOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2122",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "KIROKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2123",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "KISAKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2124",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "KISEMU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2125",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "KIZAGILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2126",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "KOLERO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2127",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "LUNDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2128",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "MATOMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2129",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "MIKESE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2130",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "MILENGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2131",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "MKULAZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2132",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "MKUYUNI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2133",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "MTOMBOZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2134",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "MVUHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2135",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "NELSON MANDELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2136",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "NGERENGERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2137",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "SELEMBALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2138",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "SINGISA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2139",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "TAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2140",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "TEGETERO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2141",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "TOMONDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2142",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro DC",
   "FIELD4": "TUNUNGUO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2143",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "BONDWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2144",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "BUNGODIMWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2145",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "KAUZENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2146",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "KAYENZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2147",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "KIHONDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2148",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "KILAKALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2149",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "KINGALU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2150",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "KINGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2151",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "KINGOLWIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2152",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "KOLA HILL",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2153",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "LUPANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2154",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "MAFIGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2155",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "MGULASI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2156",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "MJI MPYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2157",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "MOROGORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2158",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "MWEMBESONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2159",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "NANENANE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2160",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "SUA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2161",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "SUMAYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2162",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "TUBUYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2163",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "TUSHIKAMANE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2164",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "ULUGURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2165",
   "FIELD2": "Morogoro",
   "FIELD3": "Morogoro MC",
   "FIELD4": "UWANJA WA TAIFA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2166",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "BUNDUKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2167",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "DIONGOYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2168",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "DOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2169",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "HEMBETI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2170",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "KANGA HILL",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2171",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "KIKEO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2172",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "KIPERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2173",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "LANGALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2174",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "LUSANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2175",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "MASKATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2176",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "MELELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2177",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "MGETA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2178",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "MONGOLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2179",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "MTIBWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2180",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "MURAD SADDIQ",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2181",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "MVOMERO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2182",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "MZUMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2183",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "NASSORO SEIF",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2184",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "SUNGAJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2185",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "TCHENZEMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2186",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "UNGULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2187",
   "FIELD2": "Morogoro",
   "FIELD3": "Mvomero DC",
   "FIELD4": "WAMI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2188",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "CELINA KOMBANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2189",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "CHIROMBOLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2190",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "EUGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2191",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "IGOTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2192",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "ILONGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2193",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "IRAGUA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2194",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "ISONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2195",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "KICHANGANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2196",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "KWIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2197",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "LUPIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2198",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "MAHENGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2199",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "MBUGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2200",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "MINEPA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2201",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "MWAYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2202",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "NAWENGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2203",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "ULANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2204",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "UPONERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2205",
   "FIELD2": "Morogoro",
   "FIELD3": "Ulanga DC",
   "FIELD4": "VIGOI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2206",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "CHIDYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2207",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "CHIKOROPOLA",
   "FIELD5": "1158833",
   "FIELD6": ""
 },
 {
   "FIELD1": "2208",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "CHIUNGUTWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2209",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "CHIWALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2210",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "CHIWATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2211",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "ISDORE SHIRIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2212",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "LUKULEDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2213",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "LULINDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2214",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "LUPASO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2215",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "MAKONGONDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2216",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "MBEMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2217",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "MBUYUNI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2218",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "MKALAPA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2219",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "MKULULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2220",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "MPINDIMBI CHANIKANGUO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2221",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "MWENA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2222",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "NAMAJANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2223",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "NAMALENGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2224",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "NAMATUTWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2225",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "NAMOMBWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2226",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "NAMWANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2227",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "NANGANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2228",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "NANGOO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2229",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "NANJOTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2230",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "NDANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2231",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "NDWIKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2232",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi DC",
   "FIELD4": "SINDANO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2233",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi TC",
   "FIELD4": "ANNA ABDALLAH",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2234",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi TC",
   "FIELD4": "CHANIKANGUO MPINDIMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2235",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi TC",
   "FIELD4": "MARIKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2236",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi TC",
   "FIELD4": "MASASI DAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2237",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi TC",
   "FIELD4": "MASASI GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2238",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi TC",
   "FIELD4": "MTANDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2239",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi TC",
   "FIELD4": "MTAPIKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2240",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi TC",
   "FIELD4": "NANGAYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2241",
   "FIELD2": "Mtwara",
   "FIELD3": "Masasi TC",
   "FIELD4": "SULULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2242",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara DC",
   "FIELD4": "DIHIMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2243",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara DC",
   "FIELD4": "KISIWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2244",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara DC",
   "FIELD4": "KITERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2245",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara DC",
   "FIELD4": "LIBOBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2246",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara DC",
   "FIELD4": "MADIMBA",
   "FIELD5": "4554182",
   "FIELD6": ""
 },
 {
   "FIELD1": "2247",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara DC",
   "FIELD4": "MAHURUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2248",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara DC",
   "FIELD4": "MAYANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2249",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara DC",
   "FIELD4": "MSIMBATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2250",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara DC",
   "FIELD4": "MUSTAFA SABODO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2251",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara DC",
   "FIELD4": "NANGURUWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2252",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara DC",
   "FIELD4": "NDUMBWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2253",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara DC",
   "FIELD4": "ZIWANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2254",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara MC",
   "FIELD4": "BANDARI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2255",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara MC",
   "FIELD4": "CHUNO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2256",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara MC",
   "FIELD4": "MANGAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2257",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara MC",
   "FIELD4": "MIKINDANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2258",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara MC",
   "FIELD4": "MITENGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2259",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara MC",
   "FIELD4": "MTWARA GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2260",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara MC",
   "FIELD4": "MTWARA UFUNDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2261",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara MC",
   "FIELD4": "NALIENDELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2262",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara MC",
   "FIELD4": "RAHALEO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2263",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara MC",
   "FIELD4": "SABASABA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2264",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara MC",
   "FIELD4": "SHANGANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2265",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara MC",
   "FIELD4": "SINO TZ",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2266",
   "FIELD2": "Mtwara",
   "FIELD3": "Mtwara MC",
   "FIELD4": "UMOJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2267",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyamba TC",
   "FIELD4": "CHAWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2268",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyamba TC",
   "FIELD4": "KIROMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2269",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyamba TC",
   "FIELD4": "KITAYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2270",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyamba TC",
   "FIELD4": "MBEMBALEO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2271",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyamba TC",
   "FIELD4": "MNIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2272",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyamba TC",
   "FIELD4": "MNYAWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2273",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyamba TC",
   "FIELD4": "MTINIKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2274",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyamba TC",
   "FIELD4": "NANYAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2275",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyamba TC",
   "FIELD4": "NITEKELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2276",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyamba TC",
   "FIELD4": "NJENGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2277",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyumbu DC",
   "FIELD4": "CHIPUPUTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2278",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyumbu DC",
   "FIELD4": "LIKOKONA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2279",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyumbu DC",
   "FIELD4": "LUMESULE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2280",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyumbu DC",
   "FIELD4": "MANGAKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2281",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyumbu DC",
   "FIELD4": "MARATANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2282",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyumbu DC",
   "FIELD4": "MICHIGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2283",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyumbu DC",
   "FIELD4": "MIKANGAULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2284",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyumbu DC",
   "FIELD4": "NANDETE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2285",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyumbu DC",
   "FIELD4": "NANGOMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2286",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyumbu DC",
   "FIELD4": "NANYUMBU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2287",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyumbu DC",
   "FIELD4": "NAPACHO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2288",
   "FIELD2": "Mtwara",
   "FIELD3": "Nanyumbu DC",
   "FIELD4": "SENGENYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2289",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala DC",
   "FIELD4": "CHIHANGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2290",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala DC",
   "FIELD4": "CHITEKETE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2291",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala DC",
   "FIELD4": "LENGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2292",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala DC",
   "FIELD4": "MAKUKWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2293",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala DC",
   "FIELD4": "MALATU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2294",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala DC",
   "FIELD4": "MAPUTI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2295",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala DC",
   "FIELD4": "MIKUMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2296",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala DC",
   "FIELD4": "MKOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2297",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala DC",
   "FIELD4": "MMULUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2298",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala DC",
   "FIELD4": "MNYAMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2299",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala DC",
   "FIELD4": "MPELEPELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2300",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala DC",
   "FIELD4": "MPOTOLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2301",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala DC",
   "FIELD4": "MTOPWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2302",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala DC",
   "FIELD4": "USHIRIKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2303",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala DC",
   "FIELD4": "VIHOKOLI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2304",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala TC",
   "FIELD4": "DR ALEX MTAVALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2305",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala TC",
   "FIELD4": "G MKUCHIKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2306",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala TC",
   "FIELD4": "KIUTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2307",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala TC",
   "FIELD4": "KUSINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2308",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala TC",
   "FIELD4": "MAKOTE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2309",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala TC",
   "FIELD4": "MALEGESI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2310",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala TC",
   "FIELD4": "MALOCHO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2311",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala TC",
   "FIELD4": "MTANGALANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2312",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala TC",
   "FIELD4": "NAMBUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2313",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala TC",
   "FIELD4": "NANGWANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2314",
   "FIELD2": "Mtwara",
   "FIELD3": "Newala TC",
   "FIELD4": "NEWALA DAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2315",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "CHAUME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2316",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "CHINGUNGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2317",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "DINDUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2318",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "KITAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2319",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "LIENJE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2320",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "LUAGALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2321",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "LUKOKODA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2322",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "MAHUTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2323",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "MAUNDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2324",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "MCHICHIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2325",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "MDIMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2326",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "MICHENJELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2327",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "MIHAMBWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2328",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "MILONGODI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2329",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "MKONJOWANO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2330",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "MKOREHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2331",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "MKUNDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2332",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "MKWITI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2333",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "MNYAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2334",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "MWEMINAKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2335",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "NACHUNYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2336",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "NAMIKUPA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2337",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "NANDONDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2338",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "NANHYANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2339",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "NAPUTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2340",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "NGUNJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2341",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "SALAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2342",
   "FIELD2": "Mtwara",
   "FIELD3": "Tandahimba DC",
   "FIELD4": "TANDAHIMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2343",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "BANGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2344",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "BUPANDWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2345",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "ILIGAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2346",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "IRENZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2347",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "ITABULYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2348",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "KAFUNZO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2349",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "KAKOBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2350",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "KALEBEZO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2351",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "KATWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2352",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "KOME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2353",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "LUGATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2354",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "LUSHAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2355",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "MAGULUKENDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2356",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "MAISOME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2357",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "MIGUKULAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2358",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "NYAKALIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2359",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "NYAKASUNGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2360",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "NYAMADOKE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2361",
   "FIELD2": "Mwanza",
   "FIELD3": "Buchosa DC",
   "FIELD4": "NYEHUNGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2362",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "BUGOGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2363",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "BUJINGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2364",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "BUSWELU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2365",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "BWIRU BOYS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2366",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "BWIRU GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2367",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "IBINZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2368",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "IBUNGILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2369",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "KABUHORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2370",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "KANGAYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2371",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "KAYENZE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2372",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "KILIMANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2373",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "KILOLELI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2374",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "KIRUMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2375",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "KISEKE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2376",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "KISUNDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2377",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "KITANGIRI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2378",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "LUKOBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2379",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "LUMALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2380",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "MIHAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2381",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "MNARANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2382",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "MWINUKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2383",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "NUNDU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2384",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "NYAMANORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2385",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "NYASAKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2386",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "PASIANSI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2387",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "SANGABUYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2388",
   "FIELD2": "Mwanza",
   "FIELD3": "Ilemela MC",
   "FIELD4": "SHIBULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2389",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "BUJIKU SAKILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2390",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "BUNGULWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2391",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "BUPAMWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2392",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "IGONGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2393",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "IMALILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2394",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "ISENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2395",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "KIKUBIJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2396",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "KINOJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2397",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "LYOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2398",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "MALIGISU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2399",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "MALYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2400",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "MANTARE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2401",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "MHANDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2402",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "MWABOMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2403",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "MWAGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2404",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "MWAKILYAMBITI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2405",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "MWAMALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2406",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "MWAMASHIMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2407",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "MWANDU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2408",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "MWANGHALANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2409",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "MWANKULWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2410",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "MWASHILALAGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2411",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "NDAMHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2412",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "NELLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2413",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "NGHUNDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2414",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "NGUDU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2415",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "NGULLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2416",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "NYAMILAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2417",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "SUMVE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2418",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "TALLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2419",
   "FIELD2": "Mwanza",
   "FIELD3": "Kwimba DC",
   "FIELD4": "WALLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2420",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "BUJASHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2421",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "BUKANDWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2422",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "ITUMBILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2423",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "KABILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2424",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "KAHANGARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2425",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "KANDAWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2426",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "KINANGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2427",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "KITUMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2428",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "KONGOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2429",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "LUBUGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2430",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "LUGEYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2431",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "LUMVE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2432",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "LUTALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2433",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "MAGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2434",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "MAHAHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2435",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "MWAMANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2436",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "NGHAYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2437",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "NGWAMABANZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2438",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "NYANGUGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2439",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "SHISHANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2440",
   "FIELD2": "Mwanza",
   "FIELD3": "Magu DC",
   "FIELD4": "SUKUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2441",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "AIMEE MILEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2442",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "BUHINGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2443",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "BULEMEJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2444",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "BUSONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2445",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "IDETEMYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2446",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "IGOKELO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2447",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "ILUJAMATE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2448",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "ISAKAMAWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2449",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "J MAGUFULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2450",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "KANYELELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2451",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "KASOLOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2452",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "KOROMIJE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2453",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "LUBILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2454",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "MAMAYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2455",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "MAWEMATATU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2456",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "MBARIKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2457",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "MISASI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2458",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "MISUNGWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2459",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "MWANIKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2460",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "NHUNDULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2461",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "NYABUMHANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2462",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "PAUL BOMANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2463",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "SANJO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2464",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "SHILALO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2465",
   "FIELD2": "Mwanza",
   "FIELD3": "Misungwi DC",
   "FIELD4": "SUMBUGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2466",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "BUGARIKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2467",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "BUHONGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2468",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "BUTIMBA DAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2469",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "CAPRIPOINT",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2470",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "FUMAGILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2471",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "IGELEGELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2472",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "IGOGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2473",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "IGOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2474",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "LUCHELELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2475",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "LWANHIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2476",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "MAHINA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2477",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "MAPANGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2478",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "MBUGANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2479",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "MHANDU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2480",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "MIRONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2481",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "MKOLANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2482",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "MKUYUNI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2483",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "MLIMANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2484",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "MTONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2485",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "MWANZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2486",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "NGANZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2487",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "NSUMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2488",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "NYABULOGOYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2489",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "NYAKABUNGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2490",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "NYAKURUNDUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2491",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "NYAMAGANA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2492",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "NYEGEZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2493",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "OLE NJOOLAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2494",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "PAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2495",
   "FIELD2": "Mwanza",
   "FIELD3": "Mwanza CC",
   "FIELD4": "SHAMALIWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2496",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "BITOTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2497",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "BUSISI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2498",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "BUTONGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2499",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "BUYAGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2500",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "BUZILASOGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2501",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "CHIFUNFU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2502",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "IBISABAGENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2503",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "KAHUMULO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2504",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "KASUNGAMILE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2505",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "KATUNGURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2506",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "KIJUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2507",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "KILABELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2508",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "KISHINDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2509",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "LUSIKWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2510",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "LWENGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2511",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "MWABALUHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2512",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "MWALIGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2513",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "NGOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2514",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "NGWELI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2515",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "NYAMAHONA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2516",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "NYAMATONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2517",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "NYAMAZUGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2518",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "NYAMPULUKANO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2519",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "NYAMTELELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2520",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "NYANCHENCHE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2521",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "SENGEREMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2522",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "SIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2523",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "TABARUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2524",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "TAMABU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2525",
   "FIELD2": "Mwanza",
   "FIELD3": "Sengerema DC",
   "FIELD4": "TUNYENYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2526",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "BUGUZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2527",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "BUKANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2528",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "BUKIKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2529",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "BUKINDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2530",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "BUKONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2531",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "BUSANGUMUGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2532",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "BWIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2533",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "BWISYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2534",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "IGALLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2535",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "IRUGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2536",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "KAKEREGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2537",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "LUGONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2538",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "MIBUNGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2539",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "MUKITUNTU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2540",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "MUMBUGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2541",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "MURITI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2542",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "NAKATUNGURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2543",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "NAKOZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2544",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "NAMAGONDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2545",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "NANSIO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2546",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "NDURUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2547",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "NYAMANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2548",
   "FIELD2": "Mwanza",
   "FIELD3": "Ukerewe DC",
   "FIELD4": "PIUS MSEKWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2549",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "CHIEF KIDULILE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2550",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "IKOVO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2551",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "KAYAO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2552",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "KETEWAKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2553",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "LUANA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2554",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "LUGARAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2555",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "MADILU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2556",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "MADUNDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2557",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "MAKONDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2558",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "MANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2559",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "MAVALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2560",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "MAVANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2561",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "MCHUCHUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2562",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "MT LIVINGSTONE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2563",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "MT MASUSA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2564",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "MUNDINDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2565",
   "FIELD2": "Njombe",
   "FIELD3": "Ludewa DC",
   "FIELD4": "ULAYASI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2566",
   "FIELD2": "Njombe",
   "FIELD3": "Makambako TC",
   "FIELD4": "DEO SANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2567",
   "FIELD2": "Njombe",
   "FIELD3": "Makambako TC",
   "FIELD4": "KIPAGAMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2568",
   "FIELD2": "Njombe",
   "FIELD3": "Makambako TC",
   "FIELD4": "KITANDILILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2569",
   "FIELD2": "Njombe",
   "FIELD3": "Makambako TC",
   "FIELD4": "LYAMKENA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2570",
   "FIELD2": "Njombe",
   "FIELD3": "Makambako TC",
   "FIELD4": "MAGUVANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2571",
   "FIELD2": "Njombe",
   "FIELD3": "Makambako TC",
   "FIELD4": "MAHONGOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2572",
   "FIELD2": "Njombe",
   "FIELD3": "Makambako TC",
   "FIELD4": "MAKAMBAKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2573",
   "FIELD2": "Njombe",
   "FIELD3": "Makambako TC",
   "FIELD4": "MLOWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2574",
   "FIELD2": "Njombe",
   "FIELD3": "Makambako TC",
   "FIELD4": "MTIMBWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2575",
   "FIELD2": "Njombe",
   "FIELD3": "Makambako TC",
   "FIELD4": "MUKILIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2576",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "IKUWO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2577",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "IPELELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2578",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "IPEPO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2579",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "ISAPULANO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2580",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "IWAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2581",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "KINYIKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2582",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "KIPAGALO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2583",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "KITULO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2584",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "LUPALILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2585",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "LUPILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2586",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "MAKETE GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2587",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "MANGOTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2588",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "MATAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2589",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "MBALATSE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2590",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "MLONDWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2591",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "MT CHAFUKWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2592",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "MWAKAVUTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2593",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "UKWAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2594",
   "FIELD2": "Njombe",
   "FIELD3": "Makete DC",
   "FIELD4": "USILILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2595",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe DC",
   "FIELD4": "IDAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2596",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe DC",
   "FIELD4": "IKUNA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2597",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe DC",
   "FIELD4": "ITIPINGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2598",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe DC",
   "FIELD4": "J M MAKWETA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2599",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe DC",
   "FIELD4": "KIDEGEMBYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2600",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe DC",
   "FIELD4": "LUPEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2601",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe DC",
   "FIELD4": "MANYUNYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2602",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe DC",
   "FIELD4": "MFRIGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2603",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe DC",
   "FIELD4": "MULUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2604",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe DC",
   "FIELD4": "NINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2605",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe DC",
   "FIELD4": "SOVI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2606",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe TC",
   "FIELD4": "ANNE MAKINDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2607",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe TC",
   "FIELD4": "KIFANYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2608",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe TC",
   "FIELD4": "LUHOLOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2609",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe TC",
   "FIELD4": "MABATINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2610",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe TC",
   "FIELD4": "MAHEVE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2611",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe TC",
   "FIELD4": "MATOLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2612",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe TC",
   "FIELD4": "MBEYELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2613",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe TC",
   "FIELD4": "MGOLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2614",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe TC",
   "FIELD4": "MPECHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2615",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe TC",
   "FIELD4": "NJOMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2616",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe TC",
   "FIELD4": "ULIWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2617",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe TC",
   "FIELD4": "UWEMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2618",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe TC",
   "FIELD4": "VIZIWI NJOMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2619",
   "FIELD2": "Njombe",
   "FIELD3": "Njombe TC",
   "FIELD4": "YAKOBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2620",
   "FIELD2": "Njombe",
   "FIELD3": "Wanging'ombe DC",
   "FIELD4": "IGIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2621",
   "FIELD2": "Njombe",
   "FIELD3": "Wanging'ombe DC",
   "FIELD4": "IGOSI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2622",
   "FIELD2": "Njombe",
   "FIELD3": "Wanging'ombe DC",
   "FIELD4": "IGWACHANYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2623",
   "FIELD2": "Njombe",
   "FIELD3": "Wanging'ombe DC",
   "FIELD4": "ILEMBULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2624",
   "FIELD2": "Njombe",
   "FIELD3": "Wanging'ombe DC",
   "FIELD4": "KIJOMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2625",
   "FIELD2": "Njombe",
   "FIELD3": "Wanging'ombe DC",
   "FIELD4": "LUDUGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2626",
   "FIELD2": "Njombe",
   "FIELD3": "Wanging'ombe DC",
   "FIELD4": "MAKOGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2627",
   "FIELD2": "Njombe",
   "FIELD3": "Wanging'ombe DC",
   "FIELD4": "MARIA NYERERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2628",
   "FIELD2": "Njombe",
   "FIELD3": "Wanging'ombe DC",
   "FIELD4": "MOUNT KIPENGERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2629",
   "FIELD2": "Njombe",
   "FIELD3": "Wanging'ombe DC",
   "FIELD4": "PHILIP MANGULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2630",
   "FIELD2": "Njombe",
   "FIELD3": "Wanging'ombe DC",
   "FIELD4": "SAJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2631",
   "FIELD2": "Njombe",
   "FIELD3": "Wanging'ombe DC",
   "FIELD4": "THOMAS NYIMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2632",
   "FIELD2": "Njombe",
   "FIELD3": "Wanging'ombe DC",
   "FIELD4": "ULEMBWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2633",
   "FIELD2": "Njombe",
   "FIELD3": "Wanging'ombe DC",
   "FIELD4": "USUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2634",
   "FIELD2": "Njombe",
   "FIELD3": "Wanging'ombe DC",
   "FIELD4": "WANGINGOMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2635",
   "FIELD2": "Njombe",
   "FIELD3": "Wanging'ombe DC",
   "FIELD4": "WANIKE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2636",
   "FIELD2": "Rukwa",
   "FIELD3": "Kalambo DC",
   "FIELD4": "CHISENGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2637",
   "FIELD2": "Rukwa",
   "FIELD3": "Kalambo DC",
   "FIELD4": "KALAMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2638",
   "FIELD2": "Rukwa",
   "FIELD3": "Kalambo DC",
   "FIELD4": "KALEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2639",
   "FIELD2": "Rukwa",
   "FIELD3": "Kalambo DC",
   "FIELD4": "KANYELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2640",
   "FIELD2": "Rukwa",
   "FIELD3": "Kalambo DC",
   "FIELD4": "KASANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2641",
   "FIELD2": "Rukwa",
   "FIELD3": "Kalambo DC",
   "FIELD4": "KATAZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2642",
   "FIELD2": "Rukwa",
   "FIELD3": "Kalambo DC",
   "FIELD4": "MACHINDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2643",
   "FIELD2": "Rukwa",
   "FIELD3": "Kalambo DC",
   "FIELD4": "MAMBWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2644",
   "FIELD2": "Rukwa",
   "FIELD3": "Kalambo DC",
   "FIELD4": "MATAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2645",
   "FIELD2": "Rukwa",
   "FIELD3": "Kalambo DC",
   "FIELD4": "MSANZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2646",
   "FIELD2": "Rukwa",
   "FIELD3": "Kalambo DC",
   "FIELD4": "MWAZYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2647",
   "FIELD2": "Rukwa",
   "FIELD3": "Kalambo DC",
   "FIELD4": "MWIMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2648",
   "FIELD2": "Rukwa",
   "FIELD3": "Kalambo DC",
   "FIELD4": "NAMEMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2649",
   "FIELD2": "Rukwa",
   "FIELD3": "Kalambo DC",
   "FIELD4": "ULUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2650",
   "FIELD2": "Rukwa",
   "FIELD3": "Kalambo DC",
   "FIELD4": "ZENGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2651",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "CHALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2652",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "ISALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2653",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "KABWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2654",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "KALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2655",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "KATE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2656",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "KIPANDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2657",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "KIPILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2658",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "KIRANDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2659",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "KORONGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2660",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "MASHETE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2661",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "MILUNDIKWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2662",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "MKANGALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2663",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "MKOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2664",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "MKWAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2665",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "MTENGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2666",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "NINDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2667",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "NKASI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2668",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "NKOMOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2669",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "NKUNDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2670",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "NTUCHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2671",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "SINTALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2672",
   "FIELD2": "Rukwa",
   "FIELD3": "Nkasi DC",
   "FIELD4": "WAMPEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2673",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "ILEMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2674",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "KAOZE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2675",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "KAPENTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2676",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "KIKWALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2677",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "KIPETA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2678",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "KWELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2679",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "LULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2680",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "LUSAKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2681",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "MAKUZANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2682",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "MAZOKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2683",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "MIANGALUA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2684",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "MILENIA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2685",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "MPUI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2686",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "MZINDAKAYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2687",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "UCHILE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2688",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "UNYIHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2689",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga DC",
   "FIELD4": "VUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2690",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "CHANJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2691",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "IPEPA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2692",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "ITWELELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2693",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "KALANGASA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2694",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "KANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2695",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "KANTALAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2696",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "KATUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2697",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "KICHEMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2698",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "KILIMANI MAWENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2699",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "KIZWITE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2700",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "LUKANGAO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2701",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "MAFULALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2702",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "MAZWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2703",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "MBIZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2704",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "MHAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2705",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "MTIPE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2706",
   "FIELD2": "Rukwa",
   "FIELD3": "Sumbawanga MC",
   "FIELD4": "SUMBAWANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2707",
   "FIELD2": "Ruvuma",
   "FIELD3": "Madaba DC",
   "FIELD4": "GUMBIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2708",
   "FIELD2": "Ruvuma",
   "FIELD3": "Madaba DC",
   "FIELD4": "IFINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2709",
   "FIELD2": "Ruvuma",
   "FIELD3": "Madaba DC",
   "FIELD4": "LIPUPUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2710",
   "FIELD2": "Ruvuma",
   "FIELD3": "Madaba DC",
   "FIELD4": "MADABA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2711",
   "FIELD2": "Ruvuma",
   "FIELD3": "Madaba DC",
   "FIELD4": "MAGINGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2712",
   "FIELD2": "Ruvuma",
   "FIELD3": "Madaba DC",
   "FIELD4": "MAHANJE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2713",
   "FIELD2": "Ruvuma",
   "FIELD3": "Madaba DC",
   "FIELD4": "NGULUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2714",
   "FIELD2": "Ruvuma",
   "FIELD3": "Madaba DC",
   "FIELD4": "WINO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2715",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "HAGATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2716",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "HILELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2717",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "KIAMILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2718",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "KIGONSERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2719",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "KIHANGIMAHUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2720",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "KIPOLOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2721",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "KITURA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2722",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "LANGIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2723",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "LINDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2724",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "LITEMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2725",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "LITUMBANDYOSI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2726",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "LUHAGARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2727",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "LULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2728",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "MAGUU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2729",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "MAHILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2730",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "MATIRI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2731",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "MBINGA GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2732",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "MBUJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2733",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "MIKALANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2734",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "MIPARU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2735",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "MKAKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2736",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "MKOHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2737",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "MKUMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2738",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "MKUWANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2739",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "NAMSWEA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2740",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "NYONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2741",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "RUANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2742",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "UKATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2743",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga DC",
   "FIELD4": "WUKIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2744",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga TC",
   "FIELD4": "DR A M SHEIN",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2745",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga TC",
   "FIELD4": "KIKOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2746",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga TC",
   "FIELD4": "KINDIMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2747",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga TC",
   "FIELD4": "LUHUWIKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2748",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga TC",
   "FIELD4": "LUSETU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2749",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga TC",
   "FIELD4": "MAKITA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2750",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga TC",
   "FIELD4": "MBAMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2751",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga TC",
   "FIELD4": "MBANGAMAO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2752",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga TC",
   "FIELD4": "MBINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2753",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga TC",
   "FIELD4": "MKWAYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2754",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga TC",
   "FIELD4": "NDELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2755",
   "FIELD2": "Ruvuma",
   "FIELD3": "Mbinga TC",
   "FIELD4": "NGWILIZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2756",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "KIMOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2757",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "KORIDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2758",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "LISIMONJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2759",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "LUCHILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2760",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "LUEGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2761",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "LUKIMWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2762",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "LUNA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2763",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "MAGAZINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2764",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "MBUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2765",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "MGOMBASI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2766",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "MKOMANILE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2767",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "MSINDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2768",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "MTAKANINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2769",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "MWALIKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2770",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "NAHIMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2771",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "NAMABENGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2772",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "NANUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2773",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "NARWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2774",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "NASULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2775",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "PAMOJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2776",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "RWINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2777",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "SASAWALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2778",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "SELOUS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2779",
   "FIELD2": "Ruvuma",
   "FIELD3": "Namtumbo DC",
   "FIELD4": "UTWANGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2780",
   "FIELD2": "Ruvuma",
   "FIELD3": "Nyasa DC",
   "FIELD4": "ENG STELLA MANYANYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2781",
   "FIELD2": "Ruvuma",
   "FIELD3": "Nyasa DC",
   "FIELD4": "KILUMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2782",
   "FIELD2": "Ruvuma",
   "FIELD3": "Nyasa DC",
   "FIELD4": "KINGERIKITI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2783",
   "FIELD2": "Ruvuma",
   "FIELD3": "Nyasa DC",
   "FIELD4": "LIMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2784",
   "FIELD2": "Ruvuma",
   "FIELD3": "Nyasa DC",
   "FIELD4": "LIPARAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2785",
   "FIELD2": "Ruvuma",
   "FIELD3": "Nyasa DC",
   "FIELD4": "LITUHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2786",
   "FIELD2": "Ruvuma",
   "FIELD3": "Nyasa DC",
   "FIELD4": "LUNDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2787",
   "FIELD2": "Ruvuma",
   "FIELD3": "Nyasa DC",
   "FIELD4": "MANGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2788",
   "FIELD2": "Ruvuma",
   "FIELD3": "Nyasa DC",
   "FIELD4": "MBAMBA BAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2789",
   "FIELD2": "Ruvuma",
   "FIELD3": "Nyasa DC",
   "FIELD4": "MONICA MBEGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2790",
   "FIELD2": "Ruvuma",
   "FIELD3": "Nyasa DC",
   "FIELD4": "NGUMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2791",
   "FIELD2": "Ruvuma",
   "FIELD3": "Nyasa DC",
   "FIELD4": "NYASA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2792",
   "FIELD2": "Ruvuma",
   "FIELD3": "Nyasa DC",
   "FIELD4": "ST PAULS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2793",
   "FIELD2": "Ruvuma",
   "FIELD3": "Nyasa DC",
   "FIELD4": "TINGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2794",
   "FIELD2": "Ruvuma",
   "FIELD3": "Nyasa DC",
   "FIELD4": "URBERKANT",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2795",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea DC",
   "FIELD4": "BARABARANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2796",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea DC",
   "FIELD4": "DARAJAMBILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2797",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea DC",
   "FIELD4": "KILAGANO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2798",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea DC",
   "FIELD4": "LIGANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2799",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea DC",
   "FIELD4": "LITAPWASI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2800",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea DC",
   "FIELD4": "LUPUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2801",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea DC",
   "FIELD4": "MAGAGURA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2802",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea DC",
   "FIELD4": "MAPOSENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2803",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea DC",
   "FIELD4": "MATIMIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2804",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea DC",
   "FIELD4": "MHALULE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2805",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea DC",
   "FIELD4": "MPITIMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2806",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea DC",
   "FIELD4": "MUHUKURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2807",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea DC",
   "FIELD4": "NALIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2808",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea DC",
   "FIELD4": "NAMATUHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2809",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea DC",
   "FIELD4": "NAMIHORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2810",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea DC",
   "FIELD4": "NDONGOSI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2811",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "BOMBAMBILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2812",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "CHABRUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2813",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "CHANDARUA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2814",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "EMMANUEL NCHIMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2815",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "KALEMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2816",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "LIZABONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2817",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "LONDONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2818",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "LUKALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2819",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "LUWAWASI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2820",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "MASHUJAA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2821",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "MATARAWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2822",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "MATEKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2823",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "MATOGORO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2824",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "MBULANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2825",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "MDANDAMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2826",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "MFARANYAKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2827",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "MLETELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2828",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "MSAMALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2829",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "RUVUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2830",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "SILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2831",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "SONGEA BOYS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2832",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "SONGEA GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2833",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "SUBIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2834",
   "FIELD2": "Ruvuma",
   "FIELD3": "Songea MC",
   "FIELD4": "ZIMANIMOTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2835",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "FRANK WESTON",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2836",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "KIDODOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2837",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "LIGOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2838",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "LIGUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2839",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "LUKUMBULE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2840",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "MARUMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2841",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "MASONYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2842",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "MATAKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2843",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "MATEMANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2844",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "MBESA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2845",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "MCHOTEKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2846",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "MGOMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2847",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "MTUTURA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2848",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "MUHUWESI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2849",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "NAKAPANYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2850",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "NALASI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2851",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "NAMASAKATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2852",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "NAMPUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2853",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "NAMWINYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2854",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "NANDEMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2855",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "SEMENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2856",
   "FIELD2": "Ruvuma",
   "FIELD3": "Tunduru DC",
   "FIELD4": "TUNDURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2857",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kahama TC",
   "FIELD4": "ABDULRAHIM BUSOKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2858",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kahama TC",
   "FIELD4": "BUGISHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2859",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kahama TC",
   "FIELD4": "BUKAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2860",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kahama TC",
   "FIELD4": "ISAGEHE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2861",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kahama TC",
   "FIELD4": "ISUNUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2862",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kahama TC",
   "FIELD4": "KINAGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2863",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kahama TC",
   "FIELD4": "KISHIMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2864",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kahama TC",
   "FIELD4": "KITWANA",
   "FIELD5": "1329506",
   "FIELD6": ""
 },
 {
   "FIELD1": "2865",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kahama TC",
   "FIELD4": "MPERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2866",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kahama TC",
   "FIELD4": "MWENDAKULIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2867",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kahama TC",
   "FIELD4": "NGOGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2868",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kahama TC",
   "FIELD4": "NYANDEKWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2869",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kahama TC",
   "FIELD4": "NYASHIMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2870",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kahama TC",
   "FIELD4": "NYASUBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2871",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kahama TC",
   "FIELD4": "NYIHOGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2872",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kahama TC",
   "FIELD4": "SEEKE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2873",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "BUBIKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2874",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "BULEKELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2875",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "BUNAMBIYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2876",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "BUSIYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2877",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "IDUKILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2878",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "IGAGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2879",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "KILOLELI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2880",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "KISHAPU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2881",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "MAGANZO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2882",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "MANGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2883",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "MIPA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2884",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "MWADUI TECH",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2885",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "MWAKIPOYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2886",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "MWAMADULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2887",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "MWAMALASA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2888",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "MWAMASHELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2889",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "MWATAGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2890",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "MWIGUMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2891",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "NGOFILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2892",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "SHINYANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2893",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "SOMAGEDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2894",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "SONGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2895",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "TALAGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2896",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "UCHUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2897",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "UKENYENGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2898",
   "FIELD2": "Shinyanga",
   "FIELD3": "Kishapu DC",
   "FIELD4": "WISHITELEJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2899",
   "FIELD2": "Shinyanga",
   "FIELD3": "Msalala DC",
   "FIELD4": "BALOHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2900",
   "FIELD2": "Shinyanga",
   "FIELD3": "Msalala DC",
   "FIELD4": "BUGARAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2901",
   "FIELD2": "Shinyanga",
   "FIELD3": "Msalala DC",
   "FIELD4": "BULIGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2902",
   "FIELD2": "Shinyanga",
   "FIELD3": "Msalala DC",
   "FIELD4": "BULYANHULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2903",
   "FIELD2": "Shinyanga",
   "FIELD3": "Msalala DC",
   "FIELD4": "BUSANGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2904",
   "FIELD2": "Shinyanga",
   "FIELD3": "Msalala DC",
   "FIELD4": "ISAKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2905",
   "FIELD2": "Shinyanga",
   "FIELD3": "Msalala DC",
   "FIELD4": "JANA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2906",
   "FIELD2": "Shinyanga",
   "FIELD3": "Msalala DC",
   "FIELD4": "LUNGUYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2907",
   "FIELD2": "Shinyanga",
   "FIELD3": "Msalala DC",
   "FIELD4": "MWALUGULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2908",
   "FIELD2": "Shinyanga",
   "FIELD3": "Msalala DC",
   "FIELD4": "MWAMANDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2909",
   "FIELD2": "Shinyanga",
   "FIELD3": "Msalala DC",
   "FIELD4": "MWL NYERERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2910",
   "FIELD2": "Shinyanga",
   "FIELD3": "Msalala DC",
   "FIELD4": "NGAYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2911",
   "FIELD2": "Shinyanga",
   "FIELD3": "Msalala DC",
   "FIELD4": "NTOBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2912",
   "FIELD2": "Shinyanga",
   "FIELD3": "Msalala DC",
   "FIELD4": "NYIKOBOKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2913",
   "FIELD2": "Shinyanga",
   "FIELD3": "Msalala DC",
   "FIELD4": "SEGESE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2914",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "DIDIA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2915",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "GEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2916",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "IHUGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2917",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "ILOLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2918",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "IMESELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2919",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "ISELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2920",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "ISELAMAGAZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2921",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "ITWANGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2922",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "KASELYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2923",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "KITULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2924",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "LYABUKANDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2925",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "LYABUSALU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2926",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "MASENGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2927",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "MISHEPO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2928",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "MWALUKWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2929",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "MWANTINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2930",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "NGWAKITOLYO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2931",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "PANDAGICHIZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2932",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "SALAWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2933",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "SAMUYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2934",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "SHINGITA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2935",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "SOLWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2936",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "TINDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2937",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "TINDE GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2938",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "USANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2939",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "USULE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2940",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga DC",
   "FIELD4": "ZUNZULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2941",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "BUSULWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2942",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "CHAMAGUHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2943",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "IBINZAMATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2944",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "KIZUMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2945",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "KOLANDOTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2946",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "MASEKELO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2947",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "MAZINGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2948",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "MWAMALILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2949",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "MWASELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2950",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "MWAWAZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2951",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "NDALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2952",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "NGOKOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2953",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "OLD SHINYANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2954",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "RAJANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2955",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "TOWN",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2956",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "UHURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2957",
   "FIELD2": "Shinyanga",
   "FIELD3": "Shinyanga MC",
   "FIELD4": "UZOGORE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2958",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "BULUNGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2959",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "CHAMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2960",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "CHONA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2961",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "DAKAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2962",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "IDAHINA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2963",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "IGUNDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2964",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "IGWAMANONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2965",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "KINAMAPULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2966",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "KISUKE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2967",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "MPUNZE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2968",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "MWELI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2969",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "NYANKENDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2970",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "SABASABINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2971",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "UKUNE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2972",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "ULEWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "2973",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "ULOWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "TOTAL",
   "FIELD6": ""
 },
 {
   "FIELD1": "2974",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "USHETU",
   "FIELD5": "3301926",
   "FIELD6": ""
 },
 {
   "FIELD1": "2975",
   "FIELD2": "Shinyanga",
   "FIELD3": "Ushetu DC",
   "FIELD4": "UYOGO",
   "FIELD5": "3841552",
   "FIELD6": ""
 },
 {
   "FIELD1": "2976",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "BANEMHI",
   "FIELD5": "2884021",
   "FIELD6": ""
 },
 {
   "FIELD1": "2977",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "BYUNA",
   "FIELD5": "3305195",
   "FIELD6": ""
 },
 {
   "FIELD1": "2978",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "DUTWA",
   "FIELD5": "8800790",
   "FIELD6": ""
 },
 {
   "FIELD1": "2979",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "GAMBOSI",
   "FIELD5": "483689",
   "FIELD6": ""
 },
 {
   "FIELD1": "2980",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "GASUMA",
   "FIELD5": "4434018",
   "FIELD6": ""
 },
 {
   "FIELD1": "2981",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "GEGEDI",
   "FIELD5": "6695568",
   "FIELD6": ""
 },
 {
   "FIELD1": "2982",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "IBULYU",
   "FIELD5": "2317747",
   "FIELD6": ""
 },
 {
   "FIELD1": "2983",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "IGAGANULWA",
   "FIELD5": "5237185",
   "FIELD6": ""
 },
 {
   "FIELD1": "2984",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "IKINABUSHU",
   "FIELD5": "2937102",
   "FIELD6": ""
 },
 {
   "FIELD1": "2985",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "IKUNGULYABASHASHI",
   "FIELD5": "2839710",
   "FIELD6": ""
 },
 {
   "FIELD1": "2986",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "ITUBUKILO",
   "FIELD5": "2457374",
   "FIELD6": ""
 },
 {
   "FIELD1": "2987",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "KASOLI",
   "FIELD5": "5027815",
   "FIELD6": ""
 },
 {
   "FIELD1": "2988",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "KILABELA",
   "FIELD5": "2258369",
   "FIELD6": ""
 },
 {
   "FIELD1": "2989",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "MISWAKI",
   "FIELD5": "6607906",
   "FIELD6": ""
 },
 {
   "FIELD1": "2990",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "MWADOBANA",
   "FIELD5": "1459320",
   "FIELD6": ""
 },
 {
   "FIELD1": "2991",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "MWAMLAPA",
   "FIELD5": "4203576",
   "FIELD6": ""
 },
 {
   "FIELD1": "2992",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "MWANTIMBA",
   "FIELD5": "12116261",
   "FIELD6": ""
 },
 {
   "FIELD1": "2993",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "NKINDWABIYE",
   "FIELD5": "4929472",
   "FIELD6": ""
 },
 {
   "FIELD1": "2994",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "NKOLOLO",
   "FIELD5": "11012958",
   "FIELD6": ""
 },
 {
   "FIELD1": "2995",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "NYASOSI",
   "FIELD5": "6232211",
   "FIELD6": ""
 },
 {
   "FIELD1": "2996",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "NYAWA",
   "FIELD5": "5613274",
   "FIELD6": ""
 },
 {
   "FIELD1": "2997",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "SAKWE",
   "FIELD5": "3123753",
   "FIELD6": ""
 },
 {
   "FIELD1": "2998",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi DC",
   "FIELD4": "SAPIWI",
   "FIELD5": "10332806",
   "FIELD6": ""
 },
 {
   "FIELD1": "2999",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi TC",
   "FIELD4": "BARIADI",
   "FIELD5": "13253919",
   "FIELD6": ""
 },
 {
   "FIELD1": "3000",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi TC",
   "FIELD4": "BIASHARA BARIADI",
   "FIELD5": "12590845",
   "FIELD6": ""
 },
 {
   "FIELD1": "3001",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi TC",
   "FIELD4": "CHENGE",
   "FIELD5": "4636154",
   "FIELD6": ""
 },
 {
   "FIELD1": "3002",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi TC",
   "FIELD4": "GIRIKU",
   "FIELD5": "4957552",
   "FIELD6": ""
 },
 {
   "FIELD1": "3003",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi TC",
   "FIELD4": "GUDUWI",
   "FIELD5": "3906278",
   "FIELD6": ""
 },
 {
   "FIELD1": "3004",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi TC",
   "FIELD4": "KIDINDA",
   "FIELD5": "8922448",
   "FIELD6": ""
 },
 {
   "FIELD1": "3005",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi TC",
   "FIELD4": "MAHAHA",
   "FIELD5": "7912407",
   "FIELD6": ""
 },
 {
   "FIELD1": "3006",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi TC",
   "FIELD4": "MBITI",
   "FIELD5": "3079770",
   "FIELD6": ""
 },
 {
   "FIELD1": "3007",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi TC",
   "FIELD4": "NGWANGWALI",
   "FIELD5": "3212719",
   "FIELD6": ""
 },
 {
   "FIELD1": "3008",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi TC",
   "FIELD4": "NTUZU",
   "FIELD5": "3243308",
   "FIELD6": ""
 },
 {
   "FIELD1": "3009",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi TC",
   "FIELD4": "NYAKABINDI",
   "FIELD5": "3949272",
   "FIELD6": ""
 },
 {
   "FIELD1": "3010",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi TC",
   "FIELD4": "OLD MASWA",
   "FIELD5": "3493024",
   "FIELD6": ""
 },
 {
   "FIELD1": "3011",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi TC",
   "FIELD4": "SIMIYU",
   "FIELD5": "7115703",
   "FIELD6": ""
 },
 {
   "FIELD1": "3012",
   "FIELD2": "Simiyu",
   "FIELD3": "Bariadi TC",
   "FIELD4": "SOMANDA",
   "FIELD5": "4075784",
   "FIELD6": ""
 },
 {
   "FIELD1": "3013",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "ANTHONY MTAKA",
   "FIELD5": "10320692",
   "FIELD6": ""
 },
 {
   "FIELD1": "3014",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "BADUGU",
   "FIELD5": "6496183",
   "FIELD6": ""
 },
 {
   "FIELD1": "3015",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "DR CHEGENI",
   "FIELD5": "2825746",
   "FIELD6": ""
 },
 {
   "FIELD1": "3016",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "IGALUKILO",
   "FIELD5": "5496228",
   "FIELD6": ""
 },
 {
   "FIELD1": "3017",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "KABITA",
   "FIELD5": "11378390",
   "FIELD6": ""
 },
 {
   "FIELD1": "3018",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "KALEMELA",
   "FIELD5": "5481656",
   "FIELD6": ""
 },
 {
   "FIELD1": "3019",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "KIJELESHI",
   "FIELD5": "4618019",
   "FIELD6": ""
 },
 {
   "FIELD1": "3020",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "KISHAMAPANDA",
   "FIELD5": "6588317",
   "FIELD6": ""
 },
 {
   "FIELD1": "3021",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "LAMADI",
   "FIELD5": "9565714",
   "FIELD6": ""
 },
 {
   "FIELD1": "3022",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "MALILI",
   "FIELD5": "5842298",
   "FIELD6": ""
 },
 {
   "FIELD1": "3023",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "MASANZA",
   "FIELD5": "5331220",
   "FIELD6": ""
 },
 {
   "FIELD1": "3024",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "MKULA",
   "FIELD5": "7175339",
   "FIELD6": ""
 },
 {
   "FIELD1": "3025",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "MWAMAGIGISI",
   "FIELD5": "4203766",
   "FIELD6": ""
 },
 {
   "FIELD1": "3026",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "MWASAMBA",
   "FIELD5": "4698180",
   "FIELD6": ""
 },
 {
   "FIELD1": "3027",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "NASSA",
   "FIELD5": "6995602",
   "FIELD6": ""
 },
 {
   "FIELD1": "3028",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "NGASAMO",
   "FIELD5": "10791651",
   "FIELD6": ""
 },
 {
   "FIELD1": "3029",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "NYALUHANDE",
   "FIELD5": "5381412",
   "FIELD6": ""
 },
 {
   "FIELD1": "3030",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "NYANGWE",
   "FIELD5": "5052436",
   "FIELD6": ""
 },
 {
   "FIELD1": "3031",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "SHIGALA",
   "FIELD5": "4809917",
   "FIELD6": ""
 },
 {
   "FIELD1": "3032",
   "FIELD2": "Simiyu",
   "FIELD3": "Busega DC",
   "FIELD4": "SOGESCA",
   "FIELD5": "7589881",
   "FIELD6": ""
 },
 {
   "FIELD1": "3033",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "BUDALABUJIGA",
   "FIELD5": "3159879",
   "FIELD6": ""
 },
 {
   "FIELD1": "3034",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "BUKINGWAMINZI",
   "FIELD5": "2393548",
   "FIELD6": ""
 },
 {
   "FIELD1": "3035",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "BUMERA",
   "FIELD5": "1746772",
   "FIELD6": ""
 },
 {
   "FIELD1": "3036",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "BUNAMHALA MB",
   "FIELD5": "4754429",
   "FIELD6": ""
 },
 {
   "FIELD1": "3037",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "CHINAMILI",
   "FIELD5": "2466561",
   "FIELD6": ""
 },
 {
   "FIELD1": "3038",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "HABIYA",
   "FIELD5": "1862019",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3039",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "IDOSELO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3040",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "IKINDILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3041",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "IKUNGULIPU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3042",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "INALO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3043",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "ITILIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3044",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "KABALE BARIADI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3045",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "KANADI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3046",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "KINANGWELI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3047",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "LAGANGABILILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3048",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "LAINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3049",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "LUNGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3050",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "MADILANA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3051",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "MAHEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3052",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "MHUNZE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3053",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "MWAKILANGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3054",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "MWALUSHU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3055",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "MWAMTANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3056",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "MWASWALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3057",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "NDOLELEJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3058",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "NKOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3059",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "SAGATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3060",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "SHISHANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3061",
   "FIELD2": "Simiyu",
   "FIELD3": "Itilima DC",
   "FIELD4": "SUNZULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3062",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "BADI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3063",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "BINZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3064",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "BUCHAMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3065",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "BUDEKWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3066",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "BUSHASHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3067",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "IPILILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3068",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "ISANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3069",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "ITULE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3070",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "JIJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3071",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "KADOTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3072",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "KINAMWIGULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3073",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "KULIMI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3074",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "MAJEBELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3075",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "MALAMPAKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3076",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "MASELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3077",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "MASUMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3078",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "MASWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3079",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "MATABA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3080",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "MWABAYANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3081",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "MWAGALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3082",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "MWAKALEKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3083",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "MWAMANENGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3084",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "MWANDETE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3085",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "MWASAYI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3086",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "NGHUMBU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3087",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "NGULIGULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3088",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "NGWIGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3089",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "NYABUBINZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3090",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "NYALIKUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3091",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "SALAGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3092",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "SANGAMWALUGESHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3093",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "SENANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3094",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "SENGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3095",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "SHISHIYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3096",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "SUKUMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3097",
   "FIELD2": "Simiyu",
   "FIELD3": "Maswa DC",
   "FIELD4": "ZEBEYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3098",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "BUKUNDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3099",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "IMALASEKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3100",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "ITINJE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3101",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "KIMALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3102",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "KISESA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3103",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "LINGEKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "TOTAL",
   "FIELD6": ""
 },
 {
   "FIELD1": "3104",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "LUBIGA",
   "FIELD5": "3235832",
   "FIELD6": ""
 },
 {
   "FIELD1": "3105",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "LYUSA",
   "FIELD5": "1980484",
   "FIELD6": ""
 },
 {
   "FIELD1": "3106",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "MAKAO",
   "FIELD5": "417268",
   "FIELD6": ""
 },
 {
   "FIELD1": "3107",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "MEATU",
   "FIELD5": "8494917",
   "FIELD6": ""
 },
 {
   "FIELD1": "3108",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "MWABUMA",
   "FIELD5": "4292073",
   "FIELD6": ""
 },
 {
   "FIELD1": "3109",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "MWABUSALU",
   "FIELD5": "3048092",
   "FIELD6": ""
 },
 {
   "FIELD1": "3110",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "MWAKALUBA",
   "FIELD5": "2038152",
   "FIELD6": ""
 },
 {
   "FIELD1": "3111",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "MWAMALOLE",
   "FIELD5": "1760647",
   "FIELD6": ""
 },
 {
   "FIELD1": "3112",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "MWAMANONGU",
   "FIELD5": "1994118",
   "FIELD6": ""
 },
 {
   "FIELD1": "3113",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "MWAMISHALI",
   "FIELD5": "4079522",
   "FIELD6": ""
 },
 {
   "FIELD1": "3114",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "MWANDOYA",
   "FIELD5": "6991062",
   "FIELD6": ""
 },
 {
   "FIELD1": "3115",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "MWANJOLO",
   "FIELD5": "2446198",
   "FIELD6": ""
 },
 {
   "FIELD1": "3116",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "MWAUKOLI",
   "FIELD5": "2164575",
   "FIELD6": ""
 },
 {
   "FIELD1": "3117",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "NGHOBOKO",
   "FIELD5": "2899988",
   "FIELD6": ""
 },
 {
   "FIELD1": "3118",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "NYALANJA",
   "FIELD5": "3246332",
   "FIELD6": ""
 },
 {
   "FIELD1": "3119",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "PAJI",
   "FIELD5": "3463753",
   "FIELD6": ""
 },
 {
   "FIELD1": "3120",
   "FIELD2": "Simiyu",
   "FIELD3": "Meatu DC",
   "FIELD4": "SAKASAKA",
   "FIELD5": "4728060",
   "FIELD6": ""
 },
 {
   "FIELD1": "3121",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "DADU",
   "FIELD5": "2843169",
   "FIELD6": ""
 },
 {
   "FIELD1": "3122",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "DR ALLY M SHEIN",
   "FIELD5": "3985589",
   "FIELD6": ""
 },
 {
   "FIELD1": "3123",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "IGHOMBWE",
   "FIELD5": "1526935",
   "FIELD6": ""
 },
 {
   "FIELD1": "3124",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "IGLANSONI",
   "FIELD5": "1771583",
   "FIELD6": ""
 },
 {
   "FIELD1": "3125",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "IKUNGI",
   "FIELD5": "8866898",
   "FIELD6": ""
 },
 {
   "FIELD1": "3126",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "IRISYA",
   "FIELD5": "2118552",
   "FIELD6": ""
 },
 {
   "FIELD1": "3127",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "ISEKE MUUNGANO",
   "FIELD5": "4378150",
   "FIELD6": ""
 },
 {
   "FIELD1": "3128",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "ISSUNA",
   "FIELD5": "5845998",
   "FIELD6": ""
 },
 {
   "FIELD1": "3129",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "LIGHWA",
   "FIELD5": "2389480",
   "FIELD6": ""
 },
 {
   "FIELD1": "3130",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "MAKIUNGU",
   "FIELD5": "3822190",
   "FIELD6": ""
 },
 {
   "FIELD1": "3131",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "MANGONYI SHANTA",
   "FIELD5": "3173045",
   "FIELD6": ""
 },
 {
   "FIELD1": "3132",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "MASINDA DAY",
   "FIELD5": "5034303",
   "FIELD6": ""
 },
 {
   "FIELD1": "3133",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "MIANDI",
   "FIELD5": "3601923",
   "FIELD6": ""
 },
 {
   "FIELD1": "3134",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "MINYUGHE",
   "FIELD5": "4108362",
   "FIELD6": ""
 },
 {
   "FIELD1": "3135",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "MKIWA",
   "FIELD5": "3109928",
   "FIELD6": ""
 },
 {
   "FIELD1": "3136",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "MKUNGUAKIHENDO",
   "FIELD5": "1792414",
   "FIELD6": ""
 },
 {
   "FIELD1": "3137",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "MSUNGUA",
   "FIELD5": "3092505",
   "FIELD6": ""
 },
 {
   "FIELD1": "3138",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "MTUNDURU",
   "FIELD5": "4973797",
   "FIELD6": ""
 },
 {
   "FIELD1": "3139",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "MUHINTIRI",
   "FIELD5": "3206092",
   "FIELD6": ""
 },
 {
   "FIELD1": "3140",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "MUNGAA",
   "FIELD5": "6377908",
   "FIELD6": ""
 },
 {
   "FIELD1": "3141",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "MUNKINYA",
   "FIELD5": "4129194",
   "FIELD6": ""
 },
 {
   "FIELD1": "3142",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "MWARU",
   "FIELD5": "1840477",
   "FIELD6": ""
 },
 {
   "FIELD1": "3143",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "MWAU",
   "FIELD5": "2462443",
   "FIELD6": ""
 },
 {
   "FIELD1": "3144",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "NTUNTU",
   "FIELD5": "5646043",
   "FIELD6": ""
 },
 {
   "FIELD1": "3145",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "PUMA",
   "FIELD5": "5886053",
   "FIELD6": ""
 },
 {
   "FIELD1": "3146",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "SEPUKA",
   "FIELD5": "3298847",
   "FIELD6": ""
 },
 {
   "FIELD1": "3147",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "SIUYU",
   "FIELD5": "4818774",
   "FIELD6": ""
 },
 {
   "FIELD1": "3148",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "UNYAHATI",
   "FIELD5": "4957223",
   "FIELD6": ""
 },
 {
   "FIELD1": "3149",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "UTAHO",
   "FIELD5": "2252122",
   "FIELD6": ""
 },
 {
   "FIELD1": "3150",
   "FIELD2": "Singida",
   "FIELD3": "Ikungi DC",
   "FIELD4": "WEMBERE",
   "FIELD5": "2969621",
   "FIELD6": ""
 },
 {
   "FIELD1": "3151",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "KASELYA",
   "FIELD5": "4972137",
   "FIELD6": ""
 },
 {
   "FIELD1": "3152",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "KIDARU",
   "FIELD5": "3314141",
   "FIELD6": ""
 },
 {
   "FIELD1": "3153",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "KINAMBEU",
   "FIELD5": "6484436",
   "FIELD6": ""
 },
 {
   "FIELD1": "3154",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "KINAMPANDA",
   "FIELD5": "6388602",
   "FIELD6": ""
 },
 {
   "FIELD1": "3155",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "KISANA",
   "FIELD5": "1342134",
   "FIELD6": ""
 },
 {
   "FIELD1": "3156",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "KISIRIRI",
   "FIELD5": "3207460",
   "FIELD6": ""
 },
 {
   "FIELD1": "3157",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "KIZAGA",
   "FIELD5": "7557201",
   "FIELD6": ""
 },
 {
   "FIELD1": "3158",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "KYENGEGE",
   "FIELD5": "5980936",
   "FIELD6": ""
 },
 {
   "FIELD1": "3159",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "LULUMBA",
   "FIELD5": "8528204",
   "FIELD6": ""
 },
 {
   "FIELD1": "3160",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "MBELEKESE",
   "FIELD5": "5129947",
   "FIELD6": ""
 },
 {
   "FIELD1": "3161",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "MGONGO",
   "FIELD5": "2872617",
   "FIELD6": ""
 },
 {
   "FIELD1": "3162",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "MTEKENTE",
   "FIELD5": "2938572",
   "FIELD6": ""
 },
 {
   "FIELD1": "3163",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "MTOA",
   "FIELD5": "4526305",
   "FIELD6": ""
 },
 {
   "FIELD1": "3164",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "MUKULU",
   "FIELD5": "3272946",
   "FIELD6": ""
 },
 {
   "FIELD1": "3165",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "NDAGO",
   "FIELD5": "2955666",
   "FIELD6": ""
 },
 {
   "FIELD1": "3166",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "NEW KIOMBOI",
   "FIELD5": "6067913",
   "FIELD6": ""
 },
 {
   "FIELD1": "3167",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "NTWIKE",
   "FIELD5": "4838795",
   "FIELD6": ""
 },
 {
   "FIELD1": "3168",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "SHELUI",
   "FIELD5": "7062178",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3169",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "TULYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3170",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "TUMAINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3171",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "URUGHU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3172",
   "FIELD2": "Singida",
   "FIELD3": "Iramba DC",
   "FIELD4": "USHORA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3173",
   "FIELD2": "Singida",
   "FIELD3": "Itigi DC",
   "FIELD4": "HANDU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3174",
   "FIELD2": "Singida",
   "FIELD3": "Itigi DC",
   "FIELD4": "IDODYANDOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3175",
   "FIELD2": "Singida",
   "FIELD3": "Itigi DC",
   "FIELD4": "IPAMUDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3176",
   "FIELD2": "Singida",
   "FIELD3": "Itigi DC",
   "FIELD4": "ITIGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3177",
   "FIELD2": "Singida",
   "FIELD3": "Itigi DC",
   "FIELD4": "KALEKWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3178",
   "FIELD2": "Singida",
   "FIELD3": "Itigi DC",
   "FIELD4": "KAMENYANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3179",
   "FIELD2": "Singida",
   "FIELD3": "Itigi DC",
   "FIELD4": "KIMADOI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3180",
   "FIELD2": "Singida",
   "FIELD3": "Itigi DC",
   "FIELD4": "MGANDU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3181",
   "FIELD2": "Singida",
   "FIELD3": "Itigi DC",
   "FIELD4": "MITUNDU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3182",
   "FIELD2": "Singida",
   "FIELD3": "Itigi DC",
   "FIELD4": "RUNGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3183",
   "FIELD2": "Singida",
   "FIELD3": "Itigi DC",
   "FIELD4": "SANJARANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3184",
   "FIELD2": "Singida",
   "FIELD3": "Manyoni DC",
   "FIELD4": "CHIKUYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3185",
   "FIELD2": "Singida",
   "FIELD3": "Manyoni DC",
   "FIELD4": "HEKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3186",
   "FIELD2": "Singida",
   "FIELD3": "Manyoni DC",
   "FIELD4": "ISSEKE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3187",
   "FIELD2": "Singida",
   "FIELD3": "Manyoni DC",
   "FIELD4": "KILIMATINDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3188",
   "FIELD2": "Singida",
   "FIELD3": "Manyoni DC",
   "FIELD4": "KINANGALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3189",
   "FIELD2": "Singida",
   "FIELD3": "Manyoni DC",
   "FIELD4": "KINTINKU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3190",
   "FIELD2": "Singida",
   "FIELD3": "Manyoni DC",
   "FIELD4": "KIZIGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3191",
   "FIELD2": "Singida",
   "FIELD3": "Manyoni DC",
   "FIELD4": "MAKANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3192",
   "FIELD2": "Singida",
   "FIELD3": "Manyoni DC",
   "FIELD4": "MAKURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3193",
   "FIELD2": "Singida",
   "FIELD3": "Manyoni DC",
   "FIELD4": "MANYONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3194",
   "FIELD2": "Singida",
   "FIELD3": "Manyoni DC",
   "FIELD4": "MLEWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3195",
   "FIELD2": "Singida",
   "FIELD3": "Manyoni DC",
   "FIELD4": "MWANZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3196",
   "FIELD2": "Singida",
   "FIELD3": "Manyoni DC",
   "FIELD4": "NGAITI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3197",
   "FIELD2": "Singida",
   "FIELD3": "Manyoni DC",
   "FIELD4": "NKONKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3198",
   "FIELD2": "Singida",
   "FIELD3": "Manyoni DC",
   "FIELD4": "SANZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3199",
   "FIELD2": "Singida",
   "FIELD3": "Manyoni DC",
   "FIELD4": "SASAJILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3200",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "CHEMCHEM",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3201",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "GRACE MESAKI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3202",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "GUMANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3203",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "GUNDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3204",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "IBAGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3205",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "IGUGUNO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3206",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "ISANZU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3207",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "JORMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3208",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "KIKHONDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3209",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "KINAMPUNDU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3210",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "KINYANGIRI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3211",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "MALAJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3212",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "MIGANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3213",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "MWANGEZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3214",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "NDUGUTI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3215",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "NKINTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3216",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "SELENGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3217",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "SETH BENJAMIN",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3218",
   "FIELD2": "Singida",
   "FIELD3": "Mkalama DC",
   "FIELD4": "TUMULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3219",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "IKHANODA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3220",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "ILONGERO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3221",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "ITAJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3222",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "KIJOTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3223",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "KINYETO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3224",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "MADASENGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3225",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "MAGHOJOA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3226",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "MAKURO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3227",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "MATUMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3228",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "MERYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3229",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "MIKIWU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3230",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "MISINKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3231",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "MRAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3232",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "MSISI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3233",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "MTINKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3234",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "MUDIDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3235",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "MUGHAMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3236",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "MUGHUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3237",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "MWANAMWEMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3238",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "MWASAUYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3239",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "NGIMU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3240",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "NTONGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3241",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "NYERI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3242",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "POHAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3243",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "SINGITU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3244",
   "FIELD2": "Singida",
   "FIELD3": "Singida DC",
   "FIELD4": "UGHANDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3245",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "DR SALMIN AMOUR",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3246",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "IPEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3247",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "KIMPUNGUA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3248",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "KINDAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3249",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "MANDEWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3250",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "MITUNDURUNI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3251",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "MTAMAA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3252",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "MTIPA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3253",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "MUFUMBU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3254",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "MUGHANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3255",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "MUNGUMAJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3256",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "MWANKOKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3257",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "MWENGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3258",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "SENGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3259",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "UNYAMBWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3260",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "UNYAMIKUMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3261",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "UNYIANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3262",
   "FIELD2": "Singida",
   "FIELD3": "Singida MC",
   "FIELD4": "UTEMINI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3263",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "BUPIGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3264",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "IBABA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3265",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "IKINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3266",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "ILEJE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3267",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "ITALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3268",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "ITUMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3269",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "KAFULE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3270",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "KAKOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3271",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "LUBANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3272",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "LUSWISI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3273",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "MBEBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3274",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "MLALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3275",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "MSOMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3276",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "NAKALULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3277",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "NDOLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3278",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "NGULILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3279",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "NGULUGULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3280",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "SANGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3281",
   "FIELD2": "Songwe",
   "FIELD3": "Ileje DC",
   "FIELD4": "STIVEN KIBONA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3282",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "BARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3283",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "HALUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3284",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "HAMPANGALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3285",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "HEZYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3286",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "IDIMI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3287",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "IGAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3288",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "IGANDUKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3289",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "IGANYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3290",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "IHANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3291",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "ILOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3292",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "INSANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3293",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "IPUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3294",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "ISALALO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3295",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "ISANDULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3296",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "ISANGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3297",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "ITAKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3298",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "ITEPULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3299",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "ITUMPI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3300",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "KILIMAMPIMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3301",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "LUMBILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3302",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "LWATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3303",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "MLANGALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3304",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "MLOWO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3305",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "MSANGAWALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3306",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "MSANKWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3307",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "MSENSE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3308",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "MSIA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3309",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "MYOVIZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3310",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "NALYELYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3311",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "NAMBINZO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3312",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "NANSWILU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3313",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "NDUGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3314",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "NKANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3315",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "NYIMBILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3316",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "NZOVU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3317",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "SHAJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3318",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "SHIKULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3319",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "SHIWINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3320",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "SIMBEGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3321",
   "FIELD2": "Songwe",
   "FIELD3": "Mbozi DC",
   "FIELD4": "VWAWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3322",
   "FIELD2": "Songwe",
   "FIELD3": "Momba DC",
   "FIELD4": "CHIKANAMLILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3323",
   "FIELD2": "Songwe",
   "FIELD3": "Momba DC",
   "FIELD4": "CHILULUMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3324",
   "FIELD2": "Songwe",
   "FIELD3": "Momba DC",
   "FIELD4": "CHITETE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3325",
   "FIELD2": "Songwe",
   "FIELD3": "Momba DC",
   "FIELD4": "IVUNA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3326",
   "FIELD2": "Songwe",
   "FIELD3": "Momba DC",
   "FIELD4": "KAPELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3327",
   "FIELD2": "Songwe",
   "FIELD3": "Momba DC",
   "FIELD4": "MKULWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3328",
   "FIELD2": "Songwe",
   "FIELD3": "Momba DC",
   "FIELD4": "MOMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3329",
   "FIELD2": "Songwe",
   "FIELD3": "Momba DC",
   "FIELD4": "MSANGANO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3330",
   "FIELD2": "Songwe",
   "FIELD3": "Momba DC",
   "FIELD4": "NKANGAMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3331",
   "FIELD2": "Songwe",
   "FIELD3": "Momba DC",
   "FIELD4": "NZOKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3332",
   "FIELD2": "Songwe",
   "FIELD3": "Momba DC",
   "FIELD4": "UWANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3333",
   "FIELD2": "Songwe",
   "FIELD3": "Songwe DC",
   "FIELD4": "GALULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3334",
   "FIELD2": "Songwe",
   "FIELD3": "Songwe DC",
   "FIELD4": "IFWENKENYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3335",
   "FIELD2": "Songwe",
   "FIELD3": "Songwe DC",
   "FIELD4": "KANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3336",
   "FIELD2": "Songwe",
   "FIELD3": "Songwe DC",
   "FIELD4": "KAPALALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3337",
   "FIELD2": "Songwe",
   "FIELD3": "Songwe DC",
   "FIELD4": "MAWENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3338",
   "FIELD2": "Songwe",
   "FIELD3": "Songwe DC",
   "FIELD4": "MWAGALACHUNYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3339",
   "FIELD2": "Songwe",
   "FIELD3": "Songwe DC",
   "FIELD4": "NAMKUKWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3340",
   "FIELD2": "Songwe",
   "FIELD3": "Songwe DC",
   "FIELD4": "SAZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3341",
   "FIELD2": "Songwe",
   "FIELD3": "Songwe DC",
   "FIELD4": "TOTOWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3342",
   "FIELD2": "Songwe",
   "FIELD3": "Tunduma TC",
   "FIELD4": "CHAPWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3343",
   "FIELD2": "Songwe",
   "FIELD3": "Tunduma TC",
   "FIELD4": "J M KIKWETE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3344",
   "FIELD2": "Songwe",
   "FIELD3": "Tunduma TC",
   "FIELD4": "KATETE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3345",
   "FIELD2": "Songwe",
   "FIELD3": "Tunduma TC",
   "FIELD4": "MPAKANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3346",
   "FIELD2": "Songwe",
   "FIELD3": "Tunduma TC",
   "FIELD4": "MPEMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3347",
   "FIELD2": "Songwe",
   "FIELD3": "Tunduma TC",
   "FIELD4": "MUUNGANO1",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3348",
   "FIELD2": "Songwe",
   "FIELD3": "Tunduma TC",
   "FIELD4": "MWAKAKATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3349",
   "FIELD2": "Songwe",
   "FIELD3": "Tunduma TC",
   "FIELD4": "MWL J K NYERERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3350",
   "FIELD2": "Songwe",
   "FIELD3": "Tunduma TC",
   "FIELD4": "NAMOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3351",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "BUKOKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3352",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "CHOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3353",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "HANIHANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3354",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "ICHAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3355",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "IGOWEKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3356",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "IGUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3357",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "IGURUBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3358",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "ISAKAMALIWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3359",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "ITUMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3360",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "ITUNDURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3361",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "KININGINILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3362",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "KINUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3363",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "MBUTU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3364",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "MISANA NTOBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3365",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "MWAKIPANGA NYANDEKWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3366",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "MWAMASHIGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3367",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "MWAMASHIMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3368",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "MWANZUGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3369",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "MWASHIKU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3370",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "MWAYUNGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3371",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "MWISI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3372",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "NANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3373",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "NDEMBEZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3374",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "NGULUMWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3375",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "NGUVUMOJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3376",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "NKINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3377",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "SIMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3378",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "SUNGWIZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3379",
   "FIELD2": "Tabora",
   "FIELD3": "Igunga DC",
   "FIELD4": "ZIBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3380",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "IGAGALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3381",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "IGWISI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3382",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "ILEGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3383",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "KALIUA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3384",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "KANINDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3385",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "KAPUYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3386",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "KASHISHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3387",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "KAZAROHO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3388",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "MKINDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3389",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "MWONGOZO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3390",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "SELELI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3391",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "SILAMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3392",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "UGUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3393",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "UKUMBISIGANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3394",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "ULYANKULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3395",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "USHOKOLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3396",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "USINGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3397",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "UYOWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3398",
   "FIELD2": "Tabora",
   "FIELD3": "Kaliua DC",
   "FIELD4": "ZUGIMLOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3399",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "BUDUSHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3400",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "BUKENE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3401",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "HAMZA AZIZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3402",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "IGUSULE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3403",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "IKINDWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3404",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "ISAGENHE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3405",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "ISANZU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3406",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "ITOBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3407",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "KAMPALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3408",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "KARITU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3409",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "KASELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3410",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "KILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3411",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "MABONDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3412",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "MAGENGATI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3413",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "MAMBALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3414",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "MILAMBO ITOBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3415",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "MIZIBAZIBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3416",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "MOGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3417",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "MUHUGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3418",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "MWAKASHANHALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3419",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "MWAMALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3420",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "MWANGOYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3421",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "MWANHALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3422",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "NATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3423",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "NKINIZIWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3424",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "PUGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3425",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "SEMEMBELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3426",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "SHIGAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3427",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "SIGILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3428",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "TONGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3429",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega DC",
   "FIELD4": "WELA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3430",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega TC",
   "FIELD4": "BUGWANDEGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3431",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega TC",
   "FIELD4": "BULUNDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3432",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega TC",
   "FIELD4": "CHIEF NTINGINYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3433",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega TC",
   "FIELD4": "IJANIJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3434",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega TC",
   "FIELD4": "ITILO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3435",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega TC",
   "FIELD4": "MIGUWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3436",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega TC",
   "FIELD4": "MWANZOLI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3437",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega TC",
   "FIELD4": "NZEGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3438",
   "FIELD2": "Tabora",
   "FIELD3": "Nzega TC",
   "FIELD4": "UNDOMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3439",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "CHABUTWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3440",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "IGIGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3441",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "KAMAGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3442",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "KILOLI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3443",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "KILUMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3444",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "KIPILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3445",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "KISANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3446",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "KIWERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3447",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "LANGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3448",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "MIBONO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3449",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "MKOLYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3450",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "MOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3451",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "MPOMBWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3452",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "MSUVA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3453",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "NGULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3454",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "PANGALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3455",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "TUTUO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3456",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "UGUNDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3457",
   "FIELD2": "Tabora",
   "FIELD3": "Sikonge DC",
   "FIELD4": "USUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3458",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "BOMBAMZINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3459",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "CHANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3460",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "CHEYO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3461",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "FUNDIKIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3462",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "IKOMWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3463",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "IPULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3464",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "ISEVYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3465",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "ITETEMIA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3466",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "ITONJANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3467",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "KALUNDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3468",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "KANYENYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3469",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "KARIAKOO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3470",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "KAZE HILL",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3471",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "KAZIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3472",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "LWANZALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3473",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "MILAMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3474",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "MISHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3475",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "NDEVELWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3476",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "NKUMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3477",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "NYAMWEZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3478",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "SIKANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3479",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "TABORA BOYS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3480",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora MC",
   "FIELD4": "TABORA GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3481",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "GOWEKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3482",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "IBIRI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3483",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "IDETE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3484",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "IGALULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3485",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "IKONGOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3486",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "IMALAMPAKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3487",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "KIZENGI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3488",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "LOLANGULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3489",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "LOYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3490",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "LUTENDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3491",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "MABAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3492",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "MADAHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3493",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "MAKAZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3494",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "NDONO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3495",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "SHITAGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3496",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "TURA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3497",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "UPUGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3498",
   "FIELD2": "Tabora",
   "FIELD3": "Tabora UYUI DC",
   "FIELD4": "USAGARI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3499",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "CHETU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3500",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "IMALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3501",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "IMALAMAKOYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3502",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "KAPILULA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3503",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "KILOLENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3504",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "MATWIGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3505",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "MUKANGWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3506",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "UGALLA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3507",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "UKOMBOZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3508",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "UKONDAMOYO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3509",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "URAMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3510",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "USISYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3511",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "USOJI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3512",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "USONGELANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3513",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "UYOGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3514",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "UYUMBU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3515",
   "FIELD2": "Tabora",
   "FIELD3": "Urambo DC",
   "FIELD4": "VUMILIA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3516",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "BAGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3517",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "BUMBULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3518",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "CHAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3519",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "FUNTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3520",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "JANUARY MAKAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3521",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "KIHITU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3522",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "KIVILICHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3523",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "KIZANDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3524",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "KIZIMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3525",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "KWALEI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3526",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "KWAMONGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3527",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "KWEHANGALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3528",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "MAYO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3529",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "MAZUMBAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3530",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "MBELEI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3531",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "MBUZII",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3532",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "MGWASHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3533",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "MIBUKWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3534",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "MKAALIE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3535",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "MMAKAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3536",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "MPONDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3537",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "MSAMAKA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3538",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "SONI DAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3539",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "TAMOTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3540",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "VUGABAZO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3541",
   "FIELD2": "Tanga",
   "FIELD3": "Bumbuli DC",
   "FIELD4": "WENA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3542",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "CHOGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3543",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "KABUKU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3544",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "KANGATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3545",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "KISAZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3546",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "KIVA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3547",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "KOMSANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3548",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "KWACHAGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3549",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "KWALUDEGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3550",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "KWALUGURU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3551",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "KWAMATUKU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3552",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "KWAMGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3553",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "KWAMKONO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3554",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "KWAMSISI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3555",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "KWANKONJE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3556",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "KWASUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3557",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "KWEDIZINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3558",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "MANGA MPAKANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3559",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "MAZINGARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3560",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "MKATA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3561",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "NDOLWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3562",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "PANGAMBILI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3563",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "SEGERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3564",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni DC",
   "FIELD4": "SINDENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3565",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni TC",
   "FIELD4": "HANDENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3566",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni TC",
   "FIELD4": "KILELENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3567",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni TC",
   "FIELD4": "KIVESA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3568",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni TC",
   "FIELD4": "KOMNYANGANYO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3569",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni TC",
   "FIELD4": "KONJE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3570",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni TC",
   "FIELD4": "KWENJUGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3571",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni TC",
   "FIELD4": "MISIMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3572",
   "FIELD2": "Tanga",
   "FIELD3": "Handeni TC",
   "FIELD4": "MSAJE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3573",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "JAILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3574",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "KIBIRASHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3575",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "KIKUNDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3576",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "KILINDI ASILIA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3577",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "KILINDI GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3578",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "KIMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3579",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "KOMKALAKALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3580",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "KWEDIBOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3581",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "KWEKIVU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3582",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "LWANDE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3583",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "MAFISA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3584",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "MASAGALU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3585",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "MBWEGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3586",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "MGERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3587",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "MKINDI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3588",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "MKUYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3589",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "NEGERO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3590",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "NKAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3591",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "PAGWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3592",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "SEUTA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3593",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "TUNGULI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3594",
   "FIELD2": "Tanga",
   "FIELD3": "Kilindi DC",
   "FIELD4": "VIBAONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3595",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "BUIKO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3596",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "BUNA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3597",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "BUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3598",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "CHEKELEI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3599",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "DINDIRA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3600",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "HALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3601",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "KIZARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3602",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "KWAGUNDA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3603",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "KWASHEMSHI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3604",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "KWEMDIMU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3605",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "MADAGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3606",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "MAFIHILLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3607",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "MAGOMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3608",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "MASHEWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3609",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "MASHINDEI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3610",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "MAZINDE DAY",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3611",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "MBAGHAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3612",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "MFUNDIA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3613",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "MKALAMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3614",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "MKOMAZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3615",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "MLUNGUI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3616",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "MNYUZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3617",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "MSWAHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3618",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "MWISHO WA SHAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3619",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "PATEMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3620",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "SHEKILANGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3621",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe DC",
   "FIELD4": "VUGIRI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3622",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe TC",
   "FIELD4": "JOEL BENDERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3623",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe TC",
   "FIELD4": "KILOLE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3624",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe TC",
   "FIELD4": "KIMWERI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3625",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe TC",
   "FIELD4": "KOROGWE GIRLS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3626",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe TC",
   "FIELD4": "KWAMNDOLWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3627",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe TC",
   "FIELD4": "NGOMBEZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3628",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe TC",
   "FIELD4": "NYERERE MEMORIAL",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3629",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe TC",
   "FIELD4": "OLD KOROGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3630",
   "FIELD2": "Tanga",
   "FIELD3": "Korogwe TC",
   "FIELD4": "SEMKIWA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3631",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "BALOZI MSHANGAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3632",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "BERNARD MEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3633",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "CHAMBOGHO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3634",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "GARE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3635",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "GOLOGOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3636",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "HAMBALAWEI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3637",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "HEMTOYE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3638",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "KALUMELE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3639",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "KIRETI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3640",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "KISABA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3641",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "KITALA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3642",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "KITIVO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3643",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "KWAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3644",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "KWEKANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3645",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "KWEMARAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3646",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "KWEMASHAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3647",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "KWEULASI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3648",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "LUKOZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3649",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "LUNGUZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3650",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "LUSHOTO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3651",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MAGAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3652",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MAKOLE JUU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3653",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MALIBWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3654",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MANOLO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3655",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MARIAM MSHANGAMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3656",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MASANGE JUU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3657",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MAVUMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3658",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MAZASHAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3659",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MBWEI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3660",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MDANDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3661",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MIGAMBO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3662",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MKUZI JUU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3663",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MLONGWEMA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3664",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MNAZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3665",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MSALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3666",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MTAE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3667",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "MTUMBI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3668",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "NDURUMO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3669",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "NGAZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3670",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "NGULWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3671",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "NGWELO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3672",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "NTAMBWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3673",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "NYWELO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3674",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "PRINCE CLAUS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3675",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "RANGWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3676",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "SHAGHAYU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3677",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "SHAMBALAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3678",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "SHITA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3679",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "SHUME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3680",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "SUNGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3681",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "UBIRI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3682",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "UMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3683",
   "FIELD2": "Tanga",
   "FIELD3": "Lushoto DC",
   "FIELD4": "VITI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3684",
   "FIELD2": "Tanga",
   "FIELD3": "Mkinga DC",
   "FIELD4": "BOSHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3685",
   "FIELD2": "Tanga",
   "FIELD3": "Mkinga DC",
   "FIELD4": "DALUNI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3686",
   "FIELD2": "Tanga",
   "FIELD3": "Mkinga DC",
   "FIELD4": "DUGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3687",
   "FIELD2": "Tanga",
   "FIELD3": "Mkinga DC",
   "FIELD4": "GOMBERO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3688",
   "FIELD2": "Tanga",
   "FIELD3": "Mkinga DC",
   "FIELD4": "KIGONGOI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "",
   "FIELD2": "",
   "FIELD3": "",
   "FIELD4": "",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "SN",
   "FIELD2": "REGION",
   "FIELD3": "COUNCIL",
   "FIELD4": "SCHOOL NAME",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3689",
   "FIELD2": "Tanga",
   "FIELD3": "Mkinga DC",
   "FIELD4": "KWALE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3690",
   "FIELD2": "Tanga",
   "FIELD3": "Mkinga DC",
   "FIELD4": "LANZONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3691",
   "FIELD2": "Tanga",
   "FIELD3": "Mkinga DC",
   "FIELD4": "MANZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3692",
   "FIELD2": "Tanga",
   "FIELD3": "Mkinga DC",
   "FIELD4": "MAPATANO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3693",
   "FIELD2": "Tanga",
   "FIELD3": "Mkinga DC",
   "FIELD4": "MARAMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3694",
   "FIELD2": "Tanga",
   "FIELD3": "Mkinga DC",
   "FIELD4": "MAVOVO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3695",
   "FIELD2": "Tanga",
   "FIELD3": "Mkinga DC",
   "FIELD4": "MKINGALEO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3696",
   "FIELD2": "Tanga",
   "FIELD3": "Mkinga DC",
   "FIELD4": "MTIMBWANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3697",
   "FIELD2": "Tanga",
   "FIELD3": "Mkinga DC",
   "FIELD4": "MWAKIJEMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3698",
   "FIELD2": "Tanga",
   "FIELD3": "Mkinga DC",
   "FIELD4": "ZINGIBARI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3699",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "BWEMBWERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3700",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "CHIEF MANGENYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3701",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "FURAHA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3702",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "KERENGE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3703",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "KICHEBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3704",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "KIGOMBE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3705",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "KILULU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3706",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "KWABUTU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3707",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "KWAFUNGO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3708",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "KWEMKABARA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3709",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "MAGILA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3710",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "MISALAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3711",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "MISOZWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3712",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "MKURUMUZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3713",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "MKUZI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3714",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "MLINGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3715",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "MLINGANO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3716",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "MTINDIRO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3717",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "MUHEZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3718",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "NGOMENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3719",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "NKUMBA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3720",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "POTWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3721",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "SHEBOMEZA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3722",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "SONGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3723",
   "FIELD2": "Tanga",
   "FIELD3": "Muheza DC",
   "FIELD4": "ZIRAI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3724",
   "FIELD2": "Tanga",
   "FIELD3": "Pangani DC",
   "FIELD4": "BUSHIRI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3725",
   "FIELD2": "Tanga",
   "FIELD3": "Pangani DC",
   "FIELD4": "FUNGUNI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3726",
   "FIELD2": "Tanga",
   "FIELD3": "Pangani DC",
   "FIELD4": "KILIMANGWIDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3727",
   "FIELD2": "Tanga",
   "FIELD3": "Pangani DC",
   "FIELD4": "KIPUMBWI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3728",
   "FIELD2": "Tanga",
   "FIELD3": "Pangani DC",
   "FIELD4": "MKWAJA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3729",
   "FIELD2": "Tanga",
   "FIELD3": "Pangani DC",
   "FIELD4": "MWERA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3730",
   "FIELD2": "Tanga",
   "FIELD3": "Pangani DC",
   "FIELD4": "TONGANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3731",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "CHONGOLEANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3732",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "CHUMBAGENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3733",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "GALANOS",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3734",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "HORTEN",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3735",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "JAPAN",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3736",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "KIHERE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3737",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "KIOMONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3738",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "KIRARE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3739",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "MABOKWENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3740",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "MACECHU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3741",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "MARUNGU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3742",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "MAWENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3743",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "MIKANJUNI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3744",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "MKWAKWANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3745",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "MNYANJANI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3746",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "MSAMBWENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3747",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "MWAPACHU",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3748",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "NDAOYA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3749",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "NGUVUMALI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3750",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "OLD TANGA",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3751",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "PANDE MAGUBENI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3752",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "PONGWE",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3753",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "TANGA TECHNICAL",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3754",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "TOLEDO",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3755",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "TONGONI",
   "FIELD5": "",
   "FIELD6": ""
 },
 {
   "FIELD1": "3756",
   "FIELD2": "Tanga",
   "FIELD3": "Tanga CC",
   "FIELD4": "USAGARA",
   "FIELD5": "",
   "FIELD6": ""
 }
]
z = []
for a in x:
    if a['FIELD1'] == "SN" or a['FIELD3'] == "":
        continue
    else:
        if a['FIELD2'] == "Coast":
            a['FIELD2'] = "Pwani"

        z.append({'mkoa': a['FIELD2'], 'wilaya': a['FIELD3'], 'shule': a['FIELD4']})

a = []
def check(wilaya):
    x= ['SINGIDA', 'LINDI', 'BABATI', 'NJOMBE', 'MBEYA', 'IRINGA', 'ARUSHA', 'MPANDA', 'SUMBAWANGA', 'MOROGORO', 'MTWARA', 'SONGEA', 'KIBAHA', 'KIGOMA', 'TABORA', 'TANGA', 'BUKOBA', 'MOSHI', 'ILALA', 'MUSOMA', 'SHINYANGA']
    for i in x:
        if i == wilaya:
            return True
    return False

def check2(mc):
    x = ['MC', 'TC', 'CC']
    for i in x:
        if i == mc:
            return True
    return False


for data in z:
    b = data['wilaya'].split(" ")
    if check(b[0].upper()) == True and check2(b[1]) == True:
        w = b[0] + " " + "cbd"
        # print(b)
    elif len(b) == 3:
        w = "Uyui"

    elif len(b) == 1:
        w = b[0]
    else:
        # print(b)
        w = b[0]

    q = {'mkoa': data['mkoa'], 'wilaya': w, 'shule': data['shule']}
    a.append(q)


# print(check('SINGIDA'))
# print(check2('TC'))


def checkmale(data):
    male = ['ILBORU', 'KIBAHA', 'MZUMBE', 'TABORA BOYS',
            'BWIRU BOYS', 'MUSOMA TECH', 'LUGUFU BOYS',
            'KILOSA', 'BALANGDALALU', 'MOSHI', 'SONGEA BOYS', 'LUFUNGU BOYS']
    for i in male:
        if i == data:
            return True
    return False

def checkfemale(data):
    female = ['KILAKALA', 'MSALATO',
              'TABORA GIRLS', 'KAZIMA',
              'RUGAMBWA', 'ARUSHA GIRLS',
              'SONGE', 'TUMAINI', 'SONGEA GIRLS',
              'MANDERA GIRLS', 'RUVU GIRLS',
              'KIBAHA GIRLS', 'IFUNDA GIRLS',
              'IRINGA GIRLS', 'MPANDA GIRLS',
              'LUGUFU GIRLS', 'MACHAME GIRLS',
              'ILULU GIRLS', 'NACHINGWEA GIRLS',
              'BUSOKELO GIRLS', 'MASASI GIRLS',
              'MTWARA GIRLS', 'BWIRU GIRLS',
              'MAKETE GIRLS', 'MBINGA GIRLS',
              'TINDE GIRLS', 'KILINDI GIRLS', 'KOROGWE GIRLS']

    for i in female:
        if i == data:
            return True
    return False


def checktech(data):
    female = ['TANGA TECHNICAL', 'MOSHI TECH', 'IFUNDA TECH', 'MWADUI TECH']

    for i in female:
        if i == data:
            return True
    return False

c = []
for data in a:
    s = data['shule']
    if checkmale(s) == True:
        gender = "male"
        type = "special"
    elif checkfemale(s) == True:
        gender = "female"
        type = "special"

    elif checktech(s) == True:
        gender = "mixture"
        type = "technical"

    else:
        gender = "mixture"
        type = "ward"

    q = {'mkoa': data['mkoa'], 'wilaya': data['wilaya'], 'shule': data['shule'], 'type': type, 'sex': gender}
    c.append(q)












with open("school3.csv", "w", newline="") as csvfile:
    # Create a CSV writer object
    writer = csv.DictWriter(csvfile, fieldnames=["mkoa", "wilaya", "shule", 'type', 'sex'])

    # Write the header row
    writer.writeheader()

    # Write the data rows
    for person in c:
        writer.writerow(person)


