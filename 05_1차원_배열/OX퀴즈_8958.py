size_of_scoreboard = int(input())

# score = []

for ii in range(size_of_scoreboard):
    answer_sheet = input()
    number_of_quiz = len(answer_sheet)
    score_stack = 0
    score_unit = 0
    for jj, answer in enumerate(answer_sheet):
        if answer == 'O':
            score_stack = score_stack + 1
        else:
            score_stack = 0
        score_unit = score_unit + score_stack
    print(score_unit)