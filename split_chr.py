from Bio import SeqIO

for seq_record in SeqIO.parse("genome.fa","fasta"):
	print(seq_record.id)
	f = open(seq_record.id+".fa","w")
	f.write(">"+seq_record.id+"\n")
	f.write(str(seq_record.seq))
	f.close()

