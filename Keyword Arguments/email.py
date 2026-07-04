def send_email(to,sub,body):
    return to,sub,body
if __name__ == "__main__":
    print(send_email(sub="Regarding attendance",body="I went to my native place to attend the marriage of my brother",to="charansir@gmail.com"))