import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, ALIVE_NAME, USERNAME, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4, STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20 , STRING21 , STRING22 , STRING23 , STRING24 , STRING25 , STRING26 , STRING27 , STRING28 , STRING29 , STRING30 , STRING31, STRING32, STRING33, STRING34, STRING35, STRING36, STRING37, STRING38, STRING39, STRING40, STRING41, STRING42, STRING43, STRING44, STRING45, STRING46, STRING47, STRING48, STRING49, STRING50
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID
import git
import heroku3

api = API_ID
hash = API_HASH
Unknowna = STRING
Unknownb = STRING2
Unknownc = STRING3
Unknownd = STRING4
Unknowne = STRING5
Unknownf = STRING6
Unknowng = STRING7
Unknownh = STRING8
Unknowni = STRING9
Unknownj = STRING10
Unknownk = STRING11
Unknownl = STRING12
Unknownm = STRING13
Unknownn = STRING14
Unknowno = STRING15
Unknownp = STRING16
Unknownq = STRING17
Unknownr = STRING18
Unknowns = STRING19
Unknownt = STRING20
Unknownu = STRING21
Unknownv = STRING22
Unknownw = STRING23
Unknownx = STRING24
Unknowny = STRING25
Unknownz = STRING26
Unknownaa = STRING27
Unknownab = STRING28
Unknownac = STRING29
Unknownad = STRING30
Unknownae = STRING31
Unknownaf = STRING32
Unknownag = STRING33
Unknownah = STRING34
Unknownai = STRING35
Unknownaj = STRING36
Unknownak = STRING37
Unknownal = STRING38
Unknownam = STRING39
Unknownan = STRING40
Unknownao = STRING41
Unknownap = STRING42
Unknownaq = STRING43
Unknownar = STRING44
Unknownas = STRING45
Unknownat = STRING46
Unknownau = STRING47
Unknownav = STRING48
Unknownaw = STRING49
Unknownax = STRING50

bla = ""
blb = ""
blc = ""
bld = ""
ble = ""
blf = ""
blg = ""
blh = ""
bli = ""
blj = ""
blk = ""
bll = ""
blm = ""
bln = ""
blo = ""
blp = ""
blq = ""
blr = ""
bls = ""
blt = ""
blu = ""
blv = ""
blw = ""
blx = ""
bly = ""
blz = ""
baa = ""
bab = ""
bac = ""
bad = ""
bae = ""
baf = ""
bag = ""
bah = ""
bai = ""
baj = ""
bak = ""
bal = ""
bam = ""
ban = ""
bao = ""
bap = ""
baq = ""
bar = ""
bas = ""
bat = ""
bau = ""
bav = ""
baw = ""
bax = ""


que = {}

UnknownA_USERS = []
for x in SUDO: 
    UnknownA_USERS.append(x)
    
