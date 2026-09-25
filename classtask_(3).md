# Week 3, Day 5 — Classwork: Polymorphism, Abstraction, and Dataclasses

## 1. Animal Sounds

**English**
Create a base class `Animal` with `name` and `make_sound()`. Create `Dog`, `Cat`, and `Bird` that override `make_sound()` with different results. Store different objects in one list and call the same method in a loop. The loop must not check object types.

**Тоҷикӣ**
Class-и асосии `Animal`-ро бо `name` ва `make_sound()` созед. `Dog`, `Cat`, `Bird` method-и `make_sound()`-ро бо натиҷаҳои гуногун override кунанд. Object-ҳои гуногунро дар як рӯйхат нигоҳ дошта, ҳамон method-ро дар loop даъват кунед. Loop набояд навъи object-ро санҷад.

**Русский**
Создайте базовый класс `Animal` с `name` и `make_sound()`. Классы `Dog`, `Cat`, `Bird` должны переопределить `make_sound()` и возвращать разные результаты. Сохраните разные объекты в одном списке и вызывайте одинаковый метод в цикле без проверки типов объектов.

**Input**

    Rex
    Momo
    Kesha

**Output**

    Rex: Woof!
    Momo: Meow!
    Kesha: Tweet!

------------------------------------------------------------------------

## 2. Polymorphic Areas

**English**
Create a base class `Shape` with `area()`. Create `Circle`, `Rectangle`, and `Square`, each overriding `area()` with its own formula. Write `print_areas(shapes)` that accepts a mixed list and uses only `shape.area()`. Print every class name and area rounded to two decimal places.

**Тоҷикӣ**
Class-и асосии `Shape`-ро бо `area()` созед. `Circle`, `Rectangle`, `Square` ҳар кадом `area()`-ро бо формулаи худ override кунанд. `print_areas(shapes)` рӯйхати омехтаро қабул карда, танҳо `shape.area()`-ро истифода барад. Номи ҳар class ва area-ро то ду рақам пас аз нуқта чоп кунед.

**Русский**
Создайте базовый класс `Shape` с `area()`. Классы `Circle`, `Rectangle`, `Square` переопределяют `area()` своими формулами. Напишите `print_areas(shapes)`, принимающую смешанный список и использующую только `shape.area()`. Выведите имя каждого класса и площадь с двумя знаками после точки.

**Input**

    circle 5
    rectangle 4 5
    square 3

**Output**

    Circle: 78.54
    Rectangle: 20.00
    Square: 9.00

------------------------------------------------------------------------

## 3. Duck-Typed Message Senders

**English**
Create unrelated classes `EmailSender`, `SMSSender`, and `TelegramSender`. Each has `send(message)` but returns a channel-specific string. Write `notify(sender, message)` that simply calls `sender.send(message)` without inheritance and without checking its type. Pass all three objects to the same function.

**Тоҷикӣ**
Class-ҳои ба ҳам мерос надоштаи `EmailSender`, `SMSSender`, `TelegramSender` созед. Ҳар кадом `send(message)` дорад, аммо сатри махсуси канали худро бармегардонад. `notify(sender, message)` танҳо `sender.send(message)`-ро бе inheritance ва бе санҷиши type даъват кунад. Ҳар се object-ро ба ҳамон function диҳед.

**Русский**
Создайте не связанные наследованием классы `EmailSender`, `SMSSender`, `TelegramSender`. Каждый имеет `send(message)`, но возвращает строку своего канала. Напишите `notify(sender, message)`, которая просто вызывает `sender.send(message)` без наследования и проверки типа. Передайте одной функции все три объекта.

**Input**

    Lesson starts at 18:00

**Output**

    Email: Lesson starts at 18:00
    SMS: Lesson starts at 18:00
    Telegram: Lesson starts at 18:00

------------------------------------------------------------------------

## 4. Python-Style Method Overloading

**English**
Python does not keep several methods with the same name in one class—the last definition replaces earlier ones. Demonstrate this briefly, then create one `Calculator.add(*numbers)` method that accepts from 2 to 4 numbers and returns their sum. Return `Invalid number of arguments` for any other count. Test all cases without defining `add` more than once.

**Тоҷикӣ**
Python дар як class якчанд method-и ҳамномро нигоҳ намедорад — definition-и охирин пешинаҳоро иваз мекунад. Инро кӯтоҳ нишон дода, баъд як method-и `Calculator.add(*numbers)` созед, ки аз 2 то 4 рақамро қабул карда, sum-ро бармегардонад. Барои шумораи дигари argument-ҳо `Invalid number of arguments` баргардонед. Ҳама ҳолатҳоро бе definition-и такрории `add` санҷед.

