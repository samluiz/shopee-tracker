import telebot
from telebot import types
import asyncio
import time
from UserModel import User

user_service = User()

bot = telebot.TeleBot('5921437499:AAFDLifLWEhaU62k1okTM7VA3f8b4cYCpfo')

markup_track_my_order = types.ReplyKeyboardMarkup()
markup_text = "/rastrear"
markup_track_my_order.add(types.KeyboardButton(markup_text))

privacy_terms = "A sua privacidade é importante para nós. É política do ShopeeTracker respeitar a sua privacidade em relação a qualquer informação sua que possamos coletar nesta conversa. Solicitamos informações pessoais apenas quando realmente precisamos delas para lhe fornecer um serviço. Fazemo-lo por meios justos e legais, com o seu conhecimento e consentimento. Também informamos por que estamos coletando e como será usado. Apenas retemos as informações coletadas pelo tempo necessário para fornecer o serviço solicitado. Quando armazenamos dados, protegemos com criptografia de ponta a ponta dentro de meios comercialmente aceitáveis ​​para evitar perdas e roubos, bem como acesso, divulgação, cópia, uso ou modificação não autorizados. Não compartilhamos informações de identificação pessoal publicamente ou com terceiros.\n\nDigite /accept para aceitar o termo de compromisso."

user_accepted = False
user = {}

login = ''
password = ''


@bot.message_handler(commands=['start'])
def first_contact(message):
  message = message
  chat = getattr(message, 'chat')
  user['id'] = chat.id
  user['first_name'] = chat.first_name
  user['last_name'] = chat.last_name
  user['username'] = chat.username if not None else chat.first_name
  user['accepted_term'] = user_accepted
  print(user)
  user_service.create_user(user)
  bot.reply_to(message, "Bem vindo ao Shopee Tracker!")
  chat_id = getattr(chat, 'id')
  bot.send_message(chat_id, "O que deseja?", reply_markup=markup_track_my_order)
  
@bot.message_handler(commands=['rastrear'])
def terms_of_conditions(message):
  if message.text == markup_text:
    message = message
    chat = getattr(message, 'chat')
    bot.reply_to(message, 'Vou precisar de suas credenciais. Por favor, leia nosso termo de compromisso antes de continuar')
    chat_id = getattr(chat, 'id')
    bot.send_message(chat_id, privacy_terms)
    
@bot.message_handler(commands=['accept'])
def asking_for_credentials(message):
  user_accepted = True
  message = message
  chat = getattr(message, 'chat')
  if user_accepted == True:
    chat_id = getattr(chat, 'id')
    bot.send_message(chat_id, "Qual sua forma de login preferida na Shopee?\n\n/email\n/telefone\n/username")
  else:
    bot.send_messsage(chat_id, "Uma pena. Caso mude de ideia, digite /start e começaremos novamente!")    
  
@bot.message_handler(commands=['email', 'telefone', 'username'])
def asking_for_login_type(message):
  if message.text == '/email':
    bot.reply_to(message, "Informe o email da sua conta Shopee, por favor.")
  elif message.text == '/telefone':
    bot.reply_to(message, "Informe o telefone da sua conta Shopee, por favor.")
  elif message.text == '/username':
    bot.reply_to(message, "Informe o nome de usuário da sua conta Shopee, por favor.")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def getting_login(message):
  message = message
  login = getattr(message, 'text')
  global password
  if not password:
    bot.reply_to(message, "Agora informe a senha da sua conta Shopee, e fique tranquilo, ela será rapidamente apagada dessa conversa.")
  
@bot.message_handler(func=lambda message: True, content_types=['text'])
def getting_password(message):
  message = message
  password = getattr(message, 'text')
  print(password)
        
  # bot.send_message(chat_id, "Você precisa informar uma forma de login válida.")
  
  # bot.send_message(chat_id, "Agora informe a senha da sua conta Shopee, e fique tranquilo, ela será rapidamente apagada dessa conversa.")
  # message = message
  # password = getattr(message, 'text')
  
    
# @bot.message_handler(func=lambda message: True, content_types=['text'])
# def ask_for_login_type(message):
#   if message.text == accept_text:
#     user_accepted = True
#     message = message
#     chat = getattr(message, 'chat')
#     if user_accepted == False:
#       bot.send_message(chat_id, "Uma pena! Caso mude de ideia, digite /start para começar novamente.")
#     chat_id = getattr(chat, 'id')
#     bot.send_message(chat_id, "Qual sua forma de login preferida na Shopee?", reply_markup=markup_login_type)
    
# @bot.message_handler(func=lambda message: True, content_types=['text'])
# def ask_for_email(message):
#   message = message
#   chat = getattr(message, 'chat')
#   chat_id = getattr(chat, 'id')
#   if message.text == 'Email':
#     bot.send_message(chat_id, "Informe o email da sua conta Shopee, por favor.")
#   if message.text == 'Telefone':
#     bot.send_message(chat_id, "Informe o telefone da sua conta Shopee, por favor.")
#   if message.text == 'Username':
#     bot.send_message(chat_id, "Informe o nome de usuário da sua conta Shopee, por favor.")

asyncio.run(bot.polling())

  