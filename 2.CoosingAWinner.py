"""
    Randomly choosing a winner
    Input: Nothing
    Output: randomly selected name from the list
"""

from random import choice

names = ["Василь", "Петро", "Микола", "Олександр", "Вадим", "Валерій", "Сергій", "Михайло", "Іван"]

# В нашому випадку надлишкова перевірка, але хай буде
if len(names) != 0:
    print(choice(names))
else:
    print("No winners")
