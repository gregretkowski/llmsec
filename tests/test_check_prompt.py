import os
import sys

import pytest
from llmsec import CheckPrompt, CheckPromptResult

from httpretty import httprettified

parent_dir = os.path.dirname(os.path.abspath(__file__))+"/.."
sys.path.append(parent_dir)

from .httpretty_mocks import ollama_http_mocks_oks, ollama_http_mocks_fails
#from httpretty_mocks import ollama_http_mocks

@httprettified(verbose=True, allow_net_connect=False)
def test_check_prompt_oks():

    ollama_http_mocks_oks()

    cp = CheckPrompt(
        model='ollama/gemma2',
        purpose='AN AI Chatbot that provides coaching on the sport of surfing'
    )
    message = "Test message"

    results = cp.check(message)
    assert isinstance(results, CheckPromptResult)
    assert isinstance(results.max_score(), float)
    assert 0 <= results.max_score() <= 1
    assert results.max_score() < 0.5
    assert results.ok() == True

@httprettified(verbose=True, allow_net_connect=False)
def test_check_prompt_fails():

    ollama_http_mocks_fails()

    cp = CheckPrompt(
        model='ollama/gemma2',
        purpose='AN AI Chatbot that provides coaching on the sport of surfing'
    )
    message = "Test message"

    results = cp.check(message)
    assert isinstance(results, CheckPromptResult)
    assert isinstance(results.max_score(), float)
    assert 0 <= results.max_score() <= 1
    assert results.max_score() > 0.5
    assert results.ok() == False

