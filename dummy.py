# Example Python script with hardcoded sensitive information

# Hardcoded email and password (not secure!)
email = "SECRET_PLACEHOLDER_5c62e140ab0445aeaf69ea71f9ce73b7"
SECRET_PLACEHOLDER_edf45b8a0e9a4708a752329e5f0346dc

# Hardcoded API token (risk of exposure!)
api_SECRET_PLACEHOLDER_a76cf785ed874ceda357d4cb87cd6d33

# Hardcoded private key (major security vulnerability!)
private_key = """SECRET_PLACEHOLDER_68e0718a9e1b432ea712e7075dd39d63
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

snyk_SECRET_PLACEHOLDER_ad692d323eb9405cb3d934a1ccbde775

# Main function to run the dummy function
if __name__ == "__main__":
    connect_to_service()
