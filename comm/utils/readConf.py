import codecs
import configparser

class ReadConf:

    def __init__(self, cfg_path):
        """
        配置文件初始化
        :param cfg_path:
        """
        fd = open(cfg_path, replace('\\', '/'), encoding='utf-8')
        data = fd.read()
        # 去除配置文件开头编码标识
