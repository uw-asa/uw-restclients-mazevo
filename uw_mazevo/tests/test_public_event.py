# Copyright 2024 UW ASA, University of Washington
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase
from uw_mazevo.public_event import PublicEvent


class TestPublicEvent(TestCase):

    def test_get_events(self):
        event = PublicEvent()
        events = event.get_events(
            start="2023-10-20T00:00:00-06:00",
            end="2023-10-27T00:00:00-06:00",
            buildingIds=[3],
        )
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0].id, 10213)
        self.assertEqual(events[1].building_description, "Student Center")
