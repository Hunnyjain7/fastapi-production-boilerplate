from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from project.common.utility import Utility
from project.constant.status_constant import FAIL, SUCCESS
from project.routes.api import router as api_router

# This way all the tables can be created in database but cannot be updated for that use alembic migrations
# usr_user.Base.metadata.create_all(bind=engine)

app = FastAPI(title='FastApi-Boilerplate', description='A Perfect Boiler Plate For Developing In Production',
              version='1.0')

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(api_router)


@app.get('/')
def read_root():
    try:
        return Utility.json_response(status=SUCCESS, message='Welcome to FastAPI Production Boilerplate Version: 1',
                                     error=[], data={})
    except Exception as E:
        print(E)
        return Utility.json_response(status=FAIL, message='Something went wrong', error=[], data={})


@app.get('/media/images/{path}/{image}')
def images(path: str, image: str):
    file_location = f'project/media/images/{path}/{image}'
    return FileResponse(file_location)

# if __name__ == '__main__':
#     uvicorn.run("application:app", host='localhost', port=8000, log_level="debug", reload=True)
#     print("running")
