import pandas as pd 

df = pd.read_csv('D:\Python\Ex Python\Lab6\sales_data.csv')
'''
#1
#Xuất thông tin kiểu dữ liệu của các cột
print(df.info())

#Kiểm tra các hàng có chứa giá trị null hay không 
df = df.isna()
print(df)
'''

'''
#2 Xuất tất cả thông tin của file
print(df)
'''

'''
#3 Xuất hàng dữ liệu của tháng có lợi nhuận cao nhất
df = df[df.total_profit == df['total_profit'].max()]
df = df[df.columns]
print(df)
'''

'''
#4 Xuất hàng dữ liệu của tháng bán nhiều kem đánh răng nhất
df = df[df.toothpaste == df['toothpaste'].max()]
df = df[df.columns]
print(df)
'''

'''
#5 Xuất hàng dữ liệu của tháng bán nhiều mặt hàng nhất
df['total_product']  = df[['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']].sum(axis=1)
df = df[df.total_product == df['total_product'].max()]
df = df[df.columns]
print(df)
'''

'''
#6 Cho biết tổng lợi nhuận cả năm
df = df['total_profit'].sum()
print('Tổng lợi nhuận cả năm: ',df)
'''

'''
#7 Cho biết tổng số lượng mặt hàng bán theo từng mặt hàng 
df = df[['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']].sum()
print(df)
'''

'''
#8 Hiển thị số lượng mặt hàng bán trong tháng 2 
df = df.groupby('month_number')[['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']].sum().loc()[2]
print(df.loc[2])
'''

'''
#9 Số lượng mặt hàng bán chạy nhất tháng 2
df = df.groupby('month_number')[['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']].sum().loc()[2].max()
print('Số lượng mặt hàng bán chạy nhất tháng 2: ',df)
'''


#10Tìm mặt hàng bán chạy nhất trong năm
df = df[['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']].sum()
df = df.idxmax()
print('Mặt hàng bán chạy nhất năm: ',df)
