from django.shortcuts import render,redirect
from .models import Customer,Recieve,Item
from django.contrib.auth.decorators import login_required
import io
import csv
from .forms import Right_form


@login_required
def index(request):
    if "hyouji" in request.session:
        hyouji=request.session["hyouji"]
    else:
        request.session["hyouji"]="全て"
        hyouji="全て"

    if hyouji=="全て":
        cusms=Customer.objects.all()
    else:
        cusms=Customer.objects.filter(tantou=hyouji)

    return render(request,"houjin1/index.html",{"cusms":cusms})


def hyouji_all(request):
    request.session["hyouji"]="全て"
    return redirect("houjin1:index")

def hyouji_inoue(request):
    request.session["hyouji"]="井上"
    return redirect("houjin1:index")

def hyouji_furukawa(request):
    request.session["hyouji"]="古川"
    return redirect("houjin1:index")

def hyouji_mashimo(request):
    request.session["hyouji"]="眞下"
    return redirect("houjin1:index")


def koshin(request,pk):
    tantou=request.POST.get("tantou")
    dm=request.POST.get("dm")
    tel=request.POST.get("tel")
    gaisho=request.POST.get("gaisho")
    bikou=request.POST.get("bikou")

    result=Customer.objects.get(pk=pk)
    result.tantou=tantou
    result.dm_day=dm
    result.tel_day=tel
    result.gaisho_day=gaisho
    result.bikou=bikou
    result.save()

    return redirect("houjin1:index")


def delete(request,pk):
    Customer.objects.get(pk=pk).delete()
    return redirect("houjin1:index")


def csv_page(request):
    return render(request,"houjin1/csv.html")


def upload(request):
    #顧客一覧
    data = io.TextIOWrapper(request.FILES['csv1'].file, encoding="cp932")
    csv_content = csv.reader(data)
    
    csv_list=list(csv_content)
        
    h=0
    for i in csv_list:
        if h!=0:
            Customer.objects.update_or_create(
                cus_id=i[0],
                defaults={
                    "cus_id":i[0],
                    "sei":i[1],
                    "mei":i[2],
                    "sei_kana":i[3],
                    "mei_kana":i[4],
                    "mail1":i[5],
                    "mail2":i[6],
                    "mail3":i[7],
                    "yubin":i[8],
                    "pref":i[9],
                    "city":i[10],
                    "banchi":i[11],
                    "build":i[12],
                    "com":i[13],
                    "busho":i[14],
                    "tel":i[15],
                    "mob":i[16],
                    "fax":i[17],
                    "toroku":i[18],
                    "kensu":i[19],
                    "money":i[20],
                    "adress":i[21],
                }            
            )
        h+=1   


    #見積受注
    data = io.TextIOWrapper(request.FILES['csv2'].file, encoding="cp932")
    csv_content = csv.reader(data)
    
    csv_list=list(csv_content)
        
    h=0
    for i in csv_list:
        if h!=0:
            Recieve.objects.update_or_create(
                rec_id=i[0],               
                defaults={
                    "rec_id":i[0],
                    "rec_no":i[1],
                    "rec_ver":i[2],
                    "status":i[3],
                    "mitsu_day":i[4],
                    "rec_day":i[5],
                    "eigyou_sei":i[6],
                    "eigyou_mei":i[7],
                    "eigyou_busho":i[8],
                    "rec_cus_id":Customer.objects.get(cus_id=i[9]),
                    "keiro":i[10],
                    "mitsu_money":i[11],
                }                
            )
        h+=1


    #見積商品
    data = io.TextIOWrapper(request.FILES['csv3'].file, encoding="cp932")
    csv_content = csv.reader(data)
    
    csv_list=list(csv_content)
        
    h=0
    for i in csv_list:
        if h!=0:
            Item.objects.create(
                item_rec_id=Recieve.objects.get(rec_id=i[0]),
                item_name=i[1],           
            )
        h+=1


    return redirect("houjin1:index")



@login_required
def v2_index(request):
    return render(request,"houjin1/v2_index.html")


def v2_top(request):
    return render(request,"houjin1/v2_top.html")


