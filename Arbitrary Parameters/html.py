def create_html(tag,**att):
    print("Tag name is:",tag, "Att is:",*att.items())

create_html(tag='a',href='https://python.org',target='_blank')