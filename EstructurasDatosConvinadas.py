
def find_similar_words(thesaurus):
    primary_word = input("What word would you like to find similar words for? ").lower() # el metodo lower() aca al final es para q de igual si el 
    if primary_word in thesaurus:                                                        # usuario escribe con mayusculas o no.      
        print("Here are some ideas: ")
        for word in thesaurus[primary_word]:
            print(f"  ", {word}) # segun gemini siempre es mejor usar f-strings
    else:
        print(f"I don\"t know that word!",  {primary_word}) # idem q arriba, siempre mejor f-strings.

thesaurus = {
    "strong" : {"mighty", "tough", "robust"},
    "small" : {"tiny", "little"},
    "fast" : {"speedy", "quick"},
    "calm" : {"mellow", "chill", "relaxed", "peacefull"}
}
find_similar_words(thesaurus)
# arregle todo con gemini y ambas funciones a pleno!

employees = [
  {'name':'Samantha Oxford', 'title':'Sr Attorney', 'salary':200000},
  {'name':'Jim Doyle', 'title': 'Jr Engineer', 'salary':85000, 'office':'Atlanta'},
  {'name':'Rebecca Jameson', 'title': 'Sales', 'commision': 2},
  {'name':'Stanley Reed'},
    ]
def lookup_employee(employees):
    
    name = input('Employee name: ')
    found = False
    for employee in employees:
        if 'name' in employee and name.lower() in employee['name'].lower():
                print(f"Information for {employee['name']}:")
                for key, value in employee.items():
                    print(f" {key} -> {value}")
                found = True
        if not found:
             print("Employee not found!")

lookup_employee(employees)