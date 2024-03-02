# Example Python script with hardcoded sensitive information

# Hardcoded email and password (not secure!)
email = "SECRET_PLACEHOLDER_ea352255a63a4ef09422748080f90b1f"
SECRET_PLACEHOLDER_6415920a263149df82e8f5a700c8954a

# Hardcoded API token (risk of exposure!)
api_SECRET_PLACEHOLDER_a1a7181e0c8d40289b636e47e6d236ce

# Hardcoded private key (major security vulnerability!)
private_key = """SECRET_PLACEHOLDER_fa75c8994c0741f9b4426d262636e3ac
MIICXgIBAAKBgQCqGKukO1De7Zhrt4Ga3F0skO1De7Zhrt4Ga3F0skO1De7Zhrt4
Ga3F0skO1De7Zhrt4Ga3F0skO1De7Zhrt4Ga3F0skO1De7Zhrt4Ga3F0skO1De7Z
hrt4Ga3F0skO1De7Zhrt4Ga3F0skO1De7Zhrt4Ga3F0skO1De7Zhrt4Ga3F0sIDAQABAoGB
AIhlx5qo9Vqo9VbUMZjFmDZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUM
ZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFj
UMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZj
FjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUMZjFjUM
-----END RSA PRIVATE KEY-----"""

# Hardcoded OAuth token (should be securely stored!)
oauth_token = "ghp_19C69I1Ghg5OyR5J4T75DB9S7ReAVBfGh"

# Dummy function that uses the sensitive information (for illustrative purposes)
def connect_to_service():
    # Pretend we're using the sensitive information here to connect to a service
    print(f"Connecting with email {email} and password {password}")
    print(f"Using API token: {api_token}")
    print(f"Authenticating with OAuth token: {oauth_token}")
    # ... more code

snyk_SECRET_PLACEHOLDER_4cb902c291f24c45943a23e5782f8dce

# Main function to run the dummy function
if __name__ == "__main__":
    connect_to_service()
