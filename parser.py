#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse



def main():
    '''
    Find all crypto-maps and the child lines thereof
    Exerise 8
    '''

    with open("config.cfg") as f:
        config = CiscoConfParse(f)
    cmaps = config.find_objects("^crypto map")
    
    count = 0
    
    for c in cmaps:
        print c.text,
        for child in c.children:
            print child.text,
        count += 1
    print "*" * 10 + " There are %d crypto-maps " % count + "*" * 10
    print "\n"


    '''
    Find all crypto-maps that use Group2 PFS
    (Exercise 9)
    '''

    print "*" * 10 + " Those using Group2 are: " + "*" * 10
    pfs2 = config.find_objects_w_child(parentspec=r"^crypto map", childspec=r"group2")
    for p in pfs2:
        print p.text

    '''
    Find anything not using AES - exercise 10
    '''
    print "*" * 10 + " Those not using AES are: " + "*" * 10
    no_aes = config.find_objects_wo_child(parentspec=r"^crypto map", childspec=r"AES-SHA")
    for a in no_aes:
        print a.text

if __name__ == "__main__":
    main()
