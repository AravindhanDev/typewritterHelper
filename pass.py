""" 
Here, we created this for 
Typewrittersm, they can
do their calculation
with our product
 
In this
professional letter
Business letter
Government order
statements
are available"""



import math
total = 65
ltr_total = 60
class statement:
    def heading(self):
        self.head = input('enter heading: ')
        self.head = round((total - len(self.head))/2)
    
    def getdata(self):

        self.colhdsp1 = int(input('What\'s the length of largest string in a column? '))
        self.colhdsp2 = int(input('What\'s the length of largest string in a column? '))
        self.colhdsp3 = int(input('What\'s the length of largest string in a column? '))
        self.colhdsp4 = int(input('What\'s the length of largest string in a column? '))

        self.col1, self.col2, self.col3, self.col4 = self.colhdsp1+2, self.colhdsp2+2, self.colhdsp3+2, self.colhdsp4+1

    def colhdspc(self):

        print('\n')
        self.left_heading = int(input('What\'s about left heading? '))
        self.colhd1 = input('what\'s 1 column heading? ')
        self.colhd2 = input('what\'s 2 column heading? ')
        self.colhd3 = input('what\'s 3 column heading? ')
        self.colhd4 = input('what\'s 4 column heading? ')

        self.spc1 = (self.col1 - len(self.colhd1))/2
        self.spc2 = (self.col2 - len(self.colhd2))/2
        self.spc3 = (self.col3 - len(self.colhd3))/2
        self.spc4 = (self.col4 - len(self.colhd4))/2

    
    def putheading(self):
        print('The spacing for heading in statement: ', self.head)

    def total_space(self):
        self.right_total = self.col1+self.col2+self.col3+self.col4
        self.left_total = total - self.right_total
        print('Total spacing in right ',self.right_total)
        print('Total spacing in left ',self.left_total)
        print()
        print('left heading centre spacing: ', math.ceil((self.left_total - self.left_heading)/2))
        
    def display(self):
        print(self.colhd1,': ',math.ceil(self.spc1))
        print(self.colhd2,': ',math.ceil(self.spc2))
        print(self.colhd3,': ',math.ceil(self.spc3))
        print(self.colhd4,': ',math.ceil(self.spc4))


class business_letter:
    def company_info(self):
        self.companyName = input('Compnay name: ')
        self.companytype = input('What\'s about company type? ')
        self.companyName = round((ltr_total - len(self.companyName))/2)
        self.companytype = round((ltr_total - len(self.companytype))/2)

    def company_address(self):
        self.address = []

        for i in range(0, 4):

            self.ele = input('enter address ')

            self.address.append(self.ele)

        print(self.address)

        max_len = -1
        for i in self.address:
            if len(i) > max_len:
                max_len = len(i)
                self.largest = i


    def show_compInfo(self):
        print('The spacing for company name: ', self.companyName)
        print('The spacing for company type: ', self.companytype)

    def show_large(self):
        print('Maximum length address: ', self.largest)


class professional_letter:
    def professional_address(self):
        self.address = []

        for i in range(0, 4):

            self.ele = input('enter address ')

            self.address.append(self.ele)

        print(self.address)

        max_len = -1
        for i in self.address:
            if len(i) > max_len:
                max_len = len(i)
                self.largest = i

    def complement_signature(self):
        self.complement = input('What\'s the complement: ')
        self.signature = input('Signature (name with(caps)): ')

        self.spc_comp = len(self.complement)
        self.spc_sign = len(self.signature)

        self._center_sign = round((self.spc_comp - self.spc_sign)/2)


    def show_large(self):
        print('Maximum length address: ', self.largest)


    def show_verification(self):
        print('The spacing for signature : ', self._center_sign)



