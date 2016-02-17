
class AddressBook:
    """A wrapper around the contact store"""

    def __init__(self, contactstore, filepath):
        self.contactstore = contactstore
        self.filepath = filepath

    def get_contacts(self):
        contactids = self.contactstore.sections()
        return [self.get_contact(contactid) for contactid in contactids]

    def get_contact(self, contactid):
        contactinfo = self.contactstore[contactid]
        return {
            'contactid': contactid,
            'fullname': contactinfo['fullname'],
            'phonenumber': contactinfo['phonenumber']
        }

    def add_contact(self, contactinfo):
        contactid = contactinfo['contactid']

        self.contactstore.add_section(contactid)
        self.contactstore.set(contactid, 'fullname', contactinfo['fullname'])
        self.contactstore.set(contactid, 'phonenumber', contactinfo['phonenumber'])

        # persist changes
        self.save()

    def update_contact(self, contactid, contactinfo):
        contact = self.contactstore[contactid]
        contact['fullname'] = contactinfo['fullname']
        contact['phonenumber'] = contactinfo['phonenumber']

        # persist changes
        self.save()

    def remove_contact(self, contactid):
        self.contactstore.remove_section(contactid)

        # persist changes
        self.save()

    def save(self):
        with open(self.filepath, 'w') as file:
            self.contactstore.write(file)



