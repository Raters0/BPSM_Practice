while read accession
 do
 echo -e "Downloading ${accession} ..."
 wget -O- "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=${accession}&strand=1&rettype=fasta&retmode=text" >> result.fasta
done < sequence_10.seq

