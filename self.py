# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, urllib3, wikipedia,tempfile,ast,glob,shutil,unicodedata,goslate
#import html5lib
#import pafy

#admin
cl = LINETCR.LINE()
cl.login(token="EvReYAF3Zwo6aNb7Oicc.cpeslY3m06zcIbJU1zRCpa.5j+owTVHDwzNXtt/x+SHb0k0pXpPtPDZbK74U/N4lDo=")
cl.loginResult()

print u"Bearbot login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""  〘🔰prillyƒᴀᴍɪʟʏ™〙\n              ⱽ².⁰⁴
╔ ══════════════ ╗
      【Ҁомᴍᴀɴᴅ ꜱᴇʟꜰ】
╠ ══════════════ ╝
╠☛ Me
╠☛ Mymid
╠☛ MyName:
╠☛ Mybio: 「 Isi Bio 」
╠☛ TL:  「 Text  」
╠☛ Mid     「 By Tag 」
╠☛ Cek     「 By Tag 」
╠☛ Gift
╠☛ Searchid:
╠☛ Makeidlink:
╠☛ Removechat
╠☛ Bear1-6 Rchat
╠☛ BearBot Rchat
╠☛ Sider
╠☛ Ciduk
╠☛ Setlastpoint
╠☛ Viewlastseen
╠☛ Pesan add: 「 Text  」
╠☛ Pesan add cek
╠☛ 1name:  「 Text  」
╠☛ 2name:  「 Text  」
╠☛ 3name:  「 Text  」
╠☛ 4name:  「 Text  」
╠☛ 5name:  「 Text  」
╠☛ 6name:  「 Text  」
╠☛ 7name:  「 Text  」
╠☛ Allbio:「 Isi Bio semua bot 」
╠☛ All:   「 Gnti Nma smua bot 」
╠☛ Bear1 clone:  「 By Tag 」
╠☛ Bear2 clone:  「 By Tag 」
╠☛ Bear3 clone:  「 By Tag 」
╠☛ Bear4 clone:  「 By Tag 」
╠☛ Bear5 clone:  「 By Tag 」
╠☛ Bear6 clone:  「 By Tag 」
╠☛ Bear7 clone:  「 By Tag 」
╠☛ Backup [sprt awl bot]
╠☛ hmm  (u/ asist msk k grup)
╠☛ cabut (u/ asist kluar grup)
╠☛ runtime
╠☛ Restart
╠☛ Bear turn off
╚════════════════
╔═══════════════╗
    • ʙᴏᴛ ᴀᴜᴛᴏ ꜱᴇᴛᴛɪɴɢꜱ • 
╠═══════════════╝
╠☛ Auto join
╠☛ Auto joinleave
╠☛ Auto leave
╠☛ Auto add
╠☛ Auto comment
╠☛ Contact
╠☛ Rejectall
╠☛ Welcome message
╠☛ Leave message
╠☛ settings
║(Gunakan on/off untk-
║-memtikn & mnghidpkn)
╚════════════════╝
    ╔═══════ ═══════╗
 ◄▂▄ıllıı ᴍᴏᴅᴇ ᴩʀᴏᴛᴇᴄᴛ ılllı▄▂►
╔══╩════════════╩╗
╠☛ Mode easy          ║✔
╠☛ Mode hard          ║✔
╚════════════════╝
╔ ═══════════════ ╗
    【ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴩ】
╠ ═══════════════ ╝
╠☛ Tagall
╠☛ Invite 「by mid」
╠☛ Ginfo
╠☛ Group cancel
╠☛ Gn 「Nama grup」
╠☛ Gcreator
╠☛ Cancel
╠☛ Link on
╠☛ Link off
╠☛ Url
╠☛ Update Joinleave:
╠☛ Update Wmessage:
╠☛ Update Lmessage:
╠☛ Check Joinleave
╠☛ Check Wmessage
╠☛ Check Lmessage
╠☛ Bans:on
╠☛ Unbans:on
╠☛ Ban:
╠☛ Unban:
╠☛ Ban   「 By Tag 」
╠☛ Unban 「 By Tag 」
╠════════════════╗
╠════════════════╗
║ ＰＲＯＴＥＣＴ ＧＲＯＵＰ               
╠════════════════╝
╠☛ Protect
╠☛ Qrprotect
╠☛ Inviteprotect
╠☛ Cancelprotect
║(Gunakan on/off untk-
║-memtikn & mnghidpkn)
╚═════════════//''
╔ ════════════ ╗
【      ᴀʙᴏᴜᴛ [ⓉⒶⒼ]                  
╠ ════════════ ╝
╠☛ Arespon
╠☛ Arespon2
╠☛ Arespon3
╠☛ Notag
╠☛ Sider tag
╠☛ settings tag
║(Gunakan on/off untk-
║-memtikn & mnghidpkn)
╚═════════════╝
╔ ═════════ ╗
【     STEALING
╠ ═════════ ╝
╠☛ Steal pict
╠☛ Steal cover
╠☛ Steal contact
╠☛ Steal mid
╠☛ Steal bio
╠☛ Steal name
╚═══════════╝
╔════════════════╗
【       ★ ᴋɪᴄᴋᴇʀ ᴍᴏᴅᴇ ★
╠════════════════╝
╠☛ Cleanse
╠☛ sapu
╠☛ Beb
╠☛ Kmid: Kick by mid
╠☛ Bunuh 「 By Tag 」
╠☛ Bear1-6 bunuh 「 By Tag 」
╠☛ Nk  「 By Tag 」
╚═════════════════╝
╔════════════════╗
        • ᴄʜᴀᴛ ʀᴇʟᴀᴛᴇᴅ •
╠════════════════╝
╠☛ Creator
╠☛ respons
╠☛ Speed
╠☛ Ifconfig
╠☛ Kernel
╠☛ System
╠☛ Cpu
╠☛ Help
╠☛ Bear 「 Kontak smua bot 」
╠☛ Spam add: 「 Text 」
╠☛ Spam: 「 Jumlah 」
╠☛ Spam full (Jml) + 「 Text  」
╠☛ Spam +   (Jml) + 「 Text  」
╠☛ Bc 「 Text 」
╠☛ Hay 「 By Tag 」
╚══════════════════╝
╔════════════════╗
             • ＵＴＩＬＩＴＹ • 
╠════════════════╝
╠☛ /say 「 Text 」
╠☛ /say-en 「 Text 」
╠☛ /say-sunda 「 Text 」
╠☛ /say-jawa 「 Text 」
╠☛ tr-en:
╠☛ tr-fr:
╠☛ tr-ar:
╠☛ tr-cn:
╠☛ tr-de:
╠☛ tr-hi:
╠☛ tr-jp:
╠☛ tr-jw:
╠☛ tr-ko:
╠☛ tr-th:
╠☛ Dosa @
╠☛ Siapa
╠☛ Image
╠☛ Wiki
╠☛ Music
╠☛ .Youtube
╠☛ Vidio
╠☛ Instagram
╚══════════════╝
╔════════════════╗
             • ʙʀᴏᴀᴅᴄᴀꜱᴛᴇʀ • 
╠════════════════╝
╠☛ /Brod 「 Text 」
╠☛ /Bcgrup    「 Text 」
╚════════════════╝
╔════════════════╗
              • View List • 
╠════════════════╝
╠☛ Banlist
╠☛ Mcheck
╠☛ Cban
╠☛ Glist
╠☛ gidlist
╠☛ Bear1-6 gidlist
╠☛ Flist
╠☛ Get mem [nama grup]
╚════════════════╝
==================
 ╔══════════════════╗
            🤘😂🤘 ᴮⁱᵍ ᵀʰᵃⁿᵏˢ ᵗᵒ  :
