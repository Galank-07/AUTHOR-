# -*- coding: utf-8 -*-
# Special Thanks => LD TEAM & DeadLine™
import LINETCR
from LINETCR.lib.Gen.ttypes import *
from Trevor.undead import bmth
from datetime import datetime
from bs4 import BeautifulSoup
from bs4 import Tag
import pafy
import youtube_dl
import time, random, ast, sys, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia,tempfile,glob,shutil,unicodedata,goslate
from gtts import gTTS

#trev = DeadLine.trevor()
#trev.cewephp(wentworth=bmth().spirit())# ini juga sama dengan yang diatas
#trev.tembakboskue()

trev = LINETCR.LINE() #ingat yang ini dipake kalau udah dapat token baru pagerin yang  atas
trev.cewephp(wentworth="EqLimE5k92getig5cVh8.HuUm1h/UuO3MPfskq3iZYa.Zg1vkggCDlLvm518TWVnYToAWIFqlaFg6XnRf+TeIDQ=")
trev.tembakboskue()

print(""" ________        __  _            _                      ______
/_  __/ / ___   / /_(___ _ ___   (____   ___ ___ _    __/ / / /
 / / / _ / -_) / __/ /  ' / -_) / (_-<  / _ / _ | |/|/ /_/_/_/ 
/_/___//_\__/  \__/_/_/_/_\__/ /_/___/ /_//_\___|_______(_(_)  
  / _ | _______   __ _____ __ __  _______ ___ ____/ /__ \      
 / __ |/ __/ -_) / // / _ / // / / __/ -_/ _ `/ _  / /__/      
/_/ |_/_/  \__/  \_, /\___\_,_/ /_/  \__/\_,_/\_,_/ (_)        
                /___/                                          
""")
print "===[Success Trev]==="


mid = trev.getProfile().mid
Creator="u19a6336222efe94acce1b05dd39c0940"
Mike=["u19a6336222efe94acce1b05dd39c0940"]

contact = trev.getProfile()
profile = trev.getProfile()
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = trev.getProfile()
backup = trev.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
wait = {
    "LeaveRoom":True,
    "AutoJoin":True,
    'autoJoin':True,
    "ceksticker":False,
    'autoCancel':{"on":False,"members":1},
    "Members":0,
    "AutoCancel":False,
    "AutoKick":False,       
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":False,
    "trevrespon":False,
    "pembaca":False,
    "Timeline":True,
    "Contact":False,
    "lang":"JP",
    "autoJoinTicket":False,
    "BlGroup":{}
}
frederick = {
    "trevor":"!",
}



mikey = {
    "userAgent": [
		"Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
		"Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
		"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
	],
}

mulai = time.time()

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Hours %02d Minute %02d Second' % (hours, mins, secs)

def updateProfilePicture(self, path, type='p'):
        files = {'file': open(path, 'rb')}
        params = {'oid': self.profile.mid,'type': 'image'}
        if type == 'vp':
            params.update({'ver': '2.0', 'cat': 'vp.mp4'})
        data = {'params': self.genOBSParams(params)}
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/p/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update profile picture failure.')
        return True

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    try:
        trev.sendMessage(msg)
    except Exception as error:
        print error    
        
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib.request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"   
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def bot(op):
    try:
#--------------------END_OF_OPERATION--------------------
        if op.type == 0:
            return
#-------------------NOTIFIED_READ_MESSAGE----------------
        if op.type == 55:
	    try:
    	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
#------------------NOTIFIED_INVITE_INTO_ROOM-------------
        if op.type == 22:
          if wait["LeaveRoom"] == True:
            trev.leaveRoom(op.param1)
#--------------------INVITE_INTO_ROOM--------------------
        if op.type == 21:
          if wait["LeaveRoom"] == True:
            trev.leaveRoom(op.param1)

#--------------NOTIFIED_INVITE_INTO_GROUP----------------

	    if mid in op.param3:
                if wait["AutoJoin"] == True:
                    trev.acceptGroupInvitation(op.param1)
                else:
		    trev.rejectGroupInvitation(op.param1)
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Mike:
			pass
		    else:
                        trev.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			trev.cancelGroupInvitation(op.param1, [op.param3])
			trev.sendText(op.param1, "Itu kicker jgn di invite!")
		    else:
			pass
