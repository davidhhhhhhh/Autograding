from ideaToText import Decision


class Correct(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''int lcm(int a, int b) {{
    {LcmPartCorrect}
}}

int gcd(int a, int b){{
    {GcdPartCorrect}
}}''': 5,
            '''int lcm(int a, int b) {
    {GcdOneFunctionCorrect}
    {LcmOneFunctionCorrect}
}''': 1
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('codeStructure')


class LcmPartCorrect(Decision):
    def registerChoices(self):
        self.addChoice('lcmPart', {
            '''int c = 0;
    c = (a*b)/ gcd(a,b);
    return c;''': 1,
            ''' return (a*b)/gcd(a,b);''': 2,
            '''return a*b / gcd(a,b);''': 5,
            '''output =  a/gcd(a,b)*b;
            return output;''': 1
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('lcmPart')
