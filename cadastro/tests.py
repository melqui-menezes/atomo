from django.test import TestCase
from datetime import date, timedelta


# 3 de abril de 2019
d = date(2019, 4, 3)
# somar 1 dia = 4 de abril de 2019
d = d + timedelta(days=365)

print(d)