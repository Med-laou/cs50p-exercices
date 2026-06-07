def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

text = input("Veuillez saisir un texte : ")
print(convert(text))