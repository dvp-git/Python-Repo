#####################################
# Data Interchange Formats
#####################################
"""
Serialization: is the process of translating a data structure or object state into a format that can be stored (for example, in a file or memory data buffer) 
or transmitted (for example, over a computer network) and reconstructed later (possibly in a different computer environment).



Common formats: XML, YAML, and JSON . Use JSON preferably.


Deserialization: 



In JSON, a tuple is transformed into a list.

json.dumps(python_object)
json.loads(json_dumps_data)

"""
# import sys, json
# data = {
#     'big_number': 2 ** 314,
#     'max_float': sys.float_info.max,
#     'a_list': [2,3,4,5],
# }

# json_data = json.dumps(data)      # Converts real data to JSON formatted string <class 'str'>
# # print(type(json_data))
# data_out = json.loads(json_data)  # Converts the data from JSON formatted string to real data
# assert data_out == data


""" How to serialize objects which can be interpreted by JSON differently. Example datatime object in python to JSON."""
# import json
# class ComplexEncoder(json.JSONEncoder):

#     """This method is called whenever the encoder encounters an object that it cannot encode 
#      and is expected to return an encodable representation of that object."""
#     def default(self, obj):
#         print("ComplexEncoder.default:{}".format(obj))
#         if isinstance(obj, complex):
#             return {
#                 '_meta':"_complex",
#                 'num': [obj.real, obj.imag],
#             }
#         # Let the base class default method raise the TypeError
#         return super().default(self, obj)

# data = {
#     'an_int': 42,
#     'a_float': 3.14159265,
#     'a_complex': 3 + 4j,
#     'a_complex2': 2+ 1j,
# }
# json_data = json.dumps(data,cls=ComplexEncoder)
# print(json_data)

# # Decoding / Deserializing 
# def object_hook(obj):
#     print("object_hook : {}".format(obj))
#     try:
#         if obj['_meta'] == '_complex':
#             return complex(*obj['num'])
#     except KeyError:
#         return obj
    
# data_out = json.loads(json_data, object_hook=object_hook)
# print(data_out)

### Ex : 2 , Datatime

import json
from datetime import datetime, timedelta, timezone
now = datetime.now()    # datetime.datetime(2022, 12, 28, 15, 15, 48, 775889)

# With timezone 1 hour difference
now_tz  = datetime.now(tz=timezone(timedelta(hours=1))) # datetime.timedelta(seconds=3600)

# Custom class for serialization of datetime.
class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            try:
                off = obj.utcoffset().seconds   # 3600 # datetime.timedelta(seconds=3600
            except AttributeError:
                off = None
            return {
                '_meta': '_datetime',
                'data': obj.timetuple()[:6] + (obj.microsecond, ),  # time.struct_time(tm_year=2022, tm_mon=12, tm_mday=28, tm_hour=21, tm_min=16, tm_sec=6, tm_wday=2, tm_yday=362, tm_isdst=-1)
                'utcoffset': off,
            }
        return super().default(obj)
data = {
    'an_int': 42,
    'a_float': 3.14159265,
    'a_datetime': now,
    'a_datetime_tz': now_tz,
}
json_data = json.dumps(data, cls=DatetimeEncoder)
print(json_data)

def object_hook(obj):
    try:
        if obj['_meta'] == '_datetime':
            if obj['utcoffset'] is None:
                tz = None
            else:
                tz = timezone(timedelta(seconds=obj['utcoffset']))
            return datetime(*obj['data'], tzinfo=tz)
    except KeyError:
        return obj
data_out = json.loads(json_data, object_hook=object_hook)
print(data_out)