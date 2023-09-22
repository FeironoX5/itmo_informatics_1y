import main

a = input('Название папки (должна содержать tests.txt, answers.txt): ')
tests = open(a + '/' + 'tests.txt', 'r')
answers = open(a + '/' + 'answers.txt', 'w')
i = 1

for t in tests:
    a, b, c = t.replace(',', '.').split()
    answers.write(f'Test {i}: {main.convert(a, int(b), int(c))}\n')
    i += 1

tests.close()
answers.close()