class government_order:
    def header_space(self):
        self.head1 = 'Government of Tamil Nadu'
        self.head2 = 'Abstract'

        self.headspc1 = round((ltr_total - len(self.head1))/2)
        self.headspc2 = round((ltr_total - len(self.head2))/2)

        self.deptName = input('enter the department ')
        self.dept_spc = round((ltr_total - len(self.deptName))/2)

        self.dated = input('enter the date ')
        self.date_spc = round(ltr_total - len(self.dated))

    def footer_space(self):
        self.foot1 = '(By order of the Governer)'
        self.foot_spc1 = round((ltr_total - len(self.foot1))/2)

        self.foot2 = 'Forwarded/By order'
        self.foot_spc2 = round((ltr_total - len(self.foot2))/2)

        self.foot3 = 'Section Officer.'
        self.foot_spc3 = round(ltr_total - len(self.foot3))

        self.sign_name = input('enter signature as name(In Caps) ')
        self.design = input('enter designation of person ')

        self.design_spc = ltr_total - len(self.design)
        self.sign_spc = self.design_spc + round((len(self.design) - len(self.sign_name))/2)


    def show_header(self):
        print('GOVERNMENT OF TAMIL NADU spacing : ', self.headspc1)
        print('Abstract spacing : ', self.headspc2)
        print(self.deptName,': ',self.dept_spc)
        print(self.dated,':', self.date_spc)


    def show_footer(self):
        print('By order of the Governer ', self.foot_spc1)
        print(self.sign_name,' ', self.sign_spc)
        print(self.design, self.design_spc)
        print('Forwarded/By order ', self.foot_spc2)
        print('Section Officer. ', self.foot_spc3)



class TypeWritting(statement, professional_letter, business_letter, government_order):

    print('|-----------------------------------------------------------|')
    print('|                                                           |')
    print('|         -->        Type Writter Helper         <--        |')
    print('|                                                           |')
    print('|-----------------------------------------------------------|')

    print()
    print('Press 1 For Professional letter')
    print('Press 2 For Business letter')
    print('Press 3 For Government Order')
    print('Press 4 For Statement')

    print()
    choice = int(input('In these what should you work? '))
    
    if choice == 1:
        try:
            print()
            print('-----@    WELCOME TO PROFESSION LETTER CALCULATION     @-----')
            print()
            p = professional_letter()
            p.professional_address()
            p.complement_signature()
            print()
            p.show_large()
            print()
            p.show_verification()
        
        except Exception as e:
            print()
            print('## Exception Occures ##')
            print(e)
            print('Some exception occurs, Surely it will Debugged soon... ')

        finally:
            print()

    elif choice == 2:
        try:
            print()
            print('-----@     WELCOME TO BUSINESS LETTER CALCULATION     @-----')
            print()
            b = business_letter()
            b.company_info()
            b.company_address()
            print()
            b.show_compInfo()
            print()
            b.show_large()
        
        except Exception as e:
            print()
            print('## Exception Occures ##')
            print(e)
            print('Some exception occurs, Surely it will Debugged soon... ')

        finally:
            print()

    elif choice == 3:
        print()
        try:
            print('-----@     WELCOME TO GOVERNMENT ORDER CALCULATION     @-----')
            print()
            g =government_order()
            g.header_space()
            g.footer_space()
            print()
            g.show_header()
            print()
            g.show_footer()
        
        except Exception as e:
            print()
            print('## Exception Occures ##')
            print(e)
            print('Some exception occurs, Surely it will Debugged soon... ')

        finally:
            print()


    elif choice == 4:
        print()
        try:
            print('-----@     WELCOME TO STATEMENT CALCULATION     @-----')
            print()
            s = statement()
            s.heading()
            s.getdata()
            s.colhdspc()
            print()
            print('--> Spacing is here for heading ')
            print()
            s.putheading()
            print()
            print('---> Spacing left (&) right for heading ')
            print()
            s.total_space()
            print()
            print('---> Spacing is here for column heading ')
            print()
            s.display()

        except Exception as e:
            print()
            print('## Exception Occures ##')
            print(e)
            print('Some exception occurs, Surely it will Debugged soon... ')

        finally:
            print()

    else:
        print('** There is no more So, kindly practice exist one **')






typewritting = TypeWritting()





#Documentation
""" 
In, this code
we used OOPs methods
like class and objects,
inheritance.

Exception handling is
also used to handle
unidentified
errors / exceptions

@override
method overriding is used

 """