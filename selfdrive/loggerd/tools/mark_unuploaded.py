#!/usr/bin/env python3
import sys
from openpilot.common.xattr import removexattr
from openpilot.selfdrive.loggerd.uploader import UPLOAD_ATTR_NAME

for fn in sys.argv[1:]:
  print(f"unmarking {fn}")
  removexattr(fn, UPLOAD_ATTR_NAME)
