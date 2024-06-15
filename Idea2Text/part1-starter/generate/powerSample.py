import ideaToText

GRAMMAR_PATH = 'grammars/powerGrading_full'

if __name__ == '__main__':
    sampler = ideaToText.Sampler(GRAMMAR_PATH)
    for i in range(100):
        sample = sampler.singleSample()
        text = sample['text']
        choices = sample['choices']
        rubric = sample['rubric']
        print(text)
        print(choices)
