from django.shortcuts import render,redirect
from .models import Customer,Recieve,Item,Sell
from django.contrib.auth.decorators import login_required
import io
import csv
from .forms import Right_form
from django.http import HttpResponse
import datetime
from django.db import models
from django.db.models import Q



@login_required
def index(request):
    if "num" not in request.session:
        request.session["num"]=1
    if "all_num" not in request.session:
        request.session["all_num"]=""
    if "tantou" not in request.session:
        request.session["tantou"]=99
    if "adress" not in request.session:
        request.session["adress"]=""
    if "bikou" not in request.session:
        request.session["bikou"]=""
    if "toroku_from" not in request.session:
        request.session["toroku_from"]=""
    if "toroku_to" not in request.session:
        request.session["toroku_to"]=""
    if "kanshoku" not in request.session:
        request.session["kanshoku"]=0
    if request.session["kanshoku"]=="":
        request.session["kanshoku"]=0

    return render(request,"houjin/index.html")


def top(request):
    list={"99":"全て表示","1":"井上","2":"古川","3":"眞下","4":"夏八木","5":"藤井","6":"武井","7":"粂川","0":"担当なし"}
    list2={"0":"","5":"★★★★★（5）","4":"★★★★☆（4）","3":"★★★☆☆（3）","2":"★★☆☆☆（2）","1":"★☆☆☆☆（1）"}
    tantou=request.session["tantou"]  
    adress=request.session["adress"]
    bikou=request.session["bikou"]
    toroku_from=request.session["toroku_from"]
    toroku_to=request.session["toroku_to"]
    kanshoku=request.session["kanshoku"]
    params={
        "list":list,
        "list2":list2,
        "tantou":tantou,
        "adress":adress,
        "bikou":bikou,
        "toroku_from":toroku_from,
        "toroku_to":toroku_to,
        "kanshoku":kanshoku,
    }
    return render(request,"houjin/top.html",params)


def left(request):
    tantou=request.session["tantou"]
    adress=request.session["adress"]
    bikou=request.session["bikou"]
    toroku_from=request.session["toroku_from"]
    toroku_to=request.session["toroku_to"]
    kanshoku=request.session["kanshoku"]

    #検索条件
    str={}
    if adress != "":
        str["adress__contains"]=adress
    if bikou != "":
        str["bikou__contains"]=bikou
    if kanshoku != "0":
        str["kanshoku"]=kanshoku
    if toroku_from != "":
        str["toroku__gte"]=toroku_from
    if toroku_to != "":
        str["toroku__lte"]=toroku_to
    

    #検索データ取得
    if tantou=="99":
        if len(str)==0:
            cusms=Customer.objects.all().order_by("com")
        else:
            cusms=Customer.objects.filter(**str).order_by("com")
    else:
        str["tantou"]=tantou
        cusms=Customer.objects.filter(**str).order_by("com")

    #全ページ数
    if cusms.count()==0:
        all_num=1
    elif cusms.count() % 30 == 0:
        all_num=cusms.count() / 30
    else:
        all_num=cusms.count() // 30 + 1


    #件数
    kensu_all=Customer.objects.all().count()
    kensu_kensaku=cusms.count()
    if tantou=="99":
        kensu_tantou=kensu_all
    else:
        kensu_tantou=Customer.objects.filter(tantou=tantou).count()
    
    list2={"99":"全て表示","1":"井上","2":"古川","3":"眞下","4":"夏八木","5":"藤井","6":"武井","7":"粂川","0":"担当なし"}
    tan=list2[tantou]
    
    
    #表示ページ情報
    list={1:"井上",2:"古川",3:"眞下",4:"夏八木",5:"藤井",6:"武井",7:"粂川"}
    num=request.session["num"]
    request.session["all_num"]=all_num
    data=cusms[(num-1)*30 : num*30]
    params={
        "num":num,
        "all_num":all_num,
        "data":data,
        "list":list,
        "kensu_all":kensu_all,
        "kensu_tantou":kensu_tantou,
        "kensu_kensaku":kensu_kensaku,
        "tan":tan,
    }

    return render(request,"houjin/left.html",params)


def page_prev(request):
    num=request.session["num"]
    if num-1 > 0:
        request.session["num"] = num - 1
    return redirect("houjin:index")


def page_first(request):
    request.session["num"] = 1
    return redirect("houjin:index")


def page_next(request):
    num=request.session["num"]
    all_num=request.session["all_num"]
    if num+1 <= all_num:
        request.session["num"] = num + 1
    return redirect("houjin:index")


def page_last(request):
    all_num=request.session["all_num"]
    request.session["num"]=all_num
    return redirect("houjin:index")


def right(request):
    form=Right_form()
    return render(request,"houjin/right.html",{"form":form})


def right1(request,pk):
    if request.method=="POST":
        ins=Customer.objects.get(pk=pk)
        form=Right_form(request.POST,instance=ins)
        form.save()
        return redirect("houjin:left")
    else:
        ins=Customer.objects.get(pk=pk)
        cus=Customer.objects.filter(pk=pk)
        form=Right_form(instance=ins)
        sell=Sell.objects.filter(sell_cus_id = ins.cus_id).order_by("sell_mon")
        return render(request,"houjin/right.html",{"form":form,"cus":cus,"sell":sell})


