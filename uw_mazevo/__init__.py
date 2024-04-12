# Copyright 2024 UW ASA, University of Washington
# SPDX-License-Identifier: Apache-2.0

from uw_mazevo.dao import Mazevo_DAO
from restclients_core.exceptions import DataFailureException


def get_resource(url):
    """
    Issue a GET request to Mazevo with the given url
    and return the response .
    """

    response = Mazevo_DAO().getURL(url, {"Accept": "text/xml"})

    if response.status != 200:
        raise DataFailureException(url, response.status, response.data)

    return response.data
