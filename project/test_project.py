import changePrice
import savepdf
import writeProduct
from datetime import datetime
import project
import addadmin


def test_changePrice_function():
   assert changePrice.is_float("7.5") == True
   assert changePrice.is_float("hello CS50") == False
   assert changePrice.is_float(8) == True

def test_savepdf_function():
   nowtime = datetime.now()
   assert savepdf.getdate() == nowtime.strftime("%Y-%m-%d ")
   assert savepdf.gettime() == nowtime.strftime("%H:%M:%S")

def test_writeProduct_function():
   assert writeProduct.input_correct("0500","8.5", 0) == True
   assert writeProduct.input_correct("0500","8.5", 1) == False
   assert writeProduct.input_correct("A500","8.5", 0) == False
   assert writeProduct.input_correct("0500","Hello", 0) == False

def test_writeProduct_find_product():
   assert writeProduct.find_product("012") == True
   assert writeProduct.find_product("4777") == True
   assert writeProduct.find_product("001") == False
   assert writeProduct.find_product("99999") == False

def test_project_function():
   assert project.int_check("1") == True
   assert project.int_check("Hello") == False
   assert project.int_check("1.5") == False

def test_project_getPInfo():
   assert project.getPInfo("012") == "012,A Water,8"
   assert project.getPInfo("5000") == "5000,D Soda,15.5"
   assert project.getPInfo("8848") == "8848,D Energy Drink,11"

def test_addadmin_function():
   assert addadmin.name_validation("Aa123") == True
   assert addadmin.name_validation("Aa123Ab") == True
   assert addadmin.name_validation("A123") == False
   assert addadmin.name_validation("abA123") == False
   assert addadmin.name_validation("asda123") == False
   assert addadmin.name_validation("123a2D") == False
   assert addadmin.name_length_check("Aa123456") == True 
   assert addadmin.name_length_check("Aa12345") == False
   assert addadmin.name_length_check("Aa1234567891011") == False
   assert addadmin.pw_validation("!a1") == True
   assert addadmin.pw_validation("!A2") == True
   assert addadmin.pw_validation("A2131231") == False
   assert addadmin.pw_validation("!Adadwd") == False
   assert addadmin.pw_validation("!     ") == False
   assert addadmin.pw_length_check("A2131231") == True
   assert addadmin.pw_length_check("A213123194111") == False
   assert addadmin.pw_length_check("A419859") == False

