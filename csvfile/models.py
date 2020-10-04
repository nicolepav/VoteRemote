from django.db import models

# Create your models here.
class StateInformation(models.Model):
    
    name = models.CharField(max_length=50)
    ip_reg_deadline = models.DateField(default=None, blank=True, null=True)
    mail_reg_deadline = models.DateField(default=None, blank=True, null=True)
    reg_post_or_rec = models.CharField(max_length = 20)
    online_reg_deadline = models.DateField(default=None, blank=True, null=True)
    is_mail_limits = models.CharField(max_length=4)
    is_covid_changes = models.CharField(max_length=4)
    covid_change = models.CharField(max_length=300)
    ip_req_deadline = models.DateField(default=None, blank=True, null=True)
    online_req_dealine = models.DateField(default=None, blank=True, null=True)
    mail_request_deadline = models.DateField(default=None, blank=True, null=True)
    req_post_or_rec = models.CharField(max_length=20)
    reg_url = models.URLField()
    reg_status_url = models.URLField()
    reg_update_url = models.URLField()
    is_doc_req = models.CharField(max_length=4)
    req_doc = models.CharField(max_length = 250)
    req_url = models.URLField()
    ip_return_deadline = models.DateField(default=None, blank=True, null=True)
    mail_return_deadline = models.DateField(default=None, blank=True, null=True)
    return_post_or_rec = models.CharField(max_length = 20)
    notary_or_witness = models.CharField(max_length = 300)
    signiture_req = models.CharField(max_length = 50)

    def __str__(self):
        return self.name