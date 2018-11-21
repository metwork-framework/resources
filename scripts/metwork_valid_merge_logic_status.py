#!/usr/bin/env python3

import argparse
import asyncio
from aiohttp import ClientSession, BasicAuth, ClientTimeout
import os
import sys
import logging
import aiohttp_github_helpers as h

GITHUB_USER = os.environ['GITHUB_USER']
GITHUB_PASS = os.environ['GITHUB_PASS']
TIMEOUT = ClientTimeout(total=20)
AUTH = BasicAuth(GITHUB_USER, GITHUB_PASS)
ORG = "metwork-framework"


async def valid_status(owner, repo, sha):
    async with ClientSession(auth=AUTH, timeout=TIMEOUT) as session:
        r = await h.github_create_status(session, owner, repo, sha, "success",
                                         "http://metwork-framework.org:9000/"
                                         "github_webhook_ready_to_merge",
                                         "pr ready to merge logic",
                                         "pr ready to merge")
        if not(r):
            logging.critical("Impossible to create status for %s/%s@%s" %
                             (owner, repo, sha))
            sys.exit(1)
        print("status for %s/%s@%s: ok" % (owner, repo, sha))

parser = argparse.ArgumentParser(description='valid merge logic status')
parser.add_argument('REPO', type=str, help='repo name (without owner)')
parser.add_argument('SHA', type=str, help='sha to valid')

args = parser.parse_args()
loop = asyncio.get_event_loop()

loop.run_until_complete(valid_status(ORG, args.REPO, args.SHA))
loop.close()
