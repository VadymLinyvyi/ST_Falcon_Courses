"""
    Обробка тексту
    Ввідні данні не очікуються
    Рахує кількість повних речень (по факту кількість розділювальних символів, що закінчують речення)
"""

text = """Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium,
totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta
sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est,
qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi
tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima
veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea
commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam
nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
"""
#texttmp -> text_tmp або text_input

# Знаю, що костиль :)
texttmp = (text.replace("...", ".").replace("!!!", ".").replace("???", ".").replace("!?", ".").replace("?!", ".").
           replace("!", ".").replace("?", "."))

# Чи не ліпше буде спершу усі !, ?, перевести в . і після зробити replace("..", ".")
#text2 = (text.replace('!', '.').replace('?', '.').replace('..', '.'))
#if text2 == texttmp:
#    print('eq')

sentenses = texttmp.count(".")
chars_with_spaces = len(text)
chars_without_spaces = chars_with_spaces-text.count(" ")
quises = text.lower().count("quis")
words = text.split(" ")
shorttext = ""
i = 0

# ми можемо просто зробити .replace("  ", " ") і після працювати з текстом без пробілів

# Ігнорую випадок, коли в тексті є декілька пробілів підряд
while len(shorttext+words[i]) < 120:
    shorttext += words[i]+" "
    i += 1

while shorttext[-1] in {".", ",", ":", ";", "?", "!", " ", "-"}:
    shorttext = shorttext[:-1]

print(shorttext+"...")
print("Кількість речень в тексті: {}".format(sentenses))
print("""Кількість входжень слова "quis": {}""".format(quises))
print("Кількість символів в тексті: {}".format(chars_with_spaces))
print("Кількість символів в тексті, не враховуючи пробіли: {}".format(chars_without_spaces))