#------------------NOTIFIED_KICKOUT_FROM_GROUP-----------------
        if op.type == 13:
            if param3 in mid:
            	if op.param2 in Mike:
                    G = trev.getGroup(op.param1)
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            trev.rejectGroupInvitation(op.param1)
                        else:
                            trev.acceptGroupInvitation(op.param1)
                    else:
                        trev.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        trev.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    trev.cancelGroupInvitation(op.param1, matched_list)
#--------------------------------------------------------------
        if op.type == 19:
		if wait["AutoKick"] == True:
                    if op.param2 in Mike:
                        pass
                    try:
                        trev.kickoutFromGroup(op.param1,[op.param2])
			trev.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
			    trev.kickoutFromGroup(op.param1,[op.param2])
			    trev.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Mike:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Mike:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True



#--------------------------NOTIFIED_UPDATE_GROUP---------------------
        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Mike:
		    pass
		else:
                    trev.sendText(msg.to, "KONTOL!")
            else:
                pass
#--------------------------SEND_MESSAGE---------------------------
        if op.type == [25,26]:
            msg = op.message
            if "/ti/g/" in msg.text.lower():
                            if wait["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = trev.findGroupByTicket(ticket_id)
                                    trev.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    trev.sendText("Thanks for your link group!")
        if op.type == 26:
            print "SEND_MESSAGE[25]"
            msg = op.message
#----------------------------------------------------------------------------
            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in Mike:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            trev.sendText(msg.to,"already")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            trev.sendText(msg.to,"aded")
		    else:
			trev.sendText(msg.to,"Admin Detected~")


                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        trev.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        trev.sendText(msg.to,"It is not in the black list")
#--------------------------------------------------------
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     trev.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = trev.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = trev.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         trev.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                     else:
                         contact = trev.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = trev.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         trev.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))

#--------------------------------------------------------

#--------------------------------------------------------
            elif msg.text == frederick["trevor"]+"ginfo":
                if msg.toType == 2:
                    ginfo = trev.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Unknown"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "Blocked"
                        else:
                            u = "Allowed"
                        trev.sendText(msg.to,"⚔ Group Name: 「 " + str(ginfo.name) + " 」\n⚔ Group id\n 「􏿿" + msg.to + "」\n⚔ Group creator: 「􏿿 " + gCreator + " 」\n\n⚔ Members: 「􏿿" + str(len(ginfo.members)) + "」\n⚔ Pending invite 「􏿿" + sinvitee + "」\n⚔ Link Status: 「􏿿" + u + "」")
                    else:
                        trev.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        trev.sendText(msg.to,"Can not be used outside the group")
                    else:
                        trev.sendText(msg.to,"Not for use less than group")

#--------------------------------------------------------
            elif msg.text is None:
                return
#--------------------------------------------------------
            elif msg.text in [frederick["trevor"]+"creator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Creator}
                trev.sendMessage(msg)
		trev.sendText(msg.to,"Add Me:✮Ŧ€Äm ÄυŦĦōя bōŦ✮\nline.me/ti/p/~azhura07_\nline.me/ti/p/~Iechand25")
#--------------------------------------------------------
	    elif msg.text in [frederick["trevor"]+"gcreator"]:
                if msg.toType == 2:
                    msg.contentType = 13
                    gi = trev.getGroup(msg.to)
                    gc = gi.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gc}
                        gc1 = gi.creator.displayName
                        trev.sendText(msg.to,"「􏿿 Group Creator 」\n Creator: " + gc1)
                        trev.sendMessage(msg)
                    except:
                        gc = "Unknown"
#--------------------------------------------------------
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    trev.sendText(msg.to,msg.text)
#--------------------------------------------------------
            
