# import openpyxl and tkinter modules
from openpyxl import *
from tkinter import *

# globally declare wb and sheet variable

# opening the existing excel file
#wb = load_workbook('D:\python\Lab4\Bai6.xlsx')

# create the sheet object
#sheet = wb.active

#def excel():
	
	# resize the width of columns in
	# excel spreadsheet
	#

	# write given data to an excel spreadsheet
	# at particular location
	#



def focus0(event):
	# set focus on the course_field box
	mssv_field.focus_set()
# Function to set focus (cursor)
def focus1(event):
	# set focus on the course_field box
	ho_ten_field.focus_set()


# Function to set focus
def focus2(event):
	# set focus on the sem_field box
	ngay_Sinh_field.focus_set()


# Function to set focus
def focus3(event):
	# set focus on the form_no_field box
	ngay_Sinh_field.focus_set()


# Function to set focus
def focus4(event):
	# set focus on the contact_no_field box
	So_DT_field.focus_set()


# Function to set focus
def focus5(event):
	# set focus on the email_id_field box
	email_id_field.focus_set()


# Function to set focus
def focus6(event):
	# set focus on the address_field box
	address_field.focus_set()


# Function for clearing the
# contents of text entry boxes
def clear():
	
	# clear the content of text entry box
	mssv_field.delete(0, END)
	ho_ten_field.delete(0, END)
	ngay_Sinh_field.delete(0, END)
	ngay_Sinh_field.delete(0, END)
	So_DT_field.delete(0, END)
	email_id_field.delete(0, END)
	address_field.delete(0, END)

	


# Function to take data from GUI
# window and write to an excel file
def insert():
	
	# if user not fill any entry
	# then print "empty input"
	if (mssv_field.get() == "" and
		ho_ten_field.get() == "" and
		ngay_Sinh_field.get() == "" and
		ngay_Sinh_field.get() == "" and
		So_DT_field.get() == "" and
		email_id_field.get() == "" and
		address_field.get() == ""):
			
		print("empty input")

	

		# save the file
		#wb.save('E:\python\Lab4\Bai6.xlsx')

		# set focus on the name_field box
		#name_field.focus_set()

		# call the clear() function
	clear()


# Driver code
if __name__ == "__main__":
	
	# create a GUI window
	root = Tk()

	# set the background colour of GUI window
	root.configure(background='light green')

	# set the title of GUI window
	root.title("Đăng kí học phần")

	# set the configuration of GUI window
	root.geometry("500x300")

	#excel()

	# create a Form label
	heading = Label(root, text="THÔNG TIN ĐĂNG KÍ HỌC PHẦN", bg="aqua")

	# create a Name label
	mssv = Label(root, text="Mã số sinh viên", bg="light green")

	# create a Course label
	ho_ten = Label(root, text="Họ tên", bg="light green")

	# create a Semester label
	ngay_Sinh = Label(root, text="Ngày sinh", bg="light green")

	# create a Form No. label
	email = Label(root, text="Email", bg="light green")

	# create a Contact No. label
	So_DT = Label(root, text="Số điện thoại", bg="light green")

	# create a Email id label
	email_id = Label(root, text="Học kỳ", bg="light green")

	# create a address label
	address = Label(root, text="Năm học", bg="light green")
	# create an Exit Button and place it into the root window
	exit_button = Button(root, text="Thoát", fg="Black", bg="Yellow", command=root.quit)
	exit_button.grid(row=13, column=1)


	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	heading.grid(row=0, column=1)
	mssv.grid(row=1, column=0,sticky="w")
	ho_ten.grid(row=2, column=0,sticky="w")
	ngay_Sinh.grid(row=3, column=0,sticky="w")
	email.grid(row=4, column=0,sticky="w")
	So_DT.grid(row=5, column=0,sticky="w")
	email_id.grid(row=6, column=0,sticky="w")
	address.grid(row=7, column=0,sticky="w")

	# create a text entry box
	# for typing the information
	mssv_field = Entry(root)
	ho_ten_field = Entry(root)
	ngay_Sinh_field = Entry(root)
	email_field = Entry(root)
	So_DT_field = Entry(root)
	email_id_field = Entry(root)
	address_field = Entry(root)

	# bind method of widget is used for
	# the binding the function with the events

	
	# whenever the enter key is pressed
	# then call the focus1 function
	mssv_field.bind("<Return>", focus1)

	# whenever the enter key is pressed
	# then call the focus2 function
	ho_ten_field.bind("<Return>", focus2)

	# whenever the enter key is pressed
	# then call the focus3 function
	ngay_Sinh_field.bind("<Return>", focus3)

	# whenever the enter key is pressed
	# then call the focus4 function
	email_field.bind("<Return>", focus4)

	# whenever the enter key is pressed
	# then call the focus5 function
	So_DT_field.bind("<Return>", focus5)

	# whenever the enter key is pressed
	# then call the focus6 function
	email_id_field.bind("<Return>", focus6)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	mssv_field.grid(row=1, column=1, ipadx="100")
	ho_ten_field.grid(row=2, column=1, ipadx="100")
	ngay_Sinh_field.grid(row=3, column=1, ipadx="100")
	email_field.grid(row=4, column=1, ipadx="100")
	So_DT_field.grid(row=5, column=1, ipadx="100")
	email_id_field.grid(row=6, column=1, ipadx="100")
	address_field.grid(row=7, column=1, ipadx="100")

	# call excel function
	#excel()
	# create a Label for selecting programming language
	programming_label = Label(root, text="Chọn môn học", bg="light green")
	programming_label.grid(row=8, column=0)

	# create a variable to store the selected programming language
	selected_language = StringVar()

	# create Radiobuttons for selecting programming language
	language1 = Radiobutton(root, text="Lập trình Python", variable=selected_language,value="Python", bg="light green")
	language2 = Radiobutton(root, text="Lập trình Java", variable=selected_language,value="Java", bg="light green")
	language3 = Radiobutton(root, text="Công nghệ phần mềm", variable=selected_language,value="Phan mem", bg="light green")
	language4 = Radiobutton(root, text="Phát triển ứng dựng web", variable=selected_language,value="ung dung web", bg="light green")

	

	# grid the Radiobuttons
	language1.grid(row=10, column=0,sticky="w")
	language2.grid(row=10, column=1,sticky="w")
	language3.grid(row=11, column=0,sticky="w")
	language4.grid(row=11, column=1,sticky="w")
	# create a Submit Button and place into the root window
	submit = Checkbutton(root, text="Đăng kí", fg="Black",
							bg="Red", command=insert)
	submit.grid(row=13, column=0)


	# start the GUI
	root.mainloop()
