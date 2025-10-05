"""
Cryptopals crypto challenges. https://cryptopals.com/

Challenges  Set 1  Challenge 2
Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.
"""

print("--------------------------------------")
print("- Enter 2 equal length sized buffers -")
print("--------------------------------------\n")

byte_1 = bytes.fromhex(input("Enter buffer 1: "))
byte_2 = bytes.fromhex(input("Enter buffer 2: "))

xor_result = []

for a, b in zip(byte_1, byte_2):
    xor_byte = a ^ b
    xor_result.append(xor_byte)

result = bytes(xor_result)
print(result.hex())
