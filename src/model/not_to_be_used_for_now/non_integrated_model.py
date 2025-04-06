class Datenverarbeiter:
    def __init__(self):
        self.responsible_party = None
        self.processors = []
        self.system = None
        self.purpose = None
        self.data_type = None
        self.data_class = None
        self.data_category = None
        self.data_subcategory = None
        self.data_kind = None
        self.disclosure_form = None

class Verantwortlicher:
    def __init__(self, name, role, contact):
        self.name = name
        self.role = role
        self.contact = contact

class Verarbeiter:
    def __init__(self, name, permissions, access_level):
        self.name = name
        self.permissions = permissions
        self.access_level = access_level

class System:
    def __init__(self, name, version, security_level):
        self.name = name
        self.version = version
        self.security_level = security_level

class DatenTyp:
    def __init__(self, data_class, category, subcategory):
        self.data_class = data_class
        self.category = category
        self.subcategory = subcategory

class DatenArt:
    def __init__(self, name, sensitivity_level, retention_period):
        self.name = name
        self.sensitivity_level = sensitivity_level
        self.retention_period = retention_period

class Offenlegungsformular:
    def __init__(self, method, recipient, purpose):
        self.method = method
        self.recipient = recipient
        self.purpose = purpose
