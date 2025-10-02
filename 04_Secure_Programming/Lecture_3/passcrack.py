import hashlib

def crack_hash(input_pass):
    try:
        pass_file = open("passlist.txt", "r")
    except:
        print("Could not find password list file in folder")

    for password in pass_file:
        enc_pass = password.encode("utf-8")
        digest = hashlib.md5(enc_pass.strip()).hexdigest()
        if digest == input_pass:
            print("Password found : " + password)

if __name__ == '__main__':
    crack_hash("21232f297a57a5a743894a0e4a801fc3")
