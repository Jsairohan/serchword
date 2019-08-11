# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
# exlen = 25
        # data = words.objects.filter(
        #     Column_2__icontains=word
        # )
        #
        # st_data = data.filter(
        #     Column_2__istartswith = word
        # )
        # et_data = st_data.filter(
        #     Column_2__iexact=word
        # )
        # print et_data
        # exlen = exlen-(et_data.count())
        # print exlen
        # l.extend(list(et_data.values_list('Column_2',"Column_3")[:exlen]))
        # l.extend(list(st_data.values_list('Column_2',"Column_3")[:exlen]))
        # exlen = exlen - (st_data.count())
        # if exlen >=1:
        #     l.extend(list(data.values_list('Column_2',"Column_3")[:exlen]))
        #     exlen = exlen -(data.count())