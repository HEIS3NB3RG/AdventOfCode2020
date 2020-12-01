from csv import reader
read_file = open('numbers')
str_data = list(read_file)
int_data = [int(x) for x in str_data]
number_1, number_2 = 0, 0
for i in range(len(int_data)):
    for j in range(i+1,len(int_data)):
        if int_data[i]+int_data[j] == 2020:
            number_1=int_data[i]
            number_2=int_data[j]
product = number_1 * number_2
print('the two entries that sum to 2020 are',number_1,number_2,'and the product of these numbers are:',product)
