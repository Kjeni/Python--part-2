list = ["burak", "cukinia","pomidor","cytryna","ananas","papryka","dynia"]
letter= input("Wybierz swoją literkę: ")
for element in list:
    if element.startswith(letter):
        print(element, end=" ")