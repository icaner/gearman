# -*- coding: utf-8 -*-
import gearman

gm_client = gearman.GearmanClient(['www.aispring.top:4730'])
gm_client.submit_job('Task1', 'client_data', priority=gearman.PRIORITY_HIGH, background=True)
