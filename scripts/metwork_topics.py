#!/usr/bin/env python3

import argparse
import asyncio
import json
from aiohttp import ClientSession, BasicAuth, ClientTimeout
import os
import aiohttp_github_helpers as h

GITHUB_USER = os.environ.get('GITHUB_USER', None)
GITHUB_PASS = os.environ.get('GITHUB_PASS', None)
TIMEOUT = ClientTimeout(total=20)
AUTH = None
if GITHUB_USER is not None and GITHUB_PASS is not None:
    AUTH = BasicAuth(GITHUB_USER, GITHUB_PASS)
ORG = "metwork-framework"
TOPICS_TO_EXCLUDE = ["testrepo"]


async def get_repo_topics(owner, name):
    topics = []
    async with ClientSession(auth=AUTH, timeout=TIMEOUT) as session:
        topics = await h.github_get_repo_topics(session, owner, name)
    return topics

parser = argparse.ArgumentParser(description='get repo topics')
parser.add_argument('owner', type=str, help='repo owner')
parser.add_argument('name', type=str, help='repo name')
parser.add_argument('--json', action='store_true',
                    help='if set, format the output as a json list')
args = parser.parse_args()
loop = asyncio.get_event_loop()
reply = loop.run_until_complete(get_repo_topics(args.owner, args.name))
loop.close()
if args.json:
    print(json.dumps(reply))
else:
    for topic in reply:
        print(topic)
