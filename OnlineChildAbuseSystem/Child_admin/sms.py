def sendSms(message,contactno):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+contactno
    headers = {
        'authorization': "mWFABDkoNZlq8ctPVxG3sizY1dgOHR49MLnjQXh2yC0pUwaf7bme0I3cQLDfgqGdKo5782XHbRWrNjFl",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    s1 = response.text
    return s1