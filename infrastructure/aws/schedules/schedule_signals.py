from django.db.models.signals import post_delete
from django.dispatch import receiver

from backend.models import InvoiceOnetimeSchedule
from infrastructure.aws.schedules.delete_schedule import delete_schedule


@receiver(post_delete, sender=InvoiceOnetimeSchedule)
def delete_schedule_on_onetime_delete(sender, instance: InvoiceOnetimeSchedule, **kwargs):
    response = delete_schedule(instance.invoice.id, instance.id)

    if not response["success"]:
        print(f"[AWS] [SCHEDULE] Error deleting schedule: {response['error']}")
