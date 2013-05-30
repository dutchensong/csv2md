import sys

source_name = sys.argv[1]

source_file = open("source/"+source_name+".csv","r")
target_file = open("target/"+source_name+".md","w")



length = len(source_file.readlines())


# sometimes the csv file use \r between lines but not \n
if length==1:
	source_file.seek(0)
	item_lines = source_file.readline().split('\r')
	i = 0
	for item_line in item_lines:
		print "write line"+str(i)+','
		if i==1:
			print >>target_file,'-|-'
		i +=1
		line_target = item_line.replace(';','|')
		print >>target_file,line_target
else:
	source_file.seek(0)
	i = 0
	for line in source_file:
		print "write line"+str(i)+','
		if i==1:
			print >>target_file,'-|-'
		i +=1
		line_target = line[:-1].replace(';','|')
		print >>target_file,line_target
	
	


source_file.close()
target_file.close()