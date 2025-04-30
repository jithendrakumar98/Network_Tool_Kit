import whois

def whois_lookup(domain):
    try:
        result = whois.whois(domain)
        print(result)
    except Exception as e:
        print("❌ Whois not supported or failed:", e)

