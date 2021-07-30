# Author: Made with ♥ in Python 3 by Alvison Hunter - May 26th, 2021
# Description: Basic Math Operations using python eval function
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj

def fn_udf(n1, n2, op):
    try:
        expr = str(n1)+ op + str(n2)
        print(f"Result: {expr} is {eval(expr):,}.")
    except SyntaxError:
        print(f"Error: Invalid Operator! [{op}]. Please correct it & try again.")

fn_udf(7, 14, "+")
fn_udf(23, 12, "**")
fn_udf(4358, 1324, "/")
fn_udf(45, 34, "+*")
