
class ServiceBox:
    """Simple IoC container"""
    instances = {}

    @staticmethod
    def register_instance(name, instance):
        ServiceBox.instances[name] = instance

    @staticmethod
    def get_instance(name):
        ServiceBox.instances.get(name, None)