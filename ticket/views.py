from django.shortcuts import render
from ticket.forms import TicketForms


def index(request):
    form = TicketForms()
    contexto = {
        'form': form
    }
    return render(request, 'index.html', contexto)


def review_query(request):
    if request.method == 'POST':
        form = TicketForms(request.POST)
        if form.is_valid():
            contexto = {
                'form': form
            }
            return render(request, 'minha_consulta.html', contexto)
        else:
            print('Form inválido')
            contexto = {
                'form': form
            }
            return render(request, 'index.html', contexto)
