def date_format(date):
    year = date[-4::1]
    month = date[:2:]
    day = date[3:5:]
    return year + '-' + month + '-' + day