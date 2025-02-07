import csv
from StudentSimulator import ideaToText

GRAMMAR_PATH = 'grammars/powerGrading_full'

if __name__ == '__main__':
    sampler = ideaToText.Sampler(GRAMMAR_PATH)

    with open('power_grading_1000.csv', 'w', newline='') as csvfile:
        fieldnames = ['text', 'choices']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1000):
            sample = sampler.singleSample()
            text = sample['text']
            choices = sample['choices']
            rubric = sample['rubric']
            print(text)
            print(choices)

            writer.writerow({'text': text, 'choices': choices})