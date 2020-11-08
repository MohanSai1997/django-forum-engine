from django.db import models


class Thread(models.Model):
    thread_title = models.TextField(max_length=300)
    thread_content = models.TextField(max_length=40000)
    user = models.ForeignKey("account.Account", on_delete=models.CASCADE)


class Comments(models.Model):
    user = models.ForeignKey("account.Account", on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=4000)
