# portscan-ssrf

This is a Python script that performs a portscan on a specific URL, testing different ports for an SSRF (Server-Side Request Forgery) vulnerability. The purpose of the script is to identify whether the target server is responding to selection on each test port.

Requirements:

Make sure you have Python 3 installed on your system to run this script. Additionally, you'll need to install a request library, which can be installed via pip:

```pip install prompts```

How to use:

Make sure you have the ```portscan-ssrf.py``` script in your working directory. Open the ```portscan-ssrf.py``` file in a text editor. Replace ```"http://host/parameter=http://localhost:"``` with the desired URL where the vulnerable part with SSRF is present. Run the script using the following command: python3 portscan-ssrf.py

The script will test each port specified in the list of ports and display the response size and response content for each request. How it works The script uses a requests library to send HTTP to the target server on different ports specified in the port list. He constructed the test URL by substituting the port value in the vulnerable part of the available URL. It then sends a GET request to that URL and displays the size and content of the response.

This script is a basic example of how to test different ports for an SSRF vulnerability. It can be customized according to your specific needs.

Limitations:

It only tests the ports specified in the port list. You can add or modify ports as needed. The script does not implement advanced security measures or additional checks. It is important to consider the risks and implement additional safeguards when performing SSRF testing.
