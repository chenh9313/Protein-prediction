**final state of the project: Predictting the evolution tree of ADF gene family**

**1) install requirement for running function**

    conda install python=3.8, numpy, matplotlib, scipy,jupyter

**2) all ipynb files are under Models folder**
    codnoncod_Report.ipynb

    count_Report.ipynb

    download_Report.ipynb

    protein_Report.ipynb

    structure_Report.ipynb

    tree_Report.ipynb


**3) all function python files and unit test files are under package_name folder**

    codnoncod.py

    count.py

    download.py

    protein.py

    structure.py

    tree.py

    test_codnoncod.py

    test_count.py

    test_download.py

    test_protein.py

    test_structure.py

    test_tree.py

**4) Command for each function**

    **download function -> download_Report.ipynb:**
    download target gene sequence from biology database.

        Command:    download_sequence('genename','weblink')

    **count function -> count_Report.ipynb:**
    calculate the 4 different type of nucleotide number.

        Command:    count_sequence(gene genome sequence)

    **structure function -> structure_Report.ipynb:**
    get report of the gene structure info target gene.

        Command:    structure_gene(gebeID)

    **protein function -> protein_Report.ipynb:**
    get the protein sequence of target gene and calculate the 21 different type of amino acid number.

        Command:    protein_sequence(seq1, seq2)

    **codnoncod function -> codnoncod_Report.ipynb:**
    calculate the evolution selection on non-coding and coding areas.

        Command:    cod_noncod(no-coding area position, seq1, seq2)

    **tree function -> tree_Report.ipynb:**
    building evolution tree based on the above infomation.

        Command:    tree_builder(gene number, connetion between each genes)











