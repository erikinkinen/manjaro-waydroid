#!/usr/bin/env python3
# Copyright 2021 Philip Müller
# SPDX-License-Identifier: GPL-3.0-or-later
# PYTHON_ARGCOMPLETE_OK
import subprocess
import os

print("Initialzing WayDroid")
init_waydroid = subprocess.run(["waydroid", "init", "-f"])
print("The exit code was: %d" % init_waydroid.returncode)

print("Enabling Systemd Service")
enable_container = subprocess.run(["systemctl", "enable", "waydroid-container", "--now"])
print("The exit code was: %d" % enable_container.returncode)

directory = '/home/'

print("Update Desktop database")
for user in os.listdir(directory):
    update_desktop = subprocess.run(["update-desktop-database", "/home/%s/.local/share/applications" % user, "--quiet"])
    print("The exit code was: %d" % update_desktop.returncode)
