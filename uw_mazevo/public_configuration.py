from uw_mazevo import Mazevo
from uw_mazevo.models import Room, Status

PUBLICCONFIGURATION_API = "/api/PublicConfiguration/{}"


class PublicConfiguration(Mazevo):
    def get_rooms(self, building_id=0):
        """
        Gets a list of Rooms. building_id of 0 returns all rooms.
        """
        url = PUBLICCONFIGURATION_API.format('Rooms')
        body = {"buildingId": building_id}

        rooms = []
        for data in self._post_resource(url, body):
            rooms.append(Room(data))
        return rooms

    def get_statuses(self):
        """
        Gets a list of Statuses
        """
        url = PUBLICCONFIGURATION_API.format('Statuses')

        statuses = []
        for data in self._get_resource(url):
            statuses.append(Status(data))
