l={"Apple":50,"Banana":30,"orange":20,"papaya":10,"Mango":25}

k=list(filter(lambda x:x.startswith("A"),l.items()))
print(k)
