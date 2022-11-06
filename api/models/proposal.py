from django.db import models
from django.utils import timezone
from typing import Any

class Proposal(models.Model):
    web3_id = models.IntegerField(null=True)
    title = models.TextField(null=True) 
    transaction = models.TextField(null=True) 
    description = models.TextField(null=True) 
    proposer_eoa = models.CharField(max_length=42, null=True) # 作成者 の wallet account address．
    quorum = models.IntegerField(null=True) # 定足数．必要ないかも．
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    datas = models.TextField(null=True)
    
    # 以下、後で消す
    for_count = models.IntegerField(null=True)
    against_count = models.IntegerField(null=True)
    end_date = models.DateField(null=True)  
    status = models.CharField(max_length=64, null=True)

    class Meta:
        db_table = "proposal"
    
    def save(self, force_insert: bool = False, force_update: bool = False, *args: Any, **kwargs: Any) -> None:
        super().save(force_insert, force_update, *args, **kwargs)
        if self.web3_id is None:
            self.web3_id = Proposal.objects.count()
            self.save()