# dependencies
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# /dependencies

###############
# generate a private key
def gen_rsa_key():
    # crypto library required variables
    backend = default_backend()
    # generate a private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=backend
    )
    # generate a public key
    public_key = private_key.public_key()
    # send over public key, message, and signed message
    message = b"asdadw"
    signed_message = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
            hashes.SHA256()
        )
    # verify signature
    verification_result = public_key.verify(
        signed_message,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print(verification_result)
###############