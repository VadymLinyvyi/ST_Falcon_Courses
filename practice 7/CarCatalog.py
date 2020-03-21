class TOKEN_TYPE:
    OPERATOR = 0
    STRING = 1
    NUMBER = 2


class __TOKENIZER_STATE:
    WHITESPACE = 0
    INTEGER = 1
    STRING = 2
    STRING_END = 3


def tokenize(stream):
    def is_delimiter(char):
        return char.isspace() or char in "{}[]:,"

    token = []
    completed = False
    new_token = ""

    def process_char(char):
        nonlocal token, completed, new_token
        advance = True
        add_char = False
        next_state = state
        if state == __TOKENIZER_STATE.WHITESPACE:
            if char == "{":
                completed = True
                new_token = (TOKEN_TYPE.OPERATOR, "{")
            elif char == "}":
                completed = True
                new_token = (TOKEN_TYPE.OPERATOR, "}")
            elif char == "[":
                completed = True
                new_token = (TOKEN_TYPE.OPERATOR, "[")
            elif char == "]":
                completed = True
                new_token = (TOKEN_TYPE.OPERATOR, "]")
            elif char == ",":
                completed = True
                new_token = (TOKEN_TYPE.OPERATOR, ",")
            elif char == ":":
                completed = True
                new_token = (TOKEN_TYPE.OPERATOR, ":")
            elif char == "\"":
                next_state = __TOKENIZER_STATE.STRING
            elif char in "0123456789":
                next_state = __TOKENIZER_STATE.INTEGER
                add_char = True
        elif state == __TOKENIZER_STATE.INTEGER:
            if char in "0123456789":
                add_char = True
            elif is_delimiter(char):
                next_state = __TOKENIZER_STATE.WHITESPACE
                completed = True
                new_token = (TOKEN_TYPE.NUMBER, int("".join(token)))
                advance = False
        elif state == __TOKENIZER_STATE.STRING:
            if char == "\"":
                completed = True
                new_token = (TOKEN_TYPE.STRING, "".join(token))
                next_state = __TOKENIZER_STATE.STRING_END
            else:
                add_char = True
        elif state == __TOKENIZER_STATE.STRING_END:
            if is_delimiter(char):
                advance = False
                next_state = __TOKENIZER_STATE.WHITESPACE
        if add_char:
            token.append(char)

        return advance, next_state

    state = __TOKENIZER_STATE.WHITESPACE
    char = stream.read(1)
    index = 0
    while char:
        advance, state = process_char(char)
        if completed:
            completed = False
            token = []
            yield new_token
        if advance:
            char = stream.read(1)
            index += 1
    if completed:
        yield new_token


def parse(file):
    token_stream = tokenize(file)
    val, token_type, token = __parse(token_stream, next(token_stream))
    if token is not None:
        raise ValueError("Improperly closed JSON object")
    try:
        next(token_stream)
    except StopIteration:
        return val


