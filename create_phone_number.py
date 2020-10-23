def create_phone_number(lst_numb):
    converted_list = ''.join(str(el) for el in lst_numb)
    fmt_numb = "({}) {}-{}".format("".join(converted_list[:3]), "".join(converted_list[3:6]), "".join(converted_list[6:10]))  
    print(fmt_numb)
    return fmt_numb

# => This routine returns "(305) 486-3075"
create_phone_number([3, 0, 5, 4, 8, 6, 3, 0, 7, 5]) 
