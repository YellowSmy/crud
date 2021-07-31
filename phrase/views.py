from django.db.models import manager
from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PhraseSerializer
from .models import Phrase

# Create your views here.
def main(request):
    return render(request, 'phrase/index.html')

@api_view(["GET"])
def phraselist(req):
    phrases = Phrase.objects.all()
    serializer = PhraseSerializer(phrases, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def phraseCreate(req):
    serializer = PhraseSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["DELETE"])
def phraseDelete(req, pk):
    phrase = Phrase.objects.get(id=pk)
    phrase.delete()
    return Response("Delete Success")

@api_view(["PUT"])
def phraseUpdate(req, pk):
    phrase = Phrase.objects.get(id=pk)
    serializer = PhraseSerializer(phrase, data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)