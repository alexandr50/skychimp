import random

def generate_code():
    """Генерация кода"""
    random.seed()
    return str(random.randint(10000, 99999))