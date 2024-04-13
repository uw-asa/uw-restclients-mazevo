# Copyright 2024 UW ASA, University of Washington
# SPDX-License-Identifier: Apache-2.0

import json
import logging
from restclients_core.exceptions import DataFailureException
from uw_mazevo.dao import Mazevo_DAO


DAO = Mazevo_DAO()
logger = logging.getLogger(__name__)


def get_resource(url):
    """
    Issue a GET request to Mazevo with the given url
    and return the response.
    """

    response = DAO.getURL(url, {"Accept": "application/json"})
    logger.debug("GET {0} ==status==> {1}".format(url, response.status))

    if response.status != 200:
        raise DataFailureException(url, response.status, response.data)

    logger.debug("GET {0} ==data==> {1}".format(url, response.data))

    return json.loads(response.data)

def post_resource(url, body):
    """
    Issue a POST request to Mazevo with the given url and content
    and return the response.
    """

    response = DAO.postURL(url, {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }, json.dumps(body))
    logger.debug("POST {0} ==status==> {1}".format(url, response.status))

    if response.status != 200:
        raise DataFailureException(url, response.status, response.data)

    logger.debug("POST {0}s ==data==> {1}".format(url, response.data))

    return json.loads(response.data)
