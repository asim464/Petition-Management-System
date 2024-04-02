import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'pms.settings')

import django

django.setup()

from django.db.models import Count

from api.models import Petition


def maintain_marking():
    petitions = Petition.objects.annotate(currently_marked_count=Count('currently_marked')).filter(
        currently_marked_count__gt=0).all()
    for petition in petitions:
        currently_marked_list = petition.currently_marked.all()
        for user in currently_marked_list:
            for hist in petition.history.filter(marked_to=user).all():
                hist.is_retain = True
                hist.save()


if __name__ == '__main__':
    print("Starting PMS maintain marking script...")
    maintain_marking()
