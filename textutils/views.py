from django.http import HttpResponse
from django.shortcuts import render
import re

def home(request):
    #params = {"name":"Sahil", "address":"Earth"}
    return render(request, 'home.html')
    #return HttpResponse("Home Page")

def analyze(request):
    purpose = ""
    count = ""
    text = request.POST.get("text", "default")
    analyzed_text = text
    uppercase = request.POST.get("uppercase", "off")
    lowercase = request.POST.get("lowercase", "off")
    capitalize = request.POST.get("capitalize", "off")
    charcount = request.POST.get("charcount", "off")
    removespaces = request.POST.get("removespaces", "default")

    if uppercase == "on":
        analyzed_text = analyzed_text.upper()
        purpose = "Text Converted to Uppercase Successfully"
    if lowercase == "on":
        analyzed_text = analyzed_text.lower()
        purpose = "Text Converted to Lowercase Successfully"
    if capitalize == "on":
        analyzed_text = analyzed_text.capitalize()
        purpose = "Text Converted to Capitalized case Successfully"
    if removespaces == "on":
        analyzed_text = analyzed_text.strip()
        analyzed_text = re.sub('\s{2,}', ' ', analyzed_text)
        purpose = "Extra spaces removed Successfully"
    if charcount =="on":
        count = int(len(analyzed_text))
        purpose = "Characters counted Successfully"

    dictionary = {'analyzed': analyzed_text, 'chars': count, 'purpose':purpose}
    return render(request, 'analyze.html', dictionary)
'''
def lowercase(request):
    return HttpResponse("Converting text to Lowercase<br><br><a href='http://127.0.0.1:8000/'>Back</a>")

def uppercase(request):
    text = request.GET.get('text', 'default')
    print(text)
    return HttpResponse("Converting text to Uppercase<br><br><a href='http://127.0.0.1:8000/'>Back</a>")

def charcount(request):
    return HttpResponse("Counting number of characters in the text<br><br><a href='http://127.0.0.1:8000/'>Back</a>")

def removespaces(request):
    return HttpResponse("Removing extra spaces from the text<br><br><a href='http://127.0.0.1:8000/'>Back</a>")

def capitalize(request):
    return HttpResponse("Capitalizing first character in the text<br><br><a href='http://127.0.0.1:8000/'>Back</a>")
'''