fn="../human_g1k_v37.fasta"
inputfile=file(fn)
letter=inputfile.read(1)

winsize=100000

ofn="r01_"+fn.split("/")[1]+".100kb"
outputfile=file(ofn,"w")
outputfile.write("chr\tpos\tlength\tN\teffective\tAt\C\tG\tT\tGCratio\n")

i=0
prev_ch="0"
num_letter=0
num_N=0 ; num_A=0 ; num_C=0 ; num_G=0 ; num_T=0 
this_pos=0
while letter:
	i+=1
	if ">" ==letter:  # new chr
		line=inputfile.readline()
		line_split=line.rstrip().split()
		ch=line_split[0]
		print ch
		if i!=1:
			try:
				GCratio=round((num_G+num_C)/float(num_letter-num_N),2)
			except:
				GCratio=-1
			outputfile.write(prev_ch+"\t"+str(this_pos-num_letter+1)+"\t"+str(num_letter)+"\t"+str(num_N)+"\t"+str(num_letter-num_N)+"\t"+str(num_A)+"\t"+str(num_C)+"\t"+str(num_G)+"\t"+str(num_T)+"\t"+str(GCratio)+"\n")
		prev_ch=ch
		this_pos=0
		num_letter=0
		num_N=0 ; num_A=0 ; num_C=0 ; num_G=0 ; num_T=0 
		letter=inputfile.read(1)
		continue
	if letter=="\n":
		letter=inputfile.read(1)
		continue
	this_pos+=1
	num_letter+=1
	if letter=="A" or letter=="a":
		num_A+=1
	elif letter=="C" or letter=="c":
		num_C+=1
	elif letter=="G" or letter=="g":
		num_G+=1
	elif letter=="T" or letter=="t":
		num_T+=1
	elif letter=="N":
		num_N+=1
	if this_pos%winsize==0:
		print this_pos
		try:
			GCratio=round((num_G+num_C)/float(num_letter-num_N),2)
		except:
			GCratio=-1
		outputfile.write(ch+"\t"+str(this_pos-num_letter+1)+"\t"+str(num_letter)+"\t"+str(num_N)+"\t"+str(num_letter-num_N)+"\t"+str(num_A)+"\t"+str(num_C)+"\t"+str(num_G)+"\t"+str(num_T)+"\t"+str(GCratio)+"\n")
		num_letter=0
		num_N=0 ; num_A=0 ; num_C=0 ; num_G=0 ; num_T=0 
	
	letter=inputfile.read(1)

try:
	GCratio=round((num_G+num_C)/float(num_letter-num_N),2)
except:
	GCratio=-1
outputfile.write(ch+"\t"+str(this_pos-num_letter+1)+"\t"+str(num_letter)+"\t"+str(num_N)+"\t"+str(num_letter-num_N)+"\t"+str(num_A)+"\t"+str(num_C)+"\t"+str(num_G)+"\t"+str(num_T)+"\t"+str(GCratio)+"\n")

