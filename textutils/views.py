from django.http import HttpResponse
from django.shortcuts import render



#

def index(request):
    return render(request, 'index.html')

def analyze(request):

  djtext = request.POST.get('text','default')
  print(djtext)


  removepunc = request.POST.get('removepunc','off')
  uppercase = request.POST.get('uppercase','off')
  lowercase = request.POST.get('lowercase','off')
  extraspaceremover = request.POST.get('extraspaceremover','off')
  wordcounter = request.POST.get('wordcounter','off')

  if removepunc == "on":
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for char in djtext:
      if char not in punctuations:
        analyzed += char

    param = { 'puropse': 'Removed Punctuations',  'analyzed_text':analyzed
    }
    return render(request,'analyze.html',param)
    
  elif (uppercase == "on"):
    analyzed = ""
    for char in djtext:
      analyzed = analyzed + char.upper() 
    param = {
      'puropse': 'capitalise the letter',
      'analyzed_text':analyzed
    } 
    print(analyzed)
    return render(request,'analyze.html',param)
  
  elif(lowercase == "on"):
    analyzed = ""
    for char in djtext:
      analyzed = analyzed + char.lower() 
    param = {
      'puropse': 'Lowercase the letter',
      'analyzed_text':analyzed
    } 
    print(analyzed)
    return render(request,'analyze.html',param)

  elif(extraspaceremover == "on"):
    analyzed = ""
    for index,char in enumerate(djtext):
      if not (djtext[index] == " " and djtext[index+1]):
        anazlyzed  += char
    param = {
      'puropse': 'extra space removed the letter',
      'analyzed_text':analyzed
    } 
    print(analyzed)
    return render(request,'analyze.html',param)

    
  elif(wordcounter == "on"):
    analyzed = djtext.split()
    param = {
      'puropse': 'count the word :',
      'analyzed_text':len(analyzed)
    } 
    print(analyzed)
    return render(request,'analyze.html',param)

  else:
    return HttpResponse("error")






