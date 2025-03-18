from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    @abstractmethod
    def jenis (Self):
        pass
    @abstractmethod
    def nama(self):
        pass
class Kucing(Hewan):
    def nama (Self):
        return Self.nama
    def jenis(Self):
        return Self.jenis
    def __str__(self):
        return f"nama = {self.nama}jenis = {self.jenis}"
kucing1 = Kucing("mimi","anggora")
print (kucing1)