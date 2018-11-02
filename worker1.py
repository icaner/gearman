import gearman
import time

class CustomGearmanWorker(gearman.GearmanWorker):
    def on_job_execute(self, current_job):
        print "Job started"
        return super(CustomGearmanWorker, self).on_job_execute(current_job)


def task_callback(gearman_worker, job):
    print job.data
    time.sleep(3)
    return job.data


new_worker = CustomGearmanWorker(['www.aispring.top:4730'])
new_worker.register_task("echo", task_callback)
new_worker.work()
