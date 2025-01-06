import hashlib

f = open('top-10000-passwords.txt', 'r')
passwords = list(map(str.strip, f.readlines()))
f.close()
f = open('known-salts.txt', 'r')
salts = list(map(str.strip, f.readlines()))
salts.append('')
f.close()


def crack_sha1_hash(hash, use_salts=False):
    global passwords, salts
    if not use_salts:
        for password in passwords:
            password = password.strip()
            if hashlib.sha1(password.encode()).hexdigest() == hash:
                return password
    else:
        for password in passwords:
            for salt in salts:
                salt = salt.strip()
                password = password.strip()
                if hashlib.sha1((salt + password).encode()).hexdigest() == hash:
                    return password
                if hashlib.sha1((password + salt).encode()).hexdigest() == hash:
                    return password

    return "PASSWORD NOT IN DATABASE"
