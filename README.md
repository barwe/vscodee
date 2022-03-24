# 基本功能

目前支持的系统（`sys.platform` 取值）:

- `"win32"`
- `"linux"`

## create

在 `settings.VSCODE_ENV_DIR` 目录下创建一个隔离环境。

位置参数：
- `ENV_NAME` 要创建的隔离环境名称

可选参数：
- `-i XX YY ...` 根据 `settings.RECOMMENDED_EXTENSIONS` 中预设的 key 安装扩展，其中 `base` 是默认必装扩展

## list

查看所有隔离环境。

可选参数：
- `-e ENV_NAME` 查看某个环境的信息

## remove

移除指定的隔离环境，未实现，懒得写了。

## ext

 查看所有预设的扩展集。

# 依赖

windows 11 下的依赖：
- pywin32
- winshell