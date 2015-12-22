import xml.etree.ElementTree
from sys import argv

def checkFurniture(e1, e2):
    for ele1 in list(e1):
        txt = ele1.attrib["Name"]
        found = False
        for ele2 in e2.findall(ele1.tag):
            if ele2.attrib["Name"] == txt:
                found = True
                break
        if not found:
            print "    " + ele1.tag + "> " + txt

def checkSoftware(e1, e2):
    for ele1 in list(e1):
        txt = ele1.attrib["Name"]
        found = False
        for ele2 in e2.findall(ele1.tag):
            if ele2.attrib["Name"] == txt:
                found = True
                break
        if not found:
            print "    " + ele1.tag + "> " + txt
            continue
        ele3 = ele1.find("Features")
        if ele3 == None:
            continue
        ele4 = ele2.find("Features")
        if ele4 == None:
            print "    " + ele1.tag + "> " + ele3.tag
            continue
        for ele5 in list(ele3):
            txt = ele5.attrib["Name"]
            found = False
            for ele6 in ele4.findall(ele5.tag):
                if ele6.attrib["Name"] == txt:
                    found = True
                    break
            if not found:
                print "    " + ele1.tag + "> " + ele3.tag + "> " + txt

def checkUI(e1, e2):
    for ele1 in list(e1):
        found = False
        ele2 = e2.find(ele1.tag)
        if ele2 is None:
            print "    " + ele1.tag
            continue
        for ele3 in list(ele1):
            txt = ele3.attrib["Name"]
            found = False
            for ele4 in ele2.findall(ele3.tag):
                if ele4.attrib["Name"] == txt:
                    found = True
                    break
            if not found:
                print "    " + ele1.tag + "> " + txt

if __name__ == "__main__":
    e1 = xml.etree.ElementTree.parse(argv[1] + '/Furniture.xml').getroot()
    e2 = xml.etree.ElementTree.parse(argv[2] + '/Furniture.xml').getroot()
    print("Furniture:")
    print("  In [" + argv[1] + "] but not in [" + argv[2] + "]:")
    checkFurniture(e1, e2)
    print("  In [" + argv[2] + "] but not in [" + argv[1] + "]:")
    checkFurniture(e2, e1)

    e1 = xml.etree.ElementTree.parse(argv[1] + '/Software.xml').getroot()
    e2 = xml.etree.ElementTree.parse(argv[2] + '/Software.xml').getroot()
    print("Software:")
    print("  In [" + argv[1] + "] but not in [" + argv[2] + "]:")
    checkSoftware(e1, e2)
    print("  In [" + argv[2] + "] but not in [" + argv[1] + "]:")
    checkSoftware(e2, e1)

    e1 = xml.etree.ElementTree.parse(argv[1] + '/UI.xml').getroot()
    e2 = xml.etree.ElementTree.parse(argv[2] + '/UI.xml').getroot()
    print("UI:")
    print("  In [" + argv[1] + "] but not in [" + argv[2] + "]:")
    checkUI(e1, e2)
    print("  In [" + argv[2] + "] but not in [" + argv[1] + "]:")
    checkUI(e2, e1)
