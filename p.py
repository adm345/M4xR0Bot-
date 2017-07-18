#-*-coding:utf8;-*-
#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# encoding: utf-8
import re, sys, time, json, threading, base64, traceback,time, random, datetime
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from telepot.namedtuple import InlineKeyboardMarkup, ReplyKeyboardMarkup
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent

######### Modulos ###########
import telepot, sys, os, sys, random, urllib, urllib2, json, platform
from functools import partial
from telepot.namedtuple import InlineQueryResultArticle
from datetime import datetime
import threading, time, datetime, string
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
from pprint import pprint
import string
############ UTF8 ########
os.system("clear")
reload(sys)


## BOT Config
today = datetime.datetime.today()
t = today.strftime("[%H:%M:]")
tm= today.strftime("%H:%M:")
uptime = datetime.datetime.today()
hora = uptime.strftime("%H:%M")
data = uptime.strftime("%d/%m/%Y")
M = uptime.strftime("%m")
D = uptime.strftime("%d")
A = uptime.strftime("%Y")

bot =telepot.Bot('421345899:AAEl29ADerkkCGcuSLlYVFULjKR0NKM7P-0')
NomeBot = 'ha'
  
message_with_inline_keyboard = None
message_with_inline_keyboar= None
message_with_inline_keyboardi = None
message_with_inline_keyboard = None

def on_chat_message(msg):
    usr = '@' + msg['from']['username']
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == "new_chat_member":
        if (chat_id == -1001143515654):
            bot.sendMessage(chat_id,'Bem vindo ao grupo , %s!' % (usr), reply_to_message_id=True)
        

    ### BOT PARAMTS
    
    contar = msg['message_id']
    send = bot.sendMessage
    reply_to_message_id= msg['from']['id']
    chat_id = msg['chat']['id']
    chat_type = msg['chat']['type']
    msg_id = msg['message_id']
    chat_type = msg['chat']['type']
    from_id = msg['from']['id']
    from_first_name = msg['from']['first_name']
    from_username = "@" + msg['from']['username']
    texto = msg['text']
    txt = msg['text'].split(' ')
    message = msg['text'].split()
    len_msg = len(message)
    
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)
    texto = msg['text']
    user = msg['from']['username']
    nome = msg['from']['first_name']
    id = msg['from']['id']
    
    send = bot.sendMessage
    chat_id = msg['chat']['id']
    reply_msg = "reply_to_message_id=msg['message_id']"
    txt = msg['text'].split(' ')
    message = msg['text'].split()
    len_msg = len(message)
    
    print(from_username)
    print("comando: " + texto)
    print(msg)
    txt = msg['text'].split(' ')

     # end
    if content_type != 'text':

        return


    command = msg['text'][-1:].lower()
    
