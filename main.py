from translate import Translator
import os.path


def convert(target_lang):
    translator = Translator(to_lang=target_lang)
    relative_path = os.path.abspath(os.path.dirname(__file__))
    fw = open(relative_path + '/files/translations/' + target_lang + '.properties', "w")
    with open(relative_path + '/files/en.properties') as f:
        for line in f:
            splited = line.split('=')
            converted = splited[0] + "=" + translator.translate(splited[1])
            print(converted)
            fw.write(converted + "\n")
    fw.close()


if __name__ == '__main__':
    convert('hi')
