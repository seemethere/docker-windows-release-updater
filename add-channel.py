#!/usr/bin/env python

import argparse
import json

import requests

DEFAULT_ROUTE = (
    "/components/engine/windows-server/index.json"
)

DEFAULT_NOTES = "Docker for Windows Server 2016"

def grab_file(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception(f"Unable to get {url}")
    return resp

def main(args):
    try:
        index_resp = grab_file(f"{args.base_url}{DEFAULT_ROUTE}")
        index = json.loads(index_resp.content)
    except Exception:
        index = {
            "versions": {},
            "channels": {}
        }
    key = "alias" if args.is_alias else "version"
    index["channels"][args.channel_name] = {
        key: args.version_name
    }
    print(json.dumps(index, indent=4, sort_keys=True))

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Add a channel to download.docker.com for windows"
    )
    parser.add_argument(
        "base_url",
        type=str,
        help="URL to point to for the index"
    )
    parser.add_argument(
        "channel_name",
        type=str,
        help="Channel to create"
    )
    parser.add_argument(
        "version_name",
        type=str,
        help="version to put into channel"
    )
    parser.add_argument(
        "is_alias",
        type=bool,
        help="Is version an alias to another channel?"
    )
    return parser.parse_args()

if __name__ == "__main__":
    main(parse_arguments())
