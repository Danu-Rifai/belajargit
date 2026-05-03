owner = {'O1': {'nama': 'bani',
                'usia': 19,
                'alamt': 'wonosobo'}}

while True:

    print(f'''
pilihan:
1. Update
2. Cetak data
''')
    
    input_pilihan = input("masukan pilihan: ")
    
    if input_pilihan == '1':
        data_target = input('data target: ')
        input_update = input('masukan update: ')

        def update_data(data_target, data_baru):
            owner[data_target]['nama'] = input_update

        update_data(data_target, input_update)

    elif input_pilihan == "2":
        print(owner['O1']['nama'])