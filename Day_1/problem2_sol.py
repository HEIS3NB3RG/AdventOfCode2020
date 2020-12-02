from csv import reader
read_file = open('numbers')
str_data = list(read_file)
int_data = [int(x) for x in str_data]
number_1, number_2,number_3 = 0, 0, 0
for i in range(len(int_data)):
    for j in range(i+1,len(int_data)):
        for z in range(j+1,len(int_data)):
            if int_data[i]+int_data[j]+int_data[z] == 2020:
                number_1=int_data[i]
                number_2=int_data[j]
                number_3=int_data[z]
product = number_1 * number_2 * number_3
print('the three entries that sum to 2020 are',number_1,number_2,number_3,'and the product of these numbers are:',product)