# Developer Tools for LuxOS 1.0
# Extra developer tools for LuxOS. Officially created by the αβic empire.

class lux_pack:
  name="lux-dev-tools"
  version="1.0"
  aditionaldata={"datalist":[None]}
  def startscript():
    print("LuxOS Developer Tools loaded sucessfully!")
  def pexcm(cmd, cliv):
    cliv2=cliv
    splitcmd=cmd.split(" ")
    r=1
    if splitcmd[0] == "dev-tools" or splitcmd[0] == "d-tools" or splitcmd[0] == "dev-t" or splitcmd[0] == "d-t":
      try:
        if splitcmd[1] == "#version":
          print("LuxOS Developer Tools 1.0")
        elif splitcmd[1] == "update":
          print("LuxOS Developer Tools 1.0")
          print("To update \" lux-dev-tools \", input")
          print("\" fluctus packer fetch lux-dev-tools.py \"")
          print("On the command line interface.")
        elif splitcmd[1] == "help":
          print(" --- testingpackage help --- ")
          print("cliv - manages the Command Line Interface Variables")
      except:
          print(cmd+" >> dev-tools failed.")
    elif splitcmd[0] == "cliv":
        try:
            if splitcmd[1] == "editvar" or splitcmd[1] == "editv" or splitcmd[1] == "evar" or splitcmd[1] == "ev"::
                cliv["vars"][splitcmd[2]] = input(f"CLIV >> vars >> {splitcmd[2]} = ")
            elif splitcmd[1] == "seevar" or splitcmd[1] == "seev" or splitcmd[1] == "svar" or splitcmd[1] == "sv":
                print(f"CLIV >> vars >> {splitcmd[2]} = {cliv["vars"][splitcmd[2]}")
        except:
            print(cmd+" >> cliv failed.")
    else:
      r=0
    return [cliv2, r]
  class packvars:
    devtools="lux-dev-tools-1.0"