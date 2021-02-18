
import sys
import os.path
from os import path
import re

fileInput = open(sys.argv[1], "r")
fileOutputA = open("Alu.bed", "w")
fileOutputL1 = open("L1.bed", "w")
fileOutputSVA = open("SVA.bed", "w")
fileOutputHERV = open("HERV.bed", "w")

chr = []
start = []
stop = []
for line in fileInput:
        line = line.strip("\n")
        if line.startswith("#"):
                continue
        if line.startswith("H"):
                continue
        splitted = line.split("\t")
        chr = splitted[0].replace(".", " ").replace("_", " ").split()
        start = splitted[3]
        stop = splitted[4]
        if "Alu" in line:
                fileOutputA.write(chr[0] + "\t" + start + "\t" + stop + "\t" + "ALU" + "\n")
        if "L1" in line:
                fileOutputL1.write(chr[0] + "\t" + start + "\t" + stop + "\t" + "L1" + "\n")
        if "SVA" in line:
                fileOutputSVA.write(chr[0] + "\t" + start + "\t" + stop + "\t" + "SVA" + "\n")
        if "HERV" in line:
                fileOutputHERV.write(chr[0] + "\t" + start + "\t" + stop + "\t" + "HERV" + "\n")


