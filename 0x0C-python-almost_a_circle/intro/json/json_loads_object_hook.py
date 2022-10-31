#!/usr/bin/python3
""" a simple demo of object_hook & cls parameters of json module's
loads & load functions
"""
import json
from json import JSONEncoder, JSONDecoder


def as_complex(dct):
    """ demo custom decoding, returning an object (type) of
    choice/desire. By default, JSON will return a dict (python object)
    NOTE:
        object_hook: a parameter of the load(and loads) json function
        a functionality similar to default in json dump(and dumps) - a
        function for custom deserialization (& the latter, serialization)
    """
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct #otherwise (or else)

# define the Encoder and Decorder classes

class ExtendedEncoder(JSONEncoder):
    def default(self, obj):
        name = type(obj).__name__
        try:
            encoder = getattr(self, f"encode_{name}")
        except AttributeError:
            super().default(obj)
        else:
            encoded = encoder(obj)
            encoded["__extended_json_type__"] = name
            return encoded

class ExtendedDecoder(JSONDecoder):
    def __init__(self, **kwargs):
        kwargs["object_hook"] = self.object_hook
        super().__init__(**kwargs)
    def object_hook(self, obj):
        try:
            name = obj["__extended_json_type__"]
            decoder = getattr(self, f"decode_{name}")
        except (KeyError, AttributeError):
            return obj
        else:
            return decoder(obj)
            

class MyEncoder(ExtendedEncoder):
    def encode_complex(self, c):
        """ mini-encodes a complex number i.e. returns
        a (JSON) serializable object, a dict - JSON does the rest """
        return {"real": c.real, "imag": c.imag}
    
    def encode_range(self, r):
        """ mini-encodes a range """
        return {"start": r.start, "stop": r.stop, "step": r.step}

class MyDecoder(ExtendedDecoder):
    def decode_complex(self, obj):
        """ returns a complex object from a json object """
        return complex(obj["real"], obj["imag"])

    def decode_range(self, obj):
        return range(obj["start"], obj["stop"], obj["step"])
# test the function
if __name__ == "__main__":
    # test the encode_complex function...
    res = json.loads('{"__complex__": true, "real": 1, "imag": 2}',
                        object_hook = as_complex)
    print(res)
    print(type(res))
    
    # test the encoder & decoder classes
    my_data = {
            "hey": complex(1, 2),
            "there": range(1, 10, 3),
            73: False,
            }
    json_data = json.dumps(my_data, cls=MyEncoder)
    print("json_data:", json_data)
    decoded = json.loads(json_data, cls=MyDecoder)
    print("decoded:", decoded)

