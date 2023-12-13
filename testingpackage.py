# Testing Package for LuxOS 1.0
# Just a testing package to test your package system. Officially created by the αβic empire.

class lux_pack:
  name="testingpackage"
  version="1.0"
  aditionaldata={"datalist":[None]}
  def startscript():
    print("Testing Package loaded sucessfully!")
  def pexcm(cmd, cliv):
    cliv2=cliv
    splitcmd=cmd.split(" ")
    r=1
    if splitcmd[0] == "testingpackage":
      try:
        if splitcmd[1] == "#version":
          print("Testing Package 1.0")
        elif splitcmd[1] == "update":
          print("Testing Package 1.0")
          print("To update \" testingpackage \", input")
          print("\" fluctus packer fetch testingpackage.py \"")
          print("On the command line interface.")
        elif splitcmd[1] == "help":
          print(" --- testingpackage help --- ")
          print("testingpackage - tests the package")
        elif splitcmd[1] == "hello":
          print("Hello, World!")
      except:
          print(cmd+" >> testingpackage failed.")
    else:
      r=0
    return [cliv2, r]
  class packvars:
    testingvar="a"
