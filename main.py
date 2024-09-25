import re

def main():

    def read_book(path):
        file_contents = ""

        with open(path) as f:
            file_contents = f.read()
        return file_contents

    def count_words(text):
        words = text.split()

        return len(words)
    
    def make_dict(text):
        dict = {}
        lowered_words = text.lower()
        char_array = lowered_words.split()

        for word in char_array:
            split_word = re.sub(r'[^a-z0-9]', '',  word)

            for c in split_word:
                if c.isalpha(): 
                    dict[c] = dict.get(c, 0) + 1

        return dict
    
    def split_dict(dict):
        value = []
        for key in dict.keys():
            sub = {"name": key, "num": dict[key]}

            value.append(sub)

        print(value) 
        return value

    def print_report(path):
        end = "--- End Report ---"
        begin = f"--- Begin Report of {path} ---"
        newline = '\n'

        text = read_book(path)
        count = count_words(text)
        countline = f"{count} words found in the document"

        dict = make_dict(text)
        dict_array = split_dict(dict)
        sorte = sorted(dict_array, key=lambda d: d["num"], reverse=True)
        report = [begin, countline, newline]
        
        for mini in sorte:
            name = mini["name"]
            times = mini["num"]
            record = f"The '{name}' character was found {times} times"
            report.append(record)


        report.append(end)

        for line in report:
            print(line)

    print_report("books/frankenstein.txt")


main()