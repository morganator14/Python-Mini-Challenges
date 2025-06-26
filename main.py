import random
import game_data

def get_account():
    account = game_data.data[random.randint(0,len(game_data.data))]
    return account

def compare_accounts(account_a, account_b):
    if account_a["follower_count"] > account_b["follower_count"]:
        return f"{account_a["name"]}, a {account_a["description"]} from {account_a["country"]}"
    else:
        return f"{account_b["name"]}, a {account_b["description"]} from {account_b["country"]}"

comparing = True
random_account_a = get_account()
random_account_b = get_account()
if random_account_b == random_account_a:
    random_account_b = get_account()
    
print(f"Compare A: {random_account_a["name"]}, a {random_account_a["description"]} from {random_account_a["country"]}.")
print(f"with B: {random_account_b["name"]}, a {random_account_b["description"]} from {random_account_b["country"]}.")
score = 0
print(f"Current score: {score}")
while comparing:
    guess = input("Who do you think has more followers?")
    high_account = compare_accounts(random_account_a, random_account_b)
    if guess in high_account:
        print("You got it right!")
        score += 1
        new_a = high_account
        random_account = get_account()
        print(f"Compare: {new_a} with")
        print(f"with B: {random_account["name"]}, a {random_account["description"]} from {random_account["country"]}.")
        print(f"Current score: {score}")
    else:
        print("You messed up loser")
        comparing = False

