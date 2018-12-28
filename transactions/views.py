from django.shortcuts import render

def transaction_list(request):
    return render(request, 'transactions/templates/transaction_list.html', {})