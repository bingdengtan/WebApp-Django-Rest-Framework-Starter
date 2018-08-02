from django.contrib.auth.hashers import PBKDF2PasswordHasher


def encode_password(password):
    hasher = PBKDF2PasswordHasher()
    pwd = hasher.encode(password=password, salt='salt', iterations=50000)
    return pwd


def has_attribute(data, attribute):
    return attribute in data and data[attribute] is not None
