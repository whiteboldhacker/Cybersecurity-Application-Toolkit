def brute_force(password_list, secret_password):
    for guess in password_list:
        print(f"Trying password: {guess}")
        if guess == secret_password:
            print("Password found:", guess)
            return True
    print("Password not found")
    return False

if __name__ == "__main__":
    passwords = ["1234", "password", "admin", "letmein", "keerthana123"]
    secret = "keerthana123"
    brute_force(passwords, secret)
