#!/usr/bin/env python3

from dataclasses import dataclass
import os
import shutil
import subprocess


@dataclass
class Service:
    filename: str = os.path.expanduser("~/Library/LaunchAgents/com.pro6db.sync.plist")
    path_to_sync_script: str = shutil.which("pro6-dashboard-sync")
    logfile: str = os.path.expanduser("~/.local/share/pro6db/sync.log")
    interval_in_minutes: int = 30
    service_id: str = "com.pro6db.sync"

    @property
    def xml(self):
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>{self.service_id}</string>
    <key>Program</key>
    <string>{self.path_to_sync_script}</string>
    <key>RunAtLoad</key>
    <true/>
    <key>StartInterval</key>
    <integer>{self.interval_in_minutes*60}</integer>
    <key>ExitTimeOut</key>
    <integer>60</integer>
    <key>StandardOutPath</key>
    <string>{self.logfile}</string>
</dict>
</plist>
"""

    def write(self):
        with open(self.filename, "w") as f:
            f.write(self.xml)

    def rm(self):
        os.remove(self.filename)

    def is_enabled(self) -> bool:
        enabled_services = subprocess.run(
            ["launchctl", "list"], stdout=subprocess.PIPE, check=True
        ).stdout.decode("utf8")
        return self.service_id in enabled_services

    def disable(self):
        # if we're not enabled, do nothing
        if not self.is_enabled():
            return

        self.write()
        subprocess.run(["launchctl", "unload", "-F", self.filename], check=True)
        exit(1)
        self.rm()

    def enable(self):
        # if we're enabled, do nothing
        if self.is_enabled():
            return

        # make sure we disable the service first, that will make this idempotent
        self.disable()
        self.write()
        subprocess.run(["launchctl", "load", "-F", self.filename], check=True)


def enable():
    service = Service()
    service.enable()
    print(
        f"pro6 sync service enabled! It will run every {service.interval_in_minutes} minutes."
    )
    print(f"Logfile is: {service.logfile}")


def disable():
    service = Service()
    service.disable()
    print("pro6 sync service disabled!")
