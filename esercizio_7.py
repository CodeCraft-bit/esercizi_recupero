class ContactManager:
    
    def __init__(self, contacts: dict[str, list[str]]) -> None:
        self.contacts = contacts

    def create_contact(self,name: str, phone_number: list[str]) -> dict[str, list[str]]:
        nuovo_dizionario: dict[str, list[str]] = {}
        
        if name in self.contacts:
            print("Errore: il contatto esiste già.")
        else:
            self.contacts[name] = [phone_number]
            nuovo_dizionario[name] = [phone_number]
            return nuovo_dizionario
        
    def add_phone_number(self, contact_name: str, phone_number: str) -> dict[str, str]:
        nuovo_dizionario: dict = {}
        
        if contact_name in self.contacts:
            if phone_number in self.contacts[contact_name]:
                print("Errore: il numero di telefono esiste già")
            else:
                self.contacts[contact_name].append(phone_number)
                nuovo_dizionario[contact_name] = [phone_number]
                return nuovo_dizionario
        else:
            print("Errore: il contatto non esiste.")

    def remove_phone(self, contact_name: str, phone_number: str) -> dict[str, str]:
        nuovo_dizionario: dict = {}
        if contact_name in self.contacts:
            if phone_number not in self.contacts[contact_name]:
                print("Errore: il numero di telefono esiste già.")
            else:
                self.contacts[contact_name].remove(phone_number)
                nuovo_dizionario[contact_name] = [phone_number]
                return nuovo_dizionario
        else:
            print("Errore: il contatto non esiste")

    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str) -> dict[str, str]:
        nuovo_dizionario: dict = {}
        if contact_name in self.contacts:
            if old_phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(old_phone_number)
                self.contacts[contact_name].append(new_phone_number)
                nuovo_dizionario[contact_name] = [new_phone_number]
                return nuovo_dizionario
            else:
                print("Errore: il numero di telefono non è presente.")

        else:
            print("Errore: il contatto non esiste.")

    def list_contacts(self) -> list:
        return list(self.contacts.keys())
    
    def list_phone_number(self,contact_name: str) -> str:
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste."
        else:
            return self.contacts[contact_name]
        
    def search_contact_by_phone_number(self, phone_number: str) -> list[str]:
        if phone_number not in self.contacts:
            return "Nessun contatto trovato con questo numero di telefono"
        else:
            return self.contacts.keys()

            


        