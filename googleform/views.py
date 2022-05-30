from glob import glob
from unicodedata import name
from django.shortcuts import redirect, render
import pymongo
client = pymongo.MongoClient('mongodb+srv://manoj:123@cluster0.efvz2uv.mongodb.net/?retryWrites=true&w=majority')
db = client['Dbgoogleform']
col = db['collectionform']

# Create your views here.
formlist = []
formname = ""

def base(request):
    global formlist,formname
    formlist = []
    formname = ""
    a =[2,3,[4,5,6],[5,76,8,89]]
    print(len(a))
    return render(request,"base.html",{'formlist':formlist})

def newform(request):
    global formlist,formname
    formlist = []
    formname = ""
    return redirect('/')

def googleform(request):
    global formlist,formname
    return render(request,"googleform.html",{'formlist':formlist})

def result(request):
    global formlist,formname,col
    datalist = {}
    # datalist["formName"]= formname
    if request.method == "POST":
        for i in formlist:
            datalist[i[0]] = request.POST[i[0]]
    col.insert_one(datalist)
    del datalist["_id"]
    return render(request,"result.html",{"data":datalist,'formname':formname})

def form(request):
    global formlist, formname
    if request.method == "POST":
        formname = request.POST['formname']
        temp = []
        name = request.POST['name']
        temp.append(name)
        dropdown = request.POST['dropdown']
        temp.append(dropdown)
        options = request.POST.get('options')
        temp.append(options)
        mandatory = request.POST.get('mandatory')
        temp.append(mandatory)
        if temp not in formlist:
            formlist.append(temp)
        return render(request,"base.html",{'formname':formname,'formlist':formlist})