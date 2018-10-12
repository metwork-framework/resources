#!/usr/bin/env python3

import argparse
import asyncio
from aiohttp import ClientSession, BasicAuth, ClientTimeout
import os
import aiohttp_github_helpers as h

GITHUB_USER = os.environ['GITHUB_USER']
GITHUB_PASS = os.environ['GITHUB_PASS']
TIMEOUT = ClientTimeout(total=20)
AUTH = BasicAuth(GITHUB_USER, GITHUB_PASS)
ORG = "metwork-framework"
TOPICS_TO_EXCLUDE = ["testrepo"]


async def getrepos(minimal_level):
    repos = []
    async with ClientSession(auth=AUTH, timeout=TIMEOUT) as session:
        for i in range(minimal_level, 6):
            topics_to_include = ["integration-level-%i" % i]
            tmp = await h.github_get_org_repos_by_topic(session,
                                                        ORG,
                                                        topics_to_include,
                                                        TOPICS_TO_EXCLUDE)
            repos = repos + tmp
    return repos

parser = argparse.ArgumentParser(description='list metwork-framework repos '
                                             'with a minimal integration level')
parser.add_argument('--minimal-level', type=int, default=1,
                    help='minimal integration level')
args = parser.parse_args()
loop = asyncio.get_event_loop()
reply = loop.run_until_complete(getrepos(args.minimal_level))
loop.close()
for repo in reply:
    print(repo)
