''' Contains the CheckPromptResult class '''
class CheckPromptResult:
    ''' This class represents the result of a CheckPrompt. It can
    be used to check the results for pass/fail, get comments etc'''

    def __init__(self, threshold,llm_result):

        self.threshold = threshold
        self.llm_result = llm_result

        for k,v in llm_result.items():
            setattr(self, k, v)
            setattr(self, k+'_score',v['score'])
            setattr(self, k+'_comment',v['comment'])
            setattr(self, k+'_pass',v['score'] < threshold)


    def __repr__(self):
        return f'{{"ok": {self.ok()}, "max_score": {self.max_score()},'+\
             f' "results": {self.llm_result}}}'

    def ok(self):
        ''' returns True if the check passed '''
        return self.max_score() < self.threshold

    def fail_reasons(self):
        ''' returns a human-readable string detailing why the check failed '''
        return '\n'.join([f"*{k}* {v['score']}: {v['comment']}"
                          for k,v in self.llm_result.items()
                          if v['score'] >= self.threshold])

    def max_score(self):
        ''' returns the maximum score from all the results '''
        return max(list(v['score'] for k,v in self.llm_result.items()))

    def __str__(self):
        return self.__repr__()
