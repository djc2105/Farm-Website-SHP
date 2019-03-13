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
    return HttpResponse("This is a work in progress")


def rowselect(request, id):
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

    if not isdatavalid(id, row):
        return render(request, "invalid_row.html", context=context_dict)

    form = PlantForm()
    if int(row) < 10:
        row = "0"+row
    context_dict = {"id": id, "row": row, "form": form}
    return render(request, "dataform2.html", context=context_dict)


def submitdata(request, lot_id, row_id):
    form = PlantForm()
    context_dict = {"form": form}
    form = PlantForm(request.POST)
    if form.is_valid():
        plant = form.save(commit=False)
        lot = Lot.objects.filter(lotid=lot_id)
        queryreturn = Row.objects.filter(inlot=lot, rownum=row_id)
        listofrows = list(queryreturn)
        plant.row = listofrows[0]
        plant.save()
        return render(request,"success.html", context=context_dict)
    else:
        print(form.errors)
    return render(request, "dataform2.html", context=context_dict)


def dataactionselect(request):
    context_dict = {}
    return render(request,"dataactionselect.html", context=context_dict)


def viewrow(request):
    context_dict = {}
    return render(request,"viewrow.html",context=context_dict)


def rowdata(request):
    rownum = request.POST.get("row_id", "100")
    lotid = request.POST.get("lot_id", "e")
    lotid = lotid.lower()
    context_dict = {"rownum": rownum, "lot": lotid, }
    if not isdatavalid(lotid, rownum):
        return render(request, "invalid_row.html", context=context_dict)

    if(int(rownum) < 10):
        rownumwith0 = "0"+rownum
    else:
        rownumwith0 = rownum

    lot = Lot.objects.filter(lotid=lotid)
    queryreturn = Row.objects.filter(inlot=lot, rownum=rownum)
    plants = Plant.objects.filter(row=queryreturn)
    listofplants = list(plants)

    context_dict = {"rownum": rownum, "lot": lotid, "plants": listofplants, "rownumwith0": rownumwith0,}
    print (rownumwith0)
    return render(request, "rowdataviewer.html", context=context_dict)


def isdatavalid(lot, row):
    if lot != "a" and lot != "b" and lot != "c" and lot != "d":
        return False
    if lot == "a" and int(row) > 13:
        return False
    if lot == "b" and int(row) > 10:
        return False
    if lot == "c" and int(row) > 45:
        return False
    if lot == "d" and int(row) > 17:
        return False
    return True


def getplant(request, id):
    queryReturnPlant = Plant.objects.filter(id=id)
    listOfPlants = list(queryReturnPlant)
    plant = listOfPlants[0]

    context_dict = {"plant":plant,}
    return render(request, "plantinfo.html", context=context_dict)


def editplant(request, id):
    queryReturnPlant = Plant.objects.filter(id=id)
    listOfPlants = list(queryReturnPlant)
    plant = listOfPlants[0]

    context_dict = {"plant":plant,}
    return render(request, "editplant.html", context=context_dict)


def updateplant(request, id):
    plantname = request.POST.get("name")
    quantity = request.POST.get("quantity")
    date = request.POST.get("date")
    notes = request.POST.get("notes")
    context_dict = {}
    queryReturnPlant = Plant.objects.filter(id=id)
    listOfPlants = list(queryReturnPlant)
    plant = listOfPlants[0]

    print (plantname)
    print (notes)

    if(len(plantname)>0):
        plant.plantname = plantname
    if(quantity != ""):
        plant.quantity = quantity
    if(date != ""):
        plant.dateplanted = date
    if(notes != ""):
        plant.notes = notes

    plant.save()

    return render(request,"success.html", context=context_dict)


def deleteplant(request, id):
    context_dict = {}
    Plant.objects.filter(id=id).delete()
    return render(request, "success.html", context=context_dict)


def viewall(request):
    plants = Plant.objects.all()
    listofplants = list(plants)

    context_dict = {"plants": listofplants}

    return render(request, "allplantviewer.html", context=context_dict)


def deleterowdata(request, lot_id, row_id):
    context_dict = {}
    lot = Lot.objects.filter(lotid=lot_id)
    row = Row.objects.filter(inlot=lot, rownum=row_id)
    plants = list(Plant.objects.filter(row=row))
    for p in plants:
        p.delete()

    return render(request, "success.html", context=context_dict)
