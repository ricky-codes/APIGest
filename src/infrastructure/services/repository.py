from src.core.interfaces.model_abc import ModelAbstract
from src.core.interfaces.repository_abc import RepositoryAbstract
from src.shared import parse_config

from sqlalchemy.orm import Session
import logging
import logging.config
import dataclasses
from typing import List
from datetime import datetime

class SqlAlchemyRepository(RepositoryAbstract):

    def __init__(self, session, object_type) -> None:
        self.session: Session = session
        self.object_type: ModelAbstract = object_type

        logging.config.dictConfig(parse_config.get_logger_config())
        self.logger = logging.getLogger("dev")
        self.logger.debug("{} repository instanciated".format(object_type.__name__))


    def get_by_filter(self, filter) -> ModelAbstract:
        self.logger.info("get_by_filter Request")
        query = self.session.query(self.object_type).filter_by(**filter)
        result = self.session.execute(query).fetchall()
        return result

    def get_by_id(self, target_id: int) -> ModelAbstract:
        """This function retrieves an object from the database.

        Return:
            The object (ModelAbstract)
        """
        self.logger.info("get_by_id Request")
        result = self.session.query(self.object_type).get(target_id)
        return result

    def get_all(self) -> List[ModelAbstract]:
        """This function retrieves all the objects in the repository.

        Returns:
            A list of the objects (List[ModelAbstract])
        """
        self.logger.info("get_all Request")
        result = self.session.query(self.object_type).all()
        return result


    def delete_by_filter(self, filter) -> int:
        """This function deletes an object using the provided filter.

        Returns:
            Affected rows provided by the database engine (int)
        """
        self.logger.info("delete_by_filter Request")
        result = self.session.query(self.object_type).filter(filter).delete()
        return result

    def delete_by_id(self, target_id: int) -> int:
        """This function deletes an object by it's id.

        Returns:
            Affected rows provided by the database engine (int)
        """
        self.logger.info("delete_by_id Request")
        result = self.session.query(self.object_type).filter(self.object_type.id == target_id).delete()
        self.session.commit()
        return result


    def insert(self, new: ModelAbstract) -> int:
        """This function inserts an object to the database.

        Returns:
            Inserted object id (int)
        """
        self.logger.info("insert Request")
        self.session.add(new)
        self.session.commit()
        return new.id


    def update(self, values_to_update, requested_object) -> ModelAbstract:
        self.logger.info("update Request")
        for key, value in values_to_update:
            if value is not None:
                setattr(requested_object, key, value)
        setattr(requested_object, "modified_at", datetime.now())
        self.session.commit()
        return requested_object
