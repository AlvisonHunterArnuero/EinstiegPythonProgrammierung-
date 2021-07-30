agile_team = ['Front-End Lead', 'Backend Lead', 'Product Owner', 'UX/UI Lead']
responses = ['Who the hell knows?', 'I have no clue',
             'Mmm...Not me', 'What do you think?']
interjections = ["What the Hell!", "Oh Well, Well...", "For Heeavens Sake!",
                 "Bloody Norah!"]
question = "Who uploaded these changes?"


def ask(agile_team, question):
    l = 0
    print("-" * 80)
    while True:
        try:
            for elem in range(len(agile_team)):
                if agile_team[elem] == "UX/UI Lead":
                    break
                else:
                    print(
                        f"- {interjections[elem]} {agile_team[elem+1]}, {question}")
                    print(f"well....{responses[elem]}, {agile_team[l]}!!!")
                    print(f"Let me ask the {agile_team[l+2]} about it.")
                    print("-" * 80)
                    l += 1
        except IndexError as e:
            print(f"- Would you like me to ask  the {agile_team[0]} again?")
            print("-" * 80)
            break


ask(agile_team, question)
