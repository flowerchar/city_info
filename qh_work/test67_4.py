import random

# 定义牌阶和牌花
RANKS = "23456789TJQKA"
SUITS = "CDHS"

# 定义牌点
POINTS = {
    'A': 4,
    'K': 3,
    'Q': 2,
    'J': 1,
    'T': 0,
    '9': 0,
    '8': 0,
    '7': 0,
    '6': 0,
    '5': 0,
    '4': 0,
    '3': 0,
    '2': 0,
}

# 生成一副牌
def generate_deck():
    deck = [rank + suit for rank in RANKS for suit in SUITS]
    return deck

# 随机生成13张扑克牌
def deal_hand(deck, num_cards=13):
    return random.sample(deck, num_cards)

# 计算牌点
def calculate_points(hand):
    points = 0
    for card in hand:
        rank = card[0]
        points += POINTS[rank]
    return points

# 判断合理开叫策略
def determine_opening_bid(points):
    if points >= 22:
        return "2C"
    elif points >= 20:
        return "2NT"
    elif points >= 15:
        return "1NT"
    elif points >= 13:
        return "1 of a suit"
    else:
        return "P"  # Pass

# 主程序
deck = generate_deck()
hand = deal_hand(deck)
print(f"生成的手牌是: {hand}")
points = calculate_points(hand)
print(f"手牌的总点数是: {points}")
opening_bid = determine_opening_bid(points)
print(f"合理的开叫策略是: {opening_bid}")
