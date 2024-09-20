divisor = '10101'

def get_binary_dividend_for_crc():
    binary_message = ''
    message_bytes = '0x3c 0x4a 0x42 0xaf'.split(' ')
    for i in message_bytes:
        byte_dec = int(i, 16)
        binary = bin(byte_dec)[2:]
        binary_message += binary

    dividend = binary_message + '0' * (len(divisor) - 1)

    return dividend

def xor_division(dividend, divisor):
    dividend = list(map(int, dividend))
    divisor = list(map(int, divisor))
    len_divisor = len(divisor)

    for i in range(len(dividend) - len_divisor + 1):
        if dividend[i] == 1:
            for j in range(len_divisor):
                dividend[i + j] ^= divisor[j]

    remainder = dividend[-(len_divisor - 1):]
    
    return ''.join(map(str, remainder))

crc = get_binary_dividend_for_crc()
print(crc)

print(xor_division(crc, divisor))
