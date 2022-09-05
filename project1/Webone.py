from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyzer(request):
    txt = request.POST.get('text','default')
    punc = request.POST.get('check' , 'off')
    punc2 = request.POST.get('check1' , 'off')
    punc3 = request.POST.get('Removenewline' , 'off')
    punc4 = request.POST.get('charcount' , 'off')
    punc5 = request.POST.get('wordcount' , 'off')
    analyse =""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if punc == 'on':
        for char in txt:
            if char not in punctuations:
                analyse = analyse + char

            analyse = analyse.upper()
        params = {'purpose' : 'Removing Punctuations' , 'Analyzed' : analyse }
        return render(request, 'analyzer.html',params)
    elif punc2 == 'on':
        analyse += txt.capitalize()
        params = {'purpose' : 'Changing to capital' , 'Analyzed' : analyse }
        return render(request,'analyzer.html',params)
    elif punc3 == 'on':
        for char in txt:
            if char != '\n' :
                analyse = analyse + char
        params = {'purpose': 'Removing new lines', 'Analyzed': analyse}
        return  render(request,'analyzer.html',params)

    elif punc5 == 'on':
        lst = txt.split(" ")
        count = 0
        for char in lst:
            analyse = analyse + char
            count += 1
        params = {'purpose': 'Counting Words', 'Analyzed': count }
        return render(request, 'analyzer.html', params)
    else :
        return HttpResponse("Error")
