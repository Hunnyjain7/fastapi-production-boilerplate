from fastapi import APIRouter, Body, Depends, Form
from project.common.utility import Utility
from project.constant.status_constant import SUCCESS, FAIL, EXCEPTION
from fastapi import Depends
from sqlalchemy.orm import Session
from project.database.database import get_database_session
from project.common.auth import AuthHandler