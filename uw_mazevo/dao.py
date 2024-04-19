# Copyright 2024 UW ASA, University of Washington
# SPDX-License-Identifier: Apache-2.0

import os
from os.path import abspath, dirname
from restclients_core.dao import DAO


class Mazevo_DAO(DAO):
    def service_name(self):
        return "mazevo"

    def service_mock_paths(self):
        return [abspath(os.path.join(dirname(__file__), "resources"))]

    def _custom_headers(self, method, url, headers, body):
        api_key = self.get_service_setting("API_KEY")
        if api_key is not None:
            return {"X-API-Key": api_key}
