# Justin is resting and enjoying 'not being kidnapped' in Paris,
# but unfortunately local kidnappers grab him in the Louvre.
# Just before police raid gangs hideout, a semi-coded text-message was intercepted from phone in hideout. Gang is known to use shifting Caesar ciphers,with a code-key somehow indicating each letter shift
# Police have no clue what to do...can you help and find Justin? you know the code for encrypting a regular non-shift caesar (below), but how to find the offsets?
# Example of static caesar code follows.
secret = 'messagetoencode'
#'messagetoencode'
secret_offset = 6
msg = [chr((ord(v) + secret_offset -97) %26 + 97) for v in secret]
# Clock is ticking...Can you find him?
intercepted_msg = 'weshfrerot!elwiaojycqwfxbcbprrmabdhyviozepjpdgwfxbui'

UNCYPHERED ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
ROT13="NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
print(intercepted_msg.translate(intercepted_msg.maketrans(UNCYPHERED, secret)))