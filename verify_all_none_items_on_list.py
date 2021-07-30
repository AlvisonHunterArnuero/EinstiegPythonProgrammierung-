# First Example
msg01 = "No item on this list is False|None."
msg02 = "Several items on this list are False|None."
print("="*55)
A = False
B = None
C = 89
D = "Nicaragua is beautiful."
print([A, B, C, D])
print([msg01 if(all([A, B, C, D])) else msg02])
print("-"*55)
# Second Example
A = True
B = "Pinoleros for life!"
C = 1976
D = "Forever Paython!"
print([A, B, C, D])
print([msg01 if(all([A, B, C, D])) else msg02])
print("-"*55)
