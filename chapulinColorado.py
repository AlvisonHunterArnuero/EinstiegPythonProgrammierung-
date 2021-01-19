import time as t
confidential_msgs= ['Contacts', 'Spies', 'Informers', 'Snitches']

def clear_msgs(lst_messages):
    print(f"Oops, You've mistakenly sent these confidential messages: \n {lst_messages}")
    for num, item in enumerate(lst_messages):
        deleted_item = item
        print(f"Proceeding to delete message #{num+1}, Please wait...")
        t.sleep(2)
        del item
        print(f"Message << {deleted_item} >> was successfully deleted.")

clear_msgs(confidential_msgs)


