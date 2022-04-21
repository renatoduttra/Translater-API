from   translate import Translator
import translate

idioma = Translator(from_lang="pt-br", to_lang="english")
traducao = idioma.translate(input(str("Digite o Texto: ")))
print(traducao)