##################
    if '/start' in texto or '#start' in texto or '/comecar' in texto or '/on' in texto:
       mark = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='👨🏽‍💻 Devs', callback_data='menu')],[InlineKeyboardButton(text='🙋‍♂ Ajuda ', callback_data='ajuda')]+[InlineKeyboardButton(text='🖥 Microsoft ', callback_data='microsoft')],[InlineKeyboardButton(text='💡 Dicas', callback_data='html')],[InlineKeyboardButton(text='📮 Sobre ', callback_data='Sobre')]+[InlineKeyboardButton(text='🔧 Suporte ', callback_data='suporte')],[InlineKeyboardButton(text='💬 Grupo ', callback_data='grupo')],[InlineKeyboardButton(text='🎯 Extras ', callback_data='extras')]+[InlineKeyboardButton(text='🗣 Canal ', callback_data='canal')],[InlineKeyboardButton(text='🔂 Update ', callback_data='updatae')]])
       bot.sendMessage(chat_id, '''```Ola``` 🤖❤️ *{}*\n ```Sou o``` *Windows Bot*! ``` Fui desenvolvido para ajudar os usuarios Windows Desktop com minha dicas e ajuda espero que gostem da minha funcao```\nultilize o botao abaixo'''.format(msg['from']['first_name']), parse_mode='Markdown', reply_markup=mark)
    elif ("/m*" in texto or "/m_" in texto or "`" in texto):
        try:bot.sendMessage(chat_id, texto, parse_mode="Markdown")
        except:bot.sendMessage(chat_id, "\n\nVerifique os paranmetros de formatação")
    elif ("<" in texto or ">" in texto):
            try:bot.sendMessage(chat_id, texto, parse_mode="HTML")
            except:bot.sendMessage(chat_id, texto+"\n\nVerifique os paranmetros de formatação")
    elif txt[0].lower() == '/suporte':
        if len_msg > 1:
           user = msg['from']['username']
           id = msg['from']['id']
           texto = msg[u'text'].split(' ', 1)[1]
           bot.sendMessage(chat_id, '*Ok!,  Estou enviando para o suporte..📩*', parse_mode='Markdown')
           try:bot.sendMessage(263799625, "📮 <b>Mensagem</b> = {}\n\n🔎 = @{}\n<b>ID</b> = {}".format(texto, user, id), parse_mode="HTML")
           except:bot.sendMessage(chat_id, "⚠️ Ops!! sua mensagem não foi enviada", reply_to_message_id=msg["message_id"])
           bot.sendMessage(chat_id, '*Sua mensagem foi enviada!📮*', parse_mode='Markdown', reply_to_message_id=msg["message_id"])
    elif txt[0].lower() == '/ip':
    
        if msg['chat']['type'] == 'supergroup' or msg['chat']['type'] == 'private':
            if len_msg > 1:
                texto = msg[u'text'].split(' ', 1)[1]
                

                conexao = urllib.urlopen('http://freegeoip.net/json/{}'.format(texto))
                data = conexao.read()
                json_data = json.loads(data)
                if ':' not in json_data['ip']:   
                    pprint(json_data)
                    ipJ = json_data['ip']
                    nomePais = json_data['country_name']
                    nomeEstado = json_data['region_name']
                    cidade = json_data['city']
                    cep = json_data['zip_code']
                    fusoHorario = json_data['time_zone']
                    latitude = json_data['latitude']
                    longitude = json_data['longitude']
                    bot.sendLocation(chat_id, '{}'. format(latitude), '{}'.format(longitude), disable_notification=True, reply_to_message_id=msg['message_id'])

                    bot.sendMessage(chat_id, """🛡 - IP :  {}\🌏 - País: {}\n🌐 - Estado: {}\n🏙 - Cidade: {}\n🏘 - CEP: {}\n⌚ - Fuso Horário: {}""".format(ipJ, nomePais, nomeEstado, cidade, cep, fusoHorario, parse_mode='Markdown'))
    elif txt[0].lower() == '/clima':
    
        if msg['chat']['type'] == 'supergroup' or msg['chat']['type'] == 'private':
            if len_msg > 1:
                texto = msg[u'text'].split(' ', 1)[1]
                
                data = urllib.urlopen('http://api.apixu.com/v1/current.json?key=7a408e25e67545d294f10541171403&q={}'.format(texto))
                html = data.read()
                weather = json.loads(html)
                pprint(weather)
                lon = weather['location']['lon']
                lat = weather['location']["lat"]
                bot.sendPhoto(chat_id, "http:{}".format(weather['current']['condition']['icon']), '⛅️ |  CLIMA\n\n___________________\n🏙| CIDADE: {}\n🏘| ESTADO: {}\n🗺| PAÍS: {}\n🌡| TEMPERATURA: {} C°\n\nPressão atmosférica: {}\nHorário padrão:\n{}'.format(weather['location']['name'], weather['location']['region'], weather['location']['country'], weather['current']['temp_c'], weather['current']['pressure_mb'], weather['location']['localtime']))           
        else:
            bot.sendMessage(chat_id, 'Comando destinado a supergrupos e privado')
    elif txt[0].lower() == '/go':
        if (from_id ==263799625):####coloque seu-id
            if len_msg > 1:
                texto = msg[u'text'].split(' ', 1)[1]
                bot.sendMessage(chat_id, 'σk, vσu єnvíαr....')
                try:bot.sendMessage(-1001143515654, texto, parse_mode="Markdown")
                except:
                    try:bot.sendMessage(-1001144565971, texto)
                    except:bot.sendMessage(chat_id, "αlgσ єѕtα ímpєdíndσ quє єu єnvíє, pσr fαvσr vєrífíquє...", reply_to_message_id=msg["message_id"])
                
                bot.sendMessage(chat_id, 'mєnѕαgєm єnvíαdα!', reply_to_message_id=msg["message_id"])


 ######## Comandos Call######
 
 
