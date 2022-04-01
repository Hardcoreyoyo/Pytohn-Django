from django import forms
from main import models
from store.models import Catrgory, Item
from django.db import models
from django import forms


class FormModelsAddModelData(forms.ModelForm):
    name = forms.CharField(label='新增類別', required=False)
    name2 = forms.CharField(label='新增類別', required=False)

    # name3 = forms.CharField(label='新增類別', required=False)
    # name4 = forms.CharField(label='新增類別', required=False)

    class Meta:
        model = Catrgory
        fields = ('name',)


class FormModelsDelModelData(forms.ModelForm):
    id = forms.IntegerField(label='刪除類別')

    class Meta:
        model = Catrgory
        fields = ('id',)


class UpdataForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Catrgory
        fields = ('name',)


class DeleteForm(forms.ModelForm):
    class Meta:
        model = Catrgory
        fields = ('id',)


# class ItemAddModelForm(forms.ModelForm):
#     name = forms.CharField(label='名稱')
#     Category = forms.ModelChoiceField(Catrgory.objects.all(), label='類別')
#     price = forms.IntegerField(label='價錢')
#
# # 這裡的Category 變數定義名稱必須要和下方 class Meta
# #     的 fields 資料庫 column (欄位) 名稱一致
#
#     class Meta:
#         model = Item
#         fields = '__all__'


class ItemAddModelForm(forms.ModelForm):
    name = forms.CharField(label='名稱',
        widget = forms.TextInput(attrs={'class' : 'form-control'}))
    Category = forms.ModelChoiceField(Catrgory.objects.all(), label='類別',
        widget = forms.Select(attrs={'class' : 'form-control'}))
    price = forms.IntegerField(label='價錢',
        widget = forms.NumberInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = Item
        fields = '__all__'




