from ideaToText import Decision


class Incorrect(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''int lcm(int a, int b) {{
    {LcmPartIncorrect}
}}

int gcd(int a, int b){{
    {GcdPartIncorrect}
}}''': 5,
            '''int lcm(int a, int b) {{
    {OneFunctionIncorrect}
}}''': 1
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('codeStructure')


class LcmPartIncorrect(Decision):
    def registerChoices(self):
        self.addChoice('lcmPart', {
            '''int c = 0;
    c = (a*b) % gcd(a,b);
    return c;''': 1,
            ''' return (a*b)*gcd(a,b);''': 2,
            '''return a*b - gcd(a,b);''': 5,
            '''output =  a/(gcd(a,b)*b);
            return output;''': 1
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('lcmPart')


class GcdPartIncorrect(Decision):
    def registerChoices(self):
        self.addChoice('gcdPart', {
            '''
    int r = a % b;

    if (r == 0) {{
        return b;
    }} else {{
        return gcd(r, b);
    }}''': 5,
            '''if (a < b) {{
        int tmp = a;
        a = b;
        b = tmp;
    }}
    int r = a % b;
    if (r == 0) return r;
    else return gcd(r, b);''': 1,
            '''int tmp;
        //Swap the numbers so a >= b
        if(a < b)
        {{
                tmp = a;
                a = b;
                b = tmp;
        }}
        //Find the gcd
        while(b != 0)
        {{
                tmp = a % b;
                a = b;
                b = tmp;
        }}
        return b;''': 1
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('gcdPart')


class OneFunctionIncorrect(Decision):
    def registerChoices(self):
        self.addChoice('OneFunction', {
            '''int a1 = a;
            int b1 = b;
            if (a < b) {{
            a1 = b; 
            b1 = a;}}
            int r = a1 % b1;
            while (r != 0) {{
            a1 = b1; 
            b1 = r;
            r = a1 % b1;}}
            int x=a*b1/b;
            return x;''': 1,
            '''int a1=a;
    int b1=b;
    int r=1;
    while(r > 0){{
        if(a < b){{
        int tmp = a;
        a = b;
        b = tmp;
    }}
        r = a % b;
        if(r != 0){{
        a = b;
        b = r;
        }}
    }}
    int x=a*b/b1;
    return x;''': 1,
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('OneFunction')