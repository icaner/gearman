# -*- coding: utf-8 -*-

import gearman

ad_client = gearman.GearmanAdminClient(['www.aispring.top:4730'])

lists = ad_client.get_workers()

for row in lists:
        print row

print "\n"

lists = ad_client.get_status()

for row in lists:
        print row
