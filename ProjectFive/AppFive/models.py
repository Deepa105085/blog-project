from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)


    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username



# @admin.register(UserProfileInfo)
# class UserProfileInfoAdmin(admin.ModelAdmin, ExportCsvMixin):
#
#     readonly_fields = [..., "profile_pic"]
#
#     def profile_pic(self, obj):
#         return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
#             url = obj.profile_pic.url,
#             width=obj.profile_pic.width,
#             height=obj.profile_pic.height,
#             )
#     )

# useless