def on_callback_query(msg):
    
    pprint(msg)
    query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
    print('Query executado')
    print('''
nome: {} 
id: {}
query: {}
'''.format(msg['from']['first_name'], from_id, data))
  

    if data == 'ajuda':
       bot.sendMessage(from_id, '''*Sabia que*⁉️\n\n_Microsoft Windows (ou simplesmente Windows) e uma familia de sistemas operacionais desenvolvidos, comercializados e vendidos pela Microsoft. e constituida por varias familias de sistemas operacionais, cada qual atendendo a um determinado setor da industria da computacao, sendo que o sistema geralmente e associado com a arquitetura IBM PC compativel. As familias ativas do Windows incluem Windows NT, Windows Embedded e Windows Phone; estes podem abranger subfamilias, como Windows_...''', parse_mode='Markdown')
    elif data == 'microsoft':
        bot.sendMessage(from_id, '''*Sabia que* ⁉️\n\n_Microsoft Corporation (NASDAQ: MSFT) e uma empresa transnacional americana com sede em Redmond, Washington, que desenvolve, fabrica, licencia, apoia e vende softwares de computador, produtos eletronicos, computadores e servicos pessoais. Entre seus produtos de software mais conhecidos estao as linhas de sistemas operacionais Windows, a linha de aplicativos para escritorio Office e o navegador Internet Explorer. Entre seus principais produtos de hardware estao os consoles de videogame_...''', parse_mode='Markdown')
    elif data == 'html':
        bot.sendMessage(from_id, '''*Execute programas de limpeza com frequência*\n\nO CCleaner é um dos melhores programas para realizar essa tarefa, limpando o cache e arquivos temporários de vários aplicativos no seu computador, o que pode fazer uma baita diferença no desempenho.\n\n*Remova efeitos visuais desnecessários*\n\nSe você usa o Windows 7, deve estar familiarizado com o tema Aero, cheio de transparências. Apesar de bonito, ele consome muitos recursos do computador, e, a longo prazo, pode começar a contribuir para sua lentidão.\n\nPara removê-lo, clique com o botão direito na área de trabalho e selecione “Personalizar”. Pressione “Cor da janela” e desmarque a opção “Habilitar Transparência”.''', parse_mode='Markdown')
    elif data == 'menu':
        bot.sendMessage(from_id, '''`meu desenvolvedor`\n*Paulo*\n`user:` @Paulosoft''', parse_mode='Markdown')
    elif data == 'Sobre':
        bot.sendMessage(from_id, '''Nome: *windows Bot*\nversao: *1.4*\nby:paulo''', parse_mode='Markdown')
    elif data == 'suporte':
        bot.sendMessage(from_id, '''*suporte:* _esse bot tem o objetivo de ajudar os usuarios Windows Desktop Seja ele 7,8,10_\n*espero que gostem do bot*\natt: *Paulo*\nultilize o /suporte para env msg pro dono do bot''', parse_mode='Markdown')
    elif data == 'extras':
        bot.sendMessage(from_id, '''🎯 *Meu extras sao o markdown e o html*\npor ex: *bold* [*bold*]\n_italic_ [_italic_]\n\n*HTML*  bold  <b>bold</b>\n italic <i>italic</i>\n\n*Meus comandos:*\n/ip - *pesquisar o ip*\n\n/clima - *pesquisar o clima da sua cidade*''', parse_mode='Markdown')
    elif data == 'grupo':
        bot.sendMessage(from_id, '''🙋‍♂ _O meu grupo se chama_\n*Windows Grupo pc* [@Windows_Grupo]\n_o grupo tem o objetivo de ajudar os usuarios Windows Desktop com seus problemas etc_''', parse_mode='Markdown')
    elif data == 'canal':
        bot.sendMessage(from_id, '''🗣 *O informatica total e um Canal de compartilhamento de programas de informatica* 📢 @informaticatotal''', parse_mode='Markdown')
    elif data == 'updatae':
        bot.sendMessage(from_id, '''🔂  *Atualizacao*\n📅 `Dia:` *16/07/2017*\n🕒 `Hora:` *20:19*''', parse_mode='Markdown')
    else:
        bot.answerCallbackQuery(query_id, text='erro')
   
def on_inline_query(msg):
 
      
      
    def compute():

        query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')

        print('%s: Computing for: %s' % (threading.current_thread().name, query_string))


        articles = [InlineQueryResultArticle(

                        id='abcde', title='Compartilhe', input_message_content=InputTextMessageContent(message_text='Conheca o windows bot @Windows_BetaRoBot')),dict(type='article',id='fghij', title='Nosso Grupo', input_message_content=dict(message_text='entre em meu grupo https://t.me/joinchat/D7lDSUQoqgaVljLOpIviHg'))]

        photo1_url = 'https://core.telegram.org/file/811140934/1/tbDSLHSaijc/fdcc7b6d5fb3354adf'

        photo2_url = 'https://www.telegram.org/img/t_logo.png'

        photos = [InlineQueryResultPhoto(

                    id='12345', photo_url=photo1_url, thumb_url=photo1_url),dict(type='photo',id='67890', photo_url=photo2_url, thumb_url=photo2_url)]


        result_type = query_string[-1:].lower()


        if result_type == 'a':

            return articles

        elif result_type == 'p':

            return photos

        else:

            results = articles if random.randint(0,1) else photos

            if result_type == 'b':

                return dict(results=results, switch_pm_text='Back to Bot', switch_pm_parameter='Optional start parameter')

            else:

                return dict(results=results)


    answerer.answer(msg, compute)



def on_chosen_inline_result(msg):

    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')

    print('Chosen Inline Result:', result_id, from_id, query_string)
 




answerer = telepot.helper.Answerer(bot)



print('Ok! ligado.')   
bot.message_loop({'chat': on_chat_message,'callback_query': on_callback_query,'inline_query': on_inline_query,'chosen_inline_result': on_chosen_inline_result})
      
# Keep the program running.
# Keep the program running.

while 1:
    time.sleep(10)
   
