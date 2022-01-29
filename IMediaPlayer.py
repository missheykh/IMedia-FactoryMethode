#using Factory Methode for playing a media from locale and online

from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Imedia(ABC):
    name:str
    location:str
    rating:int=3

    @abstractmethod
    def play():
        pass


class Imedia_Web(Imedia):
    def play(self):
        print(f"{self.name} is playing online from: {self.location}")


class Imedia_File(Imedia):
    def play(self):
        print(f"{self.name}is playing from {self.location} file")



class Imedia_Factory():
    @abstractmethod
    def create_imedia(self,name,location):
        pass

class  Web_Imedia_Factory_Concrete(Imedia_Factory):
    def create_imedia(self,name,location):
          Imedia_Web(name,location).play()
        


class File_Imedia_Factory_Concrete(Imedia_Factory):
    def create_imedia(self,name,location):
         Imedia_File(name,location).play()




#Test

media_obj_1=Web_Imedia_Factory_Concrete()
media_obj_1.create_imedia('baharan','https://mina.ir')

media_obj_2= File_Imedia_Factory_Concrete()
media_obj_2.create_imedia('javani','/usr/music')

