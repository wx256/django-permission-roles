# django-permission-roles
django permission roles very good
Django自己实现的权限组，支持多平台，支持Token认证，支持细化功能权限验证

1，新建个app,mydjango_permission,模型参考[models.py]

2,把permission.py和exceptions.py放到[settings]同级目录

3,参考views即可  





【原理】

4张表

[mydjango_permission_group权限角色组]

[mydjango_permission_user用户分配的权限组]

[mydjango_permission_groups_permissions用户组拥有的权限]

[mydjango_permission_info权限名称]


1,项目首次启动,models加载后,自动向数据库插入权限信息,默认基础4个权限get/post/put/delete
可自定义类的接口权限和扩展权限


2,views中通过permission_classes = [UserPermission]使用权限组
其实和token认证一样的用法
如果要细化认证,使用has_object_permission(self, request,'showall')即可,参考views


3,permission原理[核心]
当用户访问接口时,自动获取接口路径,如MyDjango.views.UserinfoList和请求方法
直接到数据库中匹配,原理其实很简单,主要写了权限数据库自动初始化的函数方法,更加的自动化


【优点】

token认证和permission权限分离

你可以使用自己的用户表a_user,b_user都可以,不需要再依赖原生的django_user,因为他的表你要附加用户属性很麻烦


支持细化功能权限,直接到models里提前定义即可,项目首次运行会自动把权限表写到数据库


支持多平台,以Platformid标识,方便做多端权限管理,代码阅读和体验良好


因为使用原生认证或是使用guardian模块,受限太大功能复杂所以才自己开发了权限认证模块
经测试使用体验完美

