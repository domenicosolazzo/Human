#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.json import JSONEncoder
import calendar
from datetime import datetime
from ...core.api.models.person import Person
import json

class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, datetime):
                if obj.utcoffset() is not None:
                    obj = obj - obj.utcoffset()
                millis = int(
                    calendar.timegm(obj.timetuple()) * 1000 +
                    obj.microsecond / 1000
                )
                return millis
            if isinstance(obj, Person):
                person_obj = obj.to_json()

                return person_obj
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)
