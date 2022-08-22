from rest_framework import exceptions

EXCEPTIONS_CODE = {
    # wliot_system
    "用户登录已失效": 10000,
    "用户登录已超时": 10001,
    "登录信息不完整": 10002,
    "请求数据不合法": 10002,

    # wliot_permission
    "无访问权限": 11000,
    "权限表异常": 11001,

    # wliot_user
    "图片验证码错误": 12001,
    "用户名密码错误": 12002,

    # wliot_dealer
    "经销商名已存在": 13000,

    # wliot_hardware
    "物联网卡已存在": 14000,
}


def ExceptionsCode(msg, detail=None):
    if not detail:
        detail = msg
    exception = {"code": EXCEPTIONS_CODE[msg], "msg": msg, "detail": detail}
    return exception
