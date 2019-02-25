from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Account


# Create your views here.
def index(request):
    allAccounts = Account.objects.all()
    context = {
        "allAccounts": allAccounts
    }
    return render(request, 'accountApp/index.html', context),
# render hello plus account name
def helloAccount(request):

    return HttpResponse("hello " + request.POST['accountName'])
#  adds five to the account using the ID
def addFive(request, accountID):
    individualAccount = get_object_or_404(Account, pk = accountID)
    individualAccount.checking += 5
    individualAccount.save()

    return redirect("index")


