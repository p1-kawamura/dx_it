from django.db import models


class Customer(models.Model):
    cus_id=models.CharField("顧客ID",max_length=10,null=True,blank=True)
    sei=models.CharField("姓",max_length=10,null=True,blank=True)
    mei=models.CharField("名",max_length=10,null=True,blank=True)
    sei_kana=models.CharField("姓かな",max_length=10,null=True,blank=True)
    mei_kana=models.CharField("名かな",max_length=10,null=True,blank=True)
    mail1=models.EmailField("メール1",null=True,blank=True)
    mail2=models.EmailField("メール2",null=True,blank=True)
    mail3=models.EmailField("メール3",null=True,blank=True)
    yubin=models.CharField("郵便番号",max_length=10,null=True,blank=True)
    adress=models.CharField("住所",max_length=100,null=True,blank=True)
    pref=models.CharField("都道府県",max_length=10,null=True,blank=True)
    city=models.CharField("市区町村",max_length=50,null=True,blank=True)
    banchi=models.CharField("番地",max_length=50,null=True,blank=True)
    build=models.CharField("建物",max_length=50,null=True,blank=True)
    com=models.CharField("会社",max_length=50,null=True,blank=True)
    busho=models.CharField("部署",max_length=50,null=True,blank=True)
    tel=models.CharField("電話",max_length=20,null=True,blank=True)
    mob=models.CharField("携帯",max_length=20,null=True,blank=True)
    fax=models.CharField("FAX",max_length=20,null=True,blank=True)
    toroku=models.CharField("登録日",max_length=10,null=True,blank=True)
    kensu=models.IntegerField("件数",null=True,blank=True)
    money=models.IntegerField("金額",null=True,blank=True)
    tantou=models.IntegerField("担当",default=0)
    dm_day=models.CharField("DM",max_length=10,null=True,blank=True)
    tel_day=models.CharField("TEL",max_length=10,null=True,blank=True)
    gaisho_day=models.CharField("外商",max_length=10,null=True,blank=True)
    nohin_day=models.CharField("納品",max_length=10,null=True,blank=True)
    dm_check=models.BooleanField("DMリスト",default=False)
    bikou=models.TextField("備考",null=True,blank=True)
    kanshoku=models.IntegerField("感触",default=0)

    def __str__(self):
        return self.cus_id


class Recieve(models.Model):
    rec_id=models.CharField("見積ID",max_length=10,null=True,blank=True)
    rec_no=models.CharField("見積番号",max_length=10,null=True,blank=True)
    rec_ver=models.CharField("バージョン",max_length=10,null=True,blank=True)
    status=models.CharField("ステータス",max_length=10,null=True,blank=True)
    mitsu_day=models.CharField("見積日",max_length=10,null=True,blank=True)
    rec_day=models.CharField("受注日",max_length=10,null=True,blank=True)
    eigyou_sei=models.CharField("担当_姓",max_length=10,null=True,blank=True)
    eigyou_mei=models.CharField("担当_名",max_length=10,null=True,blank=True)
    eigyou_busho=models.CharField("営業部署",max_length=20,null=True,blank=True)
    rec_cus_id=models.ForeignKey(Customer,verbose_name="顧客ID",on_delete=models.CASCADE,null=True,blank=True)
    keiro=models.CharField("流入経路",max_length=10,null=True,blank=True)
    mitsu_money=models.IntegerField("見積金額",null=True,blank=True)

    def __str__(self):
        return self.rec_id


class Item(models.Model):
    item_rec_id=models.ForeignKey(Recieve,verbose_name="見積ID",on_delete=models.CASCADE,null=True,blank=True)
    item_name=models.CharField("品名",max_length=100,null=True,blank=True)

    def __str__(self):
        return self.item_name
