# import os
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from utils.image_path import upload_avatar_for_user
#
#
# class CustomUser(AbstractUser):
#     display_name = models.CharField(
#         max_length=50,
#         verbose_name="Отображая имя",
#     )
#     is_buyer = models.BooleanField(
#         default=False,
#         verbose_name="Покупатель",
#     )
#     avatar = models.ImageField(
#         upload_to=upload_avatar_for_user,
#         verbose_name="Аватар",
#     )
#
#     def delete(self, using=None, keep_parents=False):
#         os.remove(self.avatar.path)
#         super().delete(using, keep_parents=False)
#
#     def __str__(self):
#         return self.use