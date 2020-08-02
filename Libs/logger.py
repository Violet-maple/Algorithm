#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import logging
from logging import handlers


def load_log_config(filename):
    logging.basicConfig(
        level=logging.DEBUG,
        filename='../Log/Info_%s.log' % filename,
        filemode='a',
        format='%(asctime)s -[%(levelname)s] - %(funcName)s[line:%(lineno)d]: %(message)s'
    )


class Logger(object):
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }
    
    def __init__(self, filename, console_level=None, level=None, when='D', path_name=False, back_count=3,
                 f_fmt='[%(asctime)s]-%(levelname)s [%(funcName)s line:%(lineno)d]: %(message)s',
                 c_fmt='[%(asctime)s]-%(levelname)s %(funcName)s: %(message)s'):
        filename = '../Log/Info_%s.log' % filename
        self.logger = logging.getLogger(filename)
        if path_name:
            f_fmt = '%(asctime)s - %(pathname)s[%(funcName)s line:%(lineno)d] - %(levelname)s: %(message)s'
        f_formatter = logging.Formatter(f_fmt, "%Y-%m-%d %H:%M:%S")  # 设置日志格式
        c_formatter = logging.Formatter(c_fmt, '%Y-%m-%d %H:%M:%S')
        # self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        # 设置屏幕上显示的格式
        console_level = self.level_relations.get(console_level) or self.level_relations['info']
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setLevel(console_level)
        sh.setFormatter(c_formatter)
        # 往文件里写入#指定间隔时间自动生成文件的处理器
        th = handlers.TimedRotatingFileHandler(
            filename=filename,
            when=when,
            backupCount=back_count,
            encoding='utf-8'
        )
        level = self.level_relations.get(level) or self.level_relations['debug']
        th.setLevel(level)
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(f_formatter)  # 设置文件里写入的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(th)
    
    def debug(self, msg):
        self.debug(msg)
    
    def info(self, msg):
        self.logger.info(msg)
    
    def warn(self, msg):
        self.logger.warning(msg)
    
    def error(self, msg):
        self.logger.error(msg)
    
    def critical(self, msg):
        self.critical(msg)


if __name__ == '__main__':
    log = Logger('all.log')
    log.logger.debug('debug')
    log.logger.info('info')
    # log.logger.warning('警告')
    # log.logger.error('报错')
    # log.logger.critical('严重')
    # Logger('error.log', level='error').logger.error('error')
