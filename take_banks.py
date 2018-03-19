#The func which build dict with banks

def take_banks(array_vklads, array_cont):
    banks_array = []

    banks_names = get_banks_names(array_vklads)
    for name in banks_names:
        bank = Bank(name)
        banks_array.append(bank)

    for dict in array_vklads:
        for key in dict.keys():
            if key == 'bank':
                id = banks_names.index(dict[key])
                banks_array[id].len_vklads += 1


    for dict in array_cont:
        for key in dict.keys():
            if key == 'bank':
                id = banks_names.index(dict[key])
                banks_array[id].len_kred += 1
    array = []
    for bank in banks_array:
        dict = {
            'bank': bank.bank,
            'len_cred': str(bank.len_kred),
            'len_vklads': str(bank.len_vklads)
        }
        array.append(dict)


    return array






def get_banks_names(array):
    names = []
    for dict in array:
        for value in dict.values():
            if dict['bank'] not in names:
                names.append(dict['bank'])
    return names

class Bank():
    def __init__(self, bank):
        self.bank = bank
        self.len_kred = 0
        self.len_vklads = 0
