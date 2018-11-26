#!/usr/bin/env python3

import argparse
import asyncio
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


async def getrepos(minimal_level, exact_level):
    repos = []
    async with ClientSession(auth=AUTH, timeout=TIMEOUT) as session:
        if exact_level:
            max_level = minimal_level + 1
        else:
            max_level = 6
        for i in range(minimal_level, max_level):
            topics_to_include = ["integration-level-%i" % i]
            tmp = await h.github_get_org_repos_by_topic(session,
                                                        ORG,
                                                        topics_to_include,
                                                        TOPICS_TO_EXCLUDE)
            repos = repos + tmp
    return repos

parser = argparse.ArgumentParser(description='get metwork-framework repos')
parser.add_argument('--minimal-level', type=int, default=1,
                    help='minimal integration level')
parser.add_argument('--exact-level', action='store_true',
                    help='if set the minimal-level must be the exact level')
args = parser.parse_args()
loop = asyncio.get_event_loop()
reply = loop.run_until_complete(getrepos(args.minimal_level, args.exact_level))
loop.close()
for repo in reply:
    print(repo)
