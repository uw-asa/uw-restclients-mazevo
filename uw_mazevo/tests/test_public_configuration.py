# Copyright 2024 UW ASA, University of Washington
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase
from uw_mazevo.public_configuration import PublicConfiguration


class TestPublicConfiguration(TestCase):

    def test_get_statuses(self):
        config = PublicConfiguration()
        statuses = config.get_statuses()
        self.assertEqual(len(statuses), 3)
        self.assertEqual(statuses[0].id, 1)
        self.assertEqual(statuses[2].description, "Request")

    def test_get_rooms(self):
        config = PublicConfiguration()
        rooms = config.get_rooms(1)
        self.assertEqual(len(rooms), 2)
        self.assertEqual(rooms[0].description, "Room 100")
        self.assertEqual(rooms[1].building_description, "Student Center")
