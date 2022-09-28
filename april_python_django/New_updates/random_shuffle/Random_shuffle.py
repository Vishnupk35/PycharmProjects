import random
all_users=["a","b","c","d","e"]
def get_users():
    random.shuffle(all_users)
    return all_users[:len(all_users)]
print(get_users())
