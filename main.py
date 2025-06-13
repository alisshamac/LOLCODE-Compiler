#############################################################################################################
# References:
#       https://www.youtube.com/watch?v=Eythq9848Fg
#       https://www.tutorialspoint.com/lolcode/lolcode_syntax.htm
#       https://lokalise.com/blog/lolcode-tutorial-on-programming-language-for-cat-lovers/
#       https://github.com/elishaluzano/124-LOLCODE-Interpreter/blob/master/lexemes.literals.txt
#       https://stackoverflow.com/questions/27369675/inserting-to-a-textbox-with-tkinter
#       https://www.geeksforgeeks.org/working-of-lexical-analyzer-in-compiler/
#       https://stackoverflow.com/questions/27913310/how-to-get-the-content-of-a-tkinter-text-object
#       https://stackoverflow.com/questions/68860654/split-string-with-multiple-delimiters-and-keep-delimiters
#       https://stackoverflow.com/questions/10037742/replace-part-of-a-string-in-python
#       https://pythonguides.com/python-tkinter-treeview/
#       https://www.guru99.com/python-regular-expressions-complete-tutorial.html 
#       https://pythonbasics.org/try-except/      
#
#
############################################################################################################

import tkinter as tk
import re
from tkinter.messagebox import NO
from tkinter import CENTER, DISABLED, END, filedialog
from tkinter import ttk

# keyword phrases:
# 'I HAS A': 'variable statement', ok
# 'R MAEK': 'typecast keyword', ok
# 'BOTH SAEM' : 'comparison operator', ok
# 'IS NOW A': 'typecast keyword', ok
# 'O RLY?': 'conditional delimiter', #start
# 'YA RLY': 'conditional keyword', #if
# 'NO WAI': 'conditional keyword', #false
# 'IM IN YR': 'loop delimiter',  #start
# 'IM OUTTA YR': 'loop delimiter', #end

#single word keywords
keywords = {'HAI': 'code delimiter', 
           'KTHXBYE': 'code delimiter',
           'MKAY': 'argument keyword',
           'ITZ' : 'variable assignment',
           'DIFFRINT': 'comparison operator', 
           'SMOOSH': 'concatenation keyword', 
           'MAEK': 'typecast keyword',
           'VISIBLE': 'print keyword', 
           'GIMMEH': 'input keyword',
           'MEBBE': 'conditional keyword', #else-if
           'OIC': 'conditional and switch delimiter',  #end
           'WTF?': 'switch delimiter', 
           'OMG': 'switch condition keyword',
           'GTFO': 'exit case keyword',
           'OMGWTF': 'switch default keyword',
           'UPPIN': 'increment keyword', 
           'NERFIN': 'decrement keyword', 
           'YR': 'loop variable keyword', 
           'TIL': 'until loop keyword', 
           'WILE': 'while loop keyword',
           'SUM OF': 'math operator', 
           'DIFF OF': 'math operator', 
           'PRODUKT OF': 'math operator', 
           'QUOSHUNT OF': 'math operator', 
           'MOD OF': 'math operator', 
           'BOTH OF': 'boolean operator', 
           'EITHER OF': 'boolean operator', 
           'WON OF': 'boolean operator',
            'NOT': 'boolean operator', 
           'ANY OF': 'boolean operator', 
           'ALL OF': 'boolean operator',
           'BIGGR OF': 'comparison operator', 
           'SMALLR OF': 'comparison operator',
           'SUM': 'math operator', 
           'DIFF': 'math operator', 
           'PRODUKT': 'math operator', 
           'QUOSHUNT': 'math operator', 
           'MOD': 'math operator', 
           'BOTH': 'boolean operator', 
           'EITHER': 'boolean operator', 
           'WON': 'boolean operator',
           'ANY': 'boolean operator', 
           'ALL': 'boolean operator',
           'BIGGR': 'comparison operator', 
           'SMALLR': 'comparison operator',
            'AN': 'argument keyword',
           '\n': 'new line',
           'OBTW': 'long comment starter',
           'BTW': 'short comment', 
           'TLDR': 'long comment ender', 
}

