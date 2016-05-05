$(document).ready(function () {
    function ContactsViewModel() {
        var self = this;

        // General
        self.loading = ko.observable(true);

        // Form
        self.formIdentifier = ko.observable();
        self.formName = ko.observable();
        self.formPhonenumber = ko.observable();
        self.formIp = ko.observable();

        // Table
        self.contacts = ko.observableArray([]);

        // Methods
        self.addContact = function () {
            $.ajax({
                type: 'POST',
                url: 'http://localhost:5000/contacts',
                data: JSON.stringify({
                    identifier: self.formIdentifier(),
                    name: self.formName(),
                    phonenumber: self.formPhonenumber(),
                    ip: self.formIp()
                }),
                success: self.refresh,
                contentType: "application/json",
                dataType: 'json'
            });
        };

        self.viewDetails = function (contact) {
            console.log(contact);
            alert('Check the console log ;)');
        };

        self.deleteContact = function(contact) {
            $.ajax({
                type: 'DELETE',
                url: 'http://localhost:5000/contact/' + contact.identifier,
                success: self.refresh
            });
        };

        self.refresh = function () {
            $.get('http://localhost:5000/contacts', function (data) {
                self.contacts(data)
            });
        }
    }

    var viewModel = new ContactsViewModel();
    viewModel.refresh();

    ko.applyBindings(viewModel);
});