def get_student_scorecards():
    john = 100
    clark = 200
    brad = 50

    finalPoints = [200, 255, 100]

    # Desestructuramos y asignamos a john  y clark
    # mientas brad conservara su  valor inicial de 50
    [john,clark, *_] = finalPoints

    # Result: John: 200, Clark: 255, Brad: 50
    print(f"John: {john}, Clark: {clark}, Brad: {brad}")

get_student_scorecards()
