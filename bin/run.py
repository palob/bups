#!/usr/bin/env python2

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/..')

from app import app

exit_status = app.run(sys.argv)
sys.exit(exit_status)
