from do_oceny import MD4, RSA

def test_md4_hex(md4_instance):
    return md4_instance._hex() == "e1fefa8fb989926d1322695a4ae34503"

def test_rsa_encode_decode(rsa_instance):
    rsa_instance.generate_keypair()
    message = "Hello, World!"
    encoded_message = rsa_instance.encode(message)
    decoded_message = rsa_instance.decode(encoded_message)
    return decoded_message == message

def test_rsa_generate_prime_number(rsa_instance):
    prime_number = rsa_instance.generate_prime_number()
    return RSA.is_prime(prime_number) == True

def test_rsa_choose_coprime(rsa_instance):
    phi_n = 100
    coprime = rsa_instance.choose_coprime(phi_n)
    return RSA.nwd(coprime, phi_n) == 1

encrypted_message = ''
md4_digest = "nie wczytano wiadomosci"
rsa = RSA()
testy = 0
if(test_md4_hex(MD4(b'Ala ma kota'))): testy += 1 
if(test_rsa_choose_coprime(rsa)): testy += 1
if(test_rsa_generate_prime_number(rsa)): testy += 1
if(test_rsa_choose_coprime(rsa)): testy += 1

print ("wykonano 4 testy z czego",testy,"wykonano poprawnie")