import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_short_decl_1_id(self):
        """basic declaration"""
        testcase = """a:float;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 201))

    def test_full_decl_1_id(self):
        """"""
        testcase = """a:float=1;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 202))

    def test_full_decl_2_ids(self):
        """"""
        testcase = """a,b:float=1,2;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 203))

    def test_full_decl_unbalance(self):
        """"""
        testcase = """a, b, c, d: integer = 3, 4, 6;"""
        expect = """Error on line 1 col 29: ;"""
        self.assertTrue(TestParser.test(testcase, expect, 204))

    def test_func_def(self):
        """"""
        testcase = """main: function void() {}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 205))

    def test_func_1_stmt(self):
        """"""
        testcase = """abc: function integer() {a = 1;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 206))

    def test_func_block_stmt(self):
        """"""
        testcase = """abc: function integer() {{}}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 207))

    def test_func_def_func_call(self):
        """"""
        testcase = """abc: function integer() {abc();}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 208))

    def test_func_stmts_return(self):
        """"""
        testcase = """abc: function integer() {a=1;
            b=1;
            return 0;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 209))

    def test_short_decl_2_ids(self):
        """"""
        testcase = """a,b:float;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 210))

    def test_miss_semi(self):
        """"""
        testcase = """a,b:float=1,2"""
        expect = """Error on line 1 col 13: <EOF>"""
        self.assertTrue(TestParser.test(testcase, expect, 211))

    def test_miss_colon(self):
        """"""
        testcase = """a,b float=1,2;"""
        expect = """Error on line 1 col 4: float"""
        self.assertTrue(TestParser.test(testcase, expect, 212))

    def test_miss_id(self):
        """"""
        testcase = """:float=1;"""
        expect = """Error on line 1 col 0: :"""
        self.assertTrue(TestParser.test(testcase, expect, 213))

    def test_miss_exp_full_decl(self):
        """"""
        testcase = """a:float=;"""
        expect = """Error on line 1 col 8: ;"""
        self.assertTrue(TestParser.test(testcase, expect, 214))

    def test_miss_assign(self):
        """"""
        testcase = """a:float 1;"""
        expect = """Error on line 1 col 8: 1"""
        self.assertTrue(TestParser.test(testcase, expect, 215))

    def test_miss_type_assign(self):
        """"""
        testcase = """a:1;"""
        expect = """Error on line 1 col 2: 1"""
        self.assertTrue(TestParser.test(testcase, expect, 216))

    def test_line_cmt(self):
        """"""
        testcase = """//abc: functionwshjfuiovhsiuod void(){}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 217))

    def test_decl_list(self):
        """"""
        testcase = """a:float;
            abc:function void(){}
            //end
            b:integer;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 218))

    def test_block_cmt(self):
        """"""
        testcase = """/*@@@@@@@@@@@@@*/
    a:integer=1+a;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 219))

    def test_line_cmt_many(self):
        """"""
        testcase = """///////////////////
            a:integer;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 220))

    def test_string_expr(self):
        """"""
        testcase = """main: function void () {a= "abc"::"xyz";}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 221))

    def test_call_expr(self):
        """"""
        testcase = """main: function void() {
        printString("abc")
    }"""
        expect = """Error on line 3 col 4: }"""
        self.assertTrue(TestParser.test(testcase, expect, 222))

    def test_assign_expr(self):
        """"""
        testcase = """main: function void () {a= "abc";}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 223))

    def test_full_decl_string(self):
        """"""
        testcase = """a,b,c:string= "abc","a","""""
        expect = """Error on line 1 col 24: <EOF>"""
        self.assertTrue(TestParser.test(testcase, expect, 224))

    def test_full_decl_str_unbalance(self):
        """"""
        testcase = """a,b,c:string= "a","a" ;"""
        expect = """Error on line 1 col 22: ;"""
        self.assertTrue(TestParser.test(testcase, expect, 225))

    def test_func_is_even(self):
        """"""
        testcase = """isEven: function boolean(a:integer){if(a%2==0) return true; else return false;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 226))

    def test_io_integer(self):
        """"""
        testcase = """main: function void () {a=readInteger(); printInteger(a);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 227))

    def test_io_float(self):
        """"""
        testcase = """main: function void () {n=readFloat(); printFloat(n);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 228))

    def test_io_string(self):
        """"""
        testcase = """main: function void () {str=readString(); printString(str);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 229))

    def test_short_decl_array_2d(self):
        """"""
        testcase = """arr: array[5,5] of integer;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 230))

    def test_short_decl_array_1d(self):
        """"""
        testcase = """arr: array[10] of integer;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 231))

    def test_full_decl_array_1d(self):
        """"""
        testcase = """arr: array[5] of integer={1,2,3,4,5};"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 232))

    def test_full_decl_array_2d(self):
        """"""
        testcase = """arr: array[5,5] of integer={{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15},{16,17,18,19,20},{21,22,23,24,25}};"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 233))

    def test_print_int_cal(self):
        """"""
        testcase = """main: function void () {printInteger(10+11);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 234))

    def test_print_float_cal(self):
        """"""
        testcase = """main: function void () {printFloat(2e-7+3e-1);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 235))

    def test_print_bool_cal(self):
        """"""
        testcase = """main: function void () {printBoolean(var_a && var_b || var_c);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 236))

    def test_bool_cal(self):
        """"""
        testcase = """main: function void () {value=true && false || true;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 237))

    def test_super_func(self):
        """"""
        testcase = """main: function void () {super("name",age);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 238))

    def test_preventDefault(self):
        """"""
        testcase = """main: function void () {preventDefault();}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 239))

    def test_cal_C_of_circle(self):
        """"""
        testcase = """main: function void () {r=readFloat(); pi=3.14; C=2*r*pi; writeFloat(C);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 240))

    def test_cal_absolute(self):
        """"""
        testcase = """main: function void () {abs(100-560-741);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 241))

    def test_get_fibonum(self):
        """"""
        testcase = """main: function void () {fibonacci(5);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 242))

    def test_convert_to_string(self):
        """"""
        testcase = """main: function void () {stringConverter(120.485);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 243))

    def test_print_string(self):
        """"""
        testcase = """main: function void () {printString("Hello World!");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 244))

    def test_print_string_2(self):
        """"""
        testcase = """str:string="Hello \\nWorld!";"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 245))

    def test_print_string_3(self):
        """"""
        testcase = """str:string="Hello World!"""
        expect = """Hello World!"""
        self.assertTrue(TestParser.test(testcase, expect, 246))

    def test_assign_int_expr(self):
        """"""
        testcase = """a:integer=5+6-(123*10+(24-30));"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 247))

    def test_assign_int_list(self):
        """"""
        testcase = """a,b,c:intger=2,3;"""
        expect = """Error on line 1 col 6: intger"""
        self.assertTrue(TestParser.test(testcase, expect, 248))

    def test_print_elem(self):
        """"""
        testcase = """main: function void () {printInteger(arr[0,1]);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 249))

    def test_assign_elem(self):
        """"""
        testcase = """main: function void () {arr[3]=3.14;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 250))

    def test_validate_zero(self):
        """"""
        testcase = """main: function void () {a:integer=readInteger(); if(a!=0) printString("Non-zero"); else printString("Zero!!!");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 251))

    def test_empty_func(self):
        """"""
        testcase = """print: function void(){printString("Empty function!");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 252))

    def test_compare(self):
        """"""
        testcase = """main: function void () {printBoolean(2>3);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 253))

    def test_multiple_concat(self):
        """"""
        testcase = """main: function void () {str="abc"::"def"::("ghi"::"jkl");}"""
        expect = """Error on line 1 col 40: ::"""
        self.assertTrue(TestParser.test(testcase, expect, 254))

    def test_return_int_0(self):
        """no viable alternative at input 'foo:functionint'"""
        testcase = """foo:function int(){return 0;}"""
        expect = """Error on line 1 col 13: int"""
        self.assertTrue(TestParser.test(testcase, expect, 255))

    def test_return_float_0_001(self):
        """"""
        testcase = """foo:function float(){return 0.001;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 256))

    def test_return_string_zero(self):
        """"""
        testcase = """foo:function string(){return "zero";}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 257))

    def test_print_double_not(self):
        """"""
        testcase = """main: function void () {printBoolean(!!false);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 258))

    def test_print_triple_sign(self):
        """"""
        testcase = """main: function void () {printInteger(---3);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 259))

    def test_fibo_function(self):
        """"""
        testcase = """fibonacci:function integer(n:integer){if(n==0)return 1;else return fibonacci(n-1)+fibonacci(n-2);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 260))

    def test_check_positive(self):
        """"""
        testcase = """main: function void () {if(n>0) printBoolean(true); else printBoolean(false);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 261))

    def test_break_down_string(self):
        """"""
        testcase = """main: function void () {breakDownString("Hello My Name Is Jeff");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 262))

    def test_empty_array(self):
        """"""
        testcase = """arr:array[] of string={};"""
        expect = """Error on line 1 col 23: }"""
        self.assertTrue(TestParser.test(testcase, expect, 263))

    def test_unknown_size_array(self):
        """"""
        testcase = """arr:array[] of string={"string1","string2","string3"};"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 264))

    def test_check_proplayer(self):
        """"""
        testcase = """main: function void () {if(level==max) printString("I\'m a global elite!!!"); else printString("I\'m noob :(");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 265))

    def test_check_rich(self):
        """"""
        testcase = """main: function void () {if(money>1e6) printString("I\'m rich!"); else printString("Poor peasant!!!");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 266))

    def test_another_float(self):
        """"""
        testcase = """var_a:float=1.547e-3;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 267))

    def test_big_float(self):
        """"""
        testcase = """var_a:float=1.5e10;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 268))

    def test_sum_of_two(self):
        """"""
        testcase = """main: function void () {a:integer=readInteger(); b:integer=readInteger(); printInteger(a+b);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 269))

    def test_subtraction_of_two(self):
        """"""
        testcase = """main: function void () {a:integer=readInteger(); b:integer=readInteger(); printInteger(a-b);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 270))

    def test_multiplication_of_two(self):
        """"""
        testcase = """main: function void () {a:integer=readInteger(); b:integer=readInteger(); printInteger(a*b);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 271))

    def test_division_of_two(self):
        """"""
        testcase = """main: function void () {a:integer=readInteger(); b:integer=readInteger(); printInteger(a/b);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 272))

    def test_print_loop(self):
        """"""
        testcase = """n:integer=readInteger(); main: function void () {for(i=0,i<n,i+1) printInteger(i);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 273))

    def test_infinite_empty_loop(self):
        """"""
        testcase = """main: function void () {while(true);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 274))

    def test_infinite_loop(self):
        """"""
        testcase = """main: function void () {do{printString("looping!");}while(true);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 275))

    def test_athur_morgan(self):
        """"""
        testcase = """main: function void () {str=readString(); if(str=="Athur Morgan") printString("Wanted: dead or alive $5000+");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 276))

    def test_bored(self):
        """"""
        testcase = """main: function void () {str=readString(); if(str="bored") printString("You are bored af!"); else printString("Keep doing testcases then!");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 277))

    def test_sleepy(self):
        """"""
        testcase = """main: function void () {str=readString(); if(str="sleepy") printString("To bed we go!"); else printString("Working we continue!");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 278))

    def test_print_discount(self):
        """"""
        testcase = """main: function void () {if(discount>0.05) printFloat(price*discount); else printFloat(price);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 279))

    def test_jeff(self):
        """"""
        testcase = """main: function void () {printString("Who are you?"); str:string="Ma nam is Jeff!";}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 280))

    def test_dollar_to_vnd(self):
        """"""
        testcase = """main: function void () {n:float=readFloat(); writeFloat(24000*n);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 281))

    def test_check_only_divisible_by_5(self):
        """n%5==0 && n%10!=0 -> (n%5)==(0 && (n %10)) != 0
      None Associative"""
        testcase = """main: function void () {n:integer=readInteger(); if(n%5==0 && n%10!=0) printBoolean(true); else printBoolean(false);}"""
        expect = """Error on line 1 col 66: !="""
        self.assertTrue(TestParser.test(testcase, expect, 282))

    def test_pain(self):
        """"""
        testcase = """main: function void () {printString("I\'m in pain :(");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 283))

    def test_gpa_10_to_4(self):
        """"""
        testcase = """main: function void () {n:float=readFloat(); writeFloat(n*4/10);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 284))

    def test_empty_if(self):
        """"""
        testcase = """main: function void () {if(true);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 285))

    def test_check_equal_to_3(self):
        """"""
        testcase = """main: function void () {printBoolean(1+1==3);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 286))

    def test_empty_if_else(self):
        """"""
        testcase = """main: function void () {if(true){}else{}}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 287))

    def test_useless_loop(self):
        """"""
        testcase = """main: function void () {for(i=0,true,i+1) break;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 288))

    def test_tired(self):
        """"""
        testcase = """main: function void () {printString("Sooooooooooooooo tired!!!!!!!!!!!!!!");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(testcase, expect, 289))

    def test_no_expr_while(self):
        """"""
        testcase = """main: function void () {while();}"""
        expect = """Error on line 1 col 30: )"""
        self.assertTrue(TestParser.test(testcase, expect, 290))

    def test_no_expr_do_while(self):
        """"""
        testcase = """main: function void () {do{}while()}"""
        expect = """Error on line 1 col 34: )"""
        self.assertTrue(TestParser.test(testcase, expect, 291))

    def test_no_expr_if(self):
        """"""
        testcase = """main: function void () {if(){}}"""
        expect = """Error on line 1 col 27: )"""
        self.assertTrue(TestParser.test(testcase, expect, 292))

    def test_missing_semi(self):
        """"""
        testcase = """main: function void () {if(true) print()}"""
        expect = """Error on line 1 col 40: }"""
        self.assertTrue(TestParser.test(testcase, expect, 293))

    def test_missing_index(self):
        """"""
        testcase = """var_a:integer=arr[];"""
        expect = """Error on line 1 col 18: ]"""
        self.assertTrue(TestParser.test(testcase, expect, 294))

    def test_unkown_plusplus(self):
        """"""
        testcase = """n:integer=i++;"""
        expect = """Error on line 1 col 12: +"""
        self.assertTrue(TestParser.test(testcase, expect, 295))

    def test_missing_arg(self):
        """"""
        testcase = """main: function void () {foo(2,);}"""
        expect = """Error on line 1 col 30: )"""
        self.assertTrue(TestParser.test(testcase, expect, 296))

    def test_missing_number(self):
        """"""
        testcase = """main: function void () {goo(4/);}"""
        expect = """Error on line 1 col 30: )"""
        self.assertTrue(TestParser.test(testcase, expect, 297))

    def test_missing_closing_parenthesis(self):
        """"""
        testcase = """main: function void () {printInteger(;}"""
        expect = """Error on line 1 col 37: ;"""
        self.assertTrue(TestParser.test(testcase, expect, 298))

    def test_missing_openning_parenthesis(self):
        """"""
        testcase = """main: function void () {printFloat);}"""
        expect = """Error on line 1 col 34: )"""
        self.assertTrue(TestParser.test(testcase, expect, 299))

    def test_missing_closing_curly(self):
        """"""
        testcase = """arr:array[] of float={1.3,5.6,4.2;"""
        expect = """Error on line 1 col 33: ;"""
        self.assertTrue(TestParser.test(testcase, expect, 300))
