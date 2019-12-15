import os
import sys

sep_char = "/"  # 根据系统类型来确定路径分隔符， 类unix系统中通用为斜杠


def current_process_path():
    return os.path.dirname(sys.argv[0])