operators = ['SUM', 'DIFF', 'PRODUKT', 'QUOSHUNT', 'MOD', 'BOTH', 'EITHER', 'WON', 'ANY', 'ALL', 'BIGGR','SMALLR']
literal = [r'"(.*?)"',"^-?\d\.\d+\s*",  "^-?\d+\s*","^WIN\s*|^FAIL\s*", "^TROOF\s*|^NOOB\s*|^YARN\s*|^NUMBR\s*|^NUMBAR\s*|^BUKKIT\s*","^[a-zA-Z][a-zA-Z\d_]*\s*", "^[+-=\*]\s*"]


###############################################################                LEXICAL ANALYZER                 ###############################################################

def lexicalAnalyzer(code):
    lexemes = []
    classifications = []
    
    identifiers = []
    values = []

    copy = code     #make copy to avoid editing the actual input code
    
    
    #evaluate by line
    copy = copy.replace("\t"," ") #remove tabs in code
    codeLines = re.split("(\n)", copy) #split by line
    codeLines = list(filter(None, codeLines))
    errorFound = False
    #evaluate per line
    for line in codeLines:
        #check for comments

        line = [p for p in re.split("( |\\\".*?\\\"|'.*?')", line) if p.replace(' ','')] #split at space but preserve substrings in quotes
        while len(line)>0 and errorFound == False:
            word = line[0]
            # print(line)
            #check if word in single keywords
            for key in keywords.keys():
                is_keyword = re.search(key, word)
                if is_keyword:
                    break

            for check in literal:
                is_literal = re.match(check, word)
                if is_literal:
                    break
            
            #check if word in keyword phrases, literals
            if word == 'I' and line[1] == 'HAS' and line[2] == 'A':
                lexemes.append('I HAS A')
                classifications.append('variable statement')
                line.pop(0)
                line.pop(0)

            elif word == 'R':
                #check if R MAEK
                if line[1] == 'MAEK':
                    lexemes.append('R MAEK')
                    classifications.append('typcast keyword')
                    line.pop(0)
                else:
                    lexemes.append('R')
                    classifications.append('variable assignment')


            elif word == 'BOTH' and line[1] == 'SAEM':
                lexemes.append('BOTH SAEM')
                classifications.append('comnparison operator')
                line.pop(0)


            elif word == 'IS' and line[1] == 'NOW' and line[2] == 'A':
                lexemes.append('IS NOW A')
                classifications.append('typecast keyword')
                line.pop(0)
                line.pop(0)

            elif word == 'O' and line[1] == 'RLY?':
                lexemes.append('O RLY?')
                classifications.append('conditional delimiter')
                line.pop(0)


            elif word == 'YA' and line[1] == 'RLY?':
                lexemes.append('YA RLY?')
                classifications.append('conditional delimiter')
                line.pop(0)


            elif word == 'NO' and line[1] == 'WAI':
                lexemes.append('NO WAI')
                classifications.append('conditional keyword')
                line.pop(0)


            elif word == 'IM' and line[1] == 'IN' and line[2] == 'YR':
                lexemes.append('IM IN YR')
                classifications.append('loop delimiter')
                line.pop(0)
                line.pop(0)

            elif word == 'IM' and line[1] == 'OUTTA' and line[2] == 'YR':
                lexemes.append('IM OUTTA YR')
                classifications.append('loop delimiter')
                line.pop(0)
                line.pop(0)


            elif is_keyword:
                    #check if math, boolean, or comparison operator
                    for op in operators:
                        within = re.search(op, word)
                        if within:
                            word = word + " OF"
                            line.pop(0) #remove "OF"
                            break
                    lexemes.append(word)
                    try:
                        classifications.append(keywords[word])
                    except:
                        errorFound = True
                        print("error at ", word)

            elif is_literal:
                if literal.index(check) == 0:
                    lexemes.append('"')
                    classifications.append('string delimiter')
                    lexemes.append(word.split('"')[1])
                    classifications.append('YARN literal')
                    lexemes.append('"')
                    classifications.append('string delimiter')
                elif literal.index(check) == 1:
                    lexemes.append(word)
                    classifications.append('NUMBAR literal')
                elif literal.index(check) == 2:
                    lexemes.append(word)
                    classifications.append('NUMBR literal')
                elif literal.index(check) == 3:
                    lexemes.append(word)
                    classifications.append('TROOF literal')
                elif literal.index(check) == 4:
                    lexemes.append(word)
                    classifications.append('type literal')
                elif literal.index(check) == 5:
                    if classifications[-1] == 'variable statement':
                        identifiers.append(word)
                        values.append('NONE')
                    lexemes.append(word)
                    classifications.append('identifier')
                    
                else:
                    lexemes.append(word)
                    classifications.append('math symbols')
            else:
                errorFound = True

                
            line.pop(0)
                        
                
                

                # print(lexemes[-1],classifications[-1])
    return lexemes, classifications, identifiers, values, errorFound