def __parse(token_stream, first_token):
    class KVP:
        def __init__(self, key):
            self.key = key
            self.value = None
            self.set = False

        def __str__(self):
            if self.set:
                return "{}: {}".format(self.key, self.value)
            else:
                return "{}: <NULL>".format(self.key)

    stack = []
    token_type, token = first_token
    if token_type == TOKEN_TYPE.OPERATOR:
        if token == "{":
            stack.append({})
        elif token == "[":
            stack.append([])

    last_type, last_token = token_type, token
    try:
        token_type, token = next(token_stream)
    except StopIteration as e:
        raise ValueError("Too many opening braces") from e
    try:
        while True:
            if isinstance(stack[-1], list):
                if last_type == TOKEN_TYPE.OPERATOR:
                    if last_token == "[":
                        if token_type == TOKEN_TYPE.OPERATOR:
                            if token == "{":
                                stack.append({})
                            elif token == "[":
                                stack.append([])
                            elif token != "]":
                                raise ValueError("Array must either be empty or contain a value.  Got '{}'".
                                                 format(token))
                        else:
                            stack.append(token)
                    elif last_token == ",":
                        if token_type == TOKEN_TYPE.OPERATOR:
                            if token == "{":
                                stack.append({})
                            elif token == "[":
                                stack.append([])
                            else:
                                raise ValueError("Array value expected.  Got '{}'".format(token))
                        else:
                            stack.append(token)
                    elif last_token == "]":
                        value = stack.pop()
                        if len(stack) == 0:
                            return value, token_type, token
                        if isinstance(stack[-1], list):
                            stack[-1].append(value)
                        elif isinstance(stack[-1], dict):
                            stack[-1][value.key] = value.value
                        elif isinstance(stack[-1], KVP):
                            stack[-1].value = value
                            stack[-1].set = True
                            value = stack.pop()
                            if len(stack) == 0:
                                return value, token_type, token
                            if isinstance(stack[-1], list):
                                stack[-1].append(value)
                            elif isinstance(stack[-1], dict):
                                stack[-1][value.key] = value.value
                            else:
                                raise ValueError("Array items must be followed by a comma or closing bracket.  "
                                                 "Got '{}'".format(value))
                        else:
                            raise ValueError("Array items must be followed by a comma or closing bracket.  "
                                             "Got '{}'".format(value))
                    elif last_token == "}":
                        raise ValueError("Array closed with a '}'")
                    else:
                        raise ValueError("Array should not contain ':'")
                else:
                    raise ValueError("Unknown Error")
            elif isinstance(stack[-1], dict):
                if last_type == TOKEN_TYPE.OPERATOR:
                    if last_token == "{":
                        if token_type == TOKEN_TYPE.OPERATOR:
                            if token == "{":
                                stack.append({})
                            elif token == "[":
                                stack.append([])
                            elif token != "}":
                                raise ValueError("Object must either be empty or contain key value pairs."
                                                 "  Got '{}'".format(token))
                        elif token_type == TOKEN_TYPE.STRING:
                            stack.append(KVP(token))
                        else:
                            raise ValueError("Object keys must be strings.  Got '{}'".format(token))
                    elif last_token == ",":
                        if token_type == TOKEN_TYPE.OPERATOR:
                            if token == "{":
                                stack.append({})
                            elif token == "[":
                                stack.append([])
                            else:
                                raise ValueError("Object key expected.  Got '{}'".format(token))
                        elif token_type == TOKEN_TYPE.STRING:
                            stack.append(KVP(token))
                        else:
                            raise ValueError("Object keys must be strings.  Got '{}'".format(token))
                    elif last_token == "}":
                        value = stack.pop()
                        if len(stack) == 0:
                            return value, token_type, token
                        if isinstance(stack[-1], list):
                            stack[-1].append(value)
                        elif isinstance(stack[-1], dict):
                            stack[-1][value.key] = value.value
                        elif isinstance(stack[-1], KVP):
                            stack[-1].value = value
                            stack[-1].set = True
                            value = stack.pop()
                            if len(stack) == 0:
                                return value, token_type, token
                            if isinstance(stack[-1], list):
                                stack[-1].append(value)
                            elif isinstance(stack[-1], dict):
                                stack[-1][value.key] = value.value
                            else:
                                raise ValueError("Object key value pairs must be followed by a comma or "
                                                 "closing bracket.  Got '{}'".format(value))
                    elif last_token == "]":
                        raise ValueError("Object closed with a ']'")
                    else:
                        raise ValueError("Object key value pairs should be separated by comma, not ':'")
            elif isinstance(stack[-1], KVP):
                if stack[-1].set:
                    if token_type == TOKEN_TYPE.OPERATOR:
                        if token != "}" and token != ",":
                            raise ValueError("Object key value pairs should be followed by ',' or '}'.  Got '"
                                             + token + "'")
                        value = stack.pop()
                        if len(stack) == 0:
                            return value, token_type, token
                        if isinstance(stack[-1], list):
                            stack[-1].append(value)
                        elif isinstance(stack[-1], dict):
                            stack[-1][value.key] = value.value
                        else:
                            raise ValueError("Object key value pairs must be followed by a comma or closing bracket.  "
                                             "Got '{}'".format(value))
                        if token == "}" and len(stack) == 1:
                            return stack[0], None, None
                    else:
                        raise ValueError("Object key value pairs should be followed by ',' or '}'.  Got '"
                                         + token + "'")
                else:
                    if token_type == TOKEN_TYPE.OPERATOR and token == ":" and last_type == TOKEN_TYPE.STRING:
                        pass
                    elif last_type == TOKEN_TYPE.OPERATOR and last_token == ":":
                        if token_type == TOKEN_TYPE.OPERATOR:
                            if token == "{":
                                stack.append({})
                            elif token == "[":
                                stack.append([])
                            else:
                                raise ValueError("Object property value expected.  Got '{}'".format(token))
                        else:
                            stack[-1].value = token
                            stack[-1].set = True
                    else:
                        raise ValueError("Object keys must be separated from values by a single ':'.  "
                                         "Got '{}'".format(token))
            else:
                value = stack.pop()
                if isinstance(stack[-1], list):
                    stack[-1].append(value)
                elif isinstance(stack[-1], dict):
                    stack[-1][value.key] = value.value
                else:
                    raise ValueError("Array items must be followed by a comma or closing bracket.  "
                                     "Got '{}'".format(value))

            last_type, last_token = token_type, token
            token_type, token = next(token_stream)
    except StopIteration as e:
        if len(stack) == 1:
            return stack[0], None, None
        else:
            raise ValueError("JSON Object not properly closed") from e


