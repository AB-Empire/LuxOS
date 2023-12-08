# Testing Package for LuxOS 1.0
# Just a testing package to test your package system. Officially created by the αβic empire.

class lux_pack:
  name="testingpackage"
  version="1.0"
  aditionaldata={"datalist"=[None]}
  def startscript():
    print("Testing Package loaded sucessfully!")
  class packvars:
    testingvar="a"
