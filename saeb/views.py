from django.shortcuts import render



def pagina_cadastro(request):
    return render(request,'cadastro.html')
