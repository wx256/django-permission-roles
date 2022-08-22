def has_object_permission(view, request,method):
    module = view.__module__
    cname = view.__class__.__name__
    title = "%s.%s" % (module, cname)
    is_permission = UserPermission().has_object_permission(request, title,method)
    return is_permission



class LoginInfo(APIView):
	#增删改查基础权限
    permission_classes = [UserPermission]

    def __init__(self):
        self.platformid = 1

    def get(self, request, *args, **kwargs):
    	#功能级权限验证
        has_object_permission(self, request,'showall')

        return Response({"code": 0, "msg": "success"})