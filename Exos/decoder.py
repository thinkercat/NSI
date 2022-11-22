#! usr/bin/python
# Decoder v2.0
# Python program to decode this message :
# PRZRFFNTRARPBAGVRAGEVRAQVAGRERFFNAGZNVFVYRFGFHSSVFNZZRAGYBATCBHEARCNFYRQRPELCGRENYNZNVA
# Encode => the letter has won +x

# Unicode letter
# a  [..] z => 97 [..] 122
import os

def cleanString(encode_string:str) -> list:
    '''
    format a string to lowercase and keep only letters\n
    Exemple:
    >>> cleanString('Hel/l@O')
    >>> ['h','e','l,'l','o']
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    format_string = []

    for letter in encode_string:
        l = letter.lower()
        if l in alphabet:
            format_string.append(l)

    return format_string


def convertToUnicode(formated_list:list)->list:
    '''
    transform list character to list unicode\n
    Exemple:
    >>> convertToUnicode(['a','b','z'])
    >>> [97,98,122]
    '''
    list_unicode = []
    for letter in formated_list:
        list_unicode.append(ord(letter))

    return list_unicode


def shiftUnicode(unicode_list:list, scale:int) -> list:
    '''
    shift the letters of 'scale' and return to 97 if >122\n
    Exemple:
    >>> shiftUnicode([97,98,122],2)
    >>> [99,100,98]
    '''
    shifted_list = []
    for unicode_number in unicode_list:
        if unicode_number + scale > 122:
            shifted_list.append(unicode_number + (scale - 26))
        else:
            shifted_list.append(unicode_number + scale)

    return shifted_list


def convertToChar(unicode_list: list) -> list:
    '''
    Convert a unicode list to a char list\n
    Exemple:
    >>> convertTochar([97,98,122])
    >>> ['a','b','z']
    '''
    char_list = []
    for unicode_number in unicode_list:
        char_list.append(chr(unicode_number))

    return char_list


def convertListToSentence(char_list: list) -> str:
    '''
    Convert a list of characters to a string\n
    Exemple:
    >>> convertListToSentence(['N','A','S','A'])
    >>> 'NASA'
    '''
    sentence = ''
    for letter in char_list:
        sentence += letter

    return sentence

# MAIN FUNCTION
def decrypt(encrypt_sentence:str) -> list:
    '''
    Decrypt a sentence with character shift\n
    Exemple:
    >>> decrypt('abcde')
    >>> bcdef
    >>> cdefg
    >>> ...
    >>> zabcd
    '''
    pm_formated = cleanString(encrypt_sentence)
    pm_unicode = convertToUnicode(pm_formated)
    results = []
    for i in range(1, 27):
        pm_uni_shift = shiftUnicode(pm_unicode, i)
        pm_char_shift = convertToChar(pm_uni_shift)
        results.append(convertListToSentence(pm_char_shift))

    # SAVE ALL RESULTS IN A FILE  
    header = " _      ____   _____      ______ _____ _      ______ \n| |    / __ \ / ____|    |  ____|_   _| |    |  ____|\n| |   | |  | | |  __     | |__    | | | |    | |__\n| |   | |  | | | |_ |    |  __|   | | | |    |  __|\n| |___| |__| | |__| |    | |     _| |_| |____| |____ \n|______\____/ \_____|    |_|    |_____|______|______|\n\n=--= Decrypted strings =--=\n\n"
    print("\nCreating File",end="...")
    with open("decoderLogs.txt", "w") as log_file:
        log_file.write(header)

        for result in results:
            log_file.write(result+"\n")
        print("OK")
    
    return results        


# DEBUG FUNCTION
def decoderDebug():
    '''
    Check if all functions gives the good result
    '''
    # cleanString()
    print("cleanString() Function check",end="... ")
    assert cleanString("abcdefghijklmnopqrstuvwxyz") == ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                                                         'n','o','p','q','r','s','t','u','v','w','x','y','z']
    assert cleanString("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                                                         'n','o','p','q','r','s','t','u','v','w','x','y','z']
    assert cleanString("abc&Def::ghijK/lmnOpqR*stuVwxyz") == ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                                                              'n','o','p','q','r','s','t','u','v','w','x','y','z']
    assert cleanString("Hello=w*rLd") == ['h','e','l','l','o','w','r','l','d']
    assert cleanString("Gre@TT") == ['g','r','e','t','t']
    print("OK")

    #convertToUnicode()
    print("convertToUnicode() Function check",end="... ")
    assert convertToUnicode(['a', 'b', 'z']) == [97, 98, 122]
    assert convertToUnicode(['a', 'c', 'z']) == [97, 99, 122]
    assert convertToUnicode(['a', 'b', 'y']) == [97, 98, 121]
    assert convertToUnicode(['a', 'b', 'z', 'c']) == [97, 98, 122, 99]
    assert convertToUnicode(['a', 'b', 'z', 'a', 'a', 'a']) == [97, 98, 122, 97, 97, 97]
    print("OK")

    #shiftUnicode()
    print("shiftUnicode() Function check",end="... ")
    assert shiftUnicode([99,100],1) == [100, 101]
    assert shiftUnicode([120,122,99],3) == [97, 99, 102]
    assert shiftUnicode([1, 56, 99],0) == [1, 56, 99]
    assert shiftUnicode([100, 100, 98, 98], 2) == [102, 102, 100, 100]
    assert shiftUnicode([121,122,123,124],1) == [122,97,98,99]
    print("OK")

    #convertToChar()
    print("convertToChar() Function check",end="... ")
    assert convertToChar([97, 98, 122]) == ['a', 'b', 'z']
    assert convertToChar([97, 99, 122]) == ['a', 'c', 'z']
    assert convertToChar([97, 98, 121]) == ['a', 'b', 'y']
    assert convertToChar([97, 98, 122, 99]) == ['a', 'b', 'z', 'c']
    assert convertToChar([97, 98, 122, 97, 97, 97]) == ['a', 'b', 'z', 'a', 'a', 'a']
    print("OK")

    #convertListToSentence()
    print("convertListToSentence() Function check",end="... ")
    assert convertListToSentence(['a','b','c','d','e','f','g','h','i','j','k','l','m',
                                  'n','o','p','q','r','s','t','u','v','w','x','y','z']) == 'abcdefghijklmnopqrstuvwxyz'
    assert convertListToSentence(['h','e','l', 'l', 'o']) == 'hello'
    assert convertListToSentence(['a', 'e', 'e']) == 'aee'
    assert convertListToSentence(['p', 'u', 's', 'h']) == 'push'
    assert convertListToSentence(['d','b','g','z','a']) == 'dbgza'
    print("OK")

decoderDebug()
decrypt("PRZRFFNTRARPBAGVRAGEVRAQVAGRERFFNAGZNVFVYRFGFHSSVFNZZRAGYBATCBHEARCNFYRQRPELCGRENYNZNVA")