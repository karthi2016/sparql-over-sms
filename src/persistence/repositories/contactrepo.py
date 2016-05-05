from persistence.models import Contact


class ContactRepo:
    """Repository for storing and retreiving contacts"""

    @staticmethod
    def get_contacts():
        return (Contact
                .select()
                .order_by(Contact.name))

    @staticmethod
    def get_contact_byid(identifier):
        return (Contact
                .select()
                .where(Contact.identifier == identifier))

    @staticmethod
    def get_contact_byphonenumber(phonenumber):
        return (Contact
                .select()
                .where(Contact.phonenumber == phonenumber))

    @staticmethod
    def get_contact_byip(ip):
        return (Contact
                .select()
                .where(Contact.ip == ip))

    @staticmethod
    def find_contact(any_field):
        return (Contact
                .select()
                .where(
                    (Contact.id == any_field) |
                    (Contact.phonenumber == any_field) |
                    (Contact.name == any_field)))

    @staticmethod
    def add_contact(identifier, name, phonenumber=None, ip=None):
        Contact.create(
            identifier=identifier,
            name=name,
            phonenumber=phonenumber,
            ip=ip
        )

    @staticmethod
    def update_contact(identifier, name=None, phonenumber=None, ip=None):
        contact = ContactRepo.get_contact_byid(identifier)

        # conditionally update fields
        if name is not None:
            contact.name = name
        if phonenumber is not None:
            contact.phonenumber = phonenumber
        if ip is not None:
            contact.ip = ip

        contact.save()

    @staticmethod
    def delete_contact(identifier):
        return ((Contact
                .delete()
                .where(Contact.identifier == identifier))
                .execute())










