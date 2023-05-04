from fastapi import APIRouter, Body, Depends, Form
from sqlalchemy.orm import Session

from project.common.auth import AuthHandler
from project.common.utility import Utility
from project.constant.status_constant import EXCEPTION, FAIL, SUCCESS
from project.database.database import get_database_session
