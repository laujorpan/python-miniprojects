class InitialClass:
    def __init__(self, attrib1, attrib2):
        # type: (string, string) -> None
        self.attrib1=attrib1
        self.attrib2=attrib2

    def print_attributes(self):
        # type: () -> None
        print "Attribs:",self.attrib1,self.attrib2