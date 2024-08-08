#!/usr/bin/env python3
# -*- python -*-

''' This is the CLI For LLMSec. It invokes the CheckPrompt class'''
import argparse
import logging
import sys

# pylint: disable=import-error
from dotenv import load_dotenv

from llmsec import CheckPrompt

DESCRIPTION = '''
This tool checks if the user provided prompt is malicious. Provide
the 'purpose' of your LLM system, and provide the user 'prompt'.
'''

parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument('purpose', type=str, help='The purpose of your LLM system')
parser.add_argument('prompt', type=str, help='The user provided prompt')
parser.add_argument('--model', default='ollama/gemma2', type=str,
                    help='model name in litellm format, ex ollama/mistral')
parser.add_argument('--debug', action='store_true', help='debug mode')
args = parser.parse_args()

load_dotenv()

logging.basicConfig(
    stream=sys.stderr,
    #level=logging.INFO,
    format='%(asctime)s/%(levelname)s/%(filename)s:%(lineno)d: %(message)s'
)
if args.debug:
    logging.getLogger('llmsec').setLevel(logging.DEBUG)

cp = CheckPrompt(model=args.model, purpose=args.purpose)
result = cp.check(args.prompt)

if result.ok():
    print('No malicious behavior detected')
    sys.exit(0)
else:
    print(result.fail_reasons())
    sys.exit(1)
