class InitialClass:
    def __init__(self, attrib1, attrib2):
        # type: (string, string) -> None
        self.attrib1=attrib1
        self.attrib2=attrib2

    def attributes_str(self):
        # type: () -> String
        return "Attribs:",self.attrib1,self.attrib2