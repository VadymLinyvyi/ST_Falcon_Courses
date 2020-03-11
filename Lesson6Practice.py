# Переписати!!!
def toFixed(numObj, digits=2):
    return f"{numObj:.{digits}f}"


text = """Etiam in porta mauris, ut lacinia dui. Suspendisse maximus ipsum purus, vitae cursus mauris blandit eu. Integer tempor non neque eget eleifend. Morbi id nulla nec lectus lobortis imperdiet eget mollis enim. Donec sed quam a mi maximus suscipit lacinia vel sapien. Vivamus dolor nisl, interdum eget porttitor in, malesuada ut mi. Nam ac fermentum velit, non gravida sem. Nullam ante leo, volutpat vel sapien  nec,  dignissimfaucibus  lacus.  Proin  sed  ligula  vitae  est  porttitor  vulputate  convallis  sed  mi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent viverra, ante eget ultricies venenatis, nulla mauris euismod velit, vitae pretium neque massa at nunc. Nullaid dictum nunc. Integer efficitur dictum  felis  sed  maximus.  Cras  ultrices  erat  vitae  mauris  rhoncus  blandit.  Morbi  ultrices  at  elit  vel dignissim. Etiam libero risus, mattis iaculis magna ac, egestas varius odio.Nam  viverra  quam  id  purus  pulvinar,  ac  interdum  diam  tincidunt.  In  pulvinar  nibh  sit  amet  purus dignissim, et porttitor libero dapibus. Nunc non nisi vel mi iaculis placerat. Proin porttitor sapien dui, at tempor dolor egestas ac. Phasellus eleifend tellus eu mauris dictum sollicitudin ac ut quam.Aliquam auctor erat vitae diam bibendum feugiat. Mauris ut dolor id ante feugiat lobortis. Duis in quam cursus, tincidunt lorem at, sagittis libero. Mauris tortor nisi, efficitur sit amet sapien sit amet, ultrices lacinia mi. Nulla  facilisi.  Nullam  laoreet  tortor id  ante  interdum,  non  tempus  ante  gravida.  Integer  nec  volutpat odio, vitae ullamcorper est. Etiam ligula dui, convallis et blandit vitae, varius vitae mauris. Mauris vitae pellentesque  justo,  a  ullamcorper  metus.  Maecenas  porttitor  massa  vitae  tortor  interdum,  aliquam rutrum tellus tincidunt.Sed vehicula felis a leo tempus, in fermentum turpis elementum. Pellentesque non sodales nulla, eget efficitur neque. In hac habitasse platea dictumst. Vivamus nec ultrices est. Fusce ac erat sed lectus egestas  consequat.  Sed  scelerisque  nisi  sem,  ut  dictum  diam  efficitur  laoreet.  Integer  aliquam  in mauris in varius. Sed eget tempus ex. Praesent nec neque eu erat dapibus lacinia id quis nulla.
Praesent  quam  diam,  volutpat  at  velit  sed,  ultricies  tincidunt  nunc.  Etiam  metus  lorem,  rutrum  et sollicitudin eget, dictum feugiat augue. Sed quis libero at turpis lobortis gravida. Nunc congue eget ipsum eget euismod. Cras odio nulla, sollicitudin imperdiet diam vel, pellentesque congue nunc. Nunc a odio eu mauris blandit placerat at sit amet turpis. Donec eget mattis felis. Sed dui odio, tincidunt eget ullamcorper non, ornare eget libero. Morbi eu lorem bibendum, pharetra sem id, condimentum mauris. Integer  volutpat  pharetra  mauris  ut  hendrerit.  Interdum  et  malesuada  fames  ac  ante ipsum primis in faucibus."""

textCopy = text

char = input("Введіть символ \n")
assert len(char) == 1 and (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122), "Очікується 1 літера латинського алфавіту"

if 65 <= ord(char) <= 90:
    char = chr(ord(char) + 32)

countChars = 0
word = ""
words = []

for s in text:
    if s in {" ", "!", "?", ",", ".", "\n"}:
        if word != "":
            # case insensitive
            if 65 <= ord(word[0]) <= 90:
                word = chr(ord(word[0]) + 32) + word[1:]
            words.append(word)
            word = ""
    else:
        word += s
if word != "":
    words.append(word)
    word = ""

minLenWord = len(words[0])
firstLetterFrequency = [0] * 26

for w in words:
    # Підрахунок слів. що починаються з заданого символа
    if w[0] == char:
        countChars += 1

    # Пошук довжини найкоротшого слова
    if len(w) < minLenWord:
        minLenWord = len(w)

    # Частота появи кожної літери на початку слів
    firstLetterFrequency[ord(w[0]) - 97] += 1

maxLetterFrequency = [0, 0]

for i in range(len(firstLetterFrequency)):
    if firstLetterFrequency[i] > maxLetterFrequency[0]:
        maxLetterFrequency[0] = firstLetterFrequency[i]
        maxLetterFrequency[1] = i

# Формуємо текст, де відсутні слова з парним індексом
# В даному випадку, вважаю розділові знаки частиною слова (видаляються разом з словом)
editedText = []
for s in textCopy:
    if s in {" ", "\n"}:
        if word != "":
            word += s
            editedText.append(word)
            word = ""
    else:
        word += s
if word != "":
    editedText.append(word+" ")
    word = ""

# 0 не вважаю парним
halfText = editedText[0]
for i in range(1, len(editedText), 2):
    halfText += editedText[i]

# Поміняти місцями перше й останнє слово
swingWords = editedText[-1]
for i in range(1, len(editedText)):
    swingWords += editedText[i]
swingWords += editedText[0]

print(toFixed(countChars / len(words) * 100))
print("Кількість символів в найкоротшому слові: {}".format(minLenWord))
print("Більшість слів починається літерою '{}'".format(chr(maxLetterFrequency[1] + 97)))
print("Текст без слів з парними індексами:\n{}".format(halfText))
print("Текст, в якому поміняно місцями перше й останнє слово:\n{}".format(swingWords))
