#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class Groups(object):
    def __init__(self, group_id):
        self.__gid = group_id

    def getById(self, fields=None, access_token=None):
        return vkapirequest("groups.getById",
                            fields=fields,
                            access_token=access_token)

    def getMembers(self, fields=None, access_token=None):
        return vkapirequest("groups.getMembers",
                            fields=fields,
                            access_token=access_token)


# ---- Utils -----
def vkapirequest(method, parameters=None, access_token=None):
    def getParamsOrNothing(params):
        if params is None:
            return ""
        else:
            return "?{}".format('&'.join(["{}={}".format(k, v)
                                          for k, v in params.items()]))

    def getATorNothing(at):
        if at is None:
            return ""
        else:
            return "&access_token={}".format(at)

    base_url = "https://api.vk.com/method/"
    url = "{}{}{}{}".format(base_url, method, getParamsOrNothing(parameters),
                            getATorNothing(access_token))
    return requests.get(url).json()
