import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get('/')
@template()
def index(user_name: str = 'Anonymous'):
    return {
        'user_name': user_name
    }


@router.get('/about')
@template()
def about():
    return {}
