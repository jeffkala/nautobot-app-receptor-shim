"""Jobs."""
from nautobot.extras.jobs import Job
from receptorctl import ReceptorControl
from nautobot.core.celery import register_jobs

import time

class WorkListJob(Job):
    """Job that monitors the list of jobs."""

    class Meta:
        """Meta object boilerplate for receptorctl."""

        name = "Perform ReceptorCtl Work List"
        description = "Run ReceptorCtl Work List"
        has_sensitive_variables = False

    def run(self, *args, **data):  # pylint: disable=unused-argument
        """Run receptorctl command."""
        self.logger.warning("Run ReceptorCtl Work List.")
        r = ReceptorControl("tcp://10.1.1.10:1234")
        self.logger.info(r.simple_command("work list"))
        result = r.submit_work(worktype='gather-hostname', node="controller01", payload="")
        self.logger.info(r.simple_command("work list"))
        unit_id = result['unitid']
        resultfile = r.get_work_results(unit_id)
        time.sleep(15)
        stdout = resultfile.read()
        stdout = str(stdout, encoding='utf-8')
        self.logger.info(stdout)
        r.simple_command(f"work release {unit_id}")
        self.logger.info(r.simple_command("work list"))
        self.logger.info(r.simple_command("work list"))
        result = r.submit_work(worktype='hello-world', node="executor01", payload="")
        self.logger.info(r.simple_command("work list"))
        unit_id = result['unitid']
        resultfile = r.get_work_results(unit_id)
        time.sleep(15)
        stdout = resultfile.read()
        stdout = str(stdout, encoding='utf-8')
        self.logger.info(stdout)
        r.simple_command(f"work release {unit_id}")
        r.close()
        self.logger.info("done")
        # TODO: review awx receptor flow https://github.com/ansible/awx/blob/a176c04c14d166307256263507cc7b2310482477/awx/main/tasks/receptor.py#L160


register_jobs(WorkListJob)
