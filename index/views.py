from django.shortcuts import render
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
import os
from django.views import View
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "creds.json"

# Create your views here.
def index(request):
    cred = credentials.ApplicationDefault()
    try:
        firebase_admin.initialize_app(cred, {
        'projectId': 'firebase-integration-329812',
        })
    except Exception as e:
        print(e)
        pass
    db = firestore.client()
    doc_ref = db.collection(u'users').document(u'Grids')
    doc_ref.set({
        u'first': u'Grids',
        u'last': u'Synergy',
        u'born': 1996
    })

    return HttpResponse(True)
