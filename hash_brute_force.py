import hashlib


def make_hash(text, hash_type):
    if hash_type == "md5":
        return hashlib.md5(text.encode()).hexdigest()
    elif hash_type == "sha1":
        return hashlib.sha1(text.encode()).hexdigest()
    elif hash_type == "sha256":
        return hashlib.sha256(text.encode()).hexdigest()
    else:
        raise ValueError("Hash is not supported!!")


target_hash = input("enter the hash here: ").strip()
hash_type = input("enter the hash Type: ").lower()

mode = input("If you want to Normal attack enter 1 and if you want wordlist attack enter 2:")

found = False

if mode == "1":
    start = int(input("enter start number: "))
    end = int(input("enter end number:"))

    for num in range(start, end + 1):
        word = str(num).zfill(len(str(end)))
        if make_hash(word, hash_type) == target_hash:
            print(f"[✔] The password is: {word}")
            found = True
            break

elif mode == "2":
    file_path = input("enter the wordlist name: ")
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                word = line.strip()
                if make_hash(word, hash_type) == target_hash:
                    print(f"[✔] The password is: {word}")
                    found = True
                    break
    except FileNotFoundError:
        print("the wordlist is not avaible!!")

else:
    print("you have made wrong choise!!")

if not found:
    print("we didn't find match!!")
