#!/usr/bin/bash
if [ -d /home/s2321661/ICA_1/fastqc_result ]
then
	ls /home/s2321661/ICA_1/fastq | grep gz$ |  head -5 | while read name
	do
		fastqc -o /home/s2321661/ICA_1/fastqc_result /home/s2321661/ICA_1/fastq/${name}
	done
else
	mkdir /home/s2321661/ICA_1/fastqc_result
	ls /home/s2321661/ICA_1/fastq | grep gz$ |  head -5 | while read name
        do
                fastqc -o /home/s2321661/ICA_1/fastqc_result /home/s2321661/ICA_1/fastq/${name}
        done
fi

