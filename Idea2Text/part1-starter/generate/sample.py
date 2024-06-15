import ideaToText
from codeDotOrg import autoIndent

GRAMMAR_PATH = 'grammars/codeorg4'

def main():
	sampler = ideaToText.Sampler(GRAMMAR_PATH)

	for i in range(10):
		sample = sampler.singleSample()
		text = sample['text']
		rubric = sample['rubric']
		text = autoIndent(text)
		print(text)
		print(rubric)
		print('----')


if __name__ == '__main__':
	main()