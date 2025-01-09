from uw_mazevo import DAO, get_resource, post_resource
from uw_mazevo.models import Booking, BookingDetail, Building, Room, Status


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


class PublicCourses(object):
    URL = "/api/publiccourses/{}"

    # specific keys needed for term import
    DAYS_OF_WEEK = ["sunday", "monday", "tuesday", "wednesday",
                    "thursday", "friday", "saturday"]

    def import_term(self, courses):
        """
        Import a Term
        """
        url = self.URL.format("importterm")
        body = courses
        body["apiKey"] = DAO.get_service_setting("API_KEY")

        post_resource(url, body)


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

    def get_events_with_booking_details(self, booking_ids):
        """
        Returns all event information and resource details

        """
        url = self.URL.format("GetEventsWithBookingDetails")
        body = {"bookingIds": booking_ids}

        events = []
        for data in post_resource(url, body):
            event = Booking.from_json(data)
            event.booking_details = []
            for detail in data["bookingDetails"]:
                event.booking_details.append(BookingDetail.from_json(detail))
            events.append(event)
        return events

    def get_resource_details(self, **kwargs):
        """
        Get Resource Details with specific booking Ids and resource Ids (Optional).

        """
        url = self.URL.format("getresourcedetails")
        body = kwargs

        details = []
        for data in post_resource(url, body):
            details.append(BookingDetail.from_json(data))
        return details
