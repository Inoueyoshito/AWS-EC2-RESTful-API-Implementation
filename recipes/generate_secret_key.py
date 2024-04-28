import secrets

def generate_secret_key():
    return secrets.token_urlsafe(24)

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print("Generated SECRET_KEY:", secret_key)