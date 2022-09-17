from sqlalchemy import and_
from project.models.usr_user import UsrUser
from . import APIRouter, Body, Depends, Form, Utility, SUCCESS, FAIL, Depends, Session, get_database_session, \
    AuthHandler

router = APIRouter(
    prefix="/admin",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login", response_description="Admin authenticated")
async def login(request: dict = Body(), db: Session = Depends(get_database_session)):
    try:
        email = request['email']
        password = request['password']
        user = db.query(UsrUser).filter(and_(UsrUser.email == email), UsrUser.is_delete == 0)
        if len(user.all()) == 1:
            hash_password = user[0].password
            user_id = user[0].user_id
            verify_password = AuthHandler().verify_password(str(password), hash_password)
        else:
            return Utility.common_response(status=FAIL, message="Invalid credential's", error=[], data={})
        if verify_password is True:
            login_token = AuthHandler().encode_token(str(user_id))
        else:
            return Utility.common_response(status=FAIL, message="Invalid credential's", error=[], data={})
        if login_token:
            user.update({UsrUser.token: login_token}, synchronize_session=False)
            db.flush()
            db.commit()
            return {"status": SUCCESS, "message": "Admin logged In", "error": [], "data": user.one()}
        else:
            return Utility.common_response(status=FAIL, message="Token not assigned", error=[], data={})
    except Exception as E:
        print(E)
        return Utility.common_response(status=FAIL, message="Something went wrong", error=[], data={})

#
# @router.post("/forgot-password", response_description="Admin forgot password")
# async def forgot_password(request: dict = Body(), db: Session = Depends(get_database_session)):
#     try:
#         email = request['email']
#         url = request['url']
#         user = db.query(UsrUser).filter(UsrUser.email == email)
#         if len(user.all()) == 1:
#             forgot_password_token = Utility.uuid()
#         else:
#             return Utility.common_response(status=FAIL, message="Invalid email", error=[], data={})
#         token_update = user.update({UsrUser.forgot_password_token: str(forgot_password_token)},
#                                    synchronize_session=False)
#         db.flush()
#         db.commit()
#         if token_update == 1:
#             smtp = db.query(MstEmailAccount).filter_by(is_active=1)
#             conf = ConnectionConfig(
#                 MAIL_FROM=smtp.one().mail_sender,
#                 MAIL_USERNAME=smtp.one().username,
#                 MAIL_PASSWORD=smtp.one().password,
#                 MAIL_PORT=smtp.one().port_no,
#                 MAIL_SERVER=smtp.one().smtp_address,
#                 MAIL_TLS=True if smtp.one().is_tls == 1 else False,
#                 MAIL_SSL=True if smtp.one().is_ssl == 1 else False
#             )
#             send_email = await SendEmail(conf, email).reset_password_mail(url, forgot_password_token)
#             if send_email.status_code == 200:
#                 return Utility.common_response(status=SUCCESS, message="Email sent for reset password", error=[],
#                                                data={})
#             return Utility.common_response(status=FAIL, message="Error while sending email", error=[], data={})
#     except Exception as E:
#         print(E)
#         return Utility.common_response(status=FAIL, message="Something went wrong", error=[], data={})
#
#
# @router.post("/update-password", response_description="Admin update password")
# async def update_password(request: dict = Body(), db: Session = Depends(get_database_session)):
#     try:
#         new_password = request['new_password']
#         token = request['token']
#         if token == "" or new_password == "":
#             return Utility.common_response(status=FAIL, message="Invalid credential's", error=[], data={})
#         user = db.query(UsrUser).filter(UsrUser.forgot_password_token == token)
#         if len(user.all()) == 1:
#             hash_password = AuthHandler().get_password_hash(str(new_password))
#             password_update = user.update({UsrUser.password: hash_password, UsrUser.forgot_password_token: ''},
#                                           synchronize_session=False)
#             db.flush()
#             db.commit()
#         else:
#             return Utility.common_response(status=FAIL, message="Invalid token", error=[], data={})
#         if password_update == 1:
#             return Utility.common_response(status=SUCCESS, message="Password updated", error=[],
#                                            data={})
#         return Utility.common_response(status=FAIL, message="Fail to update new password", error=[], data={})
#     except Exception as E:
#         print(E)
#         return Utility.common_response(status=FAIL, message="Something went wrong", error=[], data={})
#
#
# @router.post("/change-password", response_description="Admin change password")
# async def change_password(auth_user=Depends(AuthHandler().auth_wrapper), request: dict = Body(),
#                           db: Session = Depends(get_database_session)):
#     try:
#         user_id = request['user_id']
#         old_password = request['old_password']
#         new_password = request['new_password']
#         if user_id == "" or old_password == "" or new_password == "":
#             return Utility.common_response(status=FAIL, message="Invalid credential's", error=[], data={})
#         if user_id is None or old_password is None or new_password is None:
#             return Utility.common_response(status=FAIL, message="Invalid credential's", error=[], data={})
#         user = db.query(UsrUser).filter(UsrUser.user_id == user_id).filter(
#             UsrUser.user_type_term == 'Admin').filter(UsrUser.is_delete == 0).filter(UsrUser.is_active == 1)
#         if len(user.all()) != 1:
#             return Utility.common_response(status=FAIL, message="Invalid detail's", error=[], data={})
#         password_check = AuthHandler().verify_password(old_password, str(user.one().password))
#
#         if password_check:
#             user.update({UsrUser.password: AuthHandler().get_password_hash(str(new_password)),
#                          UsrUser.updated_on: str(datetime.now()), UsrUser.updated_by: str(auth_user)},
#                         synchronize_session=False)
#             db.flush()
#             db.commit()
#             return Utility.common_response(status=SUCCESS, message="Password changed", error=[], data={})
#         return Utility.common_response(status=FAIL, message="Invalid password", error=[], data={})
#     except Exception as E:
#         print(E)
#         return Utility.common_response(status=FAIL, message="Something went wrong", error=[], data={})
#
#
# @router.get("/get-smtp", response_description="Admin web setting", )
# async def get_smtp(auth_user=Depends(AuthHandler().auth_wrapper), db: Session = Depends(get_database_session)):
#     try:
#         smtp = db.query(MstEmailAccount).filter(MstEmailAccount.is_active == 1).one()
#         # if len(smtp.all()) != 1:
#         #     return Utility.common_response(status=FAIL, message="Invalid smtp", error=[], data={})
#         # response_data = {
#         #     "email_protocol": smtp.one().email_protocol,
#         #     "email_id": smtp.one().email_id,
#         #     "mail_sender": smtp.one().mail_sender,
#         #     "port_no": smtp.one().port_no,
#         #     "username": smtp.one().username,
#         #     "password": smtp.one().password,
#         #     "smtp_address": smtp.one().smtp_address,
#         #     "is_tls": smtp.one().is_tls,
#         #     "is_ssl": smtp.one().is_ssl,
#         # }
#         return {"status": SUCCESS, "message": "Web setting's data fetched", "error": [], "data": smtp}
#     except Exception as E:
#         print(E)
#         return Utility.common_response(status=FAIL, message="Something went wrong", error=[], data={})
#
#
# @router.post("/update-smtp", response_description="Admin web setting")
# async def update_smtp(request: dict = Body(), auth_user=Depends(AuthHandler().auth_wrapper),
#                       db: Session = Depends(get_database_session)):
#     try:
#         email_protocol = request['email_protocol']
#         email_id = request['email_id']
#         is_tls = request['is_tls']
#         is_ssl = request['is_ssl']
#         port_no = request['port_no']
#         password = request['password']
#         smtp_address = request['smtp_address']
#         form_name = request['form_name']
#
#         if email_protocol == '' or email_id == '' or is_tls == '' or is_ssl == '' or port_no == '' or password == '' or smtp_address == '' or form_name == '':
#             return Utility.common_response(status=FAIL, message="Provide valid detail's", error=[], data={})
#         if email_protocol is None or email_id is None or is_tls is None or is_ssl is None or port_no is None or password is None or smtp_address is None or form_name is None:
#             return Utility.common_response(status=FAIL, message="Provide valid detail's", error=[], data={})
#         if int(is_tls) != 0 and int(is_tls) != 1:
#             return Utility.common_response(status=FAIL, message="Provide valid tls", error=[], data={})
#         if int(is_ssl) != 0 and int(is_ssl) != 1:
#             return Utility.common_response(status=FAIL, message="Provide valid ssl", error=[], data={})
#         if type(port_no) != int:
#             return Utility.common_response(status=FAIL, message="Port number must be integer", error=[], data={})
#
#         smtp = db.query(MstEmailAccount).filter(MstEmailAccount.is_active == 1)
#         # print(smtp)
#         # if len(smtp.all()) != 1:
#         #     return Utility.common_response(status=FAIL, message="Invalid detail's", error=[], data={})
#
#         smtp_inactivate = smtp.update({MstEmailAccount.is_active: 0}, synchronize_session=False)
#         db.flush()
#         db.commit()
#         if smtp_inactivate == 1:
#             new_smtp = MstEmailAccount(email_protocol=email_protocol, mst_account_id=Utility.uuid(),
#                                        email_id=email_id, mail_sender=email_id,
#                                        port_no=port_no, is_active=1, is_tls=is_tls, is_ssl=is_ssl, form_name=form_name,
#                                        username=email_id, password=password, created_by=str(auth_user),
#                                        updated_by=str(auth_user), created_at=str(datetime.now()),
#                                        updated_at=str(datetime.now()), smtp_address=smtp_address)
#             db.add(new_smtp)
#             db.flush()
#             db.commit()
#             if new_smtp.seq_no:
#                 return Utility.common_response(status=SUCCESS, message="Web setting's data updated", error=[], data={})
#             return Utility.common_response(status=FAIL, message="Update failed", error=[], data={})
#     except Exception as E:
#         print(E)
#         return Utility.common_response(status=FAIL, message="Something went wrong", error=[], data={})
#
#
# @router.get("/get-cms", response_description="CMS Pages", )
# async def get_cms(auth_user=Depends(AuthHandler().auth_wrapper), db: Session = Depends(get_database_session)):
#     try:
#         response_data = {}
#         pass
#         return Utility.common_response(status=SUCCESS, message="Web setting's data fetched", error=[],
#                                        data=response_data)
#     except Exception as E:
#         print(E)
#         return Utility.common_response(status=FAIL, message="Something went wrong", error=[], data={})