async def start_Unknown():
    global bla
    global blb
    global blc
    global bld
    global ble
    global blf
    global blg
    global blh
    global bli
    global blj
    global blk
    global bll
    global blm
    global bln
    global blo
    global blp
    global blq
    global blr
    global bls
    global blt
    global blu
    global blv
    global blw
    global blx
    global bly
    global blz
    global baa
    global bab
    global bac
    global bad
    global bae
    global baf
    global bag
    global bah
    global bai
    global baj
    global bak
    global bal
    global bam
    global ban
    global bao
    global bap
    global baq
    global bar
    global bas
    global bat
    global bau
    global bav
    global baw
    global bax
 

    if Unknowna:
        session_name = str(Unknowna)
        print("String 1 Found")
        bla = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 1")
            await bla.start()
            botme = await bla.get_me()
            await bla(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bla(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
            bla = "UnknownA"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        bla = TelegramClient(session_name, api, hash)
        try:
            await bla.start()
        except Exception as e:
            pass

    if Unknownb:
        session_name = str(Unknownb)
        print("String 2 Found")
        blb = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 2")
            await blb.start()
            botme = await blb.get_me()
            await blb(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blb(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 2 not Found")
        session_name = "startup"
        blb = TelegramClient(session_name, api, hash)
        try:
            await blb.start()
        except Exception as e:
            pass

    if Unknownc:
        session_name = str(Unknownc)
        print("String 3 Found")
        blc = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 3")
            await blc.start()
            botme = await blc.get_me()
            await blc(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blc(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 3 not Found")
        session_name = "startup"
        blc = TelegramClient(session_name, api, hash)
        try:
            await blc.start()
        except Exception as e:
            pass

    if Unknownd:
        session_name = str(Unknownd)
        print("String 4 Found")
        bld = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 4")
            await bld.start()
            botme = await bld.get_me()
            await bld(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bld(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 4 not Found")
        session_name = "startup"
        bld = TelegramClient(session_name, api, hash)
        try:
            await bld.start()
        except Exception as e:
            pass

    if Unknowne:
        session_name = str(Unknowne)
        print("String 5 Found")
        ble = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 5")
            await ble.start()
            botme = await ble.get_me()
            await ble(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await ble(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 5 not Found")
        session_name = "startup"
        ble = TelegramClient(session_name, api, hash)
        try:
            await ble.start()
        except Exception as e:
            pass

    if Unknownf:
        session_name = str(Unknownf)
        print("String 6 Found")
        blf = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 6")
            await blf.start()
            botme = await blf.get_me()
            await blf(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blf(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 6 not Found")
        session_name = "startup"
        blf = TelegramClient(session_name, api, hash)
        try:
            await blf.start()
        except Exception as e:
            pass

    if Unknowng:
        session_name = str(Unknowng)
        print("String 7 Found")
        blg = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 7")
            await blg.start()
            botme = await blg.get_me()
            await blg(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blg(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 7 not Found")
        session_name = "startup"
        blg = TelegramClient(session_name, api, hash)
        try:
            await blg.start()
        except Exception as e:
            pass

    if Unknownh:
        session_name = str(Unknownh)
        print("String 8 Found")
        blh = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 8")
            await blh.start()
            botme = await blh.get_me()
            await blh(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blh(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 8 not Found")
        session_name = "startup"
        blh = TelegramClient(session_name, api, hash)
        try:
            await blh.start()
        except Exception as e:
            pass

    if Unknowni:
        session_name = str(Unknowni)
        print("String 9 Found")
        bli = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 9")
            await bli.start()
            botme = await bli.get_me()
            await bli(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bli(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 9 not Found")
        session_name = "startup"
        bli = TelegramClient(session_name, api, hash)
        try:
            await bli.start()
        except Exception as e:
            pass

    if Unknownj:
        session_name = str(Unknownj)
        print("String 10 Found")
        blj = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 10")
            await blj.start()
            botme = await blj.get_me()
            await blj(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blj(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 10 not Found")
        session_name = "startup"
        blj = TelegramClient(session_name, api, hash)
        try:
            await blj.start()
        except Exception as e:
            pass

    if Unknownk:
        session_name = str(Unknownk)
        print("String 11 Found")
        blk = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 11")
            await blk.start()
            botme = await blk.get_me()
            await blk(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blk(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 11 not Found")
        session_name = "startup"
        blk = TelegramClient(session_name, api, hash)
        try:
            await blk.start()
        except Exception as e:
            pass

    if Unknownl:
        session_name = str(Unknownl)
        print("String 12 Found")
        bll = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 12")
            await bll.start()
            botme = await bll.get_me()
            await bll(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bll(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 12 not Found")
        session_name = "startup"
        bll = TelegramClient(session_name, api, hash)
        try:
            await bll.start()
        except Exception as e:
            pass

    if Unknownm:
        session_name = str(Unknownm)
        print("String 13 Found")
        blm = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 13")
            await blm.start()
            botme = await blm.get_me()
            await blm(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blm(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 13 not Found")
        session_name = "startup"
        blm = TelegramClient(session_name, api, hash)
        try:
            await blm.start()
        except Exception as e:
            pass

    if Unknownn:
        session_name = str(Unknownn)
        print("String 14 Found")
        bln = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 14")
            await bln.start()
            botme = await bln.get_me()
            await bln(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bln(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 14 not Found")
        session_name = "startup"
        bln = TelegramClient(session_name, api, hash)
        try:
            await bln.start()
        except Exception as e:
            pass

    if Unknowno:
        session_name = str(Unknowno)
        print("String 15 Found")
        blo = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 15")
            await blo.start()
            botme = await blo.get_me()
            await blo(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blo(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 15 not Found")
        session_name = "startup"
        blo = TelegramClient(session_name, api, hash)
        try:
            await blo.start()
        except Exception as e:
            pass

    if Unknownp:
        session_name = str(Unknownp)
        print("String 16 Found")
        blp = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 16")
            await blp.start()
            botme = await blp.get_me()
            await blp(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blp(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "startup"
        blp = TelegramClient(session_name, api, hash)
        try:
            await blp.start()
        except Exception as e:
            pass

    if Unknownq:
        session_name = str(Unknownq)
        print("String 17 Found")
        blq = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 17")
            await blq.start()
            botme = await blq.get_me()
            await blq(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blq(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "startup"
        blq = TelegramClient(session_name, api, hash)
        try:
            await blq.start()
        except Exception as e:
            pass

    if Unknownr:
        session_name = str(Unknownr)
        print("String 18 Found")
        blr = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 18")
            await blr.start()
            botme = await blr.get_me()
            await blr(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blr(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "startup"
        blr = TelegramClient(session_name, api, hash)
        try:
            await blr.start()
        except Exception as e:
            pass

    if Unknowns:
        session_name = str(Unknowns)
        print("String 19 Found")
        bls = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 19")
            await bls.start()
            botme = await bld.get_me()
            await bls(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bls(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "startup"
        bls = TelegramClient(session_name, api, hash)
        try:
            await bls.start()
        except Exception as e:
            pass

    if Unknownt:
        session_name = str(Unknownt)
        print("String 20 Found")
        blt = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 20")
            await blt.start()
            botme = await blt.get_me()
            await blt(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blt(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "startup"
        blt = TelegramClient(session_name, api, hash)
        try:
            await blt.start()
        except Exception as e:
            pass

    if Unknownu:
        session_name = str(Unknownu)
        print("String 21 Found")
        blu = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 21")
            await blu.start()
            botme = await blu.get_me()
            await blu(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blu(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        blu = TelegramClient(session_name, api, hash)
        try:
            await blu.start()
        except Exception as e:
            pass

    if Unknownv:
        session_name = str(Unknownv)
        print("String 22 Found")
        blv = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 22")
            await blv.start()
            botme = await blv.get_me()
            await blv(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blv(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 22 not Found")
        session_name = "startup"
        blv = TelegramClient(session_name, api, hash)
        try:
            await blv.start()
        except Exception as e:
            pass

    if Unknownw:
        session_name = str(Unknownw)
        print("String 23 Found")
        blw = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 23")
            await blw.start()
            botme = await blw.get_me()
            await blw(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blw(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 23 not Found")
        session_name = "startup"
        blw = TelegramClient(session_name, api, hash)
        try:
            await blw.start()
        except Exception as e:
            pass

    if Unknownx:
        session_name = str(Unknownx)
        print("String 24 Found")
        blx = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 24")
            await blx.start()
            botme = await blx.get_me()
            await blx(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blx(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 24 not Found")
        session_name = "startup"
        blx = TelegramClient(session_name, api, hash)
        try:
            await blx.start()
        except Exception as e:
            pass


    if Unknowny:
        session_name = str(Unknowny)
        print("String 25 Found")
        bly = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 25")
            await bly.start()
            botme = await bly.get_me()
            await bly(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bly(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 25 not Found")
        session_name = "startup"
        bly = TelegramClient(session_name, api, hash)
        try:
            await bly.start()
        except Exception as e:
            pass

    if Unknownz:
        session_name = str(Unknownz)
        print("String 26 Found")
        blz = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 26")
            await blz.start()
            botme = await blz.get_me()
            await blz(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await blz(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 26 not Found")
        session_name = "startup"
        blz = TelegramClient(session_name, api, hash)
        try:
            await blz.start()
        except Exception as e:
            pass

    if Unknownaa:
        session_name = str(Unknownaa)
        print("String 27 Found")
        baa = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 27")
            await baa.start()
            botme = await baa.get_me()
            await baa(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await baa(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 27 not Found")
        session_name = "startup"
        baa = TelegramClient(session_name, api, hash)
        try:
            await baa.start()
        except Exception as e:
            pass

    if Unknownab:
        session_name = str(Unknownab)
        print("String 28 Found")
        bab = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 28")
            await bab.start()
            botme = await bab.get_me()
            await bab(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bab(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 28 not Found")
        session_name = "startup"
        bab = TelegramClient(session_name, api, hash)
        try:
            await bab.start()
        except Exception as e:
            pass

    if Unknownac:
        session_name = str(Unknownac)
        print("String 29 Found")
        bac = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 29")
            await bac.start()
            botme = await bac.get_me()
            await bac(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bac(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 29 not Found")
        session_name = "startup"
        bac = TelegramClient(session_name, api, hash)
        try:
            await bac.start()
        except Exception as e:
            pass

    if Unknownad:
        session_name = str(Unknownad)
        print("String 30 Found")
        bad = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 30")
            await bad.start()
            botme = await bad.get_me()
            await bad(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bad(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 30 not Found")
        session_name = "startup"
        bad = TelegramClient(session_name, api, hash)
        try:
            await bad.start()
        except Exception as e:
            pass

    if Unknownae:
        session_name = str(Unknownae)
        print("String 31 Found")
        bae = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 31")
            await bae.start()
            botme = await bae.get_me()
            await bae(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bae(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 31 not Found")
        session_name = "startup"
        bae = TelegramClient(session_name, api, hash)
        try:
            await bae.start()
        except Exception as e:
            pass


    if Unknownaf:
        session_name = str(Unknownaf)
        print("String 32 Found")
        baf = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 32")
            await baf.start()
            botme = await baf.get_me()
            await baf(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await baf(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 32 not Found")
        session_name = "startup"
        baf = TelegramClient(session_name, api, hash)
        try:
            await baf.start()
        except Exception as e:
            pass

    if Unknownag:
        session_name = str(Unknownag)
        print("String 33 Found")
        bag = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 33")
            await bag.start()
            botme = await bag.get_me()
            await bag(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bag(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 33 not Found")
        session_name = "startup"
        bag = TelegramClient(session_name, api, hash)
        try:
            await bag.start()
        except Exception as e:
            pass

    if Unknownah:
        session_name = str(Unknownah)
        print("String 34 Found")
        bah = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 34")
            await bah.start()
            botme = await bah.get_me()
            await bah(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bah(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 34 not Found")
        session_name = "startup"
        bah = TelegramClient(session_name, api, hash)
        try:
            await bah.start()
        except Exception as e:
            pass

    if Unknownai:
        session_name = str(Unknownai)
        print("String 35 Found")
        bai = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 35")
            await bai.start()
            botme = await bai.get_me()
            await bai(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bai(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 35 not Found")
        session_name = "startup"
        bai = TelegramClient(session_name, api, hash)
        try:
            await bai.start()
        except Exception as e:
            pass

    if Unknownaj:
        session_name = str(Unknownaj)
        print("String 36 Found")
        baj = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 36")
            await baj.start()
            botme = await baj.get_me()
            await baj(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await baj(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 36 not Found")
        session_name = "startup"
        baj = TelegramClient(session_name, api, hash)
        try:
            await baj.start()
        except Exception as e:
            pass

    if Unknownak:
        session_name = str(Unknownak)
        print("String 37 Found")
        bak = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 37")
            await bak.start()
            botme = await bak.get_me()
            await bak(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bak(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 37 not Found")
        session_name = "startup"
        bak = TelegramClient(session_name, api, hash)
        try:
            await bak.start()
        except Exception as e:
            pass

    if Unknownal:
        session_name = str(Unknownal)
        print("String 38 Found")
        bal = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 38")
            await bal.start()
            botme = await bal.get_me()
            await bal(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bal(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 38 not Found")
        session_name = "startup"
        bal = TelegramClient(session_name, api, hash)
        try:
            await bal.start()
        except Exception as e:
            pass

    if Unknownam:
        session_name = str(Unknownam)
        print("String 39 Found")
        bam = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 39")
            await bam.start()
            botme = await bam.get_me()
            await bam(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bam(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 39 not Found")
        session_name = "startup"
        bam = TelegramClient(session_name, api, hash)
        try:
            await baclm.start()
        except Exception as e:
            pass

    if Unknownan:
        session_name = str(Unknownan)
        print("String 40 Found")
        ban = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 40")
            await ban.start()
            botme = await bad.get_me()
            await ban(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await ban(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 40 not Found")
        session_name = "startup"
        ban = TelegramClient(session_name, api, hash)
        try:
            await ban.start()
        except Exception as e:
            pass

    if Unknownao:
        session_name = str(Unknownao)
        print("String 41 Found")
        bao = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 41")
            await bao.start()
            botme = await bao.get_me()
            await bao(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bao(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 41 not Found")
        session_name = "startup"
        bao = TelegramClient(session_name, api, hash)
        try:
            await bao.start()
        except Exception as e:
            pass
    
    if Unknownap:
        session_name = str(Unknownap)
        print("String 42 Found")
        bap = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 42")
            await bap.start()
            botme = await bap.get_me()
            await bap(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bap(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 42 not Found")
        session_name = "startup"
        bap = TelegramClient(session_name, api, hash)
        try:
            await bap.start()
        except Exception as e:
            pass

    if Unknownaq:
        session_name = str(Unknownaq)
        print("String 43 Found")
        baq = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 43")
            await baq.start()
            botme = await baq.get_me()
            await baq(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await baq(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 43 not Found")
        session_name = "startup"
        baq = TelegramClient(session_name, api, hash)
        try:
            await baq.start()
        except Exception as e:
            pass

    if Unknownar:
        session_name = str(Unknownar)
        print("String 44 Found")
        bar = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 44")
            await bar.start()
            botme = await bar.get_me()
            await bar(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bar(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 44 not Found")
        session_name = "startup"
        bar = TelegramClient(session_name, api, hash)
        try:
            await bar.start()
        except Exception as e:
            pass

    if Unknownas:
        session_name = str(Unknownas)
        print("String 45 Found")
        bas = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 45")
            await bas.start()
            botme = await bas.get_me()
            await bas(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bas(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 45 not Found")
        session_name = "startup"
        bas = TelegramClient(session_name, api, hash)
        try:
            await bas.start()
        except Exception as e:
            pass

    if Unknownat:
        session_name = str(Unknownat)
        print("String 46 Found")
        bat = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 46")
            await bat.start()
            botme = await bat.get_me()
            await bat(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bat(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 46 not Found")
        session_name = "startup"
        bat = TelegramClient(session_name, api, hash)
        try:
            await bat.start()
        except Exception as e:
            pass

    if Unknownau:
        session_name = str(Unknownau)
        print("String 47 Found")
        bau = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 47")
            await bau.start()
            botme = await bau.get_me()
            await bau(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bau(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 47 not Found")
        session_name = "startup"
        bau = TelegramClient(session_name, api, hash)
        try:
            await bau.start()
        except Exception as e:
            pass

    if Unknownav:
        session_name = str(Unknownav)
        print("String 48 Found")
        bav = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 48")
            await bav.start()
            botme = await bav.get_me()
            await bav(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bav(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 48 not Found")
        session_name = "startup"
        bav = TelegramClient(session_name, api, hash)
        try:
            await bav.start()
        except Exception as e:
            pass

    if Unknownaw:
        session_name = str(Unknownaw)
        print("String 49 Found")
        baw = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 49")
            await baw.start()
            botme = await baw.get_me()
            await baw(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await baw(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 49 not Found")
        session_name = "startup"
        baw = TelegramClient(session_name, api, hash)
        try:
            await baw.start()
        except Exception as e:
            pass
    
    if Unknownax:
        session_name = str(Unknownax)
        print("String 50 Found")
        bax = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 50")
            await bax.start()
            botme = await bax.get_me()
            await bax(functions.channels.JoinChannelRequest(channel="@Unknown_fighters"))
            await bax(functions.channels.JoinChannelRequest(channel="@Unknown_Fighters_Network"))           
            botid = telethon.utils.get_peer_id(botme)
            UnknownA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 50 not Found")
        session_name = "startup"
        bax = TelegramClient(session_name, api, hash)
        try:
            await bax.start()
        except Exception as e:
            pass

    



loop = asyncio.get_event_loop()
loop.run_until_complete(start_Unknown())    
   
async def gifspam(e, Unknowna):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=Unknowna.media.document.access_hash,
                    file_reference=Unknowna.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass

@bla.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.bio"))



async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗼\n\nCommand:\n\n.bio <Message to set Bio of Userbot accounts>"
    if e.sender_id in UnknownA_USERS:
        Unknown = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)     
        if len(e.text) > 5:
            bio = str(Unknown[0])
            text = "Changing Bio"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                await event.edit("Succesfully Changed Bio...... Unknown Spam Bot")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@bla.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.join"))




async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in UnknownA_USERS:
        Unknown = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = Unknown[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
           
@bla.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in UnknownA_USERS:
        Unknown = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = Unknown[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@bla.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.leave"))



async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in UnknownA_USERS:
        Unknown = ("".leave(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) == 7:
            bc = Unknown[0]
            bc = int(bc)
            text = "Unknown TeAm Leaving...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@blb.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.spam"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in UnknownA_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Unknown = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        Unknowna = await e.get_reply_message()
        if len(Unknown) == 2:
            message = str(Unknown[1])
            counter = int(Unknown[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and Unknowna.media:  
            counter = int(alex[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter): 
                Unknowna = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, Unknowna)  
        elif e.reply_to_msg_id and Unknowna.text:
            message = Unknowna.text
            counter = int(alex[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@blb.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))





async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in UnknownA_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Unknowna = await e.get_reply_message()
        Unknown = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        Unknownsexy = Unknown[1:]
        if len(Unknownsexy) == 2:
            message = str(Unknownsexy[1])
            counter = int(Unknownsexy[0])
            sleeptime = float(Unknown[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await Unknowna.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and Unknowna.media:  
            counter = int(alexsexy[0])
            sleeptime = float(alex[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    Unknowna = await e.client.send_file(e.chat_id, Unknown, caption=Unknowna.text)
                    await gifspam(e, Unknowna) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and Unknowna.text:
            message = Unknowna.text
            counter = int(alexsexy[0])
            sleeptime = float(alex[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@blb.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))


async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in UnknownA_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Unknown = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        Unknowna = await e.get_reply_message()
        if len(Unknown) == 2:
            message = str(Unknown[1])
            counter = int(Unknown[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await Unknowna.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and Unknowna.media:  
            counter = int(Unknown[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    Unknowna = await e.client.send_file(e.chat_id, Unknowna, caption=Unknowna.text)
                    await gifspam(e, Unknowna) 
                await asyncio.sleep(0.1)  
        elif e.reply_to_msg_id and Unknowna.text:
            message = Unknowna.text
            counter = int(Unknown[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@blb.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.raid"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in UnknownA_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Unknown = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        Unknowna = await e.get_reply_message()
        if len(Unknown) == 2:
            message = str(Unknown[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(Unknown[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(Unknown[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )




@bla.on(events.NewMessage(incoming=True))
@blb.on(events.NewMessage(incoming=True))
@blc.on(events.NewMessage(incoming=True))
@bld.on(events.NewMessage(incoming=True))
@ble.on(events.NewMessage(incoming=True))
@blf.on(events.NewMessage(incoming=True))
@blg.on(events.NewMessage(incoming=True))
@blh.on(events.NewMessage(incoming=True))
@bli.on(events.NewMessage(incoming=True))
@blj.on(events.NewMessage(incoming=True))
@blk.on(events.NewMessage(incoming=True))
@bll.on(events.NewMessage(incoming=True))
@blm.on(events.NewMessage(incoming=True))
@bln.on(events.NewMessage(incoming=True))
@blo.on(events.NewMessage(incoming=True))
@blp.on(events.NewMessage(incoming=True))
@blq.on(events.NewMessage(incoming=True))
@blr.on(events.NewMessage(incoming=True))
@bls.on(events.NewMessage(incoming=True))
@blt.on(events.NewMessage(incoming=True))
@blu.on(events.NewMessage(incoming=True))
@blv.on(events.NewMessage(incoming=True))
@blw.on(events.NewMessage(incoming=True))
@blx.on(events.NewMessage(incoming=True))
@bly.on(events.NewMessage(incoming=True))
@blz.on(events.NewMessage(incoming=True))
@baa.on(events.NewMessage(incoming=True))
@bab.on(events.NewMessage(incoming=True))
@bac.on(events.NewMessage(incoming=True))
@bad.on(events.NewMessage(incoming=True))
@bae.on(events.NewMessage(incoming=True))
@baf.on(events.NewMessage(incoming=True))
@bag.on(events.NewMessage(incoming=True))
@bah.on(events.NewMessage(incoming=True))
@bai.on(events.NewMessage(incoming=True))
@baj.on(events.NewMessage(incoming=True))
@bak.on(events.NewMessage(incoming=True))
@bal.on(events.NewMessage(incoming=True))
@bam.on(events.NewMessage(incoming=True))
@ban.on(events.NewMessage(incoming=True))
@bao.on(events.NewMessage(incoming=True))
@bap.on(events.NewMessage(incoming=True))
@baq.on(events.NewMessage(incoming=True))
@bar.on(events.NewMessage(incoming=True))
@bas.on(events.NewMessage(incoming=True))
@bat.on(events.NewMessage(incoming=True))
@bau.on(events.NewMessage(incoming=True))
@bav.on(events.NewMessage(incoming=True))
@baw.on(events.NewMessage(incoming=True))
@bax.on(events.NewMessage(incoming=True))



async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )           
            

@blb.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))

async def spam(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in UnknownA_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Unknown = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        Unknowna = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(Unknown[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@blb.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))








async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in UnknownA_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Unknown = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        Unknowna = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Unknown[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
@bla.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.ping"))


async def ping(e):
    if e.sender_id in UnknownA_USERS:
        start = datetime.now()
        text = "╰•★★  ℘ơŋɠ ★★•╯"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"⚔️【★𝖡𝖫𝖠𝖹𝖤 ★】 𝙁𝙄𝙂𝙃𝙏𝙀𝙍𝙎★➤➤♛ \n\n╰★╯Ɽυкσ נαяα sαвαя кαяσ...╰★╯\n`{ms}` ℳʂ [{ALIVE_NAME}](https://t.me/{USERNAME})")


@bla.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.restart"))






async def restart(e):
    if e.sender_id in UnknownA_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await bla.disconnect()
        except Exception as e:
            pass
        try:
            await blb.disconnect()
        except Exception as e:
            pass
        try:
            await blc.disconnect()
        except Exception as e:
            pass
        try:
            await bld.disconnect()
        except Exception as e:
            pass
        try:
            await ble.disconnect()
        except Exception as e:
            pass
            await blf.disconnect()
        except Exception as e:
            pass
        try:
            await blg.disconnect()
        except Exception as e:
            pass
        try:
            await blh.disconnect()
        except Exception as e:
            pass
        try:
            await bli.disconnect()
        except Exception as e:
            pass
        try:
            await blj.disconnect()
        except Exception as e:
            pass
            await blk.disconnect()
        except Exception as e:
            pass
        try:
            await bll.disconnect()
        except Exception as e:
            pass
        try:
            await blm.disconnect()
        except Exception as e:
            pass
        try:
            await bln.disconnect()
        except Exception as e:
            pass
        try:
            await blo.disconnect()
        except Exception as e:
            pass
            await blp.disconnect()
        except Exception as e:
            pass
        try:
            await blq.disconnect()
        except Exception as e:
            pass
        try:
            await blr.disconnect()
        except Exception as e:
            pass
        try:
            await bls.disconnect()
        except Exception as e:
            pass
        try:
            await blt.disconnect()
        except Exception as e:
            pass
            await blu.disconnect()
        except Exception as e:
            pass
        try:
            await blv.disconnect()
        except Exception as e:
            pass
        try:
            await blw.disconnect()
        except Exception as e:
            pass
        try:
            await blx.disconnect()
        except Exception as e:
            pass
        try:
            await bly.disconnect()
        except Exception as e:
            pass
            await blz.disconnect()
        except Exception as e:
            pass
        try:
            await baa.disconnect()
        except Exception as e:
            pass
        try:
            await bab.disconnect()
        except Exception as e:
            pass
        try:
            await bac.disconnect()
        except Exception as e:
            pass
        try:
            await bad.disconnect()
        except Exception as e:
            pass
        try:
            await bae.disconnect()
        except Exception as e:
            pass
        try:
            await baf.disconnect()
        except Exception as e:
            pass
        try:
            await bag.disconnect()
        except Exception as e:
            pass
        try:
            await bah.disconnect()
        except Exception as e:
            pass
            await bai.disconnect()
        except Exception as e:
            pass
        try:
            await baj.disconnect()
        except Exception as e:
            pass
        try:
            await bak.disconnect()
        except Exception as e:
            pass
        try:
            await bal.disconnect()
        except Exception as e:
            pass
        try:
            await bam.disconnect()
        except Exception as e:
            pass
            await ban.disconnect()
        except Exception as e:
            pass
        try:
            await bao.disconnect()
        except Exception as e:
            pass
        try:
            await bap.disconnect()
        except Exception as e:
            pass
        try:
            await baq.disconnect()
        except Exception as e:
            pass
        try:
            await bar.disconnect()
        except Exception as e:
            pass
            await bas.disconnect()
        except Exception as e:
            pass
        try:
            await bat.disconnect()
        except Exception as e:
            pass
        try:
            await bau.disconnect()
        except Exception as e:
            pass
        try:
            await bav.disconnect()
        except Exception as e:
            pass
        try:
            await baw.disconnect()
        except Exception as e:
            pass
        try:
            await bax.disconnect()
        except Exception as e:
            pass
                                                               

            
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
@blb.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.help"))


async def help(e):
    if e.sender_id in UnknownA_USERS:
       text = "| 𝐓 𝐄 𝐀 𝐌 • ‌«[ 𝐁𝐋𝐀𝐙𝐄]»𝙁𝙄𝙂𝙃𝙏𝙀𝙍𝙎★➤➤♛✘ ๛ :\n#𝗕𝗟𝗔𝗭𝗘_𝗦𝗣𝗔𝗠𝗠𝗘𝗥\nᎪ𝚅Ꭺ𝙸ᏞᎪ𝙱Ꮮ𝙴  ᏟᎾ𝙼𝙼ᎪᏁᎠ𝚂\n\n#𝗨𝗧𝗜𝗟𝗦_𝗖𝗢𝗠𝗠𝗔𝗡𝗗:\n.𝙿ᎥᏁᎶ\n.Ꮢ𝚎𝚜𝚃𝚊𝚛𝚃\n\n#𝙐𝙨𝙚𝙧𝙗𝙤𝙩_𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.𝙱𝙸𝙾\n.𝙹𝙾𝙸𝙽\n.𝙿𝙹𝙾𝙸𝙽\n.𝙻𝙴𝙰𝚅𝙴\n\n#𝗦𝗣𝗔𝗠_𝗖𝗢𝗠𝗠𝗔𝗡𝗗:\n.𝚂𝙿𝙰𝙼\n.𝙳𝙴𝙻𝙰𝚈𝚂𝙿𝙰𝙼\n.𝙱𝙸𝙶𝚂𝙿𝙰𝙼\n.bsdk\n.replybsdk\n.dreplybsdk\n\n#𝗕𝗟𝗔𝗭𝗘_𝗦𝗣𝗔𝗠𝗠𝗘𝗥\n ғσя мσяε #нεℓρ #яεgαя∂ιηg υsαgε σғ #ρℓυgιηs түρε ρℓυgιηs #ηαмεs"
    await e.reply(text, parse_mode=None, link_preview=None )

@bla.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.repo"))



async def repo(e):
    if e.sender_id in UnknownA_USERS:
        start = datetime.now()
        text = "★★вℓαᘔε ηε✞ሠᎾяᏦ★★"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱ \n➤ 𝐃𝐄𝐏𝐋𝐎𝐘 𝐓𝐎 50 𝐒𝐏𝐀𝐌 𝐁𝐎𝐓𝐒 𝐈𝐍 𝐎𝐍 𝐓𝐌𝐄...\n➤ 𝗣𝗢𝗪𝗘𝗥𝗘𝗗 𝗕𝗬 :- [▄▀▄ 𝓊𝐧ҜＮᗝ𝓌ή ｎє𝔱ώｏг𝓚 ▄▀▄](https://t.me/Unknown_fighters)\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n ┏━━━━━━━━━━━━━━━━━━━━━\n ┣➤∆ 𝚅𝙴𝚁𝚈 𝙵𝙰𝚂𝚃 𝚂𝙿𝙰𝙼...\n ┣    ∆ 𝙽𝙾𝙽 𝚂𝚃𝙾𝙿 𝚂𝙿𝙰𝙼...    \n ┣ 🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰\n ┣\n ┣ ┈ ➤  🔱   [𝗥𝗘𝗣𝗢](https://github.com/TEAM-BLAZ/Unknown-SPAMMER-ROBOT)      \n ┣      \n ┣  ┈➤  🔱   [𝗦𝗧𝗥𝗜𝗡𝗚](https://replit.com/@Unknown-NETWORK/Unknown-SPAMMER)\n ┣\n ┗━━━━━━━━━━━━━━━━━━━━━")



#####Unknown OP BAKI LUND KI TOPI####
import os
Unknownspammer = os.environ.get("ALIVE_PIC",None)
if not Unknownspammer:
 Unknownspammer="https://telegra.ph/file/2ab64117e0f74971ddb9e.jpg"
##########COPY KRE USKI MA KA BOSDA#######

@bla.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.alive"))


async def alive(event):
  if event.sender_id in UnknownA_USERS:
    sed = await event.client.get_me()
    kk = sed.first_name
    k = sed.id
    s = f"[{kk}](tg://user?id={k})"
    tf = f"""
** 》ι'м {s} мємвєя σƒ вℓαzє ηєтωσяк《 **
**☞ 𝙸'𝙼 𝙱𝙻𝙰𝚉𝙴 𝚂𝙿𝙰𝙼𝙼𝙴𝚁 𝙰𝙻𝙸𝚅𝙴.....**
**✰𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 𝙸𝚂 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 𝙿𝙴𝚁𝙵𝙴𝙲𝚃𝙻𝚈..✰**
📢 𝗣𝗢𝗪𝗘𝗥𝗘𝗗 𝗕𝗬 :- **[▄▀▄ 𝓊𝐧ҜＮᗝ𝓌ή ｎє𝔱ώｏг𝓚 ▄▀▄](https://t.me/Unknown_fighters)** 
** ➠𝙲𝙷𝙴𝙲𝙺 𝙼𝚈 𝙰𝙻𝙻 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂《 ☞ ** `.help` 
"""
    await event.client.send_file(event.chat_id,Unknownspammer,caption=tf, force_document=False, link_preview=False)
import time
from time import sleep
        
@bla.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.purge"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.purge"))

async def purge(event):
 if event.sender_id in UnknownA_USERS:
   start = time.perf_counter()
   reply_msg = await event.get_reply_message()
   if not reply_msg:
       await event.reply(
            "`Reply to a message to select where to start purging from.`")
       return
   messages = []
   message_id = reply_msg.id
   delete_to = event.message.id
   messages.append(event.reply_to_msg_id)
   for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []
   await event.client.delete_messages(event.chat_id, messages)
   time_ = time.perf_counter() - start
   text = f"🗑 `Purged Messages` `in {time_:0.2f} seconds`"
   #hdgs = await event.respond(text, parse_mode='markdown')
   await event.delete()
   sleep(1)
   #await hdgs.delete()
   await event.delete()



##################


text = """🔰✘𓆩βƖꪖƹꫀ sρꪖꪑꪑε𝚁 ʀꪮʙʙꪮᴛ Ꭵs 𝙈𝙊𝘿𝙄𝙁𝙄𝙀𝘿...🔰"""
print(text)
print("")
print("✘𓆩βƖꪖƹꫀ sρꪖꪑꪑε𝚁 ʀꪮʙʙꪮᴛ 𝑆T𝔞R𝔱є∂ sU𝐂𝐂εS𝔣𝔲𝔩𝔩Y.")
if len(sys.argv) not in (1, 3, 4):
    try:
        bla.disconnect()
    except Exception as e:
        pass    
    try:
        blb.disconnect()
    except Exception as e:
        pass
    try:
        blc.disconnect()
    except Exception as e:
        pass
    try:
        bld.disconnect()
    except Exception as e:
        pass
    try:
        ble.disconnect()
    except Exception as e:
        pass
    try:
        blf.disconnect()
    except Exception as e:
        pass    
    try:
        blg.disconnect()
    except Exception as e:
        pass
    try:
        blh.disconnect()
    except Exception as e:
        pass
    try:
        bli.disconnect()
    except Exception as e:
        pass
    try:
        blj.disconnect()
    except Exception as e:
        pass
    try:
        blk.disconnect()
    except Exception as e:
        pass    
    try:
        bll.disconnect()
    except Exception as e:
        pass
    try:
        blm.disconnect()
    except Exception as e:
        pass
    try:
        bln.disconnect()
    except Exception as e:
        pass
    try:
        blo.disconnect()
    except Exception as e:
        pass
    try:
        blp.disconnect()
    except Exception as e:
        pass    
    try:
        blq.disconnect()
    except Exception as e:
        pass
    try:
        blr.disconnect()
    except Exception as e:
        pass
    try:
        bls.disconnect()
    except Exception as e:
        pass
    try:
        blt.disconnect()
    except Exception as e:
        pass
    try:
        blu.disconnect()
    except Exception as e:
        pass    
    try:
        blv.disconnect()
    except Exception as e:
        pass
    try:
        blw.disconnect()
    except Exception as e:
        pass
    try:
        blx.disconnect()
    except Exception as e:
        pass
    try:
        bly.disconnect()
    except Exception as e:
        pass
    try:
        blz.disconnect()
    except Exception as e:
        pass    
    try:
        baa.disconnect()
    except Exception as e:
        pass
    try:
        bab.disconnect()
    except Exception as e:
        pass
    try:
        bac.disconnect()
    except Exception as e:
        pass
    try:
        bad.disconnect()
    except Exception as e:
        pass
    try:
        bae.disconnect()
    except Exception as e:
        pass    
    try:
        baf.disconnect()
    except Exception as e:
        pass
    try:
        bag.disconnect()
    except Exception as e:
        pass
    try:
        bah.disconnect()
    except Exception as e:
        pass
    try:
        bai.disconnect()
    except Exception as e:
        pass    
    try:
        baj.disconnect()
    except Exception as e:
        pass
    try:
        bak.disconnect()
    except Exception as e:
        pass
    try:
        bal.disconnect()
    except Exception as e:
        pass
    try:
        bam.disconnect()
    except Exception as e:
        pass
    try:
        ban.disconnect()
    except Exception as e:
        pass    
    try:
        bao.disconnect()
    except Exception as e:
        pass
    try:
        bap.disconnect()
    except Exception as e:
        pass
    try:
        baq.disconnect()
    except Exception as e:
        pass
    try:
        bar.disconnect()
    except Exception as e:
        pass
    try:
        bas.disconnect()
    except Exception as e:
        pass    
    try:
        bat.disconnect()
    except Exception as e:
        pass
    try:
        bau.disconnect()
    except Exception as e:
        pass
    try:
        bav.disconnect()
    except Exception as e:
        pass
    try:
        baw.disconnect()
    except Exception as e:
        pass
    try:
        bax.disconnect()
    except Exception as e:
        pass    

else:
    
    try:
        bla.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blb.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blc.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bld.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ble.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blf.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blg.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blh.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bli.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blj.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bll.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blm.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bln.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blo.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blp.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blq.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blr.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bls.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blt.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blu.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blv.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blw.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blx.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bly.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blz.run_until_disconnected()
    except Exception as e:
        pass
    try:
        baa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bab.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bac.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bad.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bae.run_until_disconnected()
    except Exception as e:
        pass
    try:
        baf.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bag.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bah.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bai.run_until_disconnected()
    except Exception as e:
        pass
    try:
        baj.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bak.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bal.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bam.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ban.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bao.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bap.run_until_disconnected()
    except Exception as e:
        pass
    try:
        baq.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bar.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bas.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bat.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bau.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bav.run_until_disconnected()
    except Exception as e:
        pass
    try:
        baw.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bax.run_until_disconnected()
    except Exception as e:
        pass
    
