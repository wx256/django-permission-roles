# django
from django.db.models import Q

# rest_framework
from rest_framework import exceptions
from rest_framework.permissions import BasePermission
from .exceptions import *
from MyDjango_permission.models import *



class BaseUserPermission(BasePermission):
    def has_permission(self, request, view):
        # cname = self.__class__.__name__
        platformid = self.platformid  # 用户平台ID
        module = view.__module__  # 模块名role1.views
        vname = view.get_view_name()  # 视图名R1
        vname = str(vname).replace(' ', '')  # 替换掉空格Login Info2
        permission_name = "%s.%s" % (module, vname)  # 组合权限名称role1.views.r1
        method = request.method  # 请求类型
        userid = request.user  # 用户ID
        result_detail = "%s:%s" % (permission_name, method)  # 异常返回明确权限异常路径
        # print('%s-%s-%s'%(permission_name,method,userid))

        # 1,查询用户被分配的的权限角色组
        obj_permission_user = MyDjangoPermissionUser.objects.filter(Q(platformid=platformid) & Q(user_id=userid))
        if not obj_permission_user.exists():
            raise exceptions.PermissionDenied(ExceptionsCode("无访问权限", result_detail))
        user_group_ids = obj_permission_user.values_list('id')

        # 2,查询用户被分配的的权限角色组是否存在
        obj_permission_group = MyDjangoPermissionGroup.objects.filter(Q(platformid=platformid) & Q(id__in=user_group_ids))
        if not obj_permission_group.exists():
            raise exceptions.PermissionDenied(ExceptionsCode("无访问权限", result_detail))

        # 3,查询当前接口访问的权限是否存在
        obj_permission = MyDjangoPermissionInfo.objects.filter(
            Q(platformid=platformid) & Q(permission_name=permission_name) & Q(method=method))
        if not obj_permission.exists():
            raise exceptions.PermissionDenied(ExceptionsCode("无访问权限", result_detail))
        user_permission_id = obj_permission.get().id

        # 4,查询当前用户权限组&接口权限是否存在
        obj_permission_groups_permissions = MyDjangoPermissionGroupsPermissions.objects.filter(
            Q(platformid=platformid) & Q(permission_id=user_permission_id) & Q(
                group_id__in=user_group_ids))
        if not obj_permission_groups_permissions.exists():
            raise exceptions.PermissionDenied(ExceptionsCode("无访问权限", result_detail))
        return True


    def has_object_permission(self, request, permission_name, method):
        userid = request.user
        result_detail="%s:%s"%(permission_name,method)

        # 1,查询用户被分配的的权限角色组
        obj_permission_user = MyDjangoPermissionUser.objects.filter(Q(platformid=platformid) & Q(user_id=userid))
        if not obj_permission_user.exists():
            raise exceptions.PermissionDenied(ExceptionsCode("无访问权限", result_detail))
        user_group_ids = obj_permission_user.values_list('id')

        # 2,查询用户被分配的的权限角色组是否存在
        obj_permission_group = MyDjangoPermissionGroup.objects.filter(Q(platformid=platformid) & Q(id__in=user_group_ids))
        if not obj_permission_group.exists():
            raise exceptions.PermissionDenied(ExceptionsCode("无访问权限", result_detail))

        # 3,查询当前接口访问的权限是否存在
        obj_permission = MyDjangoPermissionInfo.objects.filter(
            Q(platformid=platformid) & Q(permission_name=permission_name) & Q(method=method))
        if not obj_permission.exists():
            raise exceptions.PermissionDenied(ExceptionsCode("无访问权限", result_detail))
        user_permission_id = obj_permission.get().id

        # 4,查询当前用户权限组&接口权限是否存在
        obj_permission_groups_permissions = MyDjangoPermissionGroupsPermissions.objects.filter(
            Q(platformid=platformid) & Q(permission_id=user_permission_id) & Q(
                group_id__in=user_group_ids))
        if not obj_permission_groups_permissions.exists():
            raise exceptions.PermissionDenied(ExceptionsCode("无访问权限", result_detail))
        return True


# 平台1权限类
class UserPermission(BaseUserPermission):
    def __init__(self):
        self.platformid = 1
