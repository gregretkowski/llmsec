''' Test the CheckPrompt class '''

from httpretty import httprettified

from llmsec import CheckPrompt, CheckPromptResult

from .httpretty_mocks import ollama_http_mocks_oks, ollama_http_mocks_fails

@httprettified(verbose=True, allow_net_connect=False)
def test_check_prompt_oks():
    ''' Test cases where prompt was benign '''

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
    assert results.ok() is True

@httprettified(verbose=True, allow_net_connect=False)
def test_check_prompt_fails():
    ''' Test cases where prompt was malicious '''

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
    assert results.ok() is False

def test_check_prompt_set_threshold():
    ''' Test the set_threshold method '''

    ollama_http_mocks_fails()

    cp = CheckPrompt(
        model='ollama/gemma2',
        purpose='AN AI Chatbot that provides coaching on the sport of surfing'
    )
    cp.set_threshold(0.99)
    message = "Test message"

    results = cp.check(message)
    assert results.ok() is True
