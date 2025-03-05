import re
banner = """

██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗     ██╗     ██╗███╗   ██╗██╗  ██╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██║  ██║██║██╔════╝██║  ██║██║████╗  ██║██╔════╝     ██║     ██║████╗  ██║██║ ██╔╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝███████║██║███████╗███████║██║██╔██╗ ██║██║  ███╗    ██║     ██║██╔██╗ ██║█████╔╝     ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║    ██║     ██║██║╚██╗██║██╔═██╗     ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ██║  ██║██║███████║██║  ██║██║██║ ╚████║╚██████╔╝    ███████╗██║██║ ╚████║██║  ██╗    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                          
██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██████╗ ██╗   ██╗         ███████╗ █████╗ ███╗   ██╗ ██████╗██╗  ██╗██╗████████╗            
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██╔══██╗╚██╗ ██╔╝         ██╔════╝██╔══██╗████╗  ██║██╔════╝██║  ██║██║╚══██╔══╝            
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██████╔╝ ╚████╔╝█████╗    ███████╗███████║██╔██╗ ██║██║     ███████║██║   ██║               
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ██╔══██╗  ╚██╔╝ ╚════╝    ╚════██║██╔══██║██║╚██╗██║██║     ██╔══██║██║   ██║               
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║       ██████╔╝   ██║            ███████║██║  ██║██║ ╚████║╚██████╗██║  ██║██║   ██║               
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝       ╚═════╝    ╚═╝            ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝   ╚═╝               
                                                                                                                                                        
"""

print(banner)
# List of common phishing keywords (for demonstration purposes)
phishing_keywords = [
    "login", "verify", "account", "update", "secure", "bank", "password", "signin","0", "confirm", "invoice",
    "message", "required", "file", "request", "action", "document", "verification", "efax", "vm",
    "alert", "notification", "urgent", "suspend", "limited", "unusual", "activity", "deactivate", "reactivate", "security",
    "breach", "compromise", "locked", "unlock", "reset", "support", "helpdesk", "administrator", "compliance", "policy",
    "transaction", "payment", "billing", "refund", "shipment", "delivery", "order", "purchase", "receipt", "statement",
    "balance", "overdue", "penalty", "fine", "legal", "court", "settlement", "claim", "insurance", "tax",
    "irs", "hmrc", "revenue", "lottery", "prize", "winner", "award", "bonus", "gift", "voucher", "coupon", "offer",
    "promotion", "deal", "discount", "survey", "feedback", "review", "rating", "subscription", "membership", "profile",
    "settings", "preferences", "upgrade", "renew", "expire", "expiration", "validation",
    "authenticate", "authorization", "access", "passcode", "pin", "token", "code",
    "2fa", "mfa", "otp", "encryption", "firewall", "antivirus", "malware", "spyware", "ransomware", "scam", "fraud",
    "identity", "theft", "hack", "incident", "warning", "caution", "notice", "important", "attention",
    "immediate", "response", "reply", "contact", "phone", "number", "call", "assistance", "customer", "care",
    "team", "department", "center", "manager", "director", "officer", "agent", "representative",
    "consultant", "analyst", "technician", "engineer", "supervisor", "auditor", "investigator", "advisor",
    "consultant", "executive", "ceo", "cfo", "coo", "cio", "cto", "vp", "principal", "founder",
    "business", "company", "corporation", "firm", "organization", "institution", "agency", "association", "society",
    "group", "committee", "council", "task", "force", "initiative", "campaign", "strategy", "procedure",
    "protocol", "guideline", "standard", "regulation", "law", "statute", "ordinance", "code", "act", "bill",
    "legislation", "directive", "order", "mandate", "decree", "proclamation", "announcement", "statement",
    "correspondence", "communication", "email", "mail", "post", "package", "parcel", "dispatch", "consignment",
    "cargo", "freight", "stock", "inventory", "supply", "goods", "merchandise", "product", "item", "material",
    "resource", "property", "equipment", "tool", "device", "machine", "appliance", "gadget",
    "innovation", "development", "design", "model", "prototype", "sample", "template", "pattern", "blueprint",
    "diagram", "chart", "graph", "map", "illustration", "image", "picture", "photo", "screenshot", "icon", "logo",
    "symbol", "brand", "label", "tag", "title", "name", "word", "phrase", "expression",
    "speech", "talk", "conversation", "dialogue", "discussion", "debate", "argument",
    "dispute", "controversy", "conflict", "warning", "investigation", "inquiry",
    "response", "reaction", "answer", "solution", "resolution", "agreement",
    "contract", "understanding", "alliance", "partnership", "collaboration", "cooperation"
]


# Function to check if a URL contains phishing keywords
def contains_phishing_keywords(url):
    for keyword in phishing_keywords:
        if keyword in url.lower():
            return True
    return False

# Function to check if a URL contains suspicious patterns (e.g., IP addresses)
def contains_suspicious_patterns(url):
    # Check for presence of IP address in URL
    ip_pattern = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
    if ip_pattern.search(url):
        return True

    # Check for multiple subdomains (e.g., http://secure-login.example.com)
    subdomain_pattern = re.compile(r'(\w+\.){3,}')
    if subdomain_pattern.search(url):
        return True

    return False

# Main function to scan a list of URLs for phishing
def scan_for_phishing(urls):
    for url in urls:
        if contains_phishing_keywords(url):
            print(f"Potential phishing URL detected: {url}")
        elif contains_suspicious_patterns(url):
            print(f"Suspicious URL detected: {url}")
        else:
            print(f"URL seems safe: {url}")

# Example usage
urls_to_scan = [
    "http://example.com",
    "http://secure-login.example.com",
    "http://update-password.com",
    "http://go0gle.com"
]

scan_for_phishing(urls_to_scan)