def v2_left(request):
    if "hyouji" in request.session:
        hyouji=request.session["hyouji"]
    else:
        request.session["hyouji"]="全て"
        hyouji="全て"

    if hyouji=="全て":
        cusms=Customer.objects.all()
    else:
        cusms=Customer.objects.filter(tantou=hyouji)

    return render(request,"houjin1/v2_left.html",{"cusms":cusms})


def v2_right(request):
    form=Right_form()
    return render(request,"houjin1/v2_right.html",{"form":form})


def v2_right1(request,pk):
    if request.method=="POST":
        ins=Customer.objects.get(pk=pk)
        form=Right_form(request.POST,instance=ins)
        form.save()
        return redirect("houjin1:v2_left")
    else:
        ins=Customer.objects.get(pk=pk)
        cus=Customer.objects.filter(pk=pk)
        form=Right_form(instance=ins)
        return render(request,"houjin1/v2_right.html",{"form":form,"cus":cus})


def v2_hyouji_all(request):
    request.session["hyouji"]="全て"
    return redirect("houjin1:v2_left")

def v2_hyouji_inoue(request):
    request.session["hyouji"]="井上"
    return redirect("houjin1:v2_left")

def v2_hyouji_furukawa(request):
    request.session["hyouji"]="古川"
    return redirect("houjin1:v2_left")

def v2_hyouji_mashimo(request):
    request.session["hyouji"]="眞下"
    return redirect("houjin1:v2_left")


def v2_delete(request):
    if request.method=="POST":
        cus_id=request.POST["cus_id"]
        Customer.objects.get(cus_id=cus_id).delete()
        return redirect("houjin1:v2_index")




# def upload2(request):

#     if request.method == 'POST' and request.FILES['excel']:
#         excel = request.FILES['excel']
#         #excelの読み込み
#         wb = openpyxl.load_workbook(excel)

#         ###################
#         #顧客レポート
#         ws = wb["顧客レポート"]

#         all_data=[]
#         for row in ws.iter_rows(min_row=2):
#             line=[]
#             for cell in row:
#                 line.append(cell.value)
#             all_data.append(line)

#         for i in all_data:
#             Customer.objects.update_or_create(
#                 cus_id=i[0],
#                 defaults={
#                     "cus_id":i[0],
#                     "sei":i[1],
#                     "mei":i[2],
#                     "sei_kana":i[3],
#                     "mei_kana":i[4],
#                     "mail1":i[5],
#                     "mail2":i[6],
#                     "mail3":i[7],
#                     "yubin":i[8],
#                     "pref":i[9],
#                     "city":i[10],
#                     "banchi":i[11],
#                     "build":i[12],
#                     "com":i[13],
#                     "busho":i[14],
#                     "tel":i[15],
#                     "mob":i[16],
#                     "fax":i[17],
#                     "toroku":i[18],
#                     "kensu":i[19],
#                     "money":i[20],
#                     "adress":i[21],
#                 }            
#             )
        
#         ###################
#         #見積受注
#         ws = wb["見積受注"]

#         all_data=[]
#         for row in ws.iter_rows(min_row=2):
#             line=[]
#             for cell in row:
#                 line.append(cell.value)
#             all_data.append(line)

#         for i in all_data:
#             Recieve.objects.update_or_create(
#                 rec_id=i[0],               
#                 defaults={
#                     "rec_id":i[0],
#                     "rec_no":i[1],
#                     "rec_ver":i[2],
#                     "status":i[3],
#                     "mitsu_day":str(i[4])[:10],
#                     "rec_day":str(i[5])[:10],
#                     "eigyou_sei":i[6],
#                     "eigyou_mei":i[7],
#                     "eigyou_busho":i[8],
#                     "rec_cus_id":Customer.objects.get(cus_id=i[9]),
#                     "keiro":i[10],
#                     "mitsu_money":i[11],
#                 }                
#             )


#         ###################
#         #見積商品
#         ws = wb["見積商品"]

#         all_data=[]
#         for row in ws.iter_rows(min_row=2):
#             line=[]
#             for cell in row:
#                 line.append(cell.value)
#             all_data.append(line)

#         for i in all_data:
#             Item.objects.create(
#                 item_rec_id=Recieve.objects.get(rec_id=i[0]),
#                 item_name=i[1],           
#             )


#     return redirect("houjin1:index")

