#=============Spam=========#
if "SpamGroup " in msg.text:
	txt = msg.text.replace("SpamGroup ","")
	List = txt.split("/")
	namaGrup = List[0]
	jumlah = int(List[1])
	midd = List[3]
	for x in range(jumlah):
		cl.createGroup(namaGrup, [midd])
	cl.sendText(msg.to, "Success spam "+jumlah+" group")
