from typing import Annotated
from fastapi import Depends
from db.unitofwork import ABCUnitOfWork, UnitOfWork


UOWDep = Annotated[ABCUnitOfWork, Depends(UnitOfWork)]
