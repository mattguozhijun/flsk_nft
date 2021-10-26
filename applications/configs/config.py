import logging
import os


class BaseConfig:


    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    # mysql 配置
    MYSQL_USERNAME = os.getenv('MYSQL_USERNAME') or "root"
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD') or "123456"
    MYSQL_HOST = os.getenv('MYSQL_HOST') or "127.0.0.1"
    MYSQL_PORT = int(os.getenv('MYSQL_PORT') or 3306)
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE') or "PearAdminFlask"



    # mysql 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"


class TestingConfig(BaseConfig):
    """ 测试配置 """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # 内存数据库


class DevelopmentConfig(BaseConfig):
    """ 开发配置 """
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False


class ProductionConfig(BaseConfig):
    """生成环境配置"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_RECYCLE = 8

    LOG_LEVEL = logging.ERROR


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
