sen = list(str(input("Enter a sentence : \n>")))
dis = {}
for n in sen:
    if n in dis:
        dis[n] += 1
    else:
        dis[n] = 1

print(f"\n--- Results for given sentence ---")
print(f"You entered: {sen}")
print(f"Occurrences: {dis}")