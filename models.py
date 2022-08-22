from django.db import models


class MyDjangoPermissionGroup(models.Model):
    platformid = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=60, blank=True, null=True)
    desc = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MyDjango_permission_group'


class MyDjangoPermissionGroupsPermissions(models.Model):
    platformid = models.IntegerField(blank=True, null=True)
    permission_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MyDjango_permission_groups_permissions'


class MyDjangoPermissionInfo(models.Model):
    platformid = models.IntegerField(blank=True, null=True)
    permission_name = models.CharField(max_length=60, blank=True, null=True)
    desc = models.CharField(max_length=60, blank=True, null=True)
    method = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MyDjango_permission_info'


class MyDjangoPermissionUser(models.Model):
    platformid = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MyDjango_permission_user'



# 平台权限
platformid = 1

# 自动创建4种权限(增删改查)的权限表
defauts_methods = {
    'get': 'can show',
    'post': 'can add',
    'put': 'can update ',
    'delete': 'can delete',
}

# 额外扩展权限
loginfo2_extra_methods = {'showall': "show all test"}
loginfo2_extra_methods.update(defauts_methods)

# 自定义类权限
permissions = {
    "MyDjango_user.views.LoginInfo2": loginfo2_extra_methods
}

for permission_name, methods in permissions.items():
    for method_name in methods:
        if not method_name:
            continue
        desc = methods[method_name]
        # print('%s-%s-%s'%(permission_name,desc,methodname))
        MyDjangoPermissionInfo.objects.update_or_create(platformid=platformid, permission_name=permission_name, desc=desc,
                                                     method=method_name)
