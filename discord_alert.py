import requests

def send_alert(message):
    webhook_url = "https://discord.com/api/webhooks/your_webhook_here"
    data = {"content": f" [SERVER ALERT]: {message}"}
    
    try:
        res = requests.post(webhook_url, json=data)
        if res.status_code == 204:
            print("Alert sent to Discord!")
    except:
        print("Failed to send alert.")

# send_alert("Player database is offline!")
