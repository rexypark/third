from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError

from app.models import Address


def save(request, id):
    address = request.POST['address']
    a = Address.objects.get(id=id)
    a.address = address
    a.save()

    return HttpResponse('ok')


def edit(request, id):
    address = Address.objects.get(id=id)
    return render(request, 'app/edit.html', {'address': address})


def list(request):
    address = Address.objects.all()

    return render(
        request,
        'app/app.html',
        {'address': address}
    )

    # return HttpResponse(address)


def index(request):
    address = ''
    try:
        address = request.GET['address']

        # DB insert 데이터베이스에 저장
        add = Address(address=address)
        # class     views>index>address
        add.save()
    # models의 함수를 상속받아 실행 가능

    except MultiValueDictKeyError:
        pass

    return HttpResponse(
        '{"Hello":"' + address + '"}')
