#sameer mahajan
#text util backend
from django.http import HttpResponse
from django.shortcuts import render

# to load the home page
def index(request):
    return render(request, 'index.html')

# to perform textutils
def analyze(request):

    #get text using post
    djtext = request.POST.get('text', 'default')
    
    # util data
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremove=request.POST.get('extraspaceremove','off')

    analyzed=djtext

    if removepunc=='on' or uppercase=='on' or newlineremove=='on' or extraspaceremove=='on':
        # to remove punctuations
        if removepunc == 'on': 
            punctutations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            temp=""
            for char in analyzed:
                if char not in punctutations:
                    temp=temp+char
            analyzed=temp
        
        # to turn text to upper case
        if uppercase=='on':
            temp=""
            for i in analyzed:
                temp=temp+i.upper()
            analyzed=temp
    
        # to remove new lines
        if newlineremove=='on':
            temp=""
            for i in analyzed:
                if i!='\n' and i!='\r':
                    temp=temp+i
            analyzed=temp

        # to remove extraspaces
        if extraspaceremove=='on':
            temp=""
            for index,ch in enumerate(analyzed):
                if not (djtext[index]==' ' and djtext[index+1]==' '):
                    temp=temp+ch
            analyzed=temp

        params={'purpose':'Performed operations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    else:
        return HttpResponse('select a option')
