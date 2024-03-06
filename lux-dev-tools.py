# Developer Tools for LuxOS 1.1 (06032024a)
# Extra developer tools for LuxOS. Officially created by the αβic empire.

import data

class lux_pack:

  name="lux-dev-tools"
  version="1.1"
  aditionaldata={"datalist":[None]}

  def startscript():
    print("LuxOS Developer Tools loaded sucessfully!")

  def pexcm(cmd, splitcmd, cliv):
    cliv2=cliv
    r=1
    if splitcmd[0] == "dev-tools" or splitcmd[0] == "d-tools" or splitcmd[0] == "dev-t" or splitcmd[0] == "d-t":
      try:
        if splitcmd[1] == "#version":
          print("LuxOS Developer Tools 1.1")
        elif splitcmd[1] == "update":
          print("LuxOS Developer Tools 1.1")
          print("To update \" lux-dev-tools \", input")
          print("\" fluctus packer fetch lux-dev-tools.py \"")
          print("On the command line interface.")
        elif splitcmd[1] == "help":
          print(" --- testingpackage help --- ")
          print("cliv - manages the Command Line Interface Variables")
          print("clit - manages the Command Line Interface Type")
          print("clip - manages the Command Line Interface Prestige")
          print("newo - creates a new Command Line Interface variable")
          print("edito - edits a Command Line Interface variable")
          print("out - outputs a text value")
          print("rd - reads a system data file")
          print("wd - overwrites a system data file")
      except:
          print(cmd+" >> dev-tools failed.")

    elif splitcmd[0] == "cliv" or splitcmd[0] == "clivars":
        try:
          if cliv["prestige"] >= 2.5:
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

    elif splitcmd[0] == "clip" or splitcmd[0] == "cliprestige":
      try:
        if cliv["prestige"] >= 2.5:
          if splitcmd[1] == "seeprestige" or splitcmd[1] == "seep" or splitcmd[1] == "sprestige" or splitcmd[1] == "sp":
            print("CLIV >> prestige = "+str(cliv["prestige"]))
          elif splitcmd[1] == "editprestige" or splitcmd[1] == "editp" or splitcmd[1] == "eprestige" or splitcmd[1] == "ep":
            cliv["prestige"] = input("CLIV >> prestige = ")
        else:
          print(cmd+" >> clip failed. You have no prestige to use it.")
      except:
        print(cmd+" >> clip failed.")

    elif splitcmd[0] == "newo" or splitcmd[0] == "**":
      try:
        if cliv["prestige"] >= 2.5 or cliv["type"] == "mueq":
          if splitcmd[1] == "var" or splitcmd[1] == "v":
            try:
              cliv["vars"][splitcmd[2].replace("#", "@")]
              print(cmd+" >> newo failed. New variable is already existent.")
            except:
              if splitcmd[2][:1] == "#":
                if splitcmd[3] == "<=>":
                  cliv["vars"][splitcmd[2].replace("#", "@")] = splitcmd[4].replace(r"%%%", r"%sc%").replace(r"%%", " ").replace(r"%nl%", "\n").replace(r"%#%", "@")
                elif splitcmd[3] == "<in":
                  cliv["vars"][splitcmd[2].replace("#", "@")] = input("** var "+splitcmd[2]+" <=> ")
                elif splitcmd[3] == "<=>(n)":
                  cliv["vars"][splitcmd[2].replace("#", "@")] = float(eval(splitcmd[4]))
                elif splitcmd[3] == "<in(n)":
                  cliv["vars"][splitcmd[2].replace("#", "@")] = float(eval(input("** var "+splitcmd[2]+" <=> ")))
          elif splitcmd[1] == "":
            {}
        else:
          print(cmd+" >> newo failed. You have no prestige to use it.")
      except:
        print(cmd+" >> newo failed.")

    elif splitcmd[0] == "edito" or splitcmd[0] == "***":
      try:
        if cliv["prestige"] >= 2.5 or cliv["type"] == "mueq":
          if splitcmd[1] == "var" or splitcmd[1] == "v":
            try:
              cliv["vars"][splitcmd[2].replace("#", "@")]
              if splitcmd[2][:1] == "#":
                if splitcmd[3] == "<=>":
                  cliv["vars"][splitcmd[2].replace("#", "@")] = splitcmd[4].replace(r"%%%", r"%sc%").replace(r"%%", " ").replace(r"%nl%", "\n").replace(r"%#%", "@")
                elif splitcmd[3] == "<in":
                  cliv["vars"][splitcmd[2].replace("#", "@")] = input("*** var "+splitcmd[2]+" <=> ")
                elif splitcmd[3] == "<=>(n)":
                  cliv["vars"][splitcmd[2].replace("#", "@")] = float(eval(splitcmd[4]))
                elif splitcmd[3] == "<in(n)":
                  cliv["vars"][splitcmd[2].replace("#", "@")] = float(eval(input("*** var "+splitcmd[2]+" <=> ")))
                elif splitcmd[3] == "+=>":
                  cliv["vars"][splitcmd[2].replace("#", "@")] = cliv["vars"][splitcmd[2].replace("#", "@")] + splitcmd[4]
                elif splitcmd[3] == "+in":
                  cliv["vars"][splitcmd[2].replace("#", "@")] = cliv["vars"][splitcmd[2].replace("#", "@")] + input("*** var "+splitcmd[2]+" +=> ")
                elif splitcmd[3] == "+=>(n)":
                  cliv["vars"][splitcmd[2].replace("#", "@")] = cliv["vars"][splitcmd[2].replace("#", "@")] + float(eval(splitcmd[4]))
                elif splitcmd[3] == "+in(n)":
                  cliv["vars"][splitcmd[2].replace("#", "@")] = cliv["vars"][splitcmd[2].replace("#", "@")] + float(eval(input("*** var "+splitcmd[2]+" +=> ")))
            except:
              print(cmd+" >> edito failed. Variable is not existent. / Variable could not be edited.")
          elif splitcmd[1] == "":
            {}
        else:
          print(cmd+" >> edito failed. You have no prestige to use it.")
      except:
        print(cmd+" >> edito failed.")

    elif splitcmd[0] == "out" or splitcmd[0] == "o<":
      print(splitcmd[1].replace(r"%%%", r"%sc%").replace(r"%%", " ").replace(r"%nl%", "\n").replace(r"%#%", "@").replace(r"%sc%", r"%"))

    elif splitcmd[0] == "rd" or splitcmd[0] == "readd" or splitcmd[0] == "rdata":
      try:
        if cliv["prestige"] >= 2.5:
              tempvar = open(data.system["luxoslocation.data"]+"/data/"+splitcmd[1].replace(".","/")+".data", "r", encoding='utf-8').read()
              print("START DATA  [ "+splitcmd[1]+" ]")
              print(tempvar)
              print("END   DATA  [ "+splitcmd[1]+" ]")
              print("Lines:      "+str(len(tempvar.split("\n"))))
              print("Characters: "+str(len(tempvar.replace("", "%||").split("%||"))-2))
        else:
          print(cmd+" >> rd failed. You have no prestige to use it.")
      except:
          print(cmd+" >> rd failed.")

    elif splitcmd[0] == "wd" or splitcmd[0] == "writed" or splitcmd[0] == "wdata":
      try:
        if cliv["prestige"] >= 2.5:
              tempvar = open(data.system["luxoslocation.data"]+"/data/"+splitcmd[1].replace(".","/")+".data", "r", encoding='utf-8').read()
              print("START DATA  [ "+splitcmd[1]+" ]")
              print(tempvar)
              print("END   DATA  [ "+splitcmd[1]+" ]")
              print("Lines:      "+str(len(tempvar.split("\n"))))
              print("Characters: "+str(len(tempvar.replace("", "%||").split("%||"))-2))
              print("START D2Ow  [ "+splitcmd[1]+" ]")
              tempvar2 = input("").replace(r"%%%", r"%sc%").replace(r"%%", " ").replace(r"%nl%", "\n").replace(r"%#%", "@").replace(r"%sc%", r"%")
              open(data.system["luxoslocation.data"]+"/data/"+splitcmd[1].replace(".","/")+".data", "w", encoding='utf-8').write(tempvar2)
              print("END   D2Ow  [ "+splitcmd[1]+" ]")
              print("Lines:      "+str(len(tempvar2.split("\n"))))
              print("Characters: "+str(len(tempvar2.replace("", "%||").split("%||"))-2))
              tempvar3 = open(data.system["luxoslocation.data"]+"/data/"+splitcmd[1].replace(".","/")+".data", "r", encoding='utf-8').read()
              print("START NEWDT [ "+splitcmd[1]+" ]")
              print(tempvar3)
              print("END   NEWDT [ "+splitcmd[1]+" ]")
              print("Lines:      "+str(len(tempvar3.split("\n"))))
              print("Characters: "+str(len(tempvar3.replace("", "%||").split("%||"))-2))
        else:
          print(cmd+" >> wd failed. You have no prestige to use it.")
      except:
          print(cmd+" >> wd failed.")

    else:
      r=0
    return [cliv2, r]

  class packvars:
    devtools="lux-dev-tools-1.1"
