"""This is Part4: Get the information of dN/ds of non_coding and coding area."""

def cod_noncod(number, seq1, seq2):
    """Return the value of dn and ds in the target gene."""
    n_end = number
    m_start = 0
    non_x1 = seq1[m_start:n_end]
    non_x2 = seq2[m_start:n_end]
    non_sum_dn = 0
    non_sum_ds = 0
    non_total_dn = len(non_x1)/3*2
    non_total_ds = len(non_x1)/3
    for i in range(0,len(non_x1),3):
        a_seq = non_x1[i:i+3]
        b_seq = non_x2[i:i+3]
        non_dn = 0
        non_ds = 0
        if a_seq[0] != b_seq[0]:
            non_dn = non_dn + 1
        if a_seq[1] != b_seq[1]:
            non_dn = non_dn + 1
            non_sum_dn = non_sum_dn + non_dn
        if a_seq[2] != b_seq[2]:
            non_ds = non_ds + 1
            non_sum_ds = non_sum_ds + non_ds
    print("total Non-syn is:",non_sum_dn)
    print("total Syn is:",non_sum_ds)
    print("dn is:",round((non_sum_dn/non_total_dn),2))
    print("ds is:",round((non_sum_ds/non_total_ds),2))
    non_change = (non_sum_dn/non_total_dn)/(non_sum_ds/non_total_ds)
    print("dn/ds is:",non_change)
    non_tag = ("non-coding area is:")
    if non_change == 1:
        print(non_tag,"evolution neutrally")
    if non_change < 1:
        print(non_tag,"evoultion constrained")
    if non_change >1:
        print(non_tag,"evolution changing rapidly")
    print('\n')
    ##calculate the dn and ds in coding area
    cod_x1 = seq1[n_end:len(seq1)]
    cod_x2 = seq2[n_end:len(seq2)]
    cod_sum_dn = 0
    cod_sum_ds = 0
    cod_total_dn = len(cod_x1)/3*2
    cod_total_ds = len(cod_x1)/3
    for i in range(0,len(cod_x1),3):
        a_seqc = cod_x1[i:i+3]
        b_seqc = cod_x2[i:i+3]
        cod_dn = 0
        cod_ds = 0
        if a_seqc[0] != b_seqc[0]:
            cod_dn = cod_dn + 1
        if a_seqc[1] != b_seqc[1]:
            cod_dn = cod_dn + 1
            cod_sum_dn = cod_sum_dn + cod_dn
        if a_seqc[2] != b_seqc[2]:
            cod_ds = cod_ds + 1
            cod_sum_ds = cod_sum_ds + cod_ds
    print("total Non-syn is:",cod_sum_dn)
    print("total Syn is:",cod_sum_ds)
    print("dn is:",round((cod_sum_dn/cod_total_dn),2))
    print("ds is:",round((cod_sum_ds/cod_total_ds),2))
    cod_change = (cod_sum_dn/cod_total_dn)/(cod_sum_ds/cod_total_ds)
    print("dn/ds is:",cod_change)
    cod_tag = ("coding area is:")
    if cod_change == 1:
        print(cod_tag,"evolution neutrally")
    if cod_change < 1:
        print(cod_tag,"evoultion constrained")
    if cod_change >1:
        print(cod_tag,"evolution changing rapidly")
    return(non_change, cod_change)
