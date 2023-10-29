target_hash = 3713081631934410656

for i in range(10):  # You can adjust the range as needed
    for j in range(10):
        tpl = (i,j)
        print(tpl)
        if hash(tpl) == target_hash:
            print("Found tuple with hash value 3713081631934410656:")
            print(tpl)
            break