**Русский**
Python не хранит несколько методов с одним именем в классе — последнее определение заменяет предыдущие. Кратко продемонстрируйте это, затем создайте единственный метод `Calculator.add(*numbers)`, принимающий от 2 до 4 чисел и возвращающий сумму. Для другого количества аргументов возвращайте `Invalid number of arguments`. Проверьте все случаи, не определяя `add` повторно.

**Input**

    5
    5 10
    1 2 3
    1 2 3 4
    1 2 3 4 5

**Output**

    Invalid number of arguments
    15
    6
    10
    Invalid number of arguments

------------------------------------------------------------------------

## 5. Abstract Notification

**English**
Using `ABC` and `@abstractmethod`, create an abstract class `Notification` with `send(message, recipient)`. Implement `EmailNotification` and `SMSNotification`. Store both in a list and send one message polymorphically. Also explain why `Notification()` cannot be instantiated.

**Тоҷикӣ**
Бо истифодаи `ABC` ва `@abstractmethod` class-и abstract-и `Notification`-ро бо `send(message, recipient)` созед. `EmailNotification` ва `SMSNotification`-ро амалӣ кунед. Ҳар дуро дар рӯйхат нигоҳ дошта, як message-ро polymorphic фиристед. Инчунин фаҳмонед, ки чаро `Notification()` сохта намешавад.

**Русский**
С помощью `ABC` и `@abstractmethod` создайте абстрактный класс `Notification` с `send(message, recipient)`. Реализуйте `EmailNotification` и `SMSNotification`. Сохраните оба объекта в списке и полиморфно отправьте одно сообщение. Также объясните, почему создать `Notification()` нельзя.

**Input**

    Hello
    user@mail.com
    +992900001122

**Output**

    Sent email to user@mail.com: Hello
    Sent SMS to +992900001122: Hello
    Notification is abstract

------------------------------------------------------------------------

## 6. Abstract Payment Method

**English**
Create abstract `PaymentMethod` with `pay(amount)` and `refund(amount)`. Implement `CardPayment`, `CashPayment`, and `CryptoPayment` with different messages and validation for a positive amount. Write one `process_payment(method, amount)` function that works with every implementation.

**Тоҷикӣ**
Class-и abstract-и `PaymentMethod`-ро бо `pay(amount)` ва `refund(amount)` созед. `CardPayment`, `CashPayment`, `CryptoPayment`-ро бо message-ҳои гуногун ва санҷиши amount-и мусбат амалӣ кунед. Як function-и `process_payment(method, amount)` нависед, ки бо ҳамаи implementation-ҳо кор мекунад.

**Русский**
Создайте абстрактный класс `PaymentMethod` с `pay(amount)` и `refund(amount)`. Реализуйте `CardPayment`, `CashPayment`, `CryptoPayment` с разными сообщениями и проверкой положительной суммы. Напишите единственную функцию `process_payment(method, amount)`, работающую со всеми реализациями.

**Input**

    card 250
    cash 100
    crypto 75

**Output**

    Card payment: 250
    Cash payment: 100
    Crypto payment: 75

------------------------------------------------------------------------

## 7. Abstract Exporters

**English**
Create an abstract class `Exporter` with `export(data)`. Implement `CSVExporter`, `JSONExporter`, and `XMLExporter`; each returns the same dictionary in a simple text representation of its format without writing files. Loop over the exporters and call the same method. Keep formatting simple and use no external packages.

**Тоҷикӣ**
Class-и abstract-и `Exporter`-ро бо `export(data)` созед. `CSVExporter`, `JSONExporter`, `XMLExporter` як dictionary-ро дар text representation-и содаи format-и худ бе навиштани file баргардонанд. Дар loop ҳамон method-ро барои exporter-ҳо даъват кунед. Format-ро сода нигоҳ дошта, package-и берунаро истифода набаред.

**Русский**
Создайте абстрактный класс `Exporter` с `export(data)`. Реализуйте `CSVExporter`, `JSONExporter`, `XMLExporter`: каждый возвращает один словарь в простом текстовом представлении своего формата без записи файлов. В цикле вызывайте одинаковый метод у всех экспортёров. Не усложняйте форматирование и не используйте внешние пакеты.

