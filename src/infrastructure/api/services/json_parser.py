import dataclasses
import json

def validation_to_json(success, message):
    result = {"success": success,
              "message": message}
    return result


def dataclass_to_json(input_object):
    if type(input_object) is list:
        dict_result = [dataclasses.asdict(input_dataclass) for input_dataclass in input_object]
    else:
        dict_result = dataclasses.asdict(input_object)
    dumped_result = json.dumps(dict_result, sort_keys=True, indent=4, default=str)
    loaded_result = json.loads(dumped_result)
    return loaded_result