#-------------------------------------------------------
            elif msg.text in [frederick["trevor"]+"system"]:
                 md = ""
                 if wait["AutoCancel"] == True: md+="Autocancel: [ON]\n"
                 else: md+="AutoCancel: [OFF]\n"
                 if wait["LeaveRoom"] == True: md+="LeaveRoom: [ON]\n"
                 else: md+="AutoCancel: [OFF]\n"
                 if wait["autoCancel"]["on"] == True: md+="Autoreject: [ON]\n"
                 else: md+="Autoreject: [OFF]\n"
                 if wait["Qr"] == True: md+="Qr Protect: [ON]\n"
                 else: md+="Qr Protect: [OFF]\n"
                 if wait["pembaca"] == True: md+="Autoread: [ON]\n"
                 else: md+="Autoread: [OFF]\n"
                 if wait["trevrespon"] == True: md+="Autorespon: [ON]\n"
                 else: md+="Autorespon: [OFF]\n"
                 if wait["AutoKick"] == True: md+="Autokick: [ON]\n"
                 else: md+="Autokick: [OFF]\n"
                 if wait["AutoJoin"] == True: md+="Autojoin: [ON]\n"
                 else: md+="AutoJoin: [OFF]\n"
                 if wait["pembaca"] == True: md+="Autoread: [ON]\n"
                 else: md+="Autoread: [OFF]\n"
                 trev.sendText(msg.to,"system\n\n"+md+"KALAU [ON]  BERARTI HIDUP\nKALAU [OFF] BERARTI MATI\n"+"Gunakan trevkey\n"+"["+frederick["trevor"]+"]")
#--------------------------------------------------------
            elif msg.text in [frederick["trevor"]+"listgroup"]:
            	trev.sendText(msg.to,"waiting for collect group")
                gruplist = trev.getGroupIdsJoined()
                kontak = trev.getGroups(gruplist)
                num=1
                msgs="═════[ List Group ]═══════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n═════[ List Group ]═══════\nTotal Group : %i" % len(kontak)
                trev.sendText(msg.to, msgs)
#--------------------------------------------------------
	    elif msg.text in [frederick["trevor"]+"leavegroup"]:
		ng = msg.text.replace("Leave group: ","")
		gid = trev.getGroupIdsJoined()
                for i in gid:
                    h = trev.getGroup(i).name
		    if h == ng:
			trev.sendText(i,"Bye "+h+"~")
		        trev.leaveGroup(i)
			trev.sendText(msg.to,"Success left ["+ h +"] group")
		    else:
			pass
#--------------------------------------------------------
#--------------------------------------------------------
            elif msg.text in [frederick["trevor"]+"cancel"]:
                if msg.toType == 2:
                    X = trev.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        trev.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        trev.sendText(msg.to,"No one is inviting")
                else:
                    trev.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in [frederick["trevor"]+"ourl"]:
                if msg.toType == 2:
                    X = trev.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    trev.updateGroup(X)
                    trev.sendText(msg.to,"Url Active")
                else:
                    trev.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in [frederick["trevor"]+"curl"]:
                if msg.toType == 2:
                    X = trev.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    trev.updateGroup(X)
                    trev.sendText(msg.to,"Url inActive")

                else:
                    trev.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in [frederick["trevor"]+"autojoin:on"]:
                if msg.from_ in Mike:
                    if wait["AutoJoin"] == True:
                            trev.sendText(msg.to,"「􏿿Auto Join」\n SET: ON")
                    else:
                            trev.sendText(msg.to,"「􏿿Respond」\n ALREADY SET: ON")
            elif msg.text in [frederick["trevor"]+"autojoin:off"]:
                if msg.from_ in Mike:
                    if wait["AutoJoin"] == False:
                            trev.sendText(msg.to,"「􏿿Auto Join」 SET: OFF")
                    else:
                            trev.sendText(msg.to,"「􏿿Respond」\nALREADY SET: OFF")

#--------------------------------------------------------
	    elif msg.text in [frederick["trevor"]+"autocancel:on"]:
                wait["AutoCancel"] = True
                trev.sendText(msg.to,"The group of people and below decided to automatically refuse invitation")


	    elif msg.text in [frederick["trevor"]+"autocancel:on"]:
                wait["AutoCancel"] = False
                trev.sendText(msg.to,"Invitation refused turned off")

#--------------------------------------------------------

