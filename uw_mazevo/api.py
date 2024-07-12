from uw_mazevo import get_resource, post_resource
from uw_mazevo.models import Booking, Building, Room, Status


class PublicConfiguration(object):
    URL = "/api/PublicConfiguration/{}"

    def get_buildings(self):
        """
        Gets a list of Rooms. building_id of 0 returns all rooms.
        """
        url = self.URL.format("Buildings")

        buildings = []
        for data in get_resource(url):
            buildings.append(Building.from_json(data))
        return buildings

    def get_rooms(self, building_id=0):
        """
        Gets a list of Rooms. building_id of 0 returns all rooms.
        """
        url = self.URL.format("Rooms")
        body = {"buildingId": building_id}

        rooms = []
        for data in post_resource(url, body):
            rooms.append(Room.from_json(data))
        return rooms

    def get_statuses(self):
        """
        Gets a list of Statuses
        """
        url = self.URL.format("Statuses")

        statuses = []
        for data in get_resource(url):
            statuses.append(Status.from_json(data))

        return statuses


class PublicEvent(object):
    URL = "/api/PublicEvent/{}"

    def get_events(self, **kwargs):
        """
        Only pass in the "minDateChanged" parameter if you want results
        for bookings that have been created or changed since the
        "minDateChanged" date. Changed bookings are for critical booking
        information only like date, time, status or room.
        """
        url = self.URL.format("getevents")
        body = kwargs

        events = []
        for data in post_resource(url, body):
            events.append(Booking.from_json(data))
        return events
