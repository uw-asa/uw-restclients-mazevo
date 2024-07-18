from datetime import datetime

from restclients_core import models


class Status(models.Model):
    STATUS_TYPE_DOES_NOT_BLOCK_SPACE = 0
    STATUS_TYPE_BLOCKS_SPACE = 1
    STATUS_TYPE_CHOICES = (
        (STATUS_TYPE_DOES_NOT_BLOCK_SPACE, "Does Not Block Space"),
        (STATUS_TYPE_BLOCKS_SPACE, "Blocks Space"),
    )

    description = models.CharField(max_length=30)
    id = models.PositiveIntegerField(primary_key=True)
    status_type = models.SmallIntegerField(choices=STATUS_TYPE_CHOICES)
    display_on_web = models.BooleanField(default=None)

    def __str__(self):
        return self.description

    @staticmethod
    def from_json(data):
        status = Status()
        status.id = data["statusId"]
        status.status_type = data["statusType"]
        status.description = data["description"]
        return status


class EventType(models.Model):
    description = models.CharField(max_length=30)
    id = models.PositiveIntegerField(primary_key=True)
    display_on_web = models.BooleanField(default=None)

    def __str__(self):
        return self.description


class Building(models.Model):
    description = models.CharField(max_length=50)
    building_code = models.CharField(max_length=20, null=True)
    id = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return self.description

    @staticmethod
    def from_json(data):
        building = Building()
        building.id = data["buildingId"]
        building.description = data["description"]
        building.time_zone = data["timeZone"]
        return building


class Room(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    description = models.CharField(max_length=50)
    room_type_id = models.PositiveIntegerField()
    room_type = models.CharField(max_length=50)
    building = models.ForeignKey(Building)
    building_description = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=50)
    security_level = models.PositiveIntegerField()
    min_capacity = models.PositiveIntegerField()
    max_capacity = models.PositiveIntegerField()
    has_bookings = models.BooleanField()

    def __str__(self):
        return self.description

    @staticmethod
    def from_json(data):
        room = Room()
        room.id = data["roomId"]
        room.description = data["description"]
        room.room_type_id = data["roomTypeId"]
        room.room_type = ["roomType"]
        room.building_id = data["buildingId"]
        room.building_description = data["buildingDescription"]
        room.time_zone = data["timeZone"]
        room.security_level = data["securityLevel"]
        room.min_capacity = data["minCapacity"]
        room.max_capacity = data["maxCapacity"]
        room.has_bookings = data["hasBookings"]
        return room


class Booking(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    room_description = models.CharField(max_length=75)
    organization_name = models.CharField(max_length=50)
    event_name = models.CharField(max_length=255)
    event_number = models.PositiveIntegerField()
    event_type = models.CharField(max_length=30)
    building = models.ForeignKey(Building)
    setup_minutes = models.PositiveIntegerField()
    date_time_start = models.DateTimeField()
    date_time_end = models.DateTimeField()
    teardown_minutes = models.PositiveIntegerField()
    customer_access_minutes = models.PositiveIntegerField()
    building_description = models.CharField(max_length=50)
    room = models.ForeignKey(Room)
    status = models.ForeignKey(Status)
    date_changed = models.DateTimeField()

    @staticmethod
    def from_json(data):
        booking = Booking()
        booking.id = data["bookingId"]
        booking.room_description = data["roomDescription"]
        booking.organization_name = data["organizationName"]
        booking.event_name = data["eventName"]
        booking.event_number = data["eventNumber"]
        booking.event_type = data["eventType"]
        booking.building = data["buildingId"]
        booking.setup_minutes = data["setupMinutes"]
        booking.date_time_start = datetime.fromisoformat(data["dateTimeStart"])
        booking.date_time_end = datetime.fromisoformat(data["dateTimeEnd"])
        booking.teardown_minutes = data["teardownMinutes"]
        booking.customer_access_minutes = data["customerAccessMinutes"]
        booking.building_description = data["buildingDescription"]
        booking.room_id = data["roomId"]
        booking.status_id = data["statusId"]
        booking.date_changed = datetime.fromisoformat(data["dateChanged"])
        return booking


class ServiceOrderDetail(models.Model):
    booking_date = models.DateField()
    service_order_start_time = models.TimeField(null=True)
    service_order_end_time = models.TimeField(null=True)
    resource_description = models.CharField(max_length=50)
    resource_external_reference = models.CharField(max_length=255, blank=True)
    service_order_id = models.PositiveIntegerField()
    booking = models.ForeignKey(Booking)
