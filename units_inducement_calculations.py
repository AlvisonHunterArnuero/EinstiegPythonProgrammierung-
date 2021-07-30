# -------------------------------------------------------------------------
# Basic operations with colletion types | Python exercises | Beginner level
# Get weekly production units per day & calculate if employee gets bonus
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - April 16th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------

units_lst = []
week_days = ["Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday"]
while True:
    try:
        [units_lst.append(
            int(input(f"Enter Employee Units for {d}: "))) for i, d in enumerate(week_days)]

        total = sum(units_lst)
        got_bonus = "YES" if total > 99 else "NO"
        print(f"Weekly Units: {total} | Inducement: {got_bonus}")
        break

    except ValueError:
        print("Units should be numbers! Please try again.")
        pass
