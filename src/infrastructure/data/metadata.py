from sqlalchemy import MetaData

class Metadata():

    __metadata_obj = MetaData()

    def get_metadata(self):
        return self.__metadata_obj