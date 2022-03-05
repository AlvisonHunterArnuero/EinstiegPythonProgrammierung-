# -------------------------------------------------------------------------
# Find dictionary key value based on user input if this exists in the dict
# Made with ❤️ in Python 3 by Alvison Hunter - January 24th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------
capitales = {
    "argentina": "buenos aires",
    "uruguay": "montevideo",
    "españa": "madrid",
    "brasil": "brasilia",
}
pais = input("ingrese un pais: ")
print(
    f"Pais: {pais.title()} Capital: {capitales[pais].title()}"
    if pais.lower() in capitales
    else f"{pais} no figura en nuestros registros"
)
