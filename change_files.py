def insert_tag(path_to_file, tag_name, tag_id, line):
    #otvori, učitaj
    f = open(path_to_file, "r")

    sadrzaj = f.readlines()

    f.close()

    #napravi tekst:
    tekst = f"\n<{tag_name} id=\"{tag_id}\"> \n \n</{tag_name}>\n"
    sadrzaj.insert(line, tekst)

    #otvori, te zapamti promjene
    f = open(path_to_file, "w")

    sadrzaj = "".join(sadrzaj)  ##spoji sve linije, pa ih onda upiši
    f.write(sadrzaj)

    f.close()

def insert_attribute(path_to_file, tag_id, attribute_name, attribute_value):
    with open(path_to_file, 'a') as file:
        file.write(
            f"""
            \n            
if ("{attribute_name}".toLowerCase() == "klasa" && !document.getElementById("{tag_id}").classList.contains("{attribute_value}"))
    document.getElementById("{tag_id}").classList.add("{attribute_value}");
else if ("{attribute_name}".toLowerCase() != "class")
    document.getElementById("{tag_id}").setAttribute("{attribute_name}", "{attribute_value}"); 

if ("{attribute_value}" == "btn")
    document.getElementById("{tag_id}").classList.add("btn-primary");    
            \n         
            """.strip())

def insert_text(path_to_file, tag_id, text_to_insert):
    with open(path_to_file, 'a') as file:
        file.write(
            f"""
            \n
            document.getElementById("{tag_id}").innerText = "{text_to_insert}";
            \n
            """.strip())            





