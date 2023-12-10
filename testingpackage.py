# Testing Package for LuxOS 1.0
# Just a testing package to test your package system. Officially created by the αβic empire.

class lux_pack:
  name="testingpackage"
  version="1.0"
  aditionaldata={"datalist":[None]}
  def startscript():
    print("Testing Package loaded sucessfully!")
  def pexcm(cmd, cliv):
    splitcmd=cmd.split(" ")
    r=1
    if splitcmd[0] == "testingpackage":
      try:
        if self.splitcmd[1] == "#version":
          print("Testing Package 1.0")
      except:
          print(cmd+" >> testingpackage failed.")
    else:
      r=0
    return r
  class packvars:
    testingvar="a"
