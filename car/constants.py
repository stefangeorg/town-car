from django.utils.translation import ugettext_lazy as _

STATUS_TAXI_AVAILABLE = 1
STATUS_TAXI_UNAVAILABLE = 0
STATUS_TAXI_AVAILABLE_MANUAL = 2

STATUSES = (
    (STATUS_TAXI_UNAVAILABLE, _('Available')),
    (STATUS_TAXI_AVAILABLE, _('Accept all rides automcatically')),
    (STATUS_TAXI_AVAILABLE_MANUAL, _('Accept Rides Manually')),
)

DAYS = ((x, x) for x in range(7))
