from django.db import models

# Create your models here.


class Interaction(models.Model):
    input_value = models.CharField(max_length=100)
    output = models.TextField()
    script = models.TextField()
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.input

    def get_output(self, binds):
        return self.output.format(**binds)

    def execute(self, parm):
        exec(self.script, globals())
        dic = script(**{"PARM": parm})
        return dic
