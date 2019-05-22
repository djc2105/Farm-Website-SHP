from django.shortcuts import render
from django.http import HttpResponse
from website.forms import PlantForm
from website.models import Plant, Row, Lot
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import os.path


# Create your views here.

def homepage(request):
    # Simple enough return of the homepage template
    context_dict ={}
    return render(request,'homepage.html',context=context_dict)


def lotselect(request):
    # Also a simple template return
    context_dict ={}
    return render(request, "lotselect.html", context=context_dict)


def sciencehome(request):
    # This still needs to be done
    context_dict = {}
    return render(request, "sciencehome.html", context=context_dict)


def rowselect(request, id):

    context_dict = {"id": id, "lot": "images/LOTA.png"}
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
    # To handle if no row number is entered
    gettingWholeBed = False

    rownum = request.POST.get("row_id", "100")
    lotid = request.POST.get("lot_id", "e")
    lotid = lotid.lower()
    context_dict = {"rownum": rownum, "lot": lotid, }
    if not isdatavalid(lotid, rownum):
        return render(request, "invalid_row.html", context=context_dict)

    if rownum == '':
        gettingWholeBed = True
        rownumwith0 = ""
    else:
        if int(rownum) < 10:
            rownumwith0 = "0"+rownum
        else:
            rownumwith0 = rownum

    lot = Lot.objects.filter(lotid=lotid)

    if gettingWholeBed:
        rows = Row.objects.filter(inlot=lot)
        plants = Plant.objects.filter(row=rows, archived=False)
        rownum = "all"
        listofplants = list(plants)
    else:
        queryreturn = Row.objects.filter(inlot=lot, rownum=rownum)
        plants = Plant.objects.filter(row=queryreturn, archived=False)
        listofplants = list(plants)

    context_dict = {"rownum": rownum, "lot": lotid.upper(), "plants": listofplants, "rownumwith0": rownumwith0,}
    return render(request, "rowdataviewer.html", context=context_dict)


def isdatavalid(lot, row):
    if lot != "a" and lot != "b" and lot != "c" and lot != "d":
        return False
    if row != '':
        if lot == "a" and int(row) > 13:
            return False
        if lot == "b" and int(row) > 10:
            return False
        if lot == "c" and int(row) > 51:
            return False
        if lot == "d" and int(row) > 19:
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
    archive = request.POST.get("archive")
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
    plant = list(Plant.objects.filter(id=id))[0]
    plant.archived = True
    plant.save()

    # Old archiving system that muight want to be reimplemented. It saves the data to a file indtead of keeping
    # it in the database
    #
    # date = str(plant.dateplanted)
    # monthStr = date[-2:]
    # month = int(monthStr)
    # year = date[:4]
    #
    # dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # dir = os.path.join(dir, "FarmDataArchive")
    #
    # #File is called: "month1-month31-year"
    # #Feb 1 thorugh May 31
    # if(month >= 2 and month < 6):
    #     f = open(dir + "/Feb1-May31-"+year, 'a')
    # #Jun 1 through Sept 31
    # if (month >= 6 and month < 10):
    #     f = open(dir + "/Jun1-Sept31-"+year, 'a')
    # #Oct 1 through Jan 31
    # if (month >= 10 or month < 2):
    #     f = open(dir + "/Oct1-Jan31-"+year, 'a')
    # f.write("Name:" + plant.plantname + " Date:" + str(plant.dateplanted) + " Row:" + plant.row.__str__() + " Quantity:" + str(plant.quantity) + " Notes:" + plant.notes + "\n")
    # plant.delete()

    return render(request, "success.html", context=context_dict)


def viewall(request):
    plants = Plant.objects.filter(archived=False)
    listofplants = list(plants)

    context_dict = {"plants": listofplants}

    return render(request, "allplantviewer.html", context=context_dict)


def deleterowdata(request, lot_id, row_id):
    context_dict = {}
    lot = Lot.objects.filter(lotid=lot_id)
    row = Row.objects.filter(inlot=lot, rownum=row_id)
    plants = list(Plant.objects.filter(row=row))
    for p in plants:
        p.archived = True
        p.save()

    return render(request, "success.html", context=context_dict)


def about(request):
    return HttpResponse("This website was made by Daniel Carlson and Garrett Pinkston, Class of 2019")


def qrredirect(request, lot_id, row_id):
    form = PlantForm()
    context_dict = {"id": lot_id, "row": row_id, "form":form, }
    return render(request, "dataform2.html", context=context_dict)


def archive(request, lot_id):
    datestart = request.POST.get("dateplantedstart")
    dateend = request.POST.get("dateplantedend")
    if datestart is not None and datestart != '':
        datestart = datetime.strptime(request.POST.get("dateplantedstart"), '%Y-%m-%d')
    if dateend is not None and dateend != '':
        dateend = datetime.strptime(request.POST.get("dateplantedend"), '%Y-%m-%d')
    name = request.POST.get("name")
    row = request.POST.get("row")

    allplants = list(Plant.objects.filter(archived=True, ))
    plants = []

    def toadd(plant):
        plantdatetime = datetime.combine(plant.dateplanted, datetime.min.time())
        if datestart is not None and datestart != '' and plantdatetime < datestart:
            return False
        if dateend is not None and dateend != '' and plantdatetime > dateend:
            return False
        if name is not '' and name is not None and plant.plantname != name:
            return False
        if row is not '' and row is not None and plant.row.__str__() != row:
            return False
        return True

    for plant in allplants:
        if toadd(plant):
            plants.append(plant)


    context_dict = {"plants": plants[0:50], }
    return render(request, "archiveviewer.html", context=context_dict)


@csrf_exempt
def sciencepost(request):
    alldata = request.POST.get("allpostdata")
    context_dict = {"data": alldata}
    return render(request, "realtimedatapost.html", context=context_dict)