#----------------------------------------------------------
	    elif msg.text in [frederick["trevor"]+"qr:on"]:
	        wait["Qr"] = True
	    	trev.sendText(msg.to,"QR Protect Active")

	    elif msg.text in [frederick["trevor"]+"qr:off"]:
	    	wait["Qr"] = False
	    	trev.sendText(msg.to,"Qr Protect inActive")
	    elif msg.text in [frederick["trevor"]+"leavemultichat:on"]:
	        wait["LeaveRoom"] = True
	        trev.sendText(msg.to,"Auto Leave Multi Chat ON")
	    elif msg.text in [frederick["trevor"]+"leavemultichat:off"]:
	        wait["LeaveRoom"] = False
	        trev.sendText(msg.to,"Auto Leave Multi Chat OFF")
	    elif msg.text in [frederick["trevor"]+"autoreject:on"]:
	        wait["autoCancel"]["on"] = True
	        trev.sendText(msg.to,"Auto Reject Invitation Group\n SET:ON")
	    elif msg.text in [frederick["trevor"]+"autoreject:off"]:
	        wait["autoCancel"]["on"] = False
	        trev.sendText(msg.to,"Auto Reject Invitation Group\n SET:OFF")
#--------------------------------------------------------
#--------------------------------------------------------
            elif msg.text in [frederick["trevor"]+"joinkuy"]:
                wait["autoJoinTicket"] = True
                trev.sendText(msg.to,"Kita join kakak")
            elif msg.text in [frederick["trevor"]+"janganjoin"]:
                wait["autoJoinTicket"] = False
                trev.sendText(msg.to,"Kita gamau join kakak")
            elif msg.text in [frederick["trevor"]+"contact on"]:
                wait["Contact"] = True
                trev.sendText(msg.to,"Contact Active")

            elif msg.text in [frederick["trevor"]+"contact off"]:
                wait["Contact"] = False
                trev.sendText(msg.to,"Contact inActive")
