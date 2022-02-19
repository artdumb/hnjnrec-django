from operator import itemgetter
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from first.models import Picdata, Placedata, Reviewdata, Password
from first.forms import PicdataForm, PlacedataForm
from first.forms import ReviewForm
from django.http import HttpResponseRedirect
from . import models
from django.core.paginator import Paginator
import random
from datetime import datetime
from django.utils.dateformat import DateFormat


def todayPhoto(request):
    today = DateFormat(datetime.now()).format('Ymd')
    items_pic = Picdata.objects.all()
    random.seed(today)
    item = random.sample(list(items_pic), 4)
    print(item)
    context = {
        'item': item,
    }
    return render(request, 'first/today-photo.html', context)


def mainpage(request):
    items_pic = Picdata.objects.all()
    items_place = Placedata.objects.all()
    new_item = []
    # 슬라이드에 들어갈 리스트 불러오기
    for place in items_place:
        place_pic = Picdata.objects.filter(place_id=place.id)
        new_item.append(place_pic)
    # 슬라이드 최대개수 2장으로 제한하기
    limited_item = []
    for i in range(len(new_item)):
        limited_item_temp = []
        for j in range(len(new_item[i])):
            if j < 3:
                limited_item_temp.append(new_item[i][j])
        limited_item.append(limited_item_temp)

    print(limited_item)
    # new-item의 인덱스 ==> 장소들
    # new_item[0] ==> 첫번째 장소의 모든 사진들
    # new_item[0][0]==> 첫번째 장소의 첫번째 사진
    paginator = Paginator(limited_item, 6)  # third/list?page=1 쿼리에서 페이지를 받앋옴
    page = request.GET.get('page')
    new_page_item = paginator.get_page(page)
    context = {
        'items': new_page_item,
    }
    return render(request, 'first/mainpage.html', context)


def place_list(request):
    items = Placedata.objects.all()
    context = {
        'items': items
    }
    return render(request, 'first/place_list.html', context)


def upload_place(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        password_db = get_object_or_404(Password, pk=1)
        form = PlacedataForm(request.POST)
        if form.is_valid() and password == password_db.password:
            new_item = form.save()
        return HttpResponseRedirect('/place')
    form_place = PlacedataForm()
    return render(request, 'first/upload_place.html', {'form_place': form_place})


def upload(request, id):
    if request.method == 'POST':
        imagee = request.FILES['image']
        password = request.POST.get('password', '')
        password_db = get_object_or_404(Password, pk=1)
        place = get_object_or_404(Placedata, pk=id)
        if password == password_db.password:
            picdb = models.Picdata.objects.create(
                title=request.POST['title'],
                cam=request.POST['cam'],
                film=request.POST['film'],
                lens=request.POST['lens'],
                descrip=request.POST['descrip'],
                place_name=place.place_name,
                place_id=place,
                password="aa",
                image=imagee
            )
            picdb.save()

        return redirect('/main', id=id)

    item = get_object_or_404(Placedata, pk=id)
    form = PicdataForm(initial={'place_id': item})
    return render(request, 'first/upload.html', {'form': form, 'item': item})


def detail(request, id):
    items = Picdata.objects.filter(place_id_id=id)
    paginator = Paginator(items, 8)  # third/list?page=1 쿼리에서 페이지를 받앋옴
    page = request.GET.get('page')
    new_page_item = paginator.get_page(page)
    context = {
        'items': new_page_item
    }
    return render(request, 'first/detail.html', context)


def more_detail(request, id):
    if 'id' is not None:

        item = Picdata.objects.get(id=id)
        reviews = Reviewdata.objects.filter(pic=item).all()
        context = {
            'item': item,
            'reviews': reviews,
        }
        return render(request, 'first/more_detail.html', context)
    return HttpResponseRedirect('/')


def delete(request, id):
    item = get_object_or_404(Picdata, pk=id)
    password_db = get_object_or_404(Password, pk=1)
    if request.method == 'POST' and 'password' in request.POST:
        if request.POST.get('password') == password_db.password:
            item.delete()
            return redirect('/main')
    return render(request, 'first/delete.html', {'item': item})


def review_create(request, id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('moredetail', id=id)
    item = get_object_or_404(Picdata, pk=id)
    form = ReviewForm(initial={'pic': item})
    return render(request, 'first/review_create.html', {'form': form, 'item': item})


def review_delete(request, pic_id, review_id):
    pic = get_object_or_404(Picdata, pk=pic_id)
    review = get_object_or_404(Reviewdata, pk=review_id)
    if request.method == 'POST' and 'password' in request.POST:
        if review.password == request.POST.get('password') or review.password is None:
            review.delete()
            return redirect('moredetail', id=pic_id)
    return render(request, 'first/review_delete.html', {'item': pic, 'review': review})


def seceret_img(request):
    password = request.POST.get('password', '')
    if request.method == 'POST' and 'password' in request.POST:
        if password == request.POST.get('password'):
            return render(request, 'first/secret_img.html')
    return render(request, 'first/secret.html')
