def decode(x):
    """
    Decodes given ASCII character value into ASCII character
    """

    try:
        return str(unichr(x).encode('ascii', 'replace'))  # Make sure data is encoded properly
    except ValueError as err:
        print err
        print "** ERROR - Decoded character is unrecognized **"

def modulo(a, b, c):
    """
    Calculates modulo
    """
    return ((int(a) ** int(b)) % int(c))

def endecrypt(x, e, c):
    """
    Encrpyts/decrypts given ASCII character value, via the RSA crypto algorithm
    """
    return modulo(x, e, c)

def test_decryption(d, c):
    """
    Test function for decryption
    """

#	d = int(raw_input("\nEnter d from public key\n"))
#	c = int(raw_input("\nEnter c from public key\n"))

    x = int(raw_input("\nEnter number to decrypt\n"))
    print decode(endecrypt(x, d, c))

m = int(raw_input("Enter d: "))
n = int(raw_input("Enter c: "))

test_decryption(m,n)
