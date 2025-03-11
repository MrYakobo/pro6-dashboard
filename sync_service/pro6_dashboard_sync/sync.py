#!/usr/bin/env python3

import argparse
from glob import glob
import os
from pathlib import Path
import shutil
import tempfile
from pro6_dashboard_sync.convert import generate_jsonfiles
import toml
from dataclasses import dataclass
import boto3

script_path = os.path.dirname(os.path.realpath(__file__))


class Config:
    @staticmethod
    def init(toml_filename: str):
        os.makedirs(os.path.dirname(toml_filename), exist_ok=True)
        shutil.copy(f"{script_path}/example.config.toml", toml_filename)
        print(
            f"INFO: inited empty config in {toml_filename}. Edit it and rerun this command."
        )


@dataclass
class S3Config(Config):
    aws_access_key_id: str
    aws_secret_access_key: str
    endpoint_url: str
    bucket: str

    @staticmethod
    def from_toml(toml_filename: str):
        with open(toml_filename, "r") as f:
            config = S3Config(**toml.load(f)["s3"])

        print(f"INFO: loaded config from {toml_filename}")
        return config

    def upload_file(self, file_path):
        s3 = boto3.client(
            "s3",
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            endpoint_url=self.endpoint_url,
        )
        target_path = f"data/{Path(file_path).name}"

        s3.upload_file(file_path, self.bucket, target_path)
        print(f"Uploaded to {self.bucket}/{target_path}!")


@dataclass
class PropresenterConfig(Config):
    pro6pl: str
    songs_directory: str

    @staticmethod
    def from_toml(toml_filename: str):
        with open(toml_filename, "r") as f:
            values = {
                k: os.path.expanduser(v)
                for k, v in toml.load(f)["propresenter"].items()
            }
            config = PropresenterConfig(**values)

        print(f"INFO: loaded propresenter config from {toml_filename}")
        return config

    def create_jsonfiles(self, outdir):
        generate_jsonfiles(self.pro6pl, self.songs_directory, outdir)


def sync(toml_filename: str):
    if not os.path.exists(toml_filename):
        Config.init(toml_filename)
        return

    s3_config = S3Config.from_toml(toml_filename)
    propresenter = PropresenterConfig.from_toml(toml_filename)

    # create json files and upload them
    with tempfile.TemporaryDirectory() as tmpdir:
        propresenter.create_jsonfiles(tmpdir)
        for filename in glob(f"{tmpdir}/*"):
            s3_config.upload_file(filename)


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--config", default=os.path.expanduser("~/.config/pro6db-dashboard/config.toml")
    )
    args = parser.parse_args()
    sync(args.config)


if __name__ == "__main__":
    main()
