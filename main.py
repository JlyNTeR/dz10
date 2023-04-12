from collections import UserDict


class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, index, phone):
        self.phones[index] = Phone(phone)

    def delete_phone(self, index):
        del self.phones[index]

    def __str__(self):
        return f"{self.name}: {', '.join(str(phone) for phone in self.phones)}"

    def __repr__(self):
        return str(self)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def edit_record(self, name, field, value):
        record = self.data[name]
        setattr(record, field, value)

    def delete_record(self, name):
        del self.data[name]

    def find_records(self, **kwargs):
        result = []
        for record in self.data.values():
            match = True
            for field, value in kwargs.items():
                if field == "phone":
                    match = False
                    for phone in record.phones:
                        if phone.value == value:
                            match = True
                            break
                elif getattr(record, field).value != value:
                    match = False
                if not match:
                    break
            if match:
                result.append(record)
        return result
