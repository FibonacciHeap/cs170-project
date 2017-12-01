kill -9 `ps -ef | grep solver.py | grep -v grep | awk '{print $2}'`
