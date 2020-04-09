#!/usr/bin/env python3

import shutil
import psutil
du=shutil.disk_usage("/")
print(du)
print("{:.3f}% is free".format(du.free/du.total*100))
psutil.cpu_percent(0.1)