def wait():
    while True:
        if input("\n\n[0] Повернутись назад\n") == "0":
            return


def wait_pagination():
    while True:
        command = input("\n\n[1] Наступна сторінка\n"
                            "[0] Повернутись назад\n")
        if command == "0":
            return 0
        elif command == "1":
            return 1
        else:
            print("Некоректна команда")


def get_brands(cars: set):
    brands = set()
    for car in cars:
        brands.add(car.get("Make"))
    return brands


def print_all_items(cars: list):
    keys = cars[0].keys()
    for car in cars:
        print("+=========================================================+")
        for key in keys:
            print("\t{}: {}".format(key, car.get(key)))


def generator(cars):
    for car in cars:
        yield car


def paginated_print(cars, pagination):
    gen = generator(cars)
    keys = cars[0].keys()
    while True:
        for i in range(pagination):
            try:
                car = next(gen)
            except StopIteration:
                return
            print("+=========================================================+")
            for key in keys:
                print("\t{}: {}".format(key, car.get(key)))
        if wait_pagination() == 0:
            return


def print_brands(cars: set):
    brands = get_brands(cars)
    for brand in brands:
        print(brand)


def filter_by_brand(cars, brand):
    filtered_cars = []
    brand = brand.lower()
    for car in cars:
        tmp_brand = str(car["Make"]).lower()
        if brand in tmp_brand:
            filtered_cars.append(car)
    return filtered_cars


def filter_by_model(car, model):
    filtered_cars = []
    model = model.lower()
    for car in cars:
        tmp_model = str(car["Model"]).lower()
        if model in tmp_model:
            filtered_cars.append(car)
    return filtered_cars


def filter_by_years(cars, min_year, max_year):
    if not (min_year.isdigit() and max_year.isdigit()):
        print("Некоректний запит")
    else:
        filtered_cars = []
        max_year, min_year = max(int(max_year), int(min_year)), min(int(max_year), int(min_year))
        for car in cars:
            if min_year <= car.get("Year") <= max_year:
                filtered_cars.append(car)
        return filtered_cars


def sort(cars, key, direction, enabled):
    if not enabled:
        return cars
    # Пишу після роботи втомлений... нема сил на нормальний алгоритм сортування
    for i in range(len(cars)):
        for j in range(len(cars)):
            if (cars[i][key] < cars[j][key] and direction) or (cars[i][key] > cars[j][key] and not direction):
                cars[i], cars[j] = cars[j], cars[i]
    return cars


with open("Car_Model_List.json", "r") as file:
    cars = parse(file)
    pagination = 5
    sort_enabled = False
    sorting_key = "Year"
    sorting_direction = True
