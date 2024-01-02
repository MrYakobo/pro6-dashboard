#!/usr/bin/env python3

from dataclasses import dataclass
import os
import shutil
import subprocess


@dataclass
class Service:
    filename: str
    xml: str

    def write_to_file(self):
        with open(self.filename, "w") as f:
            f.write(self.xml)

    def enable(self):
        subprocess.run(["launchctl", "unload", self.filename], check=True)
        subprocess.run(["launchctl", "load", "-w", self.filename], check=True)


def main():
    logfile = os.path.expanduser("~/.local/share/pro6db/sync.log")
    interval_in_minutes = 30
    interval_in_seconds = interval_in_minutes * 60

    path_to_sync_script = shutil.which("pro6-dashboard-sync")
    service = Service(
        filename=os.path.expanduser("~/Library/LaunchAgents/com.pro6db.sync.plist"),
        xml=f"""
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.pro6db.sync</string>
    <key>Program</key>
    <string>{path_to_sync_script}</string>
    <key>RunAtLoad</key>
    <true/>
    <key>StartInterval</key>
    <integer>{interval_in_seconds}</integer>
    <key>ExitTimeOut</key>
    <integer>60</integer>
    <key>StandardOutPath</key>
    <string>{logfile}</string>
</dict>
</plist>
""",
    )
    service.write_to_file()
    service.enable()
    print(
        f"pro6 sync service enabled! It will run every {interval_in_minutes} minutes.\nLogfile is: {logfile}"
    )


if __name__ == "__main__":
    main()