╔══╩═════════════╩══╗
║► ᴹʸ ᵀᵉᵃᵐ    [R̲̅]•[Y̲̅[S̲̅[H̲̅]             
║► ᴬˡˡ ᶠʳⁱᵉⁿᵈˢ   ₛᵤₚₚₒᵣₜ
╚═══════════════════╝
[ V2.04 ] ᴄʀᴇᴀᴛᴇᴅ ʙy:
〘 line.me/ti/p/~rhanda07 〙
"""
prilly=""

KAC=[cl]
mid = cl.getProfile().mid
#kimid = ki.getProfile().mid
#ki2mid = ki2.getProfile().mid
#ki3mid = ki3.getProfile().mid
#ki4mid = ki4.getProfile().mid
#ki5mid = ki5.getProfile().mid
#ki6mid = ki6.getProfile().mid
#ki7mid = ki7.getProfile().mid
Bots = [mid]
owner ="u08f1122f2dccd3a6428818eed59adc3c"
admin="u08f1122f2dccd3a6428818eed59adc3c"
wait = {
    'contact':False,
    'autoJoin':False,
    'autoJoinLeave':False,
    'likeOn':True,
    "jlmsg":"Gausah asal jepit lu",
    'autoCancel':{"on":False, "members":1},
    'leaveRoom':False,
    "timeline":True,
    'autoAdd':True,
    'message':"Ciee yg ng-add??,",
    "lang":"JP",
    "comment":"▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩\n  ☞ ✬ᴀ͟͟͟͞͞͞ᴜ͟͟͟͞͞͞ᴛ͟͟͟͞͞͞ᴏ͟͟͟͞͞͞ ʟ͟͟͟͞͞͞ɪ͟͟͟͞͞͞ᴋ͟͟͟͞͞͞ᴇ͟͟͟͞͞͞ ʙ͟͟͟͞ʏ:✬ ☜\n\n➥ 〘🔰Ꮔᵁᴵᵀᴬƒᴀᴍɪʟʏ™〙\n▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩\n   ☞ ▣ ᴄʀᴇᴀᴛᴏʀ ▣ ☜\n\n➦ ⇱ line.me/ti/p/~rhanda07 ⇲ \n▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩", 
    "comment2":"▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩\n  ☞ ✬ᴀ͟͟͟͞͞͞ᴜ͟͟͟͞͞͞ᴛ͟͟͟͞͞͞ᴏ͟͟͟͞͞͞ ʟ͟͟͟͞͞͞ɪ͟͟͟͞͞͞ᴋ͟͟͟͞͞͞ᴇ͟͟͟͞͞͞ ʙ͟͟͟͞ʏ:✬ ☜\n\n➥ 〘🔰Ꮔᵁᴵᵀᴬƒᴀᴍɪʟʏ™〙\n▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩\n   ☞ ▣ ᴄʀᴇᴀᴛᴏʀ ▣ ☜\n\n➦ ⇱ line.me/ti/p/~rhanda07 ⇲ \n▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩",     
    "commentOn":False,
    "commentBlack":{},
    "welmsg":"welcome to group",
    "levmsg":" muka baper left",
    "welcomemsg":False,
    "leavemsg":False,
    "wblack":False,
    "dblack":False,
    "clock":False,
    "status":False,
    "cNames":"",
    "cNames":"",
    "Arespon":False,
    "Arespon2":False,
    "Arespon3":False,
    "mresp3K":"405839",
    "mresp3G":"1008517",
    "mresp3":"apahan tong",
    "mresp2":"lu iklan sabun colek?",
    "mresp":"[AUTO RESPON]\n\nLagi off sementara",
    "Notag":False,
    "mention":{},
    "mention":True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "talkblacklist":{},  
    "talkblacklist":False,
    "talkwblacklist":{},  
    "talkwblacklist":False,
    "talkban":False,
    "untalk":False,    
    "kick":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "sticker":False,
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
res = {
    'num':{},
    'us':{},
    'au':{},
}

with open('st2__b.json','r') as fp:
    wait["blacklist"] = json.load(fp)

setTime = {}
setTime = wait2['setTime']

mulai = time.time()

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
  
def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
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

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
mulai = time.time()

def removeAllMessages(self, lastMessageId):
	return self.Talk.client.removeAllMessages(0, lastMessageId)

def createGroup(self, name, midlist):
    return self.Talk.client.createGroup(0, name, midlist)

def sendMessage(self, messageObject):
    return self.Talk.client.sendMessage(0,messageObject)

def like(self, mid, postid, likeType=1001):
    return self.channel.like(mid, postid, likeType)

def comment(self, mid, postid, text):
    return self.channel.comment(mid, postid, text)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)

def sendSticker(self, to, packageId, stickerId):
        contentMetadata = {
            'STKVER': '100',
            'STKPKGID': packageId,
            'STKID': stickerId
        }
        return self.sendMessage(to, '', contentMetadata, 7)

def sendGift(self, productId, productType):
        if productType not in ['theme','sticker']:
            raise Exception('Invalid productType value')
        contentMetadata = {
            'MSGTPL': str(randint(0, 12)),
            'PRDTYPE': productType.upper(),
            'STKPKGID' if productType == 'sticker' else 'PRDID': productId
        }
        return self.sendMessage(to, '', contentMetadata, 9)
      
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
         
def sendVideo(self, to_, path):
      M = Message(to=to_,contentType = 2)
      M.contentMetadata = {
          'VIDLEN' : '0',
              'DURATION' : '0'
        }
      M.contentPreview = None
      M_id = self.Talk.client.sendMessage(0,M).id
      files = {
            'file': open(path, 'rb'),
        }
      params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'video',
            'ver': '1.0',
        }
      data = {
            'params': json.dumps(params)
        }
      r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
            raise Exception('Upload image failure.')
      return True

def sendVideoWithURL(self, to_, url):
        path = 'pythonLines.data'
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
               shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download Audio failure.')
        try:
            self.sendVideo(to_, path)
        except Exception as e:
            raise e         
                                                     
def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
        
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def NOTIFIED_READ_MESSAGE(op):
    print op
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name + datetime.now().strftime(' [%d - %H:%M:%S]')
                wait2['ROM'][op.param1][op.param2] = "・" + Name + " ツ"
        else:
            pass
    except:
        pass
                   
def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg.from_ in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
          
    except KeyboardInterrupt:
				sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

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
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error		
		
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)
             
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
		
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                if wait["autoJoinLeave"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1,".􀜁􀄄Boring􏿿" + wait["jlmsg"])
                        cl.leaveGroup(op.param1)                
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
#-------------------WELCOME/LEAVE MESSAGE----------------------
        if op.type == 15:
	   if wait["leavemsg"] == True:            
              if op.param2 not in Bots:
                 ginfo = cl.getGroup(op.param1)
                 contact = cl.getContact(op.param2)
                 path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                 cl.sendImageWithURL(op.param1,path)
                 cl.sendText(op.param1,cl.getContact(op.param2).displayName + wait["levmsg"])

        if op.type == 17:
	   if wait["welcomemsg"] == True:
              if op.param2 not in Bots:
                 ginfo = cl.getGroup(op.param1)
                 cl.sendText(op.param1,cl.getContact(op.param2).displayName + wait["welmsg"]+ str(ginfo.name))
#-------------------NOTIFIED_READ_MESSAGE----------------
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
#===========================================
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 19:
             if op.param2 in Bots:
                   if op.param3 in admin:
                      random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
        if op.type == 19:
             if not op.param2 in Bots:
                   if op.param3 in admin:
                      random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])                
#===========================================
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)                
        if op.type == 26:
            msg = op.message
            if "@"+cl.getProfile().displayName in msg.text:
                if wait["Arespon"] == True:
                    tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
                    jawab = (cl.getProfile().displayName + wait["mresp"])
                    jawaban = (jawab)
                    cl.sendText(msg.to,jawaban)
        if op.type == 26:
            msg = op.message
            if 'MENTION' in msg.contentMetadata.keys() != None:
              if wait["Arespon2"] == True:
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = [cName + "\n" + wait["mresp2"]]
                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus                
                    ret_ = "????Boring??" + random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.sendImageWithURL(msg.to,path)
                                  break
    	if op.type == 26:
            msg = op.message
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Arespon3"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = [cName + "\n" + wait["mresp3"]]
                    ret_ = "􀜁􀄄Boring􏿿" + random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": wait["mresp3K"],
                                                       "STKPKGID": wait["mresp3G"],
                                                       "STKVER": "1" }
                                  cl.sendMessage(msg)                                                                    
                                  break                                          

#==================================================================================  
	    if 'MENTION' in msg.contentMetadata.keys() != None:
               if wait ["Notag"] == True:
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = [cName + " Dont tag me, im busy",cName + " Dihh si jones nge tag",cName + " Gak usah tag.klo pnting pc aja",cName +" Jones diLarang keras sebut² nama gue ヽ(^0^)ﾉ"]
                    ret_ = "[NOTAG] " + random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
				  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break
#------------------------[Auto respon tag]---------------------------                                        
#=================================================
	    if op.type == 46:
	        if op.param2 in Bots:
		    ki.removeAllMessages(op.param2)
		    ki2.removeAllMessages(op.param2)
		    ki3.removeAllMessages(op.param2)
		    ki4.removeAllMessages(op.param2)
		    ki5.removeAllMessages(op.param2)
		    ki6.removeAllMessages(op.param2)
		    ki7.removeAllMessages(op.param2)
#=================================================		    
#------Cek Sider-----#
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                #cl.mention(op.param1, op.param2)
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Ngapain ngintip doang?\nIkut nimbrung sini ka...    " +nick[0])
                                        #random.choice(KAC).kickoutFromGroup(op.param1, [op.param2])
                                    else:
                                        cl.sendText(op.param1, "Ngapain ngintip doang?\nIkut nimbrung sini ka...  " +nick[1])
                                        #random.choice(KAC).kickoutFromGroup(op.param1, [op.param2])
                                else:
                                    cl.sendText(op.param1, "Ngapain ngintip doang?\nIkut nimbrung sini ka...   " +Name)
                                    #random.choice(KAC).kickoutFromGroup(op.param1, [op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass
#----------------------------------------

        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "ub5661b8c4a141c7532cbc2b59a2d0274":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
                            
        if op.type == 26:
            msg = op.message
            
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     cl.like(url[25:58], url[66:], likeType=1001)                    
                     cl.comment(url[25:58], url[66:], wait["comment2"])                             
                     cl.sendText(msg.to,"『ʟɪᴋᴇ sᴜᴄᴄᴇss ☑』")                     
                     wait['likeOn'] = False
                    
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " sdh dsni pekok")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Gausah, " + _name + " dia msk blacklist")
                                 ki.sendText(msg.to,"Klo mau unban dlu nih !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"⎈ Profile Name :\n" + msg.contentMetadata["displayName"] + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Message :\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu) + "\n\n [☸]➦Powered By: メTamii々•┅─────")
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"⎈ Profile Name :\n" + contact.displayName + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Mesage:\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu) + "\n\n [☸]➦Powered By: メTamii々•┅─────")
            elif msg.contentType == 16:
                if wait["contact"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL→\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)

            elif msg.contentType == 7: 
                if wait["sticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "Sticker Detection.\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\nThats link:\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    cl.sendText(msg.to, filler)
                else:
                    pass                    

            elif msg.contentType == 16:
                if wait["contact"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL→\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
              if msg.from_ in Bots:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
            elif msg.text in ["Invite:on"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Can not be used for groups other than")
            elif msg.text.lower() == 'runtime':
                 eltime = time.time() - mulai
                 van = "Actived "+waktu(eltime)
                 cl.sendText(msg.to,van)
            elif msg.text in ["Restart"]:
                 cl.sendText(msg.to, "Succes Restarted")
                 restart_program()
                 print "@Restart"
            elif "Bear turn off" in msg.text:
               if msg.from_ in owner:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass                 
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Bear" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg) 
            elif "Bear1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "Bear2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)

            elif msg.text in ["Bear1 Gift","Han1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Bear2 Gift","Han2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)

            elif msg.text in ["B Cancel","Cancel dong","B cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")

            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")

            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open")
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close👈")
                    else:
                        cl.sendText(msg.to,"URL close👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œ")
            
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")

            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)                
#==============================================================================#
            elif "Id" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,msg.to)
            elif "Mymid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Bear1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "Bear2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "Bear3 mid" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "Han4 mid" == msg.text:
                ki4.sendText(msg.to,ki4mid)
            elif "Han5 mid" == msg.text:
                ki5.sendText(msg.to,ki5id)
            elif "Han6 mid" == msg.text:
                ki6.sendText(msg.to,ki6mid)
            elif "Han7 mid" == msg.text:
                ki7.sendText(msg.to,ki7mid)    
            elif "all mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki6mid)
                ki7.sendText(msg.to,ki6mid)                
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Allname:" in msg.text:
                string = msg.text.replace("Allname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
                    profile = ki7.getProfile()
                    profile.statusMessage = string
                    ki7.updateProfile(profile)
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈")
            elif "Mybio:" in msg.text:
                string = msg.text.replace("Mybio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Bio👉 " + string + "�")
            elif "Searchid: " in msg.text:
                msgg = msg.text.replace('Searchid: ','')
                conn = cl.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    #cl.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    cl.sendMessage(msg)
            elif "Makeidlink: " in msg.text:
                msgg = msg.text.replace('Makeidlink: ','')
                conn = cl.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    #msg.contentMetadata = {'mid': conn.mid}
                    cl.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    cl.sendMessage(msg)
#======================================================================================
#SC Remove all chat#
            #elif "Removechat" in msg.text:
              #if msg.from_ in admin or msg.from_ in staff:
                #try:
                    #cl.removeAllMessages(op.param2)
                    #cl.sendText(msg.to,"Chat telah dihapus")
                    #print "Success Remove Chat"
                #except:
                    #pass
            elif "Bear1 Rchat" in msg.text:
              if msg.from_ in admin or msg.from_ in staff:
                try:
                    ki.removeAllMessages(op.param2)
                    cl.sendText(msg.to,"Chat di Bear1 telah dihapus")
                    print "Success Remove Chat"
                except:
                    pass
            elif "Bear2 Rchat" in msg.text:
              if msg.from_ in admin or msg.from_ in staff:
                try:
                    ki2.removeAllMessages(op.param2)
                    cl.sendText(msg.to,"Chat di Bear2 telah dihapus")
                    print "Success Remove Chat"
                except:
                    pass
            elif "Bear3 Rchat" in msg.text:
              if msg.from_ in admin or msg.from_ in staff:
                try:
                    ki3.removeAllMessages(op.param2)
                    cl.sendText(msg.to,"Chat di Bear3 telah dihapus")
                    print "Success Remove Chat"
                except:
                    pass
            elif "Bear4 Rchat" in msg.text:
              if msg.from_ in admin or msg.from_ in staff:
                try:
                    ki4.removeAllMessages(op.param2)
                    cl.sendText(msg.to,"Chat di Bear4 telah dihapus")
                    print "Success Remove Chat"
                except:
                    pass
            elif "Bear5 Rchat" in msg.text:
              if msg.from_ in admin or msg.from_ in staff:
                try:
                    ki5.removeAllMessages(op.param2)
                    cl.sendText(msg.to,"Chat di Bear5 telah dihapus")
                    print "Success Remove Chat"
                except:
                    pass
            elif "Bear6 Rchat" in msg.text:
              if msg.from_ in admin or msg.from_ in staff:
                try:
                    ki6.removeAllMessages(op.param2)
                    cl.sendText(msg.to,"Chat di Bear6 telah dihapus")
                    print "Success Remove Chat"
                except:
                    pass
            elif "Bear7 Rchat" in msg.text:
              if msg.from_ in admin or msg.from_ in staff:
                try:
                    ki7.removeAllMessages(op.param2)
                    cl.sendText(msg.to,"Chat di Bear6 telah dihapus")
                    print "Success Remove Chat"
                except:
                    pass
#============================================
            elif msg.text in ["Bearbot Rchat","Removechat","removechat"]:
                if msg.from_ in admin:
		    try:
                   # ki.removeAllMessages(op.param2)
                        ki.removeAllMessages(op.param2)
                        ki2.removeAllMessages(op.param2)
                        ki3.removeAllMessages(op.param2)
                        ki4.removeAllMessages(op.param2)
                        ki5.removeAllMessages(op.param2)
                        ki6.removeAllMessages(op.param2)
                        ki7.removeAllMessages(op.param2)
                        ki.sendText(msg.to,"Hapus semua Chat Success")
                    except:
                        pass
#--------------------------------------------------------------------------------------                    
            elif msg.text in ["Mentionall","atb","Ats","Tagall"]:
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 100 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 100  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 100  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)
#-------------Fungsi Tag All Start---------------#
            elif msg.text in ["woi","Tag all"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
#-------------Fungsi Tag All Finish---------------#
#-------------Fungsi Notag Start------------------#
	    elif "Notag on" in msg.text:
                wait["Notag"] = True
                cl.sendText(msg.to,"[  ✔ ᴺᵒᵗᵃᵍ ᴬᶜᵗⁱᵛᵉᵈ  ]"+ datetime.today().strftime('%H:%M:%S')) 
            elif "Notag off" in msg.text:
                wait["Notag"] = False
                cl.sendText(msg.to,"[ ⛔ ᴺᵒᵗᵃᵍ ᵁⁿᵃᶜᵗⁱᵛᵉᵈ  ]"+ datetime.today().strftime('%H:%M:%S')) 
#-------------Fungsi Tag 1 Start---------------#
            elif msg.text in ["Arespon on"]:
                if wait["Arespon"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ̲ ]\n✔ ᴬᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                    else:
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ̲ ]\n✔ ᴬᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                else:
                   wait["Arespon"] = True
                if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ̲ ]\n✔ ᴬᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                else:
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ̲ ]\n✔ ᴬᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
            elif msg.text in ["Arespon off"]:
                if wait["Arespon"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ̲ ]\n⛔ ᵁⁿᵃᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                    else:
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ̲ ]\n⛔ ᵁⁿᵃᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                else:
                    wait["Arespon"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ̲ ]\n⛔ ᵁⁿᵃᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                    else:
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ̲ ]\n⛔ ᵁⁿᵃᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
            elif "Update Arespon:" in msg.text:
              if msg.from_ in admin:
                wait["mresp"] = msg.text.replace("Update Arespon:","")
                cl.sendText(msg.to,"update Arespon succes"+ datetime.today().strftime('%H:%M:%S'))
#-------------Fungsi Arespon 1 Finish---------------#                        
#-------------Fungsi Arespon 2 Start---------------#
            elif msg.text in ["Arespon2 on"]:
                if wait["Arespon2"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ2̲ ]\n✔ ᴬᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                    else:
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ2̲ ]\n✔ ᴬᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                else:
                   wait["Arespon2"] = True
                if wait["Arespon2"] == "JP":
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ2̲ ]\n✔ ᴬᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                else:
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ2̲ ]\n✔ ᴬᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
            elif msg.text in ["Arespon2 off"]:
                if wait["Arespon2"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ2̲ ]\n⛔ ᵁⁿᵃᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                    else:
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ2̲ ]\n⛔ ᵁⁿᵃᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                else:
                    wait["Arespon2"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ2̲ ]\n⛔ ᵁⁿᵃᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                    else:
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ2̲ ]\n⛔ ᵁⁿᵃᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
            elif "Update Arespon2:" in msg.text:
              if msg.from_ in admin:
                wait["mresp2"] = msg.text.replace("Update Arespon2:","")
                cl.sendText(msg.to,"update Arespon2 succes"+ datetime.today().strftime('%H:%M:%S'))
#-------------Fungsi Arespon 2 Finish---------------#
#-------------Fungsi Arespon 3 Start---------------#
            elif msg.text in ["Arespon3 on"]:
                if wait["Arespon3"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ3̲ ]\n✔ ᴬᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                    else:
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ3̲ ]\n✔ ᴬᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                else:
                   wait["Arespon3"] = True
                if wait["Arespon3"] == "JP":
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ3̲ ]\n✔ ᴬᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                else:
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ3̲ ]\n✔ ᴬᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
            elif msg.text in ["Arespon3 off"]:
                if wait["Arespon3"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ3̲ ]\n⛔ ᵁⁿᵃᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                    else:
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ3̲ ]\n⛔ ᵁⁿᵃᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                else:
                    wait["Arespon3"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ3̲ ]\n⛔ ᵁⁿᵃᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
                    else:
                        cl.sendText(msg.to,"[ ᴬ̲ᵘ̲ᵗ̲ᵒ̲ ᴿ̲ᵉ̲ˢ̲ᵖ̲ᵒ̲ⁿ̲ᵈ3̲ ]\n⛔ ᵁⁿᵃᶜᵗⁱᵛᵉᵈ"+ datetime.today().strftime('%H:%M:%S')) 
            elif "Update Arespon3:" in msg.text:
              if msg.from_ in admin:
                wait["mresp3"] = msg.text.replace("Update Arespon3:","")
                cl.sendText(msg.to,"update Arespon3 succes"+ datetime.today().strftime('%H:%M:%S'))
            elif "Update Kid:" in msg.text:
              if msg.from_ in admin:
                wait["mresp3K"] = msg.text.replace("Update Kid:","")
                cl.sendText(msg.to,"update Kid succes"+ datetime.today().strftime('%H:%M:%S'))                
            elif "Update Gid:" in msg.text:
              if msg.from_ in admin:
                wait["mresp3G"] = msg.text.replace("Update Gid:","")
                cl.sendText(msg.to,"update Gid succes"+ datetime.today().strftime('%H:%M:%S'))
#-------------Fungsi Arespon 3 Finish---------------#
 #==================================Sticker==================================================================   
            #elif msg.text.lower() in ['Sticker:on','Detectsticker:on','Sticker on']:
            elif msg.text in ["Sticker on","Sticker:on","Detectsticker:on"]:    
              if msg.from_ in admin:
                if wait["sticker"] == True:
                    cl.sendText(msg.to, "Sticker id detect already ON.")
                else:
                    wait["sticker"]=True
                    cl.sendText(msg.to, "active.\n"+ datetime.today().strftime('%H:%M:%S')) 
            #elif msg.text.lower() in ['Sticker:off','Detectsticker:off','Sticker off']:
            elif msg.text in ["Sticker off","Sticker:off","Detectsticker:off"]:            
              if msg.from_ in admin:
                if wait["sticker"] == False:
                    cl.sendText(msg.to, "Sticker id detect already OFF.")
                else:
                    wait["sticker"]=False
                    cl.sendText(msg.to, "Detect sticker id no active.\n\n"+ datetime.today().strftime('%H:%M:%S')) 
#=================================Detect stiker Finish====================================================================
#================================================
            elif "@"+cl.getProfile().displayName in msg.text:
                if wait["Arespon"] == True:
                    tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
                    resp = ("《《AUTO RESPON》》\n")
                    jawab = ("apa kak ? ketik /help untuk bantuan","Cie ngetag bot\nketik /help.")
                    jawabam = random.choice(jawab)
                    cl.sendText(msg.to,resp + jawabam)
#---------------------------------------------------------
            elif "1name:" in msg.text:
              if msg.from_ in owner or msg.from_ in admin or msg.from_ in staff:
                string = msg.text.replace("1name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")

            elif "2name:" in msg.text:
              if msg.from_ in owner or msg.from_ in admin or msg.from_ in staff:                
                string = msg.text.replace("2name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
                    
            elif "3name:" in msg.text:
              if msg.from_ in owner or msg.from_ in admin or msg.from_ in staff:
                string = msg.text.replace("3name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
                    
            elif "4name:" in msg.text:
                string = msg.text.replace("4name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
                    
            elif "5name:" in msg.text:
                string = msg.text.replace("5name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
                    
            elif "6name:" in msg.text:
                string = msg.text.replace("6name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
                    
            elif "7name:" in msg.text:
                string = msg.text.replace("7name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")                    
#---------------------------------------------------------
            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah On")
                    else:
                        cl.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already open 👈")
                    else:
                        cl.sendText(msg.to,"It is already open 􀜁􀇔􏿿")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sudah off ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"It is already off ô€œô€„‰👈")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"off ô€œô€„‰already")
                    else:
                        cl.sendText(msg.to,"already Close ô€œô€„‰👈")
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ʙʟᴏᴄᴋ ᴏɴ ]")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ʙʟᴏᴄᴋ ᴏɴ ]")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'qrprotect on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ Qʀ ᴏɴ ]")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ Qʀ ᴏɴ ]")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'inviteprotect on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏɴ ]")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨����👈")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏɴ ]")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'cancelprotect on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏɴ ]")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏɴ ]")
                    else:
                        cl.sendText(msg.to,"It is already On 􀜁􀇔􏿿👈")
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif msg.text in ["Protect hard","Mode hard"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏɴ ]")
                    else:
                        cl.sendText(msg.to,"Invite on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏɴ ]")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏɴ ]")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏɴ ]")      
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ʙʟᴏᴄᴋ ᴏɴ ]")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ʙʟᴏᴄᴋ ᴏɴ ]")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ Qʀ ᴏɴ ]")
                    else:
                        cl.sendText(msg.to,"")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ Qʀ ᴏɴ ]")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect easy","Mode easy"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏꜰꜰ ]")
                    else:
                        cl.sendText(msg.to,"Invite OFF")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏꜰꜰ ]")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏꜰꜰ ]")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏꜰꜰ ]")      
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ʙʟᴏᴄᴋ ᴏꜰꜰ ]")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ʙʟᴏᴄᴋ ᴏꜰꜰ ]")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ Qʀ ᴏꜰꜰ ]")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ Qʀ ᴏꜰꜰ ]")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ini sudah Off")
                    else:
                        cl.sendText(msg.to,"Auto Join set off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ʙʟᴏᴄᴋ ᴏꜰꜰ ]")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ʙʟᴏᴄᴋ ᴏꜰꜰ ]")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Qrprotect off","qrprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ Qʀ ᴏꜰꜰ ]")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ Qʀ ᴏꜰꜰ ]")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Inviteprotect off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏꜰꜰ ]")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏꜰꜰ ]")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Cancelprotect off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏꜰꜰ ]")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[ ᴩʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏꜰꜰ ]")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
#--------------------------------------------
            elif msg.text.lower() == 'auto joinleave on':
                if wait["autoJoinLeave"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sudah on bego 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["autoJoinLeave"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴊᴏɪɴʟᴇᴀᴠᴇ ᴏɴ􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'auto joinleave off':
                if wait["autoJoinLeave"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sudah off bego")
                    else:
                        cl.sendText(msg.to,"Auto Join set off")
                else:
                    wait["autoJoinLeave"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴊᴏɪɴʟᴇᴀᴠᴇ ᴏꜰꜰ")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")                        
            elif "Update Joinleave:" in msg.text:
              if msg.from_ in admin:
                wait["jlmsg"] = msg.text.replace("Update Joinleave:","")
                cl.sendText(msg.to,"update Joinleave succes"+ datetime.today().strftime('%H:%M:%S'))                        
            elif msg.text in ["Check Joinleave"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"yor bot message\n\n" + wait["jlmsg"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["jlmsg"])                                        
#--------------------------------------------
            elif "Gcancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"🙈🙈🙉🙉🙊🙊")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif "Update Gcancel:" in msg.text:
              if msg.from_ in admin:
                wait["members"] = msg.text.replace("Update Gcancel:","")
                cl.sendText(msg.to,"update Gcancel succes"+ datetime.today().strftime('%H:%M:%S'))            
            elif msg.text in ["Auto leave on","Auto leave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah terbuka 􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already open👈􀜁􀇔􏿿")
            elif msg.text in ["Auto leave off","Auto leave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"off👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah off👈􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already close👈􀜁􀇔􏿿")
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka👈")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈")
                    else:
                        cl.sendText(msg.to,"on👈")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿👈")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"Off👈")
            elif msg.text.lower() == 'set':
                md = "      ◄  | ͟͞͞  S͟e͟t͟t͟i͟n͟g͟  B͟o͟t͟͟͞  ͟͞͞ |  ►\n\n            ∆ᴬᵘᵗᵒᵐᵃᵗⁱᶜᵃˡˡʸ∆\n"                              
                if wait["contact"] == True: md+="􁤁􀇜key􏿿 Contact ➳ on \n"
                else: md+="􀔃􀆓lock and key􏿿 Contact ➳ off\n"
                if wait["timeline"] == True: md+="􁤁􀇜key􏿿 Share ➳ on \n"
                else:md+="􀔃􀆓lock and key􏿿 Share ➳ off \n"
                if wait["autoAdd"] == True: md+="􁤁􀇜key􏿿 Auto add ➳on \n"
                else:md+="􀔃􀆓lock and key􏿿 Auto add ➳ off \n"
                if wait["autoJoin"] == True: md+="􁤁􀇜key􏿿 Auto Join ➳ on \n"
                else: md +="􀔃􀆓lock and key􏿿 Auto Join ➳ off \n"
                if wait["autoCancel"]["on"] == True:md+="􀔃􀆓lock and key􏿿 Auto cancel:" + str(wait["autoCancel"]["members"]) + "􁤁􀇜key􏿿\n"
                else: md+= "􀔃􀆓lock and key􏿿 Group cancel ➳ off \n"
                if wait["autoJoinLeave"] == True: md+="􁤁􀇜key􏿿 Auto Joinleave ➳ on \n"
                else: md+="􀔃􀆓lock and key􏿿 Auto Joinleave ➳ off \n"                
                if wait["leaveRoom"] == True: md+="􁤁􀇜key􏿿 Auto leave ➳ on \n"
                else: md+="􀔃􀆓lock and key􏿿 Auto leave ➳ off \n"
                if wait['likeOn'] == True: md+="􁤁􀇜key􏿿 Auto like ➳ on \n"
                else:md+="􀔃􀆓lock and key􏿿 Auto like ➳ off\n"                
                if wait["commentOn"] == True: md+="􁤁􀇜key􏿿 Auto komentar ➳ on \n"
                else:md+="􀔃􀆓lock and key􏿿 Auto komentar ➳ off \n"
                if wait["welcomemsg"] == True: md+="􁤁􀇜key􏿿 Welcomemsg ➳ on \n"
                else:md+="􀔃􀆓lock and key􏿿 Welcomemsg ➳ off \n"
                if wait["leavemsg"] == True: md+="􁤁􀇜key􏿿 Leavemsg ➳ on \n"
                else:md+="􀔃􀆓lock and key􏿿 Leavemsg ➳ off \n"
                if wait["Notag"] == True: md+="􁤁􀇜key􏿿 Notag ➳ on \n"
                else: md+="􀔃􀆓lock and key􏿿 Notag ➳ off \n"
                if wait["Arespon"] == True: md+="􁤁􀇜key􏿿 Arespon ➳ on \n"
                else:md+="􀔃􀆓lock and key􏿿 Arespon ➳ off \n"
                if wait["Arespon2"] == True: md+="􁤁􀇜key􏿿 Arespon2 ➳ on \n"
                else:md+="􀔃􀆓lock and key􏿿 Arespon2 ➳ off \n"
                if wait["Arespon3"] == True: md+="􁤁􀇜key􏿿 Arespon3:on \n"
                else:md+="􀔃􀆓lock and key􏿿 Arespon3 ➳ off \n"                
                if wait["protect"] == True: md+="􁤁􀇜key􏿿 Protect ➳ on \n"
                else:md+="􀔃􀆓lock and key􏿿 Protect ➳ off \n"
                if wait["linkprotect"] == True: md+="􁤁􀇜key􏿿 Link Protect ➳ on \n"
                else:md+="􀔃􀆓lock and key􏿿 Link Protect ➳ off \n"
                if wait["inviteprotect"] == True: md+="􁤁􀇜key􏿿 Invite Protect ➳ on \n"
                else:md+="􀔃􀆓lock and key􏿿 Invitation Protect ➳ off \n"
                if wait["cancelprotect"] == True: md+="􁤁􀇜key􏿿 Cancel Protect ➳ on \n"
                else:md+="􀔃􀆓lock and key􏿿 Cancel Protect ➳ off \n\n"
                cl.sendText(msg.to,md+ "\n                   •™Ꮔᴜɪᴛᴀᴮᴼᵀˢ•\n                            ⱽ².⁰⁴\n" + "               ꜱᴇᴛᴛɪɴɢ ᴜᴩᴅᴀᴛᴇᴅ") 
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                             
  #-----------------------------------------------------------------            
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': owner}
                cl.sendText(msg.to,"􀜁􀇔􏿿 My Creator 􀜁􀇔􏿿 ")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"􀜁􀇔􏿿 Dont Kick out From group 􀜁􀇔􏿿 ")
                cl.sendText(msg.to,"􀜁􀇔􏿿 Script V2.04 􀜁􀇔􏿿 ")
            elif msg.text in ["Cancelall"]:
                if msg.from_ in admin:
                  gid = cl.getGroupIdsInvited()
                  for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")	
            elif "Set album:" in msg.text:
                gid = msg.text.replace("Set album:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album👈")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak👈")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "æžš\n"
                        else:
                            mg += str(y["title"]) + ":0 Pieces\n"
                    cl.sendText(msg.to,mg)
            elif "Album" in msg.text:
                gid = msg.text.replace("Album","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "\n"
                        else:
                            mg += str(y["title"]) + ":0 pieces\n"
            elif "Hapus album " in msg.text:
                gid = msg.text.replace("Hapus album ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["gid"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album🛡")
#===============================================================
            elif "Get mem " in msg.text:
                saya = msg.text.replace('Get mem ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    geger = gna.members
                    num = 1
                    gg = ""
                    if h == saya:
                      for ids in geger:
                          gg +="[%i] %s\n" % (num, ids.displayName)
                          num = (num+1)
                          cl.sendText(msg.to, "DAFTAR MEMBER:\n\n"+ gg +"\nTotal member: " +"["+str(len(geger))+"]")
            elif "Bear1 Get mem " in msg.text:
                saya = msg.text.replace('Bear1 Get mem ','')
                gid = ki.getGroupIdsJoined()
                for i in gid:
                    h = ki.getGroup(i).name
                    gna = ki.getGroup(i)
                    geger = gna.members
                    num = 1
                    gg = ""
                    if h == saya:
                      for ids in geger:
                          gg +="[%i] %s\n" % (num, ids.displayName)
                          num = (num+1)
                          ki.sendText(msg.to, "DAFTAR MEMBER:\n\n"+ gg +"\nTotal member: " +"["+str(len(geger))+"]")                          
#---------------------------------------------------------------
            elif msg.text.lower() == 'gidlist':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "🕷[%s]:\n%s\n\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text.lower() == 'bear1 gidlist':
                gid = ki.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "🕷[%s]:\n%s\n\n" % (ki.getGroup(i).name,i)
                ki.sendText(msg.to,h)         
            elif msg.text.lower() == 'bear2 gidlist':
                gid = ki2.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "🕷[%s]:\n%s\n\n" % (ki2.getGroup(i).name,i)
                ki2.sendText(msg.to,h)             
            elif msg.text.lower() == 'bear3 gidlist':
                gid = ki3.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "🕷[%s]:\n%s\n\n" % (ki3.getGroup(i).name,i)
                ki3.sendText(msg.to,h)             
            elif msg.text.lower() == 'bear4 gidlist':
                gid = ki4.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "🕷[%s]:\n%s\n\n" % (ki4.getGroup(i).name,i)
                ki4.sendText(msg.to,h)             
            elif msg.text.lower() == 'bear5 gidlist':
                gid = ki5.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "🕷[%s]:\n%s\n\n" % (ki5.getGroup(i).name,i)
                ki5.sendText(msg.to,h)             
            elif msg.text.lower() == 'bear6 gidlist':
                gid = ki6.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "🕷[%s]:\n%s\n\n" % (ki6.getGroup(i).name,i)
                ki6.sendText(msg.to,h)             
            elif msg.text.lower() == 'bear7 gidlist':
                gid = ki7.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "🕷[%s]:\n%s\n\n" % (ki7.getGroup(i).name,i)
                ki7.sendText(msg.to,h)             
#---------------------------------------------------------------
            elif msg.text in ["Flist"]:
              if msg.from_ in admin:
                gid = cl.getAllContactIds()
                h = ""
                for i in gid:
                    h += "[✞]%s\n" % (cl.getContact(i).displayName )
                cl.sendText(msg.to,"========[List Friend]========\n"+ h +"Total Friend :" +str(len(gid)))
            elif "Glist" in msg.text:
                if msg.from_ in admin:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "🕷 %s  \n" % (cl.getGroup(i).name + " | Members : [ " + str(len (cl.getGroup(i).members))+" ]")
                        cl.sendText(msg.to, "#[List Grup]# \n\n"+ h +"\nTotal Group : " +"[ "+str(len(gid))+" ]")
            elif "Ginfo" == msg.text:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
            elif "Gcreator" == msg.text:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")    
                
                cl.sendMessage(msg)            
#--------------------------------------------------------
#---------------------------------------------------------------
            elif msg.text in ["Bear cabut all gc"]:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                gid = ki7.getGroupIdsJoined()
                ginfo = ki.getGroup(msg.to)
                ki2.sendText(msg.to,"Jinlip all "  +  str(ginfo.name)  + "")
                for i in gid:
                    ki2.sendText(msg.to,"Di tarik dr smua peredaran "  +  str(ginfo.name)  + "")
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    ki6.leaveGroup(i)
                    ki7.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"BearBot Done kluar smua gc")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
            elif "Album deleted:" in msg.text:
                gid = msg.text.replace("Album deleted:","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus👈")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album👈")
            elif msg.text in ["Auto add on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Already On👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On👈")
                    else:
                        cl.sendText(msg.to,"Already On👈")
            elif msg.text in ["Auto add off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off👈")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Help set:" in msg.text:
                wait["help"] = msg.text.replace("Help set:","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add:" in msg.text:
                wait["message"] = msg.text.replace("Pesan add:","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan pembuka di ubah > \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set" in msg.text:
                c = msg.text.replace("Message set","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Come Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Auto comment on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di👈")
                    else:
                        cl.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ã‚ªãƒ³ã«ã—ã¾ã—ãŸ👈")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€👈")
            elif msg.text in ["Com off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Bear1 gurl" in msg.text:
                if msg.toType == 1:
                    gid = msg.text.replace("gurl","")
                    gurl = ki.reissueGroupTicket(tid)
                    ki.sendText(msg.to,"line://ti/p" + turl)
                else:
                    ki.sendText(msg.to,"error")

            elif "gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki3.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki3.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#=======================================================================================
            elif msg.text == "Sider":
                    cl.sendText(msg.to, "hmm..")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    print wait2

            elif msg.text == "Ciduk":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "== Bakekok Sider == %s\n\nNah nah\n\nIni nih yg terciduk han\n\n%skampret lo sider. ♪\nDasar KidsJamanNow\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")						
#=============================================================================================================================================================================================================================================================        
            elif "Sider tag on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                cl.sendText(msg.to,"「 Sider Mode Diaktifkan ツ◈ 」")
                
            elif "Sider tag off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    cl.sendText(msg.to, "Cek sider off")
                else:
                    cl.sendText(msg.to, "Heh belom di Set")
#-------Cek sider biar mirip kek siri-----------------------------
            elif "Setlastpoint" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                #cl.sendText(msg.to, "Checkpoint checked!")
                cl.sendText(msg.to, "Set the lastseens' point(｀・ω・´)\n\n" + datetime.now().strftime('%H:%M:%S'))
                print "Setlastpoint"
#--------------------------------------------
            elif "Viewlastseen" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%d日 %H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        grp = '\n• '.join(str(f) for f in dataResult)
                        total = '\nThese %iuesrs have seen at the lastseen\npoint(｀・ω・´)\n\n%s' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        cl.sendText(msg.to, "• %s %s" % (grp, total))
                    else:
                        cl.sendText(msg.to, "Sider ga bisa di read cek setpoint dulu bego tinggal ketik\nSetlastpoint\nkalo mau liat sider ketik\nViewlastseen")
                    print "Viewlastseen"
#-----------------------[Add Staff Section]------------------------
            elif "Add staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Add admin @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the admin list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Remove Staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove Staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Remove staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "=>" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"								
            
            elif msg.text in ["Adminlist","adminlist"]:
              if msg.from_ in admin:
                if admin == []:
                    cl.sendText(msg.to,"The adminlist is empty")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    mc = ""
                    for mi_d in admin:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#-----------------------------------------------------------

            elif ("Bunuh " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Vk " in msg.text:                  
                       nk0 = msg.text.replace("Vk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"Good Bye")

#----------------------------------------------------------------
            elif "1jepit: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("1jepit: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki.findAndAddContactsByMid(msg.from_)
                            ki.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki.sendText(msg.to,"Gua ga dstu pekok, suru bot laen")
            elif "2jepit: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("2jepit: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki2.findAndAddContactsByMid(msg.from_)
                            ki2.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki2.sendText(msg.to,"Gua ga dstu pekok, suru bot laen")
            elif "3jepit: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("3jepit: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki3.findAndAddContactsByMid(msg.from_)
                            ki3.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki2.sendText(msg.to,"Gua ga dstu pekok, suru bot laen")
            elif "4jepit: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("4jepit: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki4.findAndAddContactsByMid(msg.from_)
                            ki4.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki4.sendText(msg.to,"Gua ga dstu pekok, suru bot laen")
            elif "5jepit: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("5jepit: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki5.findAndAddContactsByMid(msg.from_)
                            ki5.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki5.sendText(msg.to,"Gua ga dstu pekok, suru bot laen")
            elif "6jepit: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("6jepit: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki6.findAndAddContactsByMid(msg.from_)
                            ki6.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki6.sendText(msg.to,"Gua ga dstu pekok, suru bot laen")
            elif "7jepit: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("7jepit: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki7.findAndAddContactsByMid(msg.from_)
                            ki7.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki7.sendText(msg.to,"Gua ga dstu pekok, suru bot laen")                            
#---------------------Fungsi spam start--------------------------
            elif "Spam change: " in msg.text:
                wait["spam"] = msg.text.replace("Spam change: ","")
                cl.sendText(msg.to,"spam changed")

            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")

            elif "Spam: " in msg.text:
                strnum = msg.text.replace("Spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])
#-------------------Fungsi spam finish----------------------------                
            elif "Spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                    else:
                        pass
#=========================================
            elif "Mimic:" in msg.text:
            	if msg.from_ in admin:
            		cmd = msg.text.replace("Mimic:","")
            		if cmd == "on":
            			if mimic["status"] == False:
            				mimic["status"] = True
            				cl.sendText(msg.to,"Mimic on")
            			#	ki.sendText(msg.to,"Mimic on")
            			else:
            				cl.sendText(msg.to,"Mimic already on")
            			#	ki.seneText(msg.to,"Mimic already on")
            		elif cmd == "off":
            			if mimic["status"] == True:
            				mimic["status"] = False
            				cl.sendText(msg.to,"Mimic off")
            			#	ki.sendText(msg.to,"Mimic off")
            			else:
            				cl.sendText(msg.to,"Mimic already off")
            			#	ki.sendText(msg.to,"Mimic already off")
            		elif "add:" in cmd:
            			target0 = msg.text.replace("Mimic:add:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			#gInfo = ki.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            			#	ki.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						mimic["target"][target] = True
            						cl.sendText(msg.to,"Success added target")
            			#			ki.sendText(msg.to,"Success added target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed")
            			#			ki.sendText(msg.to,"Failed")
            						break
            		elif "del:" in cmd:
            			target0 = msg.text.replace("Mimic:del:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			#gInfo = ki.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            			#	ki.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						del mimic["target"][target]
            						cl.sendText(msg.to,"Success deleted target")
            			#			ki.sendText(msg.to,"Success deleted target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed!")
            			#			ki.sendText(msg.to,"Failed!")
            						break
            		elif cmd == "ListTarget":
            			if mimic["target"] == {}:
            				cl.sendText(msg.to,"No target")
            				#ki.sendText(msg.to,"No target")
                    	else:
                    		lst = "<<List Target>>"
                    		total = len(mimic["target"])
                    		for a in mimic["target"]:
                				if mimic["target"][a] == True:
                					stat = "On"
                				else:
                					stat = "Off"
                				lst += "\n->" + cl.getContact(mi_d).displayName +" | " + stat
                                cl.sendText(msg.to,lst + "\nTotal:" + total)
                               # ki.sendText(msg.to,lst + "\nTotal:" + total)
#=========================================
#------------------------------ BROADCAST PC --------------------------------
            elif "/Brod " in msg.text:
                if msg.from_ in admin:
                    broadcasttxt = msg.text.replace("/Brod ", "")
                    orang = cl.getAllContactIds()
                    for manusia in orang:
                        cl.sendText(manusia,(broadcasttxt))
                        print "[Command] BC Contact"        
#----------------------------------------------------------------------------
#------------------------------ BROADCAST GC --------------------------------
            elif "/Bcgrup " in msg.text:
                if msg.from_ in admin:
                    broadcasttxt = msg.text.replace("/Bcgrup ", "")
                    orang = cl.getGroupIdsJoined()
                    for manusia in orang:
                        cl.sendText(manusia,(broadcasttxt))
                        print "[Command] BC Grup"        
#----------------------------------------------------------------------------
#==========================================
            elif "y-mp3 " in msg.text.lower():
                if msg.from_ in admin:
                   query = msg.text.replace("y-mp3 ","")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
			   vid = pafy.new(isi)
			   stream = vid.streams
                           hasil = vid[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                           cl.sendAudioWithURL(msg.to, vid[3])
                       else:
                           isi = yt(query[1])
			   vid = pafy.new(isi)
			   stream = vid.streams
                           cl.sendText(msg.to, vid[0])
                           cl.sendAudioWithURL(msg.to, vid[3])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
            elif 'Vidio ' in msg.text:
	      if msg.from_ in admin:
                try:
                    textToSearch = (msg.text).replace('Vidio ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ght=('https://www.youtube.com' + results['href'])
		    cl.sendVideoWithURL(msg.to,ght)
                except:
                    cl.sendText(msg.to,"Could not find it")
#-----------------------------------------------
            elif ".Youtube " in msg.text:
                 query = msg.text.replace(".Youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                               cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])
#=========================================================================================================
            elif 'instagram ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    instagram = msg.text.lower().replace("instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "======INSTAGRAM INFO USER======\n"
                    details = "\n======INSTAGRAM INFO USER======"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif 'music ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
			hasil += '\nLirik :\n ' + song[5]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[3])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
#===================================================================================     
            elif "/say " in msg.text:
                 psn = msg.text.replace("/say ","")
                 tts = gTTS(psn, lang='id', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
#------------------------------------------------
            elif "/say-en " in msg.text:
                say = msg.text.replace("/say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#------------------------------------------------
            elif "/say-sunda " in msg.text.lower():
                    query = msg.text.replace("/say-sunda ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'su', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)

            elif "/say-jawa " in msg.text.lower():
                    query = msg.text.replace("/say-jawa ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'jw', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
#========================================================
            elif "text: " in msg.text:
                txt = msg.text.replace("text: ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"                        
#========================================================
            elif msg.text == "Trans":
                text = "Translator\n'' -> To Indo\n'tr-en: ' -> Indonesia-English"
            #elif "" in msg.text:
            #    isi = msg.text.replace("","")
            #    translator = Translator()
            #    hasil = translator.translate(isi, dest='id')
            #    A = hasil.text
            #    A = A.encode('utf-8')
            #    cl.sendText(msg.to, A)
            elif "tr-en: " in msg.text:
                isi = msg.text.replace("tr-en: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-fr: " in msg.text:
                isi = msg.text.replace("tr-fr: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='fr')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-ar: " in msg.text:
                isi = msg.text.replace("tr-ar: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-cn: " in msg.text:
                isi = msg.text.replace("tr-cn: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='zh-CN')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-de: " in msg.text:
                isi = msg.text.replace("tr-de: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='de')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-hi: " in msg.text:
                isi = msg.text.replace("tr-hi: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='hi')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-jp: " in msg.text:
                isi = msg.text.replace("tr-jp: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-jw: " in msg.text:
                isi = msg.text.replace("tr-jw: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='jw')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-ko: " in msg.text:
                isi = msg.text.replace("tr-ko: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-th: " in msg.text:
                isi = msg.text.replace("tr-th: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
#========================================================
            elif 'wiki ' in msg.text.lower():
              if msg.from_ in admin:
                  try:
                      wiki = msg.text.lower().replace("wiki ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
#-----------------------------------------------
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass         
#-----------------------------------------------
            elif "Siapa " in msg.text:
    		tanya = msg.text.replace("Siapa ","")
    		jawab = ("Dia yg kebanyakan micin"," Dia gila")
    		jawaban = random.choice(jawab)
		tts = gTTS(text=jawaban, lang='en')
		tts.save('tts.mp3')
    		cl.sendAudio(msg.to,'tts.mp3')
#==========================================
            elif "Dosa @" in msg.text:
                tanya = msg.text.replace("Dosa @","")
                jawab = ("60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='en')
                tts.save('tts.mp3')
                cl.sendText(msg.to,"Dosanya adalah cek voice ini")
                cl.sendAudio(msg.to,'tts.mp3')
#================================================================================
            elif msg.text.lower() == 'ifconfig':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
            elif msg.text.lower() == "blank":
              if msg.from_ in owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "c33b66e4b7709e54a6fe6eced6e57c157',"}
                cl.sendMessage(msg)            
#=================================================================================
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                #Burhan Kull~
                if txt[1] == "full":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "+":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")

            elif "Hay @" in msg.text:
                _name = msg.text.replace("Hay @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")  
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")  
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")  
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")  
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"
                       
#            elif "gift @" in msg.text:
#                _name = msg.text.replace("gift @","")
#                _nametarget = _name.rstrip(' ')
#                gs = cl.getGroup(msg.to)
#                for g in gs.members:
#                    if _nametarget == g.displayName:
#                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
#                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")  
#                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")  
#                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
#                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")  
#                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")  
#                       #ki7.sendText(g.mid,"Your Account Has Been Spammed !")
#                       cl.sendText(msg.to, "Done")
#                       print " Spammed !"

            elif "Hallo " in msg.text:
                midd = msg.text.replace("Hallo ","")
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ki.sendText(g.mid,[miid] + "Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki3.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki4.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki6.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki7.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"
#-----------------------------------------------------------)
            elif ("Ban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Bosque")
                   except:
                      pass
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Unlocked")
                            except:
                                cl.sendText(msg.to,"Error")

            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    kk.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    kk.sendText(msg.to,"Error")
                                    
            elif msg.text in ["Clear ban"]:
              if msg.from_ in admin:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"Succes Clear Blacklist")
                
            elif msg.text in ["Cban","Contactban","Contact ban"]:
              if msg.from_ in admin and Bots:
                    if wait["blacklist"] == {}:
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendText(msg.to,"No Blacklist")
                    else:
                        cl.sendText(msg.to,"Daftar Blacklist")
                        h = ""
                        for i in wait["blacklist"]:
                            h = cl.getContact(i)
                            M = Message()
                            M.to = msg.to
                            M.contentType = 13
                            M.contentMetadata = {'mid': i}
                            cl.sendMessage(M)                    
#-----------------------------------------------------------
#===========================================================
#SC CLONE
            elif "Myclone @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Myclone @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.CloneContactProfile(target)
                                    cl.sendText(msg.to, "Succes Copy profile")
                                except Exception as e:
                                    print e
#---------------------------------------------------------------------
            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "backup done")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                    
            elif msg.text in ["Backup"]:
                try:
                    ki.updateDisplayPicture(abackup.pictureStatus)
                    ki.updateProfile(abackup)
                    ki2.updateDisplayPicture(bbackup.pictureStatus)
                    ki2.updateProfile(bbackup)
                    ki3.updateDisplayPicture(cbackup.pictureStatus)
                    ki3.updateProfile(cbackup)
                    ki4.updateDisplayPicture(dbackup.pictureStatus)
                    ki4.updateProfile(dbackup)
                    ki5.updateDisplayPicture(ebackup.pictureStatus)
                    ki5.updateProfile(ebackup)
                    ki6.updateDisplayPicture(fbackup.pictureStatus)
                    ki6.updateProfile(fbackup)
                    ki7.updateDisplayPicture(gbackup.pictureStatus)
                    ki7.updateProfile(gbackup)
                    ki.sendText(msg.to, "BearBot backup done")
                except Exception as e:
                    ki.sendText(msg.to, str (e))
#===========================================================
#-----------------------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"Target Lock")
#-----------------------------------------------------------
            elif msg.text in ["Sp","sp"]:
                start = time.time()
                cl.sendText(msg.to, "Progres Responspeed by łḓ⁴°² †ℯᾰՊℬ0七")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                #ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                #ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
                
            elif msg.text in ["My speed","Speed"]:              
                start = time.time()
                cl.sendText(msg.to, "「ᴅᴇʙᴜᴅ sᴘᴇᴇᴅ」\nsᴘᴇᴇᴅ ɪᴛ's sᴛᴀʀᴛɪɴɢ♪\n ᴀʙᴏʀᴛ ᴛᴏ ᴀʙᴏʀᴛ♪")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "「ᴅᴇʙᴜɢ sᴘᴇᴇᴅ」\nᴛʏᴘᴇ : sᴘᴇᴇᴅ\nᴛɪᴍᴇ ᴛᴀᴋᴇɴ : %ssᴇᴄᴏɴᴅs♪♪" % (elapsed_time))                                                      
#-----------------------------------------------------------
#------------------------------------------------------------------	
#===========[PAP IS DONE]===============
            elif "Cover @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Cover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
            elif "Midpict " in msg.text:
                umid = msg.text.replace("Midpict ","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithURL(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass
#============================================================
#STEALING
            elif "Steal mid" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
            elif "Steal contact" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
            elif "Steal bio" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,contact.statusMessage)
                except:
                    cl.sendText(msg.to,contact.statusMessage)
            elif "Steal name" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,contact.displayName)
                except:
                    cl.sendText(msg.to,contact.displayName)                    
            elif "Steal cover @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal cover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			

            elif "Steal pict " in msg.text:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Steal pict ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = cl.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Nama yg kMu tag Gak Punya Muka (*^o^*)")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")
#===========================================================================
#------------------------------------------------------------------
            elif msg.text in ["Gcreator:inv"]:
              if msg.toType == 2:
                 ginfo = cl.getGroup(msg.to)
                 gCreator = ginfo.creator.mid
                 try:
                    cl.findAndAddContactsByMid(gCreator)
                    cl.inviteIntoGroup(msg.to,[gCreator])
                    print "success inv gCreator"
                 except:
                    pass
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif msg.text in ["Bans:on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unbans:on"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'mcheck':
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "➡" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'banlist':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "➡" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "=List Banned=")
            elif msg.text.lower() == 'kill ban':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"pfftt")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            ki6.kickoutFromGroup(msg.to,[jj])
                            ki7.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
#-----------------------------------------------------------
            elif ("Bunuh " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
#=====================================================================                           
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Beb" in msg.text:
                if msg.toType == 2:
                        print "[Command]Cleanse executing"
                        _name = msg.text.replace("Beb","")
                        gs = ki.getGroup(msg.to)
                        gs = ki2.getGroup(msg.to)
                        gs = ki3.getGroup(msg.to)
                        gs = ki4.getGroup(msg.to)
                        gs = ki5.getGroup(msg.to)
                        gs = ki6.getGroup(msg.to)
                        gs = ki7.getGroup(msg.to)
                        ki.sendText(msg.to,"Group cleansing begin")
                        ki2.sendText(msg.to,"Goodbye :)")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                                try:
                                    klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7]
                                    kicker=random.choice(klist)
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Group Bersihkan")
            elif "sapu" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("sapu","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    ki.sendText(msg.to,"Simisi tod, gosah panic")
                    ki2.sendText(msg.to,"Uhuuuyyyy.")
                    ki3.sendText(msg.to,"Ngebut coyyyy")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        ki2.sendText(msg.to,"Not found.")
                        ki3.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if target not in Bots:    
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg.to,"Group cleanse")
                                ki.sendText(msg.to,"Group cleanse")
                                ki2.sendText(msg.to,"Group cleanse")
#-----------------------------------------------------------
                                
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled👈")
    
            elif msg.text in ["Mangat","B"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"B")
                    cl.sendText(msg.to,"B")
                    cl.sendText(msg.to,"B")
            elif "Album" in msg.text:
                try:
                    albumtags = msg.text.replace("Album","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "We created an album👈")
                except:
                    cl.sendText(msg.to,"Error")
                    
            elif "fakecat" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakecat","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass			

#-----------------------------------------------

#-----------------------------------------------
            elif msg.text.lower() == ["Masuk"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = ki7.getGroup(msg.to)
                        ginfo = ki7.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
                       
#-----------------------------------------------
            elif msg.text in ["Bear in","hmm"]:
                if msg.from_ in owner:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1),
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1),
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1),
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1),
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1),
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1),
                        G = ki7.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)

            elif msg.text.lower() == 'sp come':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ki7.getGroup(msg.to)
                        ginfo = ki7.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
#-----------------------------------------------
            elif "Bear1 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Bear2 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Bear3 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Bear4 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif "Bear5 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#-----------------------------------------------
            elif "Bear6 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
#-----------------------------------------------
            elif "Bear7 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki7.updateGroup(G)                        
#-----------------------------------------------
            elif msg.text in ["cabut"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"Jinlip all😘 "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bear1 cabut" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bear2 cabut" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bear3 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bear4 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bear5 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bear6 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bear7 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki7.leaveGroup(msg.to)
                    except:
                        pass                    
#-----------------------------------------------
            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
            elif "Bear say " in msg.text:
				bctxt = msg.text.replace("Bear say ","")
				ki2.sendText(msg.to,(bctxt))
            elif "Bc" in msg.text:
              if msg.from_ in admin:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
            elif msg.text.lower() == 'ping':
                ki.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki2.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki3.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki4.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki5.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki6.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki7.sendText(msg.to,"Ping 􀜁􀇔􏿿")
#===============================================================
            
            elif msg.text in ["Auto like:on","Auto like on","Like on"]:
              if msg.from_ in admin and Bots:
                if wait['likeOn'] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait['likeOn'] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。\n\n"+ datetime.today().strftime('%H:%M:%S')) 
            elif msg.text in ["Auto like:off","Auto like off","Like off"]:
              if msg.from_ in admin and Bots:
                if wait['likeOn'] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait['likeOn'] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。\n\n"+ datetime.today().strftime('%H:%M:%S')) 
#==========================================================
            elif msg.text in ["Like me","Like:me"]: #Semua Bot Ngelike Status Akun Utama
              if msg.from_ in admin:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Already like on") 
             #   ki.sendText(msg.to,"Kami Siap Like Status BOS\nKami Delay untuk beberapa Detik\nJangan perintah kami dulu sampai kami Selesai Ngelike")
                try:
                  likePost()
                except:
                  pass

            elif msg.text in ["Like2 on", "Bot like2 on"]: #Semua Bot Ngelike Status Teman
              if msg.from_ in admin:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Already like 2 on")
                #ki.sendText(msg.to,"Kami Siap Like Status Owner\nKami Delay untuk beberapa Detik\nJangan perintah kami dulu sampai kami Selesai Ngelike")
                try:
                  autolike()
                except:
                  pass
#=============================W/L MESSAGE=====================================
            elif msg.text in ["Welcome message on"]:
              if msg.from_ in admin and Bots: 
                if wait["welcomemsg"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message on")
            elif msg.text in ["Welcome message off"]:
              if msg.from_ in admin and Bots:
                if wait["welcomemsg"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Update Wmessage:" in msg.text:
              if msg.from_ in admin:
                wait["welmsg"] = msg.text.replace("Update Wmessage:","")
                cl.sendText(msg.to,"update welcome message succes"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Check Wmessage"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"yor bot message\n\n" + wait["welmsg"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["welmsg"])                        
#-----------------------------------------------
            elif msg.text in ["Leave message on"]:
              if msg.from_ in admin and Bots: 
                if wait["leavemsg"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"leave message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"leave message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["leavemsg"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"leave message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"leave message on")
            elif msg.text in ["Leave message off"]:
              if msg.from_ in admin and Bots:
                if wait["leavemsg"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"leave message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"leave message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["leavemsg"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"leave message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"leave message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Update Lmessage:" in msg.text:
              if msg.from_ in admin:
                wait["levmsg"] = msg.text.replace("Update Lmessage:","")
                cl.sendText(msg.to,"update leave message succes"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Check Lmessage"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"yor bot message\n\n" + wait["levmsg"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows?\n\n" + wait["levmsg"])                        
#===================REJECTALL===============================
            elif msg.text in ["Rejectall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All Invites has been Rejected")
                else:
                    cl.sendText(msg.to,"拒绝了全部的邀请。")
#=============================================================
#--------------------
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")

	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			random.choice(KAC).updateGroup(G)
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
#========================================
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
#---------------------
#=========================================================================
	if op.type == 32:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n-> " + Nama
                        wait2['ROM'][op.param1][op.param2] = "-> " + Nama
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    cl.sendText
            except:
                pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
#=======================DEF 2================================
def likePost():
    for zx in range(0,500):
        hasil = cl.activity(limit=500)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in admin:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Plak"
#=========================DEF 1=================================
def autolike():
    for zx in range(0,500):
      hasil = cl.activity(limit=500)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉 ᴀᴜᴛᴏ ʟɪᴋᴇ ʙʏ 👈\n☆ ʀ͟͟͟͞•ʏ͟͟͟͞s͟͟͟͞ʜ͟͟͟͞ ᴛ͟͟͟͞ᴇ͟͟͟͞ᴀ͟͟͟͞ᴍ͟͟͟͞ s͟͟͟͞ᴇ͟͟͟͞ʟ͟͟͟͞ғ͟͟͟͞ʙ͟͟͟͞ᴏ͟͟͟͞ᴛ͟͟͟͞ ᴘ͟͟͟͞ʀ͟͟͟͞ᴏ͟͟͟͞ᴛ͟͟͟͞ᴇ͟͟͟͞ᴄ͟͟͟͞ᴛ͟͟͟͞  ☆ \n ⇨▣ ᴄʀᴇᴀᴛᴏʀ ▣⇦\n http://line.me/ti/p/jodohku_")
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.01)
#============================================================
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
