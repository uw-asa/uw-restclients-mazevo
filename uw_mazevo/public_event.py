from uw_mazevo import Mazevo
from uw_mazevo.models import Booking

PUBLICEVENT_API = "/api/PublicEvent/{}"


class PublicEvent(Mazevo):
    def get_events(self, **kwargs):
        """
        Only pass in the "minDateChanged" parameter if you want results
        for bookings that have been created or changed since the
        "minDateChanged" date. Changed bookings are for critical booking
        information only like date, time, status or room.
        """
        url = PUBLICEVENT_API.format('getevents')
        body = kwargs

        events = []
        for data in self._post_resource(url, body):
            events.append(Booking(data))
        return events