**Input**

    name Ali
    age 22

**Output**

    CSV: name,age | Ali,22
    JSON: {"name": "Ali", "age": 22}
    XML: <person><name>Ali</name><age>22</age></person>

------------------------------------------------------------------------

## 8. Student Dataclass

**English**
Use `@dataclass` to create `Student` with `student_id`, `name`, and `score=0`. Create three objects, print one object to observe the generated representation, compare two equal objects, sort all students by score descending, and print the ranking. Do not manually write `__init__`, `__repr__`, or `__eq__`.

**Тоҷикӣ**
Бо `@dataclass` class-и `Student`-ро бо `student_id`, `name`, `score=0` созед. Се object сохта, як object-ро барои дидани representation-и сохташуда чоп кунед, ду object-и баробарро муқоиса кунед, ҳамаи донишҷӯёнро аз рӯйи score камшаванда sort карда, ranking-ро чоп кунед. `__init__`, `__repr__`, `__eq__`-ро дастӣ нанависед.

**Русский**
С помощью `@dataclass` создайте `Student` с `student_id`, `name`, `score=0`. Создайте три объекта, выведите один для наблюдения за автоматически созданным представлением, сравните два равных объекта, отсортируйте студентов по убыванию балла и выведите рейтинг. Не пишите `__init__`, `__repr__` и `__eq__` вручную.

**Input**

    S01 Ali 85
    S02 Sara 95
    S01 Ali 85

**Output**

    Student(student_id='S01', name='Ali', score=85)
    Student 1 == Student 3: True
    Sara: 95
    Ali: 85
    Ali: 85

------------------------------------------------------------------------

## 9. Course Dataclass with Safe List

**English**
Create a `Course` dataclass with `code`, `title`, `price=0`, and `students` using `field(default_factory=list)`. Add `enroll(student_name)` without duplicates and implement `__len__()` for enrollment count. Create two courses, add students to only one, and prove their lists are independent.

**Тоҷикӣ**
Dataclass-и `Course`-ро бо `code`, `title`, `price=0` ва `students` тавассути `field(default_factory=list)` созед. `enroll(student_name)`-ро бе такрор ва `__len__()`-ро барои шумораи сабтшудагон илова кунед. Ду course сохта, student-ҳоро танҳо ба яке илова карда нишон диҳед, ки рӯйхатҳояшон мустақиланд.

**Русский**
Создайте dataclass `Course` с `code`, `title`, `price=0` и `students` через `field(default_factory=list)`. Добавьте `enroll(student_name)` без повторов и `__len__()` для количества записанных студентов. Создайте два курса, добавьте студентов только в один и докажите независимость списков.

**Input**

    PY Python 500
    DJ Django 700
    PY Ali
    PY Sara
    PY Ali

**Output**

    Duplicate student: Ali
    PY students: ['Ali', 'Sara']
    DJ students: []
    PY count: 2
    DJ count: 0

------------------------------------------------------------------------

## 10. Abstract Shapes as Dataclasses

**English**
Create abstract `Shape` with abstract `area()` and `perimeter()`. Implement `Rectangle`, `Circle`, and `Triangle` as dataclasses containing only their required dimensions and concrete calculations. Process a mixed list using one `print_report(shape)` function. For the triangle, use Heron's formula and valid sides.

**Тоҷикӣ**
Class-и abstract-и `Shape`-ро бо method-ҳои abstract-и `area()` ва `perimeter()` созед. `Rectangle`, `Circle`, `Triangle`-ро ҳамчун dataclass бо dimension-ҳои зарурӣ ва ҳисобҳои concrete амалӣ кунед. Рӯйхати омехтаро бо як function-и `print_report(shape)` коркард кунед. Барои triangle формулаи Герон ва тарафҳои дурустро истифода баред.

**Русский**
Создайте абстрактный `Shape` с абстрактными `area()` и `perimeter()`. Реализуйте `Rectangle`, `Circle`, `Triangle` как dataclasses, содержащие только необходимые размеры и конкретные вычисления. Обработайте смешанный список единственной функцией `print_report(shape)`. Для треугольника используйте формулу Герона и допустимые стороны.

**Input**

    rectangle 4 5
    circle 3
    triangle 3 4 5

**Output**

    Rectangle | area: 20.00 | perimeter: 18.00
    Circle | area: 28.27 | perimeter: 18.85
    Triangle | area: 6.00 | perimeter: 12.00
