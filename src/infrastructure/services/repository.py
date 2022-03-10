from datetime import datetime
from typing import List

from src.core.interfaces.model_abc import ModelAbstract
from src.core.interfaces.repository_abc import RepositoryAbstract

from src.shared import errors

from sqlalchemy.orm import Session

class SqlAlchemyRepository(RepositoryAbstract):

    def __init__(self, session, object_type) -> None:
        self.session: Session = session
        self.object_type = object_type

    def get_by_filter(self, filter) -> List[ModelAbstract]:
        try:
            result = self.session.query(self.object_type).filter(filter).all()
            if result == None:
                result = 0
            return result
        except Exception as err:
            print(err)

    def get_by_id(self, target_id: int) -> ModelAbstract:
        try:
            result = self.session.query(self.object_type).get(target_id)
            if not result:
                raise errors.EmptyError
            return result
        except Exception as err:
            print(err)

    def delete_by_filter(self, filter) -> int:
        try:
            result = self.session.query(self.object_type).filter(filter).delete()
            if result == None:
                result = 0
            return result
        except Exception as err:
            print(err)

    def delete_by_id(self, target_id: int) -> int:
        try:
            result = self.session.query(self.object_type).filter(self.object_type.id == target_id).delete()
            if result is None:
                result = 0
            return result
        except Exception as err:
            print(err)


    def insert(self, new: ModelAbstract) -> int:
        try:
            new.inserted_at=datetime.now()
            self.session.add(new)
        except Exception as err:
            print(err)


    def update(self, new):
        return super().update(new)