from django.db import models

# Create your models here.
class Document(models.Model):
    id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=20)
    filename = models.CharField(max_length=255, null=False, blank=False)
    full_path = models.CharField(max_length=255, null=False, blank=False)
    source = models.CharField(max_length=20, null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        s = "id=%d|created_date=%s|type=%s|filename=%.2f|full_path=%s|source=%s" % (
            self.id,
            self.created_date,
            self.type,
            self.filename,
            self.full_path,
            self.source
        )
        return s

    class Meta:
        db_table = "document"
        constraints = [
            models.UniqueConstraint(fields=['filename','full_path'], 
                                    name='doc_filenamepath_non_identical', include=['id','created_date'])
        ]        
    