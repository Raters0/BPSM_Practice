#!/usr/bin/bash
ls /home/s2321661/ICA_1/fastqc_result | grep zip$ | while read name
do
        unzip -d /home/s2321661/ICA_1/fastqc_assess  /home/s2321661/ICA_1/fastqc_result/${name}
done

ls /home/s2321661/ICA_1/fastqc_assess | while read file_name
do
	echo Numbers and quality of the raw sequence data in ${file_name}:
        grep 'Total Sequences' /home/s2321661/ICA_1/fastqc_assess/${file_name}/fastqc_data.txt | xargs echo
	grep 'Sequences flagged as poor quality' /home/s2321661/ICA_1/fastqc_assess/${file_name}/fastqc_data.txt | xargs echo
	echo ''
done


