texte_codé = 'TRCHT,DIODTITA DTSREM3TRÈ EN OFHENAÉIEEE T M" AUSREJMIT IL TS MDOP4 ENQÉ G* EÉD EI ARSONRRELSIE AAÛRMETMUUBENN OGNLPT EEID   NEQN CACECA EOSCLNE NECEN EÀTR DHNUVSIEB P ORHMT,  ATL AATUIHTMEUDTTIE ETNN EEI"IOTPTEFOEI FRUÉROGS SN LNIOESFR APEFTSAILUMSE:I OS  EGP URRIINTEOOA NSEN FLT ES F SLSI.VTPROAN,SOI NREDFNESPS    ÉINU UI QUSNÉIOMASOJEDEUNT PLS.U*ONCHS GE.'
texte_codé = 'Bournno etjAg Q'
taille_tableau = 5

def createTab(texte,tab_size):
    t =[]
    for n in range(0 ,len(texte_codé), taille_tableau):
        t.append([texte_codé[n:n+taille_tableau]])
    return t

tab = createTab(texte_codé, taille_tableau)
print(tab)
