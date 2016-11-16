from django.utils.translation import ugettext_lazy as _

STATUS_ACCEPTED = 1
STATUS_REJECTED = -1
STATUS_WAITING = 0

JOB_STATUSES = (
    (STATUS_REJECTED, _('Rejected')),
    (STATUS_ACCEPTED, _('Accepted')),
    (STATUS_WAITING, _('Waiting'))
)
