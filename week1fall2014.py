# def print_name():
#     age = 41
#     first_name = "stussy"
#     print(first_name + ' is ' + str(age))
#
# print_name()

value = 1

while value >= 0:
    print(value)
    value -= 1

    people = ["sts ","stussy","shanna","shanna t doolittle","mrs doolittle"]

    index = 0
    found = False
    while not found:
        print(people[index])
        if people[index] == "shanna":
            found =True
        else:
            index += 1
    print("found at index " + str(index))

    data = [
        {"name": "audrey", "age": 16},
        {"name": "dianne", "age": 20},
        {"name": "brandon", "age": 43}
    ]
    index = 0
    age = 0
    total_age = 0

    while age < 31:
        person = data[index]
        age = person["age"]
        if age < 30:
            print("total age is %s " % total_age)
            index += 1
            total_age = age + total_age

        else:
            print(str(total_age) + " is greater than 30.")
            index = 0

    for ppl in data:
        name = data[index]["name"]
        years_old = str(data[index]["age"])


        print "Sup dog. yr name is " + name + " and you are " + years_old + " years old"
        print "yep, your name is %s you are %s years old." % (name, years_old)
        index += 1
    all(data)

print bin((abs(19000000000/498)))


 #first function in a class refers to itself. "init" is a constructor.
 # object.variable like nouns also called property
# function (like verbs) inside a class is called a method
#classes have access to all the methods inside them. import classes into other docs to use.


class Transaction():
        def __init__(self, amount, payee, memo):
            self.amount = amount
            self.payee = payee
            self.memo = memo
            #copied into an instance of the object with all the self.'s

class Account():
        def __init__(self, named, balance):
            self.named = named
            self.balance = balance
            self.transactions = []

        def addTransaction(self, transaction):
            self.transactions.append(transaction)
            self.balance += transaction.amount

        def printLedger(self):
            print("Ledger...")
            for t in self.transactions:
                print(t.amount, t.payee, t.memo)

account = Account("checking", 0)
account.addTransaction(Transaction(3000, "Landlord", "December Rent"))
account.addTransaction(Transaction(3, "Starbucks", "coffee"))
account.printLedger()

class Demo():
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print(self.name)
print_name(sts)






#

