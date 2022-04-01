from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import request
from store.models import Catrgory, Item
from store.forms import FormModelsDelModelData, FormModelsAddModelData, UpdataForm, DeleteForm,ItemAddModelForm
from django.urls import reverse
from django.contrib import messages
from django.forms import inlineformset_factory


def Category_Out_All_Data(request):
    if request.method == 'GET':
        CategoryModelAllData = Catrgory.objects.order_by("id")
        CategoryModelAllDataCount1 = Catrgory.objects.count()
        Input_Table = FormModelsAddModelData()

        CategoryModelAllDataCount1Out = []
        for i in range(CategoryModelAllDataCount1):
            CategoryModelAllDataCount1Out.append(i + 1)

        DeleteForm = FormModelsDelModelData()
        messages.success(request, '歡迎來到Django World')
        return render(request, 'category.html',
                      {'CategoryModelAllData': CategoryModelAllData,
                       'CategoryModelAllDataCount1Out': CategoryModelAllDataCount1Out,
                       'Input_Table': Input_Table})
    if request.method == 'POST':

        if request.POST.getlist('one', []):
            try:
                FormPostData = request.POST.getlist('one', [])

                FormPostDataIntList = []
                for FormPostData11 in FormPostData:
                    FormPostData2 = int(FormPostData11)
                    FormPostDataIntList.append(FormPostData2)

                for qq in FormPostDataIntList:
                    Check_id = Catrgory.objects.get(id=qq)
                    Check_id.delete()

            except:
                return redirect(reverse('store2:category'))

            messages.success(request, '刪除資料成功')

        # if request.POST['name']:
        if request.POST['name'] or request.POST['name2']:
            if request.POST['name']:
                name = request.POST.getlist('name')
                c = min([len(name)])
                for FormPostData11DD in range(c):
                    form = FormModelsAddModelData({'name': name[FormPostData11DD]})
                    if form.is_valid():
                        form.save()

            if request.POST['name2']:
                name2 = request.POST.getlist('name2')
                c = min([len(name2)])
                for FormPostData11DD in range(c):
                    form = FormModelsAddModelData({'name': name2[FormPostData11DD]})
                    if form.is_valid():
                        form.save()

            messages.success(request, '新增資料成功')

    return redirect(reverse('store2:category'))


def CategoryUpdata(request, id):
    category = get_object_or_404(Catrgory, id=id)
    category = Catrgory.objects.get(id=id)
    if request.method == 'GET':
        UpdataOut = UpdataForm(instance=category)
        return render(request, 'Updata.html', {'UpdataOut': UpdataOut})

    elif request.method == 'POST':
        UpdataOut = UpdataForm(request.POST, instance=category)
        if not UpdataOut.is_valid():
            return render(request, 'Updata.html', {'UpdataOut': UpdataOut})

        UpdataOut.save()
        messages.success(request, '修改成功')
        return redirect('/store2/category')


def NewCategory2Func(request):
    if request.method == 'GET':
        AllData = Catrgory.objects.all()
        return render(request, 'NewCategory2.html', {'AllData': AllData})

def CategoryDelete(request):
    if request.method == 'GET':
        CategoryList = Catrgory.objects.order_by("id")
        return render(request, 'CategoryDeleteTP.html', {'CategoryList':CategoryList})
    if request.method == 'POST':
        category = request.POST["id"]
        category = Catrgory.objects.get(id=category)
        category.delete()
        messages.success(request, '刪除成功')
        return redirect('/store2/category')


def ItemAdd(request):
    if request.method == 'GET':
        ItemAddTpForm = ItemAddModelForm()
        return render(request, 'ItemAddTP.html', {'ItemAddTpForm':ItemAddTpForm})
    elif request.method == 'POST':
        ItemAddPostData = ItemAddModelForm(request.POST)
        if not ItemAddPostData.is_valid():
            messages.success(request, '增加未通過驗證')
            return redirect(reverse('store2:category'))

        ItemAddPostData.save()
        messages.success(request, '增加成功')
        return redirect(reverse('store2:category'))

def ItemDataAllOut(request):
    if request.method == 'POST':
        j = Catrgory.objects.get(name="肉類")
        for i in range(10):
            Item.objects.create(name='test'+str(i+1), Category=j,  price=int(i+1))
        return redirect(reverse('store2:ItemDataPath'))
    if request.method == 'GET':
        categoryst = Item.objects.all()
        paginator = Paginator(categoryst, 10)
        page = request.GET.get('page')
        categorys = paginator.get_page(page)
        return render(request, 'ItemData.html', {'categorys': categorys})



def BootstrapTestFunc(request):
    return render(request, 'BootstrapTest.html')