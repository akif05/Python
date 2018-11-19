def sort_by_last_letter(strings):
    def last_letter(s):
        return s[0]

    return sorted(strings, key=last_letter)

strings = ['akif', 'nigyar', 'izet']
print(sort_by_last_letter(strings))
