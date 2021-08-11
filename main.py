from googletrans import Translator
import os.path


def convert(target_lang):
    translator = Translator()
    relative_path = os.path.abspath(os.path.dirname(__file__))
    fw = open(relative_path + '/files/translations/' + target_lang + '.properties', "w", encoding="utf-8")
    temp_key = [];
    temp_value = [];
    with open(relative_path + '/files/en.properties') as f:
        i = 1
        for line in f:
            if line.strip() != '':
                splited = line.split('=')
                try:
                    temp_value.append(splited[1].strip())
                    temp_key.append(splited[0].strip())
                except IndexError as re:
                    temp_value.append('')
                    temp_key.append(splited[0].strip())
            if (i % 50) == 0:
                call_string = ''
                for x in temp_value:
                    call_string = call_string + x + '\n'
                translated = translator.translate(call_string, target_lang)
                print(translated.text.split('\n'))
                for k, v in zip(temp_key, translated.text.split('\n')):
                    fw.write(k + '=' + v + '\n')
                temp_key = []
                temp_value = []
            i = i + 1

    call_string = ''
    for x in temp_value:
        call_string = call_string + x + '\n'
    translated = translator.translate(call_string, target_lang)

    for k, v in zip(temp_key, translated.text.split('\n')):
        fw.write(k + '=' + v + '\n')
    fw.close()


if __name__ == '__main__':
    convert('ja')
