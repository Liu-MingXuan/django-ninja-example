from ninja import NinjaAPI
from ninja import Router


router = Router(tags=['web'])

@router.get('/hello/')
def hello(request):
    return {'message': 'hello world'}

@router.get('/abc')
def abc(request):
    return {'message': 'abc'}