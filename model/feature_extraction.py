import tldextract
import socket
import re

def extract_features(url):

    features = {}

    # 1 URL length
    features["url_length"] = len(url)

    # 2 number of dots
    features["dot_count"] = url.count(".")

    # 3 https presence
    features["has_https"] = 1 if "https" in url else 0

    # 4 @ symbol
    features["has_at"] = 1 if "@" in url else 0

    # 5 dash symbol
    features["has_dash"] = 1 if "-" in url else 0

    # 6 number of digits
    features["digit_count"] = sum(c.isdigit() for c in url)

    # 7 number of subdirectories
    features["directory_count"] = url.count("/")

    # 8 suspicious words
    suspicious_words = ["login","verify","secure","account","update","bank","free"]

    features["suspicious_word"] = 1 if any(word in url.lower() for word in suspicious_words) else 0

    # 9 domain length
    ext = tldextract.extract(url)

    domain = ext.domain + "." + ext.suffix

    features["domain_length"] = len(domain)

    # 10 IP length
    try:
        ip = socket.gethostbyname(domain)
    except:
        ip = "0.0.0.0"

    features["ip_length"] = len(ip)

    # 11 special character count
    features["special_char_count"] = len(re.findall(r"[!@#$%^&*(),?\":{}|<>]", url))

    return list(features.values()), ip, features