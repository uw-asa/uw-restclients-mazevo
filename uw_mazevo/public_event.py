from uw_mazevo import post_resource
from uw_mazevo.models import Booking

PUBLICEVENT_API = "/api/PublicEvent/{}"


class PublicEvent(object):
    def get_events(self, **kwargs):
        """
        Only pass in the "minDateChanged" parameter if you want results
        for bookings that have been created or changed since the
        "minDateChanged" date. Changed bookings are for critical booking
        information only like date, time, status or room.
        """
        url = PUBLICEVENT_API.format("getevents")
        body = kwargs

        events = []
        for data in post_resource(url, body):
            events.append(Booking.from_json(data))
        return events
