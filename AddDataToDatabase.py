import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://faceattendencesystem-d1b02-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "12345":
        {
            "name": "PewDiePie",
            "department": "IT",
            "total attendance": "75%",
            "starting year": "2020",
            "year": "TY",
            "sem": "5",
            "last_attendance_time": "2023-03-05 00:54:34"
        },

    "13579":
        {
            "name": "Elon Musk",
            "department": "IT",
            "total attendance": "80%",
            "starting year": "2021",
            "year": "SY",
            "sem": "3",
            "last_attendance_time": "2023-03-05 00:54:34"
        },

    "246810":
        {
            "name": "JJ Olatunji",
            "department": "IT",
            "total attendance": "65%",
            "starting year": "2021",
            "year": "SY",
            "sem": "3",
            "last_attendance_time": "2023-03-05 00:54:34"
        },

    "67890":
        {
            "name": "Mujtaba Mohamed",
            "department": "IT",
            "total attendance": "95%",
            "starting year": "2021",
            "year": "SY",
            "sem": "4",
            "last_attendance_time": "2023-03-05 00:54:34"
        },
    "98765":
        {
            "name": "Dhruv Mokashe",
            "department": "IT",
            "total attendance": "60%",
            "starting year": "2021",
            "year": "SY",
            "sem": "4",
            "last_attendance_time": "2023-03-05 00:54:34"
        },
    "54321":
        {
            "name": "Manan Gohil",
            "department": "IT",
            "total attendance": "70%",
            "starting year": "2021",
            "year": "SY",
            "sem": "4",
            "last_attendance_time": "2023-03-05 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)