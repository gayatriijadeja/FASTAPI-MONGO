def individual_serial(ioc) -> dict:
    return {
        "id": str(ioc["_id"]),
        "filename": ioc["filename"],
        "sender": ioc["sender"],
        "subject": ioc["subject"],
        "time": ioc["time"],
        "body": ioc["body_content"],
        "ips": ioc["ips"],
        "emails": ioc["emails"],
        "domains": ioc["domains"],
        "urls": ioc["urls"],
        "headers_footers":ioc["headers_footers"],
    }

def list_serial(iocs) -> list:
    return [individual_serial(ioc) for ioc in iocs] 