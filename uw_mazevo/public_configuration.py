from uw_mazevo import get_resource, post_resource
from uw_mazevo.models import Room, Status

PUBLICCONFIGURATION_API = "/api/PublicConfiguration/{}"


class PublicConfiguration(object):
    def get_rooms(self, building_id=0):
        """
        Gets a list of Rooms. building_id of 0 returns all rooms.
        """
        url = PUBLICCONFIGURATION_API.format("Rooms")
        body = {"buildingId": building_id}

        rooms = []
        for data in post_resource(url, body):
            rooms.append(Room.from_json(data))
        return rooms

    def get_statuses(self):
        """
        Gets a list of Statuses
        """
        url = PUBLICCONFIGURATION_API.format("Statuses")

        statuses = []
        for data in get_resource(url):
            statuses.append(Status.from_json(data))

        return statuses
