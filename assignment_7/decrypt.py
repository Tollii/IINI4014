import rsa
import itertools

'''
rsa.py

Adapted by Donn Morrison for Python for Programmers IFUD1056-IINI4014
March 2018
donn.morrison@ntnu.no


decrypt.py written by Andreas Tolnes, for the 7th assignment in IINI4014, python for programmers.
'''


"""" Returns an array with the first value being the decrypted message,
     and the second value being an array with the private key.

Arguments:
public-key -- The public key of the encrypted message in an array format
ciphered_text -- The encrypted text as a string 
"""

def decryption(public_key, ciphered_text):
    primes = rsa.PrimeGen(100)
    n = []
    for i in itertools.product(primes, repeat=2):
        if(i[0] * i[1] == public_key[1]):
            n.append(i)

    try:
        for x in range(0, len(n)):
            phi = (n[x][0] - 1) * (n[x][1] - 1)
            invers = rsa.multiplicative_inverse(public_key[0], phi)
            message = rsa.decrypt((invers, public_key[1]), ciphered_text)
            if(message.startswith("h")):
                d = invers
                return [message, [d, public_key[1]]]      
    except ValueError:
        pass

if __name__ == "__main__":
    public_key = (29815, 100127)
    ciphered_text = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]
    
    print(decryption(public_key, ciphered_text))