##############################################################                  EXECUTION                   ###############################################################
def ignoreComments(lexemes,classifications):
    #remove all comments
        for i,lex in enumerate(lexemes):
            if lex == 'BTW':
                while lexemes[i+1] != '\n':
                    lexemes.pop(i+1)
                    classifications.pop(i+1)
            elif lex == 'OBTW':
                while lexemes[i+1] != 'TLDR':
                    lexemes.pop(i+1)
                    classifications.pop(i+1)

        #remove comment keywords
        lexemes = [x for x in lexemes if x != 'BTW']
        lexemes = [x for x in lexemes if x != 'OBTW']
        lexemes = [x for x in lexemes if x != 'TLDR']
        classifications = [x for x in classifications if x != 'short comment delimiter']
        classifications = [x for x in classifications if x != 'long comment starter']
        classifications = [x for x in classifications if x != 'long comment ender']
        return lexemes

def variableAssignment(lexemes, classifications, identifiers, values, currentCount):
    #determine identifiers
    if classifications[currentCount] == 'identifier' and classifications[currentCount-1] == 'variable statement':
        print('1')
        identifiers.append(lexemes[currentCount])
        values.append('None')
    #assign value
    if classifications[currentCount] == 'ITZ':
        print("2")
        i = identifiers.index(lexemes[currentCount-1])
        values[i] = classifications[currentCount+1]


    return currentCount, identifiers, values
            

def printing(lexemes, classifications, identifiers, values, currentCount):
    content = ""
    if lexemes[currentCount] == 'VISIBLE':
        currentCount+=1 #skip VISIBLE
        while classifications[currentCount] != 'new line':
            if classifications[currentCount] == 'string delimiter':
                currentCount+=1
            else:
                if classifications[currentCount] == 'identifier':
                    #find value then content = content + value
                    i = identifiers.index(lexemes[currentCount])
                    content = content + values[i]
                else:
                    content = content + lexemes[currentCount]
                    currentCount+=1
        execContentBox.insert(tk.END, content+"\n") #inserts file content
    return currentCount


def semantics(lexemes, classifications, identifiers, values):
    currentCount = 1
    errorFound = False

    #ignore comments
    print("with comments\n ",lexemes)
    lexemes = ignoreComments(lexemes, classifications)
    print("\n\n without comments \n",lexemes)


    if lexemes[0] == 'HAI' and lexemes[-1] == 'KTHXBYE':  
        #traverse through lexemes and classifications
        while currentCount<(len(lexemes)) and errorFound == False:
            currentCount = printing(lexemes, classifications, identifiers, values, currentCount)
            currentCount+=1
    else:
        errorFound = True

    return errorFound, identifiers, values, lexemes, classifications
    
