required_skill = ['python', 'github', 'linux']

candidates = {
          "anna": {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
          "bob": {'github', 'linux', 'python'},
          "carol": {'linux', 'javascript', 'html', 'python', 'github'},
          "daniel": {'pascal', 'java', 'c++', 'github'},
          "ekani": {'html', 'css', 'github', 'python', 'linux'},
          "fenna": {'linux', 'pascal', 'java', 'c', 'lisp', 'modula-2', 'perl', 'github'}
}

interviewees = set()

for candidate, skills in candidates.items():
    #if skills.issuperset(required_skill):
    if skills > set(required_skill):
        interviewees.add(candidate)

print(interviewees)

frozen = set([frozenset(['a', 'b', 'c']), frozenset(['d', 'e', 'f'])])
