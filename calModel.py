import pandas as pd



def search_by_compostion(element_judge):
    df = pd.read_excel(r'data4.xls')
    st_name = []
    class_name_1 = []
    class_name_2 = []
    for n in range(len(df)):
        sum =0
        for element in element_judge:

            element_min = df.iloc[n][element+"_min"]
            element_max = df.iloc[n][element+"_max"]
            if (eval(element) >=element_min) and (eval(element) <= element_max):
                sum += 1
                        
            if sum == len(element_judge):
                st_name.append(df.iloc[n]['st_no'])
                class_name_1.append(df.iloc[n]['tag'])
                class_name_2.append(df.iloc[n]['2nd_tag'])
    result_dict={}
    result_dict["符合要求的钢种代码"]= st_name
    result_dict["对应的钢种代号01"] = class_name_1
    result_dict["对应的钢种代号02"] = class_name_2
    output = pd.DataFrame(result_dict)


    return output

def search_by_steelgrade(steelgrade):

    df = pd.read_excel(r'data4.xls')
    l = len(df['no'])
    names = df['st_no']

    for i in range(l):
        output = '未找到对应钢种！'
        if steelgrade == names[i]:
            element = [df['c_min'][i], df['c_max'][i], df['si_min'][i], df['si_max'][i], df['mn_min'][i], df['mn_max'][i], \
                   df['p_min'][i], df['p_max'][i], df['s_min'][i], df['s_max'][i], df['cu_min'][i], df['cu_max'][i], \
                   df['as_min'][i], df['as_max'][i], df['sn_min'][i], df['sn_max'][i], \
                   df['nb_min'][i], df['nb_max'][i], df['v_min'][i], df['v_max'][i], df['al_min'][i], df['al_max'][i], \
                   df['b_min'][i], \
                   df['b_max'][i], \
                   df['ni_min'][i], df['ni_max'][i], df['cr_min'][i], df['cr_max'][i], df['tag'][i], df['2nd_tag'][i]]

            output = 'C：' + str(element[0]) + "-" + str(element[1]) + '\tSi：' + str(element[2]) + "-" + str(
            element[3]) + '\n' \
                          'Mn:' + str(element[4]) + "-" + str(element[5]) + \
                 'P：' + str(element[6]) + "-" + str(element[7]) + '\tS：' + str(element[8]) + "-" + str(
            element[9]) + '\n' \
                          'Cu：' + str(element[10]) + "-" + str(element[11]) + '\n' \
                                                                              'As：' + str(element[12]) + "-" + str(
            element[13]) + '\tSn：' + str(element[14]) + "-" + str(element[15]) + \
                 '\tNb：' + str(element[16]) + "-" + str(element[17]) + '\n' \
                                                                       'V：' + str(element[18]) + "-" + str(
            element[19]) + '\t' + '\tAl：' + str(element[20]) + "-" + str(element[21]) + \
                 '\tB:' + str(element[22]) + "-" + str(element[23]) + '\n' \
                                                                      'Ni:' + str(element[24]) + "-" + str(
            element[25]) + '\tCr' + str(element[26]) + "-" + str(element[27]) + \
                 '\t钢种分组结果：' + str(element[28]) + \
                 str(element[29])
        break

    return output







if __name__ == "__main__":
    composition_dict = {'c': 0.6, 'si': 0, 'mn': 0, 'p': 0, 's': 0, 'cu': 0, 'ass': 0, 'sn': 0, 'nb': 0, 'v': 0,
                        'al': 0, 'b': 0, 'ni': 0, 'cr': 0}

    steelgrade = 'a1111'

    output1 = search_by_compostion(composition_dict)
    output2 = search_by_steelgrade(steelgrade)

    print(output1)
    print(output2)
