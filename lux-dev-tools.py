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
          print("clit - manages the Command Line Interface Type")
      except:
          print(cmd+" >> dev-tools failed.")

    elif splitcmd[0] == "cliv" or splitcmd[0] == "clivars":
        try:
          if cliv["prestige"] >= 1:
            if splitcmd[1] == "seevar" or splitcmd[1] == "seev" or splitcmd[1] == "svar" or splitcmd[1] == "sv":
                print(f"CLIV >> vars >> {splitcmd[2]} = {cliv['vars'][splitcmd[2]]}")
            elif splitcmd[1] == "editvar" or splitcmd[1] == "editv" or splitcmd[1] == "evar" or splitcmd[1] == "ev":
                cliv["vars"][splitcmd[2]] = input(f"CLIV >> vars >> {splitcmd[2]} = ")
            elif splitcmd[1] == "listvars" or splitcmd[1] == "listv" or splitcmd[1] == "lvars" or splitcmd[1] == "lv":
                print(f"CLIV >> vars = {cliv['vars']}")
          else:
            print(cmd+" >> cliv failed. You have no prestige to use it.")
        except:
          print(cmd+" >> cliv failed.")

    elif splitcmd[0] == "clit" or splitcmd[0] == "clitype":
                try:
                  if cliv["prestige"] >= 1:
                    if splitcmd[1] == "seetype" or splitcmd[1] == "seet" or splitcmd[1] == "stype" or splitcmd[1] == "st":
                      print("CLIV >> type = "+cliv["type"])
                    elif splitcmd[1] == "edittype" or splitcmd[1] == "editt" or splitcmd[1] == "etype" or splitcmd[1] == "et":
                      cliv["type"] = input("CLIV >> type = ")
                  else:
                    print(cmd+" >> clit failed. You have no prestige to use it.")
                except:
                  print(cmd+" >> clit failed.")
    else:
      r=0
    return [cliv2, r]
  class packvars:
    devtools="lux-dev-tools-1.0"
