
import pickle


#menu method, asks the user which option they would like to pick and validates
def menu():
    choice=input('Enter your choice:\n1) Create letters from template\n2) List recipients\n3) Add recipient\n4) Delete recipient\n5) Import recipient list\n6) Export recipient list\n7) Quit\n')
    while choice!='1' and choice!='2' and choice!='3' and choice!='4' and choice!='5' and choice !='6' and choice!='7':
        choice=input('Please enter a valid option.')
    return choice

#general validation method for blank lines
def validate(s1):
    while s1=="":
        s1=input('Sorry, Invalid. Please re-enter:')
    return s1

#input_address that allows user to use additional lines to fill out full address
def input_address():
    add1=input('Address\n')
    add1=validate(add1)
    add2=input()
    while(add2!=""):
        add1=add1+"\n"+add2
        add2=input()
    return add1

#Recipient object, which contains shortname, fullname, and address variables. 
class Recipient:
    def __init__(self, shortname):
        self._shortname=shortname
        self.fullname=""
        self.address=""
    
    @property
    def shortname(self):
        return self._shortname
    #shortname=property(fget=_get_shortname, fset=None, fdel=None, doc=None)

    #substitute method to put variables into text, which is the letter template
    def substitute(self, text):
        x=text.replace('{shortname}', self._shortname)
        x=x.replace('{fullname}', self.fullname)
        x=x.replace('{address}', self.address)
        return x



def main():
    recList={}
    choice=0
    while choice!='7':
        choice=menu()

        #when user wants to add a recipient, option 3
        if choice=='3':
            sname=input('\nShort Name:')
            sname=validate(sname)
            while sname in recList:
                sname=input('Recipient exists. Please write another short name.')
            rec1=Recipient(sname)
            rec1.fullname=input('Full Name:')
            rec1.fullname=validate(rec1.fullname)
            rec1.address=input_address()
            recList[sname]=rec1

        #when user wants to export/import list
        if choice=='6':
            datExp=open("recipients.bin", "bw")
            pickle.dump(recList, datExp)
            datExp.close()
            print('\nRecipients exported to recipients.bin\n')
        if choice=='5':
            datExp=open("recipients.bin", "rb")
            recList=pickle.load(datExp)
            datExp.close()
            print("\nRecipients imported from recipients.bin\n")

        #when user wants to view list of recipients
        if choice=='2':
            print("\nRecipient List\n_____________\n")
            lisKeys=recList.keys()
            for x in lisKeys:
                print(x)
            print("_________________\n")

        #when user wants to delete a recipient
        if choice=='4':
            s1=input('\nName (blank to cancel)')
            if s1!="":
                while (s1 not in recList) and s1!="":
                    s1=input('That name is not in the list. Please enter a valid name or press enter to cancel.')
                if s1!="":
                    recList.pop(s1)
            print("\n")

        #when user wants to make letters
        if choice=='1':
            fname=input('\nTemplate filename:')

            #catch errors if the file isnt valid
            try:
                f=open(fname, "r")
            except:
                print("Could not open file for reading\n")
            else:
                text=f.read()
                l2=fname.split(".")
                lisKeys=recList.keys()
                for x in lisKeys:
                    obj=recList[x]
                    let1=obj.substitute(text)
                    newfname=l2[0]+"."+obj._shortname+".txt"
                    f2=open(newfname, "w")
                    f2.write(let1)
                    f2.close()
                f.close()
                print("Substitution completed\n")

            
    quit()


main()





