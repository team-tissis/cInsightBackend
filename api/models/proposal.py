from django.db import models
from django.utils import timezone

class Proposal(models.Model):
    title = models.TextField(null=True) 
    transaction = models.TextField(null=True) 
    description = models.TextField(null=True) 
    proposer_eoa = models.CharField(max_length=42, null=True) # 作成者 の wallet account address．
    quorum = models.IntegerField(null=True) # 定足数．必要ないかも．
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    # 以下、後で消す
    for_count = models.IntegerField(null=True)
    against_count = models.IntegerField(null=True)
    end_date = models.DateField(null=True)  
    status = models.CharField(max_length=64, null=True)

    class Meta:
        db_table = "proposal"
    