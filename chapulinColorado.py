chapulin_msgs= ['msg_01', 'msg_02', 'msg_03', 'msg_04', 'msg_05', 'msg_06']

def clear_msgs(lst):
    print('Tito mistakenly sent these confidential messages: \n ',lst)
    for item in lst:
        print('Proceeding to delete message ',item, ' Please wait...')
        del item
        print('This message was successfully deleted.')

clear_msgs(chapulin_msgs)


