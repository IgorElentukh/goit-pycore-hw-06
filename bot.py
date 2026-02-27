from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not isinstance(value, str) and len(value.strip() == 0):
              raise ValueError("Name should be a text")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
              raise ValueError("Telephone must contain 10 digits")
        super().__init__(value)
          

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    
    def add_phone(self, value):
         self.phones.append(Phone(value))


    def edit_phone(self, oldNumber, newNumber):
         for i, phone in enumerate(self.phones):
            if phone.value == oldNumber:
                self.phones[i] = Phone(newNumber)
                break

    
    def remove_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)
                return


    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
            
        return None        
         

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    
    def find(self, name):
        return self.data.get(name)
    

    def delete(self, name):
        self.data.pop(name, None)


if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    book.delete("Jane")
