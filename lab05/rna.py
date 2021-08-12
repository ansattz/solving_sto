# Douglas Vieira
# @ansattz


def traducao_RNAm(st):
    try:
        RNAxAm = {
            "UUU": "Phe",
            "UUC": "Phe",
            "UUA": "Leu",
            "UUG": "Leu",
            "UCU": "Ser",
            "UCC": "Ser",
            "UCA": "Ser",
            "UCG": "Ser",
            "UAU": "Tyr",
            "UAC": "Tyr",
            "UGU": "Cys",
            "UGC": "Cys",
            "CUU": "Leu",
            "CUC": "Leu",
            "CUA": "Leu",
            "CUG": "Leu",
            "AUU": "Ile",
            "AUC": "Ile",
            "AUA": "Ile",
            "GUU": "Val",
            "GUC": "Val",
            "GUA": "Val",
            "GUG": "Val",
            "CCU": "Pro",
            "CCC": "Pro",
            "CCA": "Pro",
            "CCG": "Pro",
            "ACU": "Thr",
            "ACC": "Thr",
            "ACA": "Thr",
            "ACG": "Thr",
            "GCU": "Ala",
            "GCC": "Ala",
            "GCA": "Ala",
            "GCG": "Ala",
            "CAU": "His",
            "CAC": "His",
            "CAA": "Gln",
            "CAG": "Gln",
            "AAU": "Asn",
            "AAC": "Asn",
            "AAA": "Lys",
            "AAG": "Lys",
            "GAU": "Asp",
            "GAC": "Asp",
            "GAA": "Glu",
            "GAG": "Glu",
            "CGU": "Arg",
            "CGC": "Arg",
            "CGA": "Arg",
            "CGG": "Arg",
            "AGU": "Ser",
            "AGC": "Ser",
            "AGA": "Arg",
            "AGG": "Arg",
            "GGU": "Gly",
            "GGC": "Gly",
            "GGA": "Gly",
            "GGG": "Gly",
        }
        
        tRNA = RNAxAm[st[0:3]] + '-' + RNAxAm[st[3:6]] + '-' + RNAxAm[st[6:9]]
        return tRNA
    except KeyError:
        print('Sequência incorreta!')


print(traducao_RNAm(str(input("Sequência: "))))