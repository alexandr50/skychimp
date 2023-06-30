import datetime
from dateutil.tz import tz
from django.utils import timezone

from django.core.mail import send_mail

from customer.models import Customer
from sending.models import Sending, TrySending
from skychimp import settings


def sending_mail(id):
    obj_sending = Sending.objects.get(pk=id)
    query_clients = Customer.objects.all()
    list_emails_customers = [x.email for x in query_clients]
    timezone = tz.gettz(settings.TIME_ZONE)
    actual_date = datetime.datetime.now(timezone)

    new_attempt = TrySending.objects.create(sending=obj_sending, last_attempt=actual_date)
    # for item in query_sending:
    #     if (item.start_sending <= timezone.now() and item.end_sending >= timezone.now())\
    #             and (item.status_sending == Sending.ACTIVATED or item.start_sending == Sending.CREATED):
    #         pass