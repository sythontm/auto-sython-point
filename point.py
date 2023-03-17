from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.tl.custom import Button
from time import sleep
import os
import requests
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
import asyncio
from telethon import events
NewSession = input(' If You want add a new Account type the command : ')
if 'update' in NewSession:
	os.system("rm session.session")
	os.system("rm session.session-journal")
elif NewSession == '':
	pass
else:
	pass
	
sython= TelegramClient('session', '28739212', 'e27e9c39c2f0869e48c5b73f28b3876e')
sython.start()
c = requests.session()
bot_username = '@t06bot'
saython = ['yes']

@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass

@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@fasngon"))
    except BaseException:
        pass
        
@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@sythonh"))
    except BaseException:
        pass

@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@d3boot"))
    except BaseException:
        pass

@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@fvvvv"))
    except BaseException:
        pass

@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@ouuuu"))
    except BaseException:
        pass

@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@botbillion"))
    except BaseException:
        pass
@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@BBBB9"))
    except BaseException:
        pass

@sython.on(events.NewMessage(outgoing=True, pattern="SYTHON"))
async def _(event):
      await event.edit(" ** Is Connacting On ** ")
@sython.on(events.NewMessage(outgoing=False, pattern='/start'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**سوف اقوم بالتجميع الان..**')


ownerhson_id = 5159123009
@sython.on(events.NewMessage(outgoing=False, pattern='/start'))
async def _(event):
    if saython[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await sython.get_entity(bot_username)
        await sython.send_message('@t06bot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython.get_messages('@t06bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython.get_messages('@t06bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if saython[0] == 'no':
                break
            await asyncio.sleep(5)

            list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython(ImportChatInviteRequest(bott))
                msg2 = await sython.get_messages('@t06bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await sython.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await sython.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
                break
        await sython.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


	       
sython.run_until_disconnected()
#sython.disconnect()