###############################################################                GUI FUNCTIONS                 ###############################################################
def openFile():
    fileName = filedialog.askopenfilename(filetypes=[("LOLCODE Files", "*.lol")], defaultextension=(".lol"))    # opens a file dialog box
    if fileName != "":  # if the user selected a file
        file = open(fileName, "r")  # opens the file to read
        inp = file.read()  # reads the file content
        fileNameBox.delete(1.0, END) #clears text box
        fileNameBox.insert(1.0, fileName.split('/')[-1]) #inserts file name only from path

        fileContentBox.delete(1.0, END) #clears content text box
        fileContentBox.insert(1.0, inp) #inserts file content
        file.close()    # closes the file
        

def executeCode():
    execContentBox.delete(1.0, END)
    for i in lexemeTree.get_children():
        lexemeTree.delete(i)
    
    for i in symbolTree.get_children():
        symbolTree.delete(i)
    code = fileContentBox.get(1.0, "end-1c")

    #get lexemes, classifications, and symbol table
    lexemes = []
    lexeme_classification = []
    identifiers = []
    values = []

    lexemes,lexeme_classification,identifiers, values, errorFound = lexicalAnalyzer(code)
    
    #show lexemes and classifications in table
    if errorFound == False:
        for i in range(0, len(lexemes)):
            lexemeTree.insert('', tk.END, values = (lexemes[i], lexeme_classification[i]))        
        if len(identifiers)>0:
            for i in range(0, len(identifiers)):
                symbolTree.insert('', tk.END, values = (identifiers[i], 0)) #0 placeholder for values
        #execute code in terminal
        errorFound, identifiers, values, lexemes, lexeme_classification = semantics(lexemes, lexeme_classification, identifiers, values)
   
        #display symbol table content
       

    if errorFound == True:
        execContentBox.delete(1.0, END) #clears content text box
        execContentBox.insert(1.0, "ERROR") #inserts file content


###############################################################              MAIN CODE              ###############################################################
root = tk.Tk()
root.title('Cardona LOLCODE')
root.resizable(False,False)
root.geometry('850x500')

style=ttk.Style()
style.theme_use('xpnative')

#File name and button
fileNameBox = tk.Text(root, height=1, width=28)
fileNameBox.place(x=10, y=10)
fileButton = tk.Button(root, text ='Open File', command = openFile)
fileButton.place(x=215, y=10)


#File content
fileContentBox = tk.Text(root, height=10, width=32, wrap = 'none')
fileCBar=ttk.Scrollbar(root, orient='horizontal', command=fileContentBox.xview)
fileCBar.place(x=10,y=205, width = 260)
fileContentBox.configure(xscrollcommand=fileCBar.set)
fileContentBox.place(x=10, y=40)


#lexeme table
lexemeTree=ttk.Treeview(root, column=('Lexeme','Classification'), show='headings', height=9)
lexemeTree.column('# 1',anchor=CENTER, stretch=NO, width=130)  
lexemeTree.heading('# 1', text='Lexeme')
lexemeTree.column('# 2',anchor=CENTER, stretch=NO, width=130)  
lexemeTree.heading('# 2', text='Classification')
vsb = ttk.Scrollbar(root, orient='vertical', command=lexemeTree.yview)
lexemeTree.configure(yscrollcommand=vsb.set)
vsb.place(x=280+260+5, y=28, height=190)
lexemeTree.place(x=280, y=10)
#Symbol table
symbolTree=ttk.Treeview(root, column=('Identifier','Value'), show='headings', height=9)  
symbolTree.column('# 1',anchor=CENTER, stretch=NO, width=130)  
symbolTree.heading('# 1', text='Identifier')
symbolTree.column('# 2',anchor=CENTER, stretch=NO, width=130)  
symbolTree.heading('# 2', text='Value')
vsb2 = ttk.Scrollbar(root, orient='vertical', command=symbolTree.yview)
symbolTree.configure(yscrollcommand=vsb2.set)
vsb2.place(x=560+260+5, y=28, height=190)
symbolTree.place(x=560, y=10)

execButton = tk.Button(root, text ='EXECUTE', width=117,command = executeCode)
execContentBox = tk.Text(root, height=14, width=103)

execButton.place(x=10, y=222)
execContentBox.place(x=10, y=250)


root.mainloop()

