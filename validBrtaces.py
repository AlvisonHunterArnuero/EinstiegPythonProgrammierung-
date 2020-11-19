def validBraces(string):
    braces = list(string)
    lst_tracer = []
    last_value = ''
    print(braces)
    for el in braces:
        if(el == "(" or el== "{" or el == "["):
            lst_tracer.append(el)
        else:
            if(len(lst_tracer)== 0):
                  return False
            last_value = lst_tracer[len(lst_tracer)-1]
            if( (el == ']' and last_value == '[') or (el == '}' and last_value == '{') or (el== ')' and last_value == '(')):
                  lst_tracer.pop()
                  print(lst_tracer)
            else:
                  return True

    if lst_tracer == 0:
        print(lst_tracer)
        return lst_tracer


validBraces('()[[{}')
validBraces("()")
validBraces("[(])")
