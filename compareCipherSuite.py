import xlsxwriter

def main():
    ne_list = []
    while 1 :
        ciphersuite = input("NE cipher suite를 입력하세요 : ")
        
        if ciphersuite == 'q':
            print("입력 종료")
            break
        
        ne_list.append(ciphersuite)

    print(ne_list)

    wx_list = []
    while 1 :
        ciphersuite = input("WX cipher suite를 입력하세요 : ")
        
        if ciphersuite == 'q':
            print("입력 종료")
            break
        
        wx_list.append(ciphersuite)

    new_cipher = wx_list
    
    #wx와 ne를 비교해서 wx에 없는 값이 ne에 있으면 append
    for i in ne_list :
        if i not in wx_list :
            new_cipher.append(i)

    print("최종 값")
    print(tuple(new_cipher))

    insert_cipher = ( ['cipherlist'] ) + new_cipher

    workbook = xlsxwriter.Workbook('new_cipehrsuite.xlsx')
    worksheet = workbook.add_worksheet('sheet1')

    row = 0
    for cipherlist in insert_cipher:
        worksheet.write(row, 1, cipherlist)
        row += 1

    workbook.close()

if __name__ == "__main__":
    main()