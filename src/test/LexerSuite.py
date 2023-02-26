import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lexer1(self):
        """"""
        testcase = """main: function void () {}"""
        expect = """main,:,function,void,(,),{,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 101))

    def test_lexer2(self):
        """"""
        testcase = """str:string="Hello World!"""
        expect = """str,:,string,=,Unclosed String: Hello World!"""
        self.assertTrue(TestLexer.test(testcase, expect, 102))

    def test_lexer3(self):
        """"""
        testcase = """str:string="Hello \\n\\tWorld!";"""
        expect = """str,:,string,=,Hello \\n\\tWorld!,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 103))

    def test_lexer4(self):
        """"""
        testcase = """str:string="Hello \\aWorld!";"""
        expect = """str,:,string,=,Illegal Escape In String: Hello \\a"""
        self.assertTrue(TestLexer.test(testcase, expect, 104))

    def test_lexer5(self):
        """"""
        testcase = """str:string="Hello \nWorld!";"""
        expect = """str,:,string,=,Unclosed String: Hello """
        self.assertTrue(TestLexer.test(testcase, expect, 105))

    def test_lexer6(self):
        """"""
        testcase = """abjkabv gega ghei giaw3y gue ve"""
        expect = """abjkabv,gega,ghei,giaw3y,gue,ve,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 106))

    def test_lexer7(self):
        """"""
        testcase = """1.12e+2 3.14e-312 12e8 1. 0.33E-3 123_5e10 6_3 1_0.12E-12 1_1_0.12e-10"""
        expect = """1.12e+2,3.14e-312,12e8,1.,0.33E-3,1235e10,63,10.12E-12,110.12e-10,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 107))

    def test_lexer8(self):
        """"""
        testcase = """/*this is block comt*/"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 108))

    def test_lexer9(self):
        """"""
        testcase = """            /* This is a block cmt */
                /* This is a block cmt */"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 109))

    def test_lexer10(self):
        """"""
        testcase = """/* This is /*a block*/ cmt */"""
        expect = """cmt,*,/,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 110))

    def test_lexer11(self):
        """"""
        testcase = """// this is a line comment a=5;"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 111))

    def test_lexer12(self):
        """"""
        testcase = """a = 5; //this is a line comment"""
        expect = """a,=,5,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 112))

    def test_lexer13(self):
        """"""
        testcase = """/* ksannaannonae
    ibdfiiaeini"""
        expect = """/,*,ksannaannonae,ibdfiiaeini,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 113))

    def test_lexer14(self):
        """"""
        testcase = """127 0 4_3_2_1 112_000 12_0 43512_1 -51_0 +12_59_0_19219 0_12_34_5"""
        expect = """127,0,4321,112000,120,435121,-,510,+,1259019219,0,_12_34_5,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 114))

    def test_lexer15(self):
        """"""
        testcase = """a:float;"""
        expect = """a,:,float,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 115))

    def test_lexer16(self):
        """"""
        testcase = """a:float=1;"""
        expect = """a,:,float,=,1,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 116))

    def test_lexer17(self):
        """"""
        testcase = """a,b:float=1,2;"""
        expect = """a,,,b,:,float,=,1,,,2,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 117))

    def test_lexer18(self):
        """"""
        testcase = """a, b, c, d: integer = 3, 4, 6;"""
        expect = """a,,,b,,,c,,,d,:,integer,=,3,,,4,,,6,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 118))

    def test_lexer19(self):
        """"""
        testcase = """main: function void() {}"""
        expect = """main,:,function,void,(,),{,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 119))

    def test_lexer20(self):
        """"""
        testcase = """abc: function integer() {a = 1;}"""
        expect = """abc,:,function,integer,(,),{,a,=,1,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 120))

    def test_lexer21(self):
        """"""
        testcase = """abc: function integer() {{}}"""
        expect = """abc,:,function,integer,(,),{,{,},},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 121))

    def test_lexer22(self):
        """"""
        testcase = """abc: function integer() {abc();}"""
        expect = """abc,:,function,integer,(,),{,abc,(,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 122))

    def test_lexer23(self):
        """"""
        testcase = """abc: function integer() {a=1;
            b=1;
            return 0;}"""
        expect = """abc,:,function,integer,(,),{,a,=,1,;,b,=,1,;,return,0,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 123))

    def test_lexer24(self):
        """"""
        testcase = """a,b:float;"""
        expect = """a,,,b,:,float,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 124))

    def test_lexer25(self):
        """"""
        testcase = """a,b:float=1,2"""
        expect = """a,,,b,:,float,=,1,,,2,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 125))

    def test_lexer26(self):
        """"""
        testcase = """a,b float=1,2;"""
        expect = """a,,,b,float,=,1,,,2,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 126))

    def test_lexer27(self):
        """"""
        testcase = """:float=1;"""
        expect = """:,float,=,1,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 127))

    def test_lexer28(self):
        """"""
        testcase = """a:float=;"""
        expect = """a,:,float,=,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 128))

    def test_lexer29(self):
        """"""
        testcase = """a:float 1;"""
        expect = """a,:,float,1,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 129))

    def test_lexer30(self):
        """"""
        testcase = """a:1;"""
        expect = """a,:,1,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 130))

    def test_lexer31(self):
        """"""
        testcase = """//abc: functionwshjfuiovhsiuod void(){}"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 131))

    def test_lexer32(self):
        """"""
        testcase = """a:float;
            abc:function void(){}
            //end
            b:integer;"""
        expect = """a,:,float,;,abc,:,function,void,(,),{,},b,:,integer,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 132))

    def test_lexer33(self):
        """"""
        testcase = """/*@@@@@@@@@@@@@*/
    a:integer=1+a;"""
        expect = """a,:,integer,=,1,+,a,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 133))

    def test_lexer34(self):
        """"""
        testcase = """///////////////////
            a:integer;"""
        expect = """a,:,integer,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 134))

    def test_lexer35(self):
        """"""
        testcase = """main: function void () {a= "abc"::"xyz";}"""
        expect = """main,:,function,void,(,),{,a,=,abc,::,xyz,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 135))

    def test_lexer36(self):
        """"""
        testcase = """main: function void() {
        printString("abc")
    }"""
        expect = """main,:,function,void,(,),{,printString,(,abc,),},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 136))

    def test_lexer37(self):
        """"""
        testcase = """main: function void () {a= "abc";}"""
        expect = """main,:,function,void,(,),{,a,=,abc,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 137))

    def test_lexer38(self):
        """"""
        testcase = """a,b,c:string= "abc","a","""""
        expect = """a,,,b,,,c,:,string,=,abc,,,a,,,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 138))

    def test_lexer39(self):
        """"""
        testcase = """a,b,c:string= "a","a" ;"""
        expect = """a,,,b,,,c,:,string,=,a,,,a,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 139))

    def test_lexer40(self):
        """"""
        testcase = """isEven: function boolean(a:integer){if(a%2==0) return true; else return false;}"""
        expect = """isEven,:,function,boolean,(,a,:,integer,),{,if,(,a,%,2,==,0,),return,true,;,else,return,false,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 140))

    def test_lexer41(self):
        """"""
        testcase = """main: function void () {a=readInteger(); printInteger(a);}"""
        expect = """main,:,function,void,(,),{,a,=,readInteger,(,),;,printInteger,(,a,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 141))

    def test_lexer42(self):
        """"""
        testcase = """main: function void () {n=readFloat(); printFloat(n);}"""
        expect = """main,:,function,void,(,),{,n,=,readFloat,(,),;,printFloat,(,n,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 142))

    def test_lexer43(self):
        """"""
        testcase = """main: function void () {str=readString(); printString(str);}"""
        expect = """main,:,function,void,(,),{,str,=,readString,(,),;,printString,(,str,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 143))

    def test_lexer44(self):
        """"""
        testcase = """arr: array[5,5] of integer;"""
        expect = """arr,:,array,[,5,,,5,],of,integer,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 144))

    def test_lexer45(self):
        """"""
        testcase = """arr: array[10] of integer;"""
        expect = """arr,:,array,[,10,],of,integer,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 145))

    def test_lexer46(self):
        """"""
        testcase = """arr: array[5] of integer={1,2,3,4,5};"""
        expect = """arr,:,array,[,5,],of,integer,=,{,1,,,2,,,3,,,4,,,5,},;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 146))

    def test_lexer47(self):
        """"""
        testcase = """arr: array[5,5] of integer={{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15},{16,17,18,19,20},{21,22,23,24,25}};"""
        expect = """arr,:,array,[,5,,,5,],of,integer,=,{,{,1,,,2,,,3,,,4,,,5,},,,{,6,,,7,,,8,,,9,,,10,},,,{,11,,,12,,,13,,,14,,,15,},,,{,16,,,17,,,18,,,19,,,20,},,,{,21,,,22,,,23,,,24,,,25,},},;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 147))

    def test_lexer48(self):
        """"""
        testcase = """main: function void () {printInteger(10+11);}"""
        expect = """main,:,function,void,(,),{,printInteger,(,10,+,11,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 148))

    def test_lexer49(self):
        """"""
        testcase = """main: function void () {printFloat(2e-7+3e-1);}"""
        expect = """main,:,function,void,(,),{,printFloat,(,2e-7,+,3e-1,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 149))

    def test_lexer50(self):
        """"""
        testcase = """main: function void () {printBoolean(var_a && var_b || var_c);}"""
        expect = """main,:,function,void,(,),{,printBoolean,(,var_a,&&,var_b,||,var_c,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 150))

    def test_lexer51(self):
        """"""
        testcase = """main: function void () {value=true && false || true;}"""
        expect = """main,:,function,void,(,),{,value,=,true,&&,false,||,true,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 151))

    def test_lexer52(self):
        """"""
        testcase = """main: function void () {super("name",age);}"""
        expect = """main,:,function,void,(,),{,super,(,name,,,age,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 152))

    def test_lexer53(self):
        """"""
        testcase = """main: function void () {preventDefault();}"""
        expect = """main,:,function,void,(,),{,preventDefault,(,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 153))

    def test_lexer54(self):
        """"""
        testcase = """main: function void () {r=readFloat(); pi=3.14; C=2*r*pi; writeFloat(C);}"""
        expect = """main,:,function,void,(,),{,r,=,readFloat,(,),;,pi,=,3.14,;,C,=,2,*,r,*,pi,;,writeFloat,(,C,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 154))

    def test_lexer55(self):
        """"""
        testcase = """main: function void () {abs(100-560-741);}"""
        expect = """main,:,function,void,(,),{,abs,(,100,-,560,-,741,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 155))

    def test_lexer56(self):
        """"""
        testcase = """main: function void () {fibonacci(5);}"""
        expect = """main,:,function,void,(,),{,fibonacci,(,5,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 156))

    def test_lexer57(self):
        """"""
        testcase = """main: function void () {stringConverter(120.485);}"""
        expect = """main,:,function,void,(,),{,stringConverter,(,120.485,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 157))

    def test_lexer58(self):
        """"""
        testcase = """main: function void () {printString("Hello World!");}"""
        expect = """main,:,function,void,(,),{,printString,(,Hello World!,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 158))

    def test_lexer59(self):
        """"""
        testcase = """str:string="Hello \\nWorld!";"""
        expect = """str,:,string,=,Hello \\nWorld!,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 159))

    def test_lexer60(self):
        """"""
        testcase = """str:string="Hello World!"""
        expect = """str,:,string,=,Unclosed String: Hello World!"""
        self.assertTrue(TestLexer.test(testcase, expect, 160))

    def test_lexer61(self):
        """"""
        testcase = """a:integer=5+6-(123*10+(24-30));"""
        expect = """a,:,integer,=,5,+,6,-,(,123,*,10,+,(,24,-,30,),),;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 161))

    def test_lexer62(self):
        """"""
        testcase = """a,b,c:intger=2,3;"""
        expect = """a,,,b,,,c,:,intger,=,2,,,3,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 162))

    def test_lexer63(self):
        """"""
        testcase = """main: function void () {printInteger(arr[0,1]);}"""
        expect = """main,:,function,void,(,),{,printInteger,(,arr,[,0,,,1,],),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 163))

    def test_lexer64(self):
        """"""
        testcase = """main: function void () {arr[3]=3.14;}"""
        expect = """main,:,function,void,(,),{,arr,[,3,],=,3.14,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 164))

    def test_lexer65(self):
        """"""
        testcase = """main: function void () {a:integer=readInteger(); if(a!=0) printString("Non-zero"); else printString("Zero!!!");}"""
        expect = """main,:,function,void,(,),{,a,:,integer,=,readInteger,(,),;,if,(,a,!=,0,),printString,(,Non-zero,),;,else,printString,(,Zero!!!,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 165))

    def test_lexer66(self):
        """"""
        testcase = """print: function void(){printString("Empty function!");}"""
        expect = """print,:,function,void,(,),{,printString,(,Empty function!,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 166))

    def test_lexer67(self):
        """"""
        testcase = """main: function void () {printBoolean(2>3);}"""
        expect = """main,:,function,void,(,),{,printBoolean,(,2,>,3,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 167))

    def test_lexer68(self):
        """"""
        testcase = """main: function void () {str="abc"::"def"::("ghi"::"jkl");}"""
        expect = """main,:,function,void,(,),{,str,=,abc,::,def,::,(,ghi,::,jkl,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 168))

    def test_lexer69(self):
        """"""
        testcase = """foo:function int(){return 0;}"""
        expect = """foo,:,function,int,(,),{,return,0,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 169))

    def test_lexer70(self):
        """"""
        testcase = """foo:function float(){return 0.001;}"""
        expect = """foo,:,function,float,(,),{,return,0.001,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 170))

    def test_lexer71(self):
        """"""
        testcase = """foo:function string(){return "zero";}"""
        expect = """foo,:,function,string,(,),{,return,zero,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 171))

    def test_lexer72(self):
        """"""
        testcase = """main: function void () {printBoolean(!!false);}"""
        expect = """main,:,function,void,(,),{,printBoolean,(,!,!,false,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 172))

    def test_lexer73(self):
        """"""
        testcase = """main: function void () {printInteger(---3);}"""
        expect = """main,:,function,void,(,),{,printInteger,(,-,-,-,3,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 173))

    def test_lexer74(self):
        """"""
        testcase = """fibonacci:function integer(n:integer){if(n==0)return 1;else return fibonacci(n-1)+fibonacci(n-2);}"""
        expect = """fibonacci,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,fibonacci,(,n,-,1,),+,fibonacci,(,n,-,2,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 174))

    def test_lexer75(self):
        """"""
        testcase = """main: function void () {if(n>0) printBoolean(true); else printBoolean(false);}"""
        expect = """main,:,function,void,(,),{,if,(,n,>,0,),printBoolean,(,true,),;,else,printBoolean,(,false,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 175))

    def test_lexer76(self):
        """"""
        testcase = """main: function void () {breakDownString("Hello My Name Is Jeff");}"""
        expect = """main,:,function,void,(,),{,breakDownString,(,Hello My Name Is Jeff,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 176))

    def test_lexer77(self):
        """"""
        testcase = """arr:array[] of string={};"""
        expect = """arr,:,array,[,],of,string,=,{,},;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 177))

    def test_lexer78(self):
        """"""
        testcase = """arr:array[] of string={"string1","string2","string3"};"""
        expect = """arr,:,array,[,],of,string,=,{,string1,,,string2,,,string3,},;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 178))

    def test_lexer79(self):
        """"""
        testcase = """main: function void () {if(level==max) printString("I\'m a global elite!!!"); else printString("I\'m noob :(");}"""
        expect = """main,:,function,void,(,),{,if,(,level,==,max,),printString,(,I'm a global elite!!!,),;,else,printString,(,I'm noob :(,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 179))

    def test_lexer80(self):
        """"""
        testcase = """main: function void () {if(money>1e6) printString("I\'m rich!"); else printString("Poor peasant!!!");}"""
        expect = """main,:,function,void,(,),{,if,(,money,>,1e6,),printString,(,I'm rich!,),;,else,printString,(,Poor peasant!!!,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 180))

    def test_lexer81(self):
        """"""
        testcase = """var_a:float=1.547e-3;"""
        expect = """var_a,:,float,=,1.547e-3,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 181))

    def test_lexer82(self):
        """"""
        testcase = """var_a:float=1.5e10;"""
        expect = """var_a,:,float,=,1.5e10,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 182))

    def test_lexer83(self):
        """"""
        testcase = """main: function void () {a:integer=readInteger(); b:integer=readInteger(); printInteger(a+b);}"""
        expect = """main,:,function,void,(,),{,a,:,integer,=,readInteger,(,),;,b,:,integer,=,readInteger,(,),;,printInteger,(,a,+,b,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 183))

    def test_lexer84(self):
        """"""
        testcase = """main: function void () {a:integer=readInteger(); b:integer=readInteger(); printInteger(a-b);}"""
        expect = """main,:,function,void,(,),{,a,:,integer,=,readInteger,(,),;,b,:,integer,=,readInteger,(,),;,printInteger,(,a,-,b,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 184))

    def test_lexer85(self):
        """"""
        testcase = """main: function void () {a:integer=readInteger(); b:integer=readInteger(); printInteger(a*b);}"""
        expect = """main,:,function,void,(,),{,a,:,integer,=,readInteger,(,),;,b,:,integer,=,readInteger,(,),;,printInteger,(,a,*,b,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 185))

    def test_lexer86(self):
        """"""
        testcase = """main: function void () {a:integer=readInteger(); b:integer=readInteger(); printInteger(a/b);}"""
        expect = """main,:,function,void,(,),{,a,:,integer,=,readInteger,(,),;,b,:,integer,=,readInteger,(,),;,printInteger,(,a,/,b,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 186))

    def test_lexer87(self):
        """"""
        testcase = """n:integer=readInteger(); main: function void () {for(i=0,i<n,i+1) printInteger(i);}"""
        expect = """n,:,integer,=,readInteger,(,),;,main,:,function,void,(,),{,for,(,i,=,0,,,i,<,n,,,i,+,1,),printInteger,(,i,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 187))

    def test_lexer88(self):
        """"""
        testcase = """main: function void () {while(true);}"""
        expect = """main,:,function,void,(,),{,while,(,true,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 188))

    def test_lexer89(self):
        """"""
        testcase = """main: function void () {do{printString("looping!");}while(true);}"""
        expect = """main,:,function,void,(,),{,do,{,printString,(,looping!,),;,},while,(,true,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 189))

    def test_lexer90(self):
        """"""
        testcase = """main: function void () {str=readString(); if(str=="Athur Morgan") printString("Wanted: dead or alive $5000+");}"""
        expect = """main,:,function,void,(,),{,str,=,readString,(,),;,if,(,str,==,Athur Morgan,),printString,(,Wanted: dead or alive $5000+,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 190))

    def test_lexer91(self):
        """"""
        testcase = """main: function void () {str=readString(); if(str="bored") printString("You are bored af!"); else printString("Keep doing testcases then!");}"""
        expect = """main,:,function,void,(,),{,str,=,readString,(,),;,if,(,str,=,bored,),printString,(,You are bored af!,),;,else,printString,(,Keep doing testcases then!,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 191))

    def test_lexer92(self):
        """"""
        testcase = """main: function void () {str=readString(); if(str="sleepy") printString("To bed we go!"); else printString("Working we continue!");}"""
        expect = """main,:,function,void,(,),{,str,=,readString,(,),;,if,(,str,=,sleepy,),printString,(,To bed we go!,),;,else,printString,(,Working we continue!,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 192))

    def test_lexer93(self):
        """"""
        testcase = """main: function void () {if(discount>0.05) printFloat(price*discount); else printFloat(price);}"""
        expect = """main,:,function,void,(,),{,if,(,discount,>,0.05,),printFloat,(,price,*,discount,),;,else,printFloat,(,price,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 193))

    def test_lexer94(self):
        """"""
        testcase = """main: function void () {printString("Who are you?"); str:string="Ma nam is Jeff!";}"""
        expect = """main,:,function,void,(,),{,printString,(,Who are you?,),;,str,:,string,=,Ma nam is Jeff!,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 194))

    def test_lexer95(self):
        """"""
        testcase = """main: function void () {n:float=readFloat(); writeFloat(24000*n);}"""
        expect = """main,:,function,void,(,),{,n,:,float,=,readFloat,(,),;,writeFloat,(,24000,*,n,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 195))

    def test_lexer96(self):
        """"""
        testcase = """main: function void () {n:integer=readInteger(); if(n%5==0 && n%10!=0) printBoolean(true); else printBoolean(false);}"""
        expect = """main,:,function,void,(,),{,n,:,integer,=,readInteger,(,),;,if,(,n,%,5,==,0,&&,n,%,10,!=,0,),printBoolean,(,true,),;,else,printBoolean,(,false,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 196))

    def test_lexer97(self):
        """"""
        testcase = """main: function void () {printString("I\'m in pain :(");}"""
        expect = """main,:,function,void,(,),{,printString,(,I'm in pain :(,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 197))

    def test_lexer98(self):
        """"""
        testcase = """main: function void () {n:float=readFloat(); writeFloat(n*4/10);}"""
        expect = """main,:,function,void,(,),{,n,:,float,=,readFloat,(,),;,writeFloat,(,n,*,4,/,10,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 198))

    def test_lexer99(self):
        """"""
        testcase = """main: function void () {if(true);}"""
        expect = """main,:,function,void,(,),{,if,(,true,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 199))

    def test_lexer100(self):
        """"""
        testcase = """main: function void () {printBoolean(1+1==3);}"""
        expect = """main,:,function,void,(,),{,printBoolean,(,1,+,1,==,3,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 200))



