import json
from StudentSimulator import ideaToText


GRAMMAR_PATH = 'grammars/Pyramid_Challenge_KS'

if __name__ == '__main__':
    sampler = ideaToText.Sampler(GRAMMAR_PATH)

    data = []

    for i in range(50):
        sample = sampler.singleSample()
        text = sample['text']
        choices = sample['choices']
        rubric = sample['rubric']
        print(text)
        print(choices)

        data.append({'text': text, 'choices': choices})

    with open('ImageGenerator/imagesByKs/pyramid_ks_50.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)