#--------------------------------------------------------
            elif msg.text in [frederick["trevor"]+"set"]:
            	if msg.from_ in Mike:
            	    trev.sendText(msg.to,"❤selfbot ❤\n"+
"  ❤ ᴛʀᴇᴠᴏʀ ❤\n"+
"\n"+
"▶️"+frederick["trevor"]+"autokick:\n"+
"▶️ "+frederick["trevor"]+"qr:\n"+
"▶️ "+frederick["trevor"]+"leavemultichat: \n"
"▶️ "+frederick["trevor"]+"autocancel:\n"+
"▶️ "+frederick["trevor"]+"autojoin: \n"+
"Seperti ini:\n"
" ▶️ PILIH SATU : on/off」\n"+
" ▶️ CONTOH: autojoin:on」\n"+
" ▶️ GUNAKAN 「"+frederick["trevor"]+"」 BIAR BERHASIL\n izin dulu kalau mau di remake🙏")
#--------------------------------------------------------
            
            #--------------------------------------------------------
            elif 'pengangguran' in msg.text.lower():
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "5508",
                                     "STKPKGID": "608",
                                     "STKVER": "16" }
                trev.sendMessage(msg)
            elif 'muka tua' in msg.text.lower():
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "5508",
                                     "STKPKGID": "608",
                                     "STKVER": "16" }
                trev.sendMessage(msg)    
            elif msg.text in ["muka jelek"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "5508",
                                     "STKPKGID": "608",
                                     "STKVER": "16" }
                trev.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                trev.sendMessage(msg)


            elif msg.text in ["Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                trev.sendMessage(msg)

            elif msg.text in ["Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                trev.sendMessage(msg)

            elif msg.text in ["Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                trev.sendMessage(msg)

#--------------------------------------------------------

#--------------------------CEK SIDER------------------------------

           
#--------------------------------------------------------

#KICK_BY_TAG
	    elif (frederick["trevor"]+"trevkick " in msg.text):
		if 'MENTION' in msg.contentMetadata.keys()!= None:
		    names = re.findall(r'@(\w+)', msg.text)
		    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		    mentionees = mention['MENTIONEES']
		    print mentionees
		    for mention in mentionees:
			trev.kickoutFromGroup(msg.to,[mention['M']])

#--------------------------------------------------------
	    elif (frederick["trevor"]+"addall" in msg.text):
		thisgroup = trev.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		trev.findAndAddContactsByMids(mi_d)
		trev.sendText(msg.to,"Success Add all")
#--------------------------------------------------------
	    elif (frederick["trevor"]+"recover" in msg.text):
		thisgroup = trev.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		trev.createGroup("Recover", mi_d)
		trev.sendText(msg.to,"Success recover")
#--------------------------------------------------------
	    elif msg.text in ["Remove all chat"]:
		trev.removeAllMessages(op.param2)
		trev.sendText(msg.to,"Removed all chat")
#--------------------------------------------------------
            elif (frederick["trevor"]+"gname: " in msg.text):
            	if msg.from_ in Mike:
                    if msg.toType == 2:
                        X = trev.getGroup(msg.to)
                        X.name = msg.text.replace(frederick["trevor"]+"gname: ","")
                        trev.updateGroup(X)
                        trev.sendText(msg.to,"Status: Success \n Changed to: " + X)
                    else:
                        trev.sendText(msg.to,"[Respond] it can't be used besides the group.")
#--------------------------------------------------------
            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		if midd not in Mike:
		    trev.kickoutFromGroup(msg.to,[midd])
		else:
		    trev.sendText(msg.to,"Admin Detected")
#--------------------------------------------------------

#--------------------------------------------------------
            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                trev.findAndAddContactsByMid(midd)
                trev.inviteIntoGroup(msg.to,[midd])
#--------------------------------------------------------
            elif msg.text in ["#welcome","Welcome","welcome","Welkam","welkam"]:
                gs = trev.getGroup(msg.to)
                trev.sendText(msg.to,"Selamat datang di "+ gs.name)
#--------------------------------------------------------
	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = trev.getGroupIdsJoined()
		for i in gid:
		    trev.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/~azhura07_")
		trev.sendText(msg.to,"Sukses Trev!\n Pesan Broadcast:"+ bc)
#--------------------------------------------------------
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "??? Running ?\n? Running Time is: \n"+waktu(eltime)
                trev.sendText(msg.to,van)
            elif msg.text in [frederick["trevor"]+"cancelall"]:
                gid = trev.getGroupIdsInvited()
                for i in gid:
                    trev.rejectGroupInvitation(i)
                trev.sendText(msg.to,"All invitations have been refused")
#--------------------------------------------------------
            elif msg.text in [frederick["trevor"]+"gurl","get url"]:
                if msg.toType == 2:
                    x = trev.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        trev.updateGroup(x)
                    gurl = trev.reissueGroupTicket(msg.to)
                    trev.sendText(msg.to,"「􏿿 Link Group 」\n line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        trev.sendText(msg.to,"Can't be used outside the group")
                    else:
                        trev.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------------
	    elif msg.text in ["Self Like"]:
		try:
		    print "activity"
		    url = trev.activity(limit=1)
		    print url
		    trev.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    trev.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Follow ig : @mikef.s")
		    trev.sendText(msg.to, "Success~")
		except Exception as E:
		    try:
			trev.sendText(msg.to,str(E))
		    except:
			pass

#--------------------------------------------------------
	    elif msg.text in [frederick["trevor"]+"autoread:on"]:
                    wait["pembaca"] = True
                    trev.sendText(msg.to,"Autoread Set: ON")
            elif msg.text in [frederick["trevor"]+"autoread:off"]:
                    wait["pembaca"] = False
                    trev.sendText(msg.to,"Autoread Set: OFF")
            elif msg.text in [frederick["trevor"]+"trevrespon:on"]:
                    wait["trevrespon"] = True
                    trev.sendText(msg.to,"Autorespon for personal chat set:on")
            elif msg.text in [frederick["trevor"]+"trevrespon:off"]:
                    wait["trevrespon"] = False
                    trev.sendText(msg.to,"Autorespon for personal chat set:off")
            elif msg.text in [frederick["trevor"]+"sp","speed",frederick["trevor"]+"debug"]:
                start =time.time()
                trev.sendText(msg.to,"Wait trev...")
                enlapsed_time = time.time() -start
                trev.sendText(msg.to,"%s Seconds" % (enlapsed_time))
#--------------------------------------------------------
            elif (frederick["trevor"]+"cname: " in msg.text):
                if msg.from_ in Mike:
                    profile = trev.getProfile()
                    X = msg.text.replace(frederick["trevor"]+"cname: ","")
                    profile.displayName = X
                    trev.updateProfile(profile)
                    trev.sendText(msg.to,"Success Change To: " + X)
                else:
                    trev.sendText(msg.to,"Failed")
#--------------------------------------------------------
            elif msg.text in [frederick["trevor"]+"help"]:
            	if msg.from_ in Mike:
            	    trev.sendText(msg.to,"ѕєℓfвσт \n™ᴠᴇʀsɪᴏɴ™\n"+
"  ᴛʀᴇᴠᴏʀ\n\n"+
"▶️"+frederick["trevor"]+"speed\n"+
"▶️"+frederick["trevor"]+"cname: \n"+
"▶️"+frederick["trevor"]+"gurl\n"+
"▶️"+frederick["trevor"]+"gname:  \n"+
"▶️"+frederick["trevor"]+"set \n"+
"▶️"+frederick["trevor"]+"media \n"+
"▶️"+frederick["trevor"]+"backup\n"+
"▶️"+frederick["trevor"]+"system\n"+
"▶️"+frederick["trevor"]+"clone \n"+
"▶️"+frederick["trevor"]+"set\n"+
"▶️「trevkey」\n"+
"   gunakan 「"+frederick["trevor"]+"」 utamakan huruf kecil")
            elif msg.text in [frederick["trevor"]+"media"]:
            	if msg.from_ in Mike:
            	    trev.sendText(msg.to,"ѕєℓfвσт\νєяѕισи\n"+
"  мє∂ια\n"+
"\n"+
"▶️"+frederick["trevor"]+"ytube:\n"+
"▶"+frederick["trevor"]+"geturl:\n"++
"   gυиαкαи 「"+frederick["trevor"]+"」\nвιαя кєяα∂")
#--------------------------------------------------------
            elif frederick["trevor"]+"geturl: " in msg.text.lower():
                        sep = msg.text.lower().replace(frederick["trevor"]+"geturl: ","")                                                                                                                            
                        with requests.session() as web:
                                r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib2.quote(sep)))
                                data = r.text
                                data = json.loads(data)
                                trev.sendImageWithURL(msg.to, data["result"])
            if frederick["trevor"]+"ytube: " in msg.text.lower():
            	trev.sendText(msg.to,"「􏿿 Youtube 」\nWaiting For: Youtube")
		query = msg.text.split(":")
		try:
		    if len(query) == 3:
	  	        isi = yt(query[2])
		        hasil = isi[int(query[1])-1]
		        trev.sendText(msg.to, 'Total search = ' + str(len(isi)) + " ini adalah hasil pencarian ke [" + str(query[1]) + "]")
		        trev.sendText(msg.to,"「􏿿 Youtube 」\n\nWaiting For Search Youtube..")
		        trev.sendText(msg.to, hasil)
		    else:
	                isi = yt(query[1])				
                        trev.sendText(msg.to, "Total search = " + str(len(isi)))
		        trev.sendText(msg.to, isi[0])
		        trev.sendAudio(msg.to, isi[0])
	 	except Exception as e:
	            print(e)

                
            elif msg.text in ["reset trev"]:
            	if msg.from_ in Mike:
            	    frederick["trevor"] = ""
                    trev.sendText(msg.to,"Reset Key Success")
            elif msg.text in ["trevkey"]:
            	    trev.sendText(msg.to,"「Trev Key 」\n Key Active is: 「" + frederick["trevor"] + "」")
            elif ("trevchange: " in msg.text):
            	    frederick["trevor"] = msg.text.replace("trevchange: ","")
                    trev.sendText(msg.to,"Set Trevkey To: 「" + frederick["trevor"] + "」 Success")
#--------------------------------------------------------
            elif msg.text in [frederick["trevor"]+"ban"]:
                wait["wblacklist"] = True
                trev.sendText(msg.to,"send contact")

            elif msg.text in [frederick["trevor"]+"unban"]:
                wait["dblacklist"] = True
                trev.sendText(msg.to,"send contact")
#--------------------------------------------------------
                    
	    elif msg.text in [frederick["trevor"]+"backup"]:
                try:
                    trev.updateDisplayPicture(backup.pictureStatus)
                    trev.updateProfile(backup)
                    trev.sendText(msg.to, "Status: success back profile")
                except Exception as e:
                    trev.sendText(msg.to, str(e))
            elif "setspam: " in msg.text:
                wait["spam"] = msg.text.replace("setspam: ","")
                trev.sendText(msg.to,"Spam Text has been set to: "+ wait["spam"])
                
            elif "spam: " in msg.text:
                strnum = msg.text.replace("spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    trev.sendText(msg.to, wait["spam"])
#--------------------------------------------------------
	    elif (frederick["trevor"]+"clone " in msg.text):
                if msg.from_ in Mike:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            trev.CloneContactProfile(target)
                            trev.sendText(msg.to,"「􏿿 Cloning 」\n Type: Clone Profile\n Status: Success~")
                        except Exception as e:
                            print e

#--------------------------------------------------------
            elif (frederick["trevor"]+"ban @ " in msg.text):
                if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace(frederick["trevor"]+"ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = trev.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        trev.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in Mike:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    trev.sendText(msg.to,"Succes BosQ")
                                except:
                                    trev.sendText(msg.to,"Error")
			    else:
				trev.sendText(msg.to,"Admin Detected~")
#--------------------------------------------------------
            elif msg.text in [frederick["trevor"]+"banlist"]:
                if wait["blacklist"] == {}:
                    trev.sendText(msg.to,"nothing")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +trev.getContact(mi_d).displayName + "\n"
                    trev.sendText(msg.to,"👉[вℓα¢кℓιѕт υѕєя]👈\n"+mc)

#--------------------------------------------------------
            elif (frederick["trevor"]+"unban @ " in msg.text):
                if msg.toType == 2:
                    print "@Unban by mention"
                    _name = msg.text.replace(frederick["trevor"]+"unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = trev.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        trev.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                trev.sendText(msg.to,"Succes BosQ")
                            except:
                                trev.sendText(msg.to,"Succes BosQ")
#--------------------------------------------------------
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = trev.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        trev.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        trev.kickoutFromGroup(msg.to,[jj])
                    trev.sendText(msg.to,"Blacklist emang pantas tuk di usir")
#—–—––—--------------------------------------------------------------------------------------------------
#Restart_Program
	    elif msg.text in [frederick["trevor"]+"restart"]:
		trev.sendText(msg.to, "Bot has been restarted")
		restart_program()
		print "@Restart"
#--------------------------------------------------------
        if op.type == 26:
            msg = op.message
            if wait["trevrespon"] == True:
                if msg.toType == 0:                	
                    trev.sendChatChecked(msg.from_,msg.id)
                    contact = trev.getContact(msg.from_)
                    cName = contact.displayName
                    responft = "http://oi66.tinypic.com/10z4q36.jpg"
                    balas = ["Hallo 「" + cName + "」\nMohon Maaf Saya Sedang Sibuk, Ini Adalah Pesan Otomatis, Jika Ada Yang Penting Mohon Hubungi Saya Nanti, Terimakasih...","Lagi sibuk ya kak jangan diganggu","saya sedang tidur kak"]
                    trevor = "" + random.choice(balas)
                    trev.sendImageWithURL(msg.from_, responft)
                    trev.sendText(msg.from_,trevor)
        if wait["pembaca"] == True:     
                if msg.toType == 0:
                    trev.sendChatChecked(msg.from_,msg.id)
                else:
                    trev.sendChatChecked(msg.to,msg.id)

                    
        if op.type == 59:
            print op


    except Exception as error:
        print error


#thread2 = threading.Thread(target=nameUpdate)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = trev.fetchOps(trev.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(trev.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            trev.Poll.rev = max(trev.Poll.rev, Op.revision)
            bot(Op)
