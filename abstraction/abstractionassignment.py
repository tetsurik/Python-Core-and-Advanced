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
        print("This shpit scrooooollsss")

class DELL(TouchScreenLaptop):

    def scroll(self):
        print("WOAH DUDELL this scroooooooll")

class HPNotebook(HP):

    def click(self):
        print("CLICK CLICK MOTHERFUCKERRR")

class DELLNotebook(DELL):

    def click(self):
        print("I LIKE THE WAY YOU CLICK")

h = HPNotebook()
d = DELLNotebook()

h.scroll()
h.click()

d.scroll()
d.click()