while True:
    print("Виберіть пункт меню:")
    print("\t[1] Вивести повну інформацію про всі авто")
    print("\t[2] Вивести список доступних брендів")
    print("\t[3] Вивести список моделей вказаного бренду")
    print("\t[4] Вивести усі моделі виробника за вказаний проміжок часу")
    print("\t[5] Вивести доступні авто вказаної моделі")

    print("\t[9] Налаштування")
    print("\t[0] Вихід")
    command = input()
    if command == "0":
        break
    elif command == "9":
        while True:
            print("\t\t[1] Змінити кількість авто на сторінку")
            print("\t\t[2] Налаштування сортування")
            print("\t\t[0] Назад")
            command2 = input()
            if command2 == "0":
                break
            elif command2 == "1":
                pagination = int(input("\t\t\t Введіть кількість авто на сторінку. Поточне значення = {}\n"
                                       "\t\t\t* При введенні нуля виводимуться усі авто\n".format(pagination)))
            elif command2 == "2":
                while True:
                    print("\t\t\t[1] Ввімкнути/вимкнути сортування. Поточний стан - {}".format("ввімкнуто" if sort_enabled
                                                                                               else "вимкнуто"))
                    print("\t\t\t[2] Змінити ключ сортування. Поточне значення - {}".format(sorting_key))
                    print("\t\t\t[3] Змінити напрямок сортування. Поточне значення - {}".format("А-я" if sorting_direction
                                                                                            else "я-А"))
                    print("\t\t\t[0] Назад")
                    command3 = input()
                    if command3 == "0":
                        break
                    elif command3 == "1":
                        sort_enabled = not sort_enabled
                    elif command3 == "2":
                        while True:
                            print("\t\t\t\t[1] Сортувати за роком випуску")
                            print("\t\t\t\t[2] Сортувати за назвою моделі")
                            print("\t\t\t\t[3] Сортувати за виробником")
                            print("\t\t\t\t[0] Назад")
                            command4 = input()
                            if command4 == "0":
                                break
                            elif command4 == "1":
                                sorting_key = "Year"
                            elif command4 == "2":
                                sorting_key = "Model"
                            elif command4 == "3":
                                sorting_key = "Make"
                            else:
                                print("Некоректна команда")
                    elif command3 == "3":
                        sorting_direction = not sorting_direction
                    else:
                        print("Некоректна команда")
            else:
                print("Некоректна команда")
    elif command == "1":
        if pagination == 0:
            print_all_items(sort(cars, sorting_key, sorting_direction, sort_enabled))
            wait()
        else:
            paginated_print(sort(cars, sorting_key, sorting_direction, sort_enabled), pagination)
    elif command == "2":
        print_brands(cars)
        wait()
    elif command == "3":
        brand = input("Введіть назву бренда\n")
        if pagination == 0:
            print_all_items(filter_by_brand(sort(cars, sorting_key, sorting_direction, sort_enabled), brand))
            wait()
        else:
            paginated_print(filter_by_brand(sort(cars, sorting_key, sorting_direction, sort_enabled), brand), pagination)
    elif command == "4":
        brand = input("Введіть назву бренда\n")
        min_year = input("Введіть мінімальний рік випуску (yyyy)\n")
        max_year = input("Введіть максимальний рік випуску (yyyy)\n")
        if pagination == 0:
            print_all_items(sort(filter_by_brand(filter_by_years(cars, min_year, max_year), brand),
                                 sorting_key, sorting_direction, sort_enabled))
            wait()
        else:
            paginated_print(sort(filter_by_brand(filter_by_years(cars, min_year, max_year), brand),
                                 sorting_key, sorting_direction, sort_enabled), pagination)
    elif command == "5":
        model = input("Введіть назву моделі\n")
        if pagination == 0:
            print_all_items(filter_by_model(sort(cars, sorting_key, sorting_direction, sort_enabled), model))
            wait()
        else:
            paginated_print(filter_by_model(sort(cars, sorting_key, sorting_direction, sort_enabled), model), pagination)
    else:
        print("Некоректна команда")
