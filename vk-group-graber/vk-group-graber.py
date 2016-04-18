#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def getById(gid, fields=None, access_token=None):
    """
    Get info about group by gid or it's name. You can extract
    group name from it's link.
    """
    extended_fields = fields or {}
    extended_fields.update({"group_id": gid})
    return vkapirequest("groups.getById",
                        fields=extended_fields,
                        access_token=access_token)


def getMembers(gid, fields=None, access_token=None):
    """
    Here gid must be group id (number). That my opinion.
    You can get it with getById function.
    """
    extended_fields = fields or {}
    extended_fields.update({"group_id": gid})
    return vkapirequest("groups.getMembers",
                        fields=extended_fields,
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
