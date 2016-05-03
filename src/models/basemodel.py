import json


class Model:
    """Base class for models"""

    def as_json(self):
        return json.dumps(self.__dict__)

