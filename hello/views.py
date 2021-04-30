from django.http import HttpResponse

from django.shortcuts import render


#def index (request):
#    return  HttpResponse("home")
#def about (request):
 #   return  HttpResponse("hello")
# def removepunk(request):
#     return  HttpResponse("remove punk")

# def capfirst(request):
#     return  HttpResponse("capfirst <a href = '/'> back</a>")  

# def spaceremove(request):
#     return  HttpResponse("spaceremove")


# def newlineremove(request):
#     return  HttpResponse("newlineremove")


# def charcount(request):
#     #get the text 
#     print(request.GET.get('text','default'))
#     #analyse the text 
#     return  HttpResponse("charcount") 
# def exe1(request):

#        s = '''<h2>Navigation Bar<br></h2>
#        <table style = width:150;>

#        <tr>
#        <th>FIRST<th>
#        </tr>
#        <tr>
#        <td>

#             <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br> 
#     </td>
#     </tr>
#             <a href="https://www.facebook.com/">Facebook</a><br>
#             <a href="https://www.flipkart.com/">Flipkart</a><br>
#             <a href="https://www.hindustantimes.com">News</a><br>
#             <a href="https://www.google.com/">Google</a>'''
#        return HttpResponse(s)
  
def index(request):
    return render(request,"index2.html")


def removepunk(request):
    djtext =request.POST.get("text","off")
    print(djtext)
    remove = request.POST.get("remove","no")
    print(remove)
    fullcap = request.POST.get("fullcap" ,"no")
    print(fullcap)
    newline  = request.POST.get("newline","no")
    print(newline)
    smallcap =request.POST.get("smallcap","off")
    print(smallcap)
    if smallcap =="on":
     analised = ""
     for char in djtext:
           analised = analised + char.lower()
     daman = {"purpose":"LOWER THE TEXT","analized":analised }
     return render ( request,"analize.html",daman)

    elif (remove == "on"):
     punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
     analised =""
     for  char in djtext:

        if char not in punctuations:
            analised =analised+char

     daman = {"purpose": "remove puncation" , "analized": analised }
     return render( request,"analize.html",daman)

    elif(fullcap =="on"):
     analised = ""
     for char in djtext:
        analised =analised + char.upper()
        
        
     daman = {"purpose": "capital the letter" , "analized": analised }
     return render( request,"analize.html",daman)

    elif(newline =="on"):
     analised= "" 
     for char in djtext:

          if char!="\n"and char!= "\r":
            analised = analised+char

     daman = {"purpose": "new line remover" ,"analized":analised}
     return render(request,"analize.html",daman)


    else:
        return HttpResponse("error")


