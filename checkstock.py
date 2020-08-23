import requests
import webscraper

discord_webhook_url = 'https://discordapp.com/api/webhooks/713989387469324298/TP-HrzMPtmHdRcZkammh74PtqZaVlUlB4UB24qXAXfxkx27mucnPUMgCPatxlGPMqVT2'

Message_OUT = {
    "content": "OUT OF STOCK!"
}

Message_IN = {
    "content": "IN STOCK!"
}

result = webscraper.check_stock()
if (result):
    requests.post(discord_webhook_url, data=Message_OUT)
else:
    requests.post(discord_webhook_url, data=Message_IN)