# -*- coding: utf-8 -*-

import gearman

gm_worker = gearman.GearmanWorker(['www.aispring.top:4730'])


def task_listener_reverse(gearman_worker, gearman_job):
    # gearman_job 就是client端传过来的数据

    print "这里是想要干的事"

    return gearman_job.data[::-1]  # 返回数据的逆序

# GRARMAN_TASK_NAME  这个名字需要是任务的唯一标识
gm_worker.register_task('Task1', task_listener_reverse)
gm_worker.work()
