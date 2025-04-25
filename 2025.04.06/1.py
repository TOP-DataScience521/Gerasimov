def strong_password(password):
    if len(password) > 7:
        if password.islower() == False and password.isupper() == False:
            if password.isalnum() == False:
                if sum(c.isdigit() for c in password) >= 2:
                    return True
                return False
            return False
        return False
    return False


# >>> strong_password('aP3:kD_l3')
# True
# >>> strong_password('password')
# False
# >>> strong_password('aP3:kD_l')
# False
# >>>