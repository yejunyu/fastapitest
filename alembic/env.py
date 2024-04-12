# 导入所需的模块
from logging.config import fileConfig  # 用于配置日志的模块
from sqlalchemy import engine_from_config  # 从配置文件创建数据库引擎的工具
from sqlalchemy import pool  # 数据库连接池的相关工具
from alembic import context  # Alembic的运行上下文
from app.database.database import DATABASE_URL  # 从应用的database模块导入数据库的URL
from app.database.base import (
    Base,
)  # 从应用的base模块导入SQLAlchemy的Base，它包含数据库模型的元数据

# 获取Alembic的配置对象，这个对象中包含了.ini配置文件中的配置信息
config = context.config

# 如果配置文件名存在，则使用fileConfig函数读取配置文件，以设置日志系统
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 将你的数据库模型的元数据对象赋值给target_metadata变量，以便在自动生成迁移脚本时使用
target_metadata = Base.metadata


# run_migrations_offline函数定义了一个在"离线"模式下运行迁移的方法
def run_migrations_offline() -> None:
    # 离线模式意味着不直接与数据库建立连接，而是生成可以手工执行的SQL脚本
    url = config.get_main_option("sqlalchemy.url")  # 从配置中获取数据库的URL
    # 使用上下文对象配置离线运行的具体细节，包括数据库URL、目标元数据等
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    # 开启一个事务块，运行迁移脚本
    with context.begin_transaction():
        context.run_migrations()


# run_migrations_online函数定义了一个在"在线"模式下运行迁移的方法
def run_migrations_online() -> None:
    # 在线模式下，Alembic会创建一个数据库引擎，并与数据库建立连接进行迁移
    configuration = config.get_section(
        config.config_ini_section
    )  # 获取.ini文件中的配置节
    configuration["sqlalchemy.url"] = DATABASE_URL  # 将数据库URL设置到配置中
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    # 使用获取的连接来配置上下文，然后运行迁移脚本
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


# 检查是处于在线还是离线模式，然后调用相应的函数执行迁移
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
