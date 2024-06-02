
def below_zero(operations):
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False
