from getpass import getpass


# Host information
SSL_VERIFY = False


def auth(session, host, api_port=4343):
    http_headers = {"Content-Type": "application/json"}

    # Creds
    USERNAME = input("Enter username: ")
    PASSWORD = getpass("Enter Aruba Controller password: ")
    creds = f"username={USERNAME}&password={PASSWORD}"

    # Login URL
    login_url = f"https://{host}:{api_port}/v1/api/login"

    # Authenticate
    response = session.post(
        login_url, data=creds, headers=http_headers, verify=SSL_VERIFY
    )

    # Verify Authentication Worked
    if response.status_code == 200:
        auth_response = response.json().get("_global_result")
        if auth_response.get("X-CSRF-Token"):
            # Bind headers to requests' session object
            session.headers["X-CSRF-Token"] = auth_response["X-CSRF-Token"]

        if auth_response.get("UIDARUBA"):
            return auth_response["UIDARUBA"]
        else:
            return None
    elif response.status_code == 401:
        raise ValueError("401 Response code: Authentication Failed")
    else:
        raise ValueError(f"Authentication Failed: {response.status_code}")


def get(session, base_url, relative_url):
    full_url = f"{base_url}{relative_url}"
    return session.get(full_url, verify=SSL_VERIFY)
