import re
from datetime import datetime

from sqlalchemy import and_

from project.models.usr_user import UsrUser

from ...schemas.login import Login
from ...schemas.register import Register
from . import (EXCEPTION, FAIL, SUCCESS, APIRouter, AuthHandler, Depends,
               Session, Utility, get_database_session)

# APIRouter creates path operations for product module
router = APIRouter(
    prefix='/admin',
    tags=['Admin Authentication'],
    responses={404: {'description': 'Not found'}},
)


@router.post('/login', response_description='Admin authenticated')
def admin_login(request: Login, db: Session = Depends(get_database_session)):
    try:
        email = request.email
        password = request.password
        user = db.query(UsrUser).filter(UsrUser.email == email, UsrUser.is_delete == '0', UsrUser.is_active == '1',
                                        UsrUser.user_type_term == 'Admin')
        if user.count() != 1:
            return Utility.json_response(status=FAIL, message="Invalid credential's", error=[], data={})
        verify_password = AuthHandler().verify_password(str(password), user.one().password)
        if not verify_password:
            return Utility.json_response(status=FAIL, message="Invalid credential's", error=[], data={})
        login_token = AuthHandler().encode_token(user.one().user_id)
        if not login_token:
            return Utility.json_response(status=FAIL, message='Token not assigned', error=[], data={})
        user.update({UsrUser.token: login_token}, synchronize_session=False)
        db.flush()
        db.commit()
        return Utility.dict_response(status=SUCCESS, message='Logged in successfully', error=[], data=user.one())
    except Exception as E:
        print(E)
        db.rollback()
        return Utility.json_response(status=EXCEPTION, message='Something went wrong', error=[], data={})


@router.post('/register', response_description='User Registration')
async def register(request: Register, db: Session = Depends(get_database_session)):
    try:
        user_name = request.user_name
        contact = request.contact
        email = request.email
        password = request.password
        if user_name == '' or contact == '' or email == '' or password == '':
            return Utility.json_response(status=FAIL, message="Provide valid detail's", error=[], data={})
        if user_name is None or contact is None or email is None or password is None:
            return Utility.json_response(status=FAIL, message="Provide valid detail's", error=[], data={})
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(email_regex, email):
            return Utility.json_response(status=FAIL, message='Provide valid email', error=[], data={})
        # contact_digits = math.floor(math.log10(contact)) + 1
        if len(str(contact)) < 7 or len(str(contact)) > 13:
            return Utility.json_response(status=FAIL, message='Contact number not valid. Length must be 7-13.',
                                         error=[], data={})
        user_with_email = db.query(UsrUser).filter(and_(UsrUser.email == email), UsrUser.is_delete == 0).all()
        if len(user_with_email) != 0:
            return Utility.json_response(status=FAIL, message='Email already exists', error=[], data={})

        user_data = UsrUser(user_id=Utility.uuid(), user_type_term='Admin', user_name=user_name,
                            status_term='Active', profile_pic='',
                            password=AuthHandler().get_password_hash(str(password)),
                            display_name=str(user_name).title(), email=email, mobile_no=contact, is_active=1,
                            created_on=str(datetime.now()), is_default=0, is_it_admin=0, is_delete=0)
        db.add(user_data)
        db.flush()
        db.commit()
        if user_data.seq_no:
            return Utility.json_response(status=SUCCESS, message='User Registered Successfully', error=[],
                                         data={'user_id': user_data.user_id})
        else:
            return Utility.json_response(status=FAIL, message='Something went wrong', error=[], data={})
    except Exception as E:
        print(E)
        db.rollback()
        return Utility.json_response(status=FAIL, message='Something went wrong', error=[], data={})


@router.get('/get-users', response_description='User List')
def get_users(auth_user=Depends(AuthHandler().auth_wrapper), db: Session = Depends(get_database_session)):
    try:
        users = db.query(UsrUser).all()
        return Utility.dict_response(status=SUCCESS, message='Users data fetched', error=[], data=users)
    except Exception as E:
        print(E)
        return Utility.json_response(status=FAIL, message='Something went wrong', error=[], data={})
