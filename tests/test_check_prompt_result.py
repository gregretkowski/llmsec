''' Test the CheckPromptResult class '''
from llmsec import CheckPromptResult

def test_check_prompt_result_ok():
    ''' Test cases where prompt was benign '''

    llm_result = {

        'harmful': {
            'score': 0.1,
            'comment': 'seems fine'
        },
        'subversive': {
            'score': 0.1,
            'comment': 'seems fine'
        },
        'prompt_leak': {
            'score': 0.1,
            'comment': 'seems fine'
        },
        'jailbreaking': {
            'score': 0.1,
            'comment': 'seems fine'
        }
    }
    cpr = CheckPromptResult(
        threshold=0.6,
        llm_result=llm_result
    )
    assert cpr
    assert cpr.ok()
    assert cpr.max_score() == 0.1
    assert cpr.fail_reasons() == ''

def test_check_prompt_result_fail():
    ''' Test cases where prompt was malicious '''

    llm_result = {

        'harmful': {
            'score': 0.8,
            'comment': 'harmful prompt'
        },
        'subversive': {
            'score': 0.1,
            'comment': 'seems fine'
        },
        'prompt_leak': {
            'score': 0.1,
            'comment': 'seems fine'
        },
        'jailbreaking': {
            'score': 0.9,
            'comment': 'jailbreaking prompt'
        }
    }
    cpr = CheckPromptResult(
        threshold=0.6,
        llm_result=llm_result
    )
    assert cpr
    assert cpr.ok() is False
    assert cpr.max_score() == 0.9
    expected_fail_reasons = '''*harmful* 0.8: harmful prompt
*jailbreaking* 0.9: jailbreaking prompt'''
    assert cpr.fail_reasons() == expected_fail_reasons
