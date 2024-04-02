import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'pms.settings')

import django

django.setup()

from django.db.models import Count

from api.models import Petition


def self_marking():
    petitions = Petition.objects.annotate(history_count=Count('history')).filter(
        history_count__gt=0).all()
    for petition in petitions:
        history_list = petition.history.order_by('-marked_at').all()
        for hist in history_list:
            if hist.marked_from == hist.marked_to and 'Sponsor Organization Changed' not in hist.comment \
                    and hist.is_seen:
                hist.is_seen = False
                hist.is_retain = True
                hist.save()


if __name__ == '__main__':
    print("Starting PMS self marking script...")
    self_marking()
