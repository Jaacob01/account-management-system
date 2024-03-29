import platform

_DEBUG = False
# _STATIC_URL = '/static/'
WINDOWS = 'Windows'
LINUX = 'Linux'
MacOS = 'Darwin'
CURRENT_SYSTEM = platform.system()

if CURRENT_SYSTEM == WINDOWS:
    _DEBUG = True
    import pymysql

    pymysql.version_info = (1, 4, 13, "final", 0)
    pymysql.install_as_MySQLdb()  # 使用pymysql代替mysqldb连接数据库

elif CURRENT_SYSTEM == MacOS:
    _DEBUG = True
    import pymysql

    pymysql.version_info = (1, 4, 13, "final", 0)
    pymysql.install_as_MySQLdb()  # 使用pymysql代替mysqldb连接数据库
else:
    """
        服务器环境 
    """
    import pymysql

    pymysql.version_info = (1, 4, 13, "final", 0)
    pymysql.install_as_MySQLdb()  # 使用pymysql代替mysqldb连接数据库
print(f"this app is running on {CURRENT_SYSTEM},DEBUG:{_DEBUG}")
