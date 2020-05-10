from abc import abstractmethod, ABC

class TouchScreenLaptop(ABC):

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):

    def scroll(self):
        print("This HP scrolls")

class DELL(TouchScreenLaptop):

    def scroll(self):
        print("This DELL scrolls")

class HPNotebook(HP):

    def click(self):
        print("This HP clicks")

class DELLNotebook(DELL):

    def click(self):
        print("This DELL clicks")

h = HPNotebook()
d = DELLNotebook()

h.scroll()
h.click()

d.scroll()
d.click()