def hyouji(request):
    tantou=request.POST["tantou"]
    adress=request.POST["find_adress"]
    bikou=request.POST["find_bikou"]
    toroku_from=request.POST["find_toroku_from"]
    toroku_to=request.POST["find_toroku_to"]
    kanshoku=request.POST["find_kanshoku"]

    request.session["tantou"]=tantou
    request.session["num"]=1
    request.session["adress"]=adress
    request.session["bikou"]=bikou
    request.session["toroku_from"]=toroku_from
    request.session["toroku_to"]=toroku_to
    request.session["kanshoku"]=kanshoku

    return redirect("houjin:index")



def delete(request):
    if request.method=="POST":
        cus_id=request.POST["cus_id"]
        Customer.objects.get(cus_id=cus_id).delete()
        return redirect("houjin:index")


def dm_down(request):
    return render(request,"houjin/index.html",{"dm":"OK"})


def dm_send(request):
    response = HttpResponse(content_type='text/csv; charset=CP932')
    response['Content-Disposition'] = 'attachment;  filename="dm_send.csv"'
    writer = csv.writer(response)

    tan=request.session["tantou"]
    if tan == "99":
        dm_csv=Customer.objects.filter(dm_check=True)
    else:
        dm_csv=Customer.objects.filter(dm_check=True,tantou=tan)

    for i in dm_csv:
        writer.writerow([
            i.com,
            i.busho,
            i.sei + i.mei,
            i.mail1,
            ])
    
    dt=datetime.date.today()
    dm_csv.update(dm_day=dt,dm_check=False)

    return response
    


def csv_page(request):
    return render(request,"houjin/csv.html")


@login_required
def download(request):
    response = HttpResponse(content_type='text/csv; charset=CP932')
    response['Content-Disposition'] = 'attachment;  filename="customer.csv"'
    writer = csv.writer(response)

    cus=Customer.objects.all()
    for i in cus:
        writer.writerow([
            i.cus_id,
            i.kensu,
            i.money,
            ])
    return response


def sell(request):
    id=request.POST["sell_cus_id"]
    mon=request.POST["sell_mon"]
    money=request.POST["sell_money"]
    Sell.objects.create(sell_cus_id=id, sell_mon=mon, sell_money=money)

    ins=Customer.objects.get(cus_id=id)
    cus=Customer.objects.filter(cus_id=id)
    form=Right_form(instance=ins)
    sell=Sell.objects.filter(sell_cus_id=id).order_by("sell_mon")

    return render(request,"houjin/right.html",{"form":form,"cus":cus,"sell":sell})


def sell_delete(request,pk):
    Sell.objects.get(pk=pk).delete()

    id=request.POST["sell_cus_id"]
    ins=Customer.objects.get(cus_id=id)
    cus=Customer.objects.filter(cus_id=id)
    form=Right_form(instance=ins)
    sell=Sell.objects.filter(sell_cus_id=id).order_by("sell_mon")

    return render(request,"houjin/right.html",{"form":form,"cus":cus,"sell":sell})



def index2(request):
    
    if "nen" not in request.session:
        nen="2022"
        request.session["nen"]="2022"
    else:
        nen=request.session["nen"]

    nen_list=["2022","2023","2024","2025"]
    tsuki_list=[]
    juchu=[]
    yotei=[]
    
    
    cus=Sell.objects.distinct().values_list("sell_cus_id",flat=True)

    for i in range(1,13):
        tsuki_list.append(str(i)+"月")

        #担当付きの場合
        # total=Recieve.objects.filter(~Q(rec_cus_id__tantou = "0"),rec_day__contains = nen + "/" + str(i) +"/").aggregate(total = models.Sum("mitsu_money"))
        #目標設定ありの場合
        total=Recieve.objects.filter(rec_cus_id__cus_id__in=cus , rec_day__contains = nen + "/" + str(i) +"/").aggregate(total = models.Sum("mitsu_money"))
        if total["total"] is None:
            total["total"]=0
        juchu.append(total["total"])

        total2=Sell.objects.filter(sell_mon__contains  = nen + "-" + str(i).zfill(2)).aggregate(total2 = models.Sum("sell_money"))
        if total2["total2"] is None:
            total2["total2"]=0
        yotei.append(total2["total2"])

    tsuki_list.append("合計")   
    juchu.append(sum(juchu))
    yotei.append(sum(yotei))
    
    params={
        "nen_list":nen_list,
        "tsuki_list":tsuki_list,
        "nen":nen,
        "juchu":juchu,
        "yotei":yotei,
    }   
    return render(request,"houjin/index2.html",params)



def index2_nen(request):
    nen=request.POST["nen"]
    request.session["nen"]=nen
    return redirect("houjin:index2")



def index2_click(request):
    if request.method == "POST":
        row=request.POST["row"]
        col=request.POST["col"]
        print(row,col)

    return redirect("houjin:index2")



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



    #WEB更新
    data = io.TextIOWrapper(request.FILES['csv4'].file, encoding="cp932")
    csv_content = csv.reader(data)
    
    csv_list=list(csv_content)

    if len(csv_list[0])>0:
        for i in csv_list:
            Customer.objects.update_or_create(
                cus_id=i[0],
                defaults={
                    "cus_id":i[0],
                    "kensu":i[1],
                    "money":i[2],
                }            
            )  

    return redirect("houjin:index")

