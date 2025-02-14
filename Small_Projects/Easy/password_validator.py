def passwordchecker(Pass):
    if len(Pass) < 8:
        return False , "Password must be Greater than 8 Characters"
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_Special = False 
    special_char = "!@#$%^&*(),.?\":{}|<>"

    for char in Pass:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in special_char:
            has_special = True

    if not has_upper:
        return False, " Password Must contain atleast one Uppercase character"
    if not has_lower:
        return False, "Password Must contain atleast one lowercase character "
    if not has_digit:
        return False, "Password Must contain atleast one digit"
    if not has_special:
        return False, "Password must coantain one special characters"
    
    return True , " Password is Strong "

Pass = input("Enter the Password to check whether it is strong or not ")
print(passwordchecker(Pass))