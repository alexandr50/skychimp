from datetime import datetime, date, time, timedelta
from dateutil.tz import tz
from django.core.validators import EmailValidator
from django.utils import timezone

from django.core.mail import send_mail

from customer.models import Customer
from sending.models import Sending, TrySending
from sending.utils import install_nex_date
from skychimp import settings
from django.utils import timezone

from user.models import User


def sending_mail():
    query_sending = Sending.objects.exclude(status_sending='завершена') \
        .filter(start_sending_date=date.today()) \
        .filter(start_sending_time__lte=time(*list(map(int, datetime.now().time().strftime("%H:%M:%S").split(':')))))
    # .filter(next_run=timezone.now())

    for sending in query_sending:
        email_list = [x.email for x in sending.customer.all()]
        sending.status_sending = Sending.ACTIVATED
        sending.save()
        query_try_sending = TrySending.objects.filter(sending=sending)
        try:
            # validation_email_list = list(map(lambda x: EmailValidator(x), email_list))
            result = send_mail(
                subject=sending.message.theme,
                message=sending.message.content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=email_list,
                fail_silently=False
            )
            if result:
                TrySending.objects.create(sending=sending,
                                          last_attempt=datetime.now(),
                                          status_attempt='success',
                                          answer_server='ok')
                sending.start_sending_date = install_nex_date(sending)
                sending.status_sending = Sending.COMPLITED
                sending.save()
        except Exception as error:
            TrySending.objects.create(sending=sending,
                                      last_attempt=datetime.now(),
                                      status_attempt='failure',
                                      answer_server=error)

    # obj_sending = Sending.objects.get(pk=id)
    # query_clients = Customer.objects.all()
    # list_emails_customers = [x.email for x in query_clients]
    # timezone = tz.gettz(settings.TIME_ZONE)
    # actual_date = datetime.datetime.now(timezone)

    # for item in query_sending:
    #     if (item.start_sending <= timezone.now() and item.end_sending >= timezone.now())\
    #             and (item.status_sending == Sending.ACTIVATED or item.start_sending == Sending.CREATED):
    #         pass
