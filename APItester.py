import requests
# Function to test for SQL Injection
def test_sql_injection(url):
# Payload that might cause SQL error if improperly handled
    payload = "' OR '1'='1"
    params = {'input': payload}
    response = requests.get(url, params=params)
    if "SQL syntax" in response.text:
        print("Potential SQL Injection vulnerability found")
    else:
        print("No obvious SQL Injection vulnerability detected")
# Function to test for XSS
def test_xss(url):
    # Simple script tag payload
    payload = "<script>alert('XSS')</script>"
    params = {'input': payload}
    response = requests.get(url, params=params)
    if payload in response.text:
        print("Potential XSS vulnerability found")
    else:
        print("No obvious XSS vulnerability detected")
# Function to test for Misconfiguration
def test_misconfiguration(url):
    response = requests.get(url)
    # Check for insecure headers or too much information in error messages
    if 'X-Powered-By' in response.headers or 'Server' in response.headers:
        print("Potential misconfiguration found (informative headers)")
    else:
        print("No obvious misconfiguration detected")
# Main function to run our tests
def main():
    url = input("Enter the URL of the API endpoint to test: ")
    print("\nTesting for SQL Injection...")
    test_sql_injection(url)
    print("\nTesting for XSS...")
    test_xss(url)
    print("\nTesting for Misconfiguration...")
    test_misconfiguration(url)
if __name__ == "__main__":
    main()