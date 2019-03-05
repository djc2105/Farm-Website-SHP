from django.shortcuts import render
from django.http import HttpResponse
from website.forms import PlantForm
from website.models import Plant,Row,Lot


# Create your views here.

def homepage(request):
    context_dict ={}
    return render(request,'homepage.html',context=context_dict)


def lotselect(request):
    context_dict ={}
    return render(request, "lotselect.html", context=context_dict)


def sciencehome(request):
    context_dict = {}
    return render("hello")


def rowselect(request,id):
    context_dict = {"id":id}
    if (id == 'a'):
        return render(request, "rowselectA.html", context=context_dict)
    if (id == 'b'):
        return render(request, "rowselectB.html", context=context_dict)
    if (id == 'c'):
        return render(request, "rowselectC.html", context=context_dict)

    return render(request, "rowselectD.html", context=context_dict)


def getrow(request,id):
    row = request.POST.get("row","100")
    context_dict = {"id": id, "row":row}
    if(id=="a" and int(row)>13):
        return render(request, "invalid_row.html", context=context_dict)
    if(id=="b" and int(row)>10):
        return render(request, "invalid_row.html", context=context_dict)
    if(id=="c" and int(row)>45):
        return render(request, "invalid_row.html", context=context_dict)
    if(id=="d" and int(row)>17):
        return render(request, "invalid_row.html", context=context_dict)

    form = PlantForm()
    context_dict = {"id": id, "row": row, "form": form}
    return render(request, "dataform2.html", context=context_dict)


def submitdata(request, lot_id, row_id):
    form = PlantForm()
    context_dict = {"form": form}
    form = PlantForm(request.POST)
    if form.is_valid():
        plant = form.save(commit=False)
        lot = Lot.objects.filter(lotid=lot_id)
        a = Row.objects.filter(inlot=lot, rownum=row_id)
        b = list(a)
        plant.row = b[0]
        plant.save()
        return render(request,"success.html", context=context_dict)
    else:
        print(form.errors)
    return render(request, "dataform2.html", context=context_dict)




