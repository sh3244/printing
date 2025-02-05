# serve 3 octoprint instances on 5001, 5002, 5003
# make them persistent in the background daemons and save to separate folders
# create folders first if necessary
# run with python3 octoprints.py

import os
import subprocess

NUMBER_OF_INSTANCES = 3

# create folders if necessary
for i in range(NUMBER_OF_INSTANCES):
    folder = f"octoprint{i}"
    if not os.path.exists(folder):
        os.makedirs(folder)

threads = []
# start octoprint instances
for i in range(3):
    folder = f"octoprint{i}"
    port = 5001 + i
    thread = subprocess.Popen(f"octoprint serve --port {port} --basedir {folder}", shell=True)
    print(f"Started octoprint on port {port} with basedir {folder}")
    threads.append(thread)

# wait for the threads to finish
for thread in threads:
    thread.wait()

# FBg3-ofgBTEdwd60oxUb7ashlfIJnspfXLYsJQoIGYU
# BRpMMF7UUHZnMWBSvVsQbaf4Q78ODlnerljwDZiyOtU