from django.db import models
from django.utils import timezone

class Proposal(models.Model):
    title = models.TextField() 
    transaction = models.TextField() 
    description = models.TextField() 
    proposer_eoa = models.CharField(max_length=42) # 作成者 の wallet account address．
    quorum = models.IntegerField() # 定足数．必要ないかも．
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "proposal"