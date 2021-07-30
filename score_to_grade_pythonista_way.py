
from typing import Dict


def score_to_grade(inputs: str, ordered_passing_grades: Dict[str, float]):
    try:
        score = float(inputs)
    except Exception as e:
        raise e
    else:
        if score // 1:
            raise Exception("Score Out of Range")
    for(key, value) in ordered_passing_grades.items():
        if score >= value:
            return key
    else:
        return "F"


if __name__ == "__main__":
    str_score = input("Please Enter your Score: ")
    grades_dict = {"A": .9, "B": .8, "C": .7, "D": .6, "E": .5}
    result = score_to_grade(str_score, grades_dict)
    print(f"You Grade is: {result}")
