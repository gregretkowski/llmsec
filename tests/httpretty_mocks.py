import json
import os
import re

import httpretty
from httpretty import httprettified, HTTPretty

# httpretty Docs:
# https://httpretty.readthedocs.io/en/latest/guides.html


def ollama_http_mocks_oks():
    httpretty.enable(allow_net_connect=False, verbose=True)

    httpretty.register_uri(
        HTTPretty.POST,
        "http://localhost:11434/api/generate",
        body=json.dumps({
            "model": "llama3",
            "created_at": "2023-08-04T08:52:19.385406455-07:00",
            "response": "{\"score\": 0.1, \"comment\": \"great\"}",
            "done": True
        }),
        priority=1
    )

def ollama_http_mocks_fails():
    httpretty.enable(allow_net_connect=False, verbose=True)

    httpretty.register_uri(
        HTTPretty.POST,
        "http://localhost:11434/api/generate",
        body=json.dumps({
            "model": "llama3",
            "created_at": "2023-08-04T08:52:19.385406455-07:00",
            "response": "{\"score\": 0.9, \"comment\": \"baddude\"}",
            "done": True
        }),
        priority=1
    )
