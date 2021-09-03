# -*- coding: utf-8 -*-
from datetime import datetime
from logging import getLogger, config, StreamHandler, DEBUG
import os

import sys
sys.path.append('./')
from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

if __name__ == '__main__':
  now = datetime.now()
  date_s = (now.strftime('%Y-%m-%d %H:%M:%S.%f'))

  logger.info(now)
  logger.info(date_s)
  logger.info(type(now))

  # unixtimeに変換する。float()が戻ってくる。
  logger.info(now.timestamp())

  # unixtime（マイクロ秒） -> date変換する
  # 1625900408684995
  # 秒とミリ秒の間に「.」を入れる必要がある。
  logger.info(datetime.fromtimestamp(float('1625900408.684995')))

  # マイクロ秒 -> ミリ秒変換する
  # 後でやる
  
  
  # 2021-07-08T23:40:59.962933+00:00
  # 後でやる