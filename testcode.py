'''
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from Pizzas.models import Pizza

pizzas = Pizza.objects.all()

print(pizza)

for p in
'''