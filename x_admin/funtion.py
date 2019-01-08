from hashlib import md5
def get_hash(str,salt=None):
    str = '!@#$%'+str+"&^**("
    if salt:
        str = str + salt
    sh = md5()
    sh.update(str.encode('utf-8'))
    return sh.hexdigest()