from pyrogram import Client, filters, ContinuePropagation, StopPropagation
from os import getenv
from dotenv import load_dotenv
from UserModel import User

load_dotenv()

# Creating User Object
user_service = User()

app = Client("ShopeeTracker", api_id=getenv("API_ID"), api_hash=getenv("API_HASH"), bot_token=getenv("TOKEN"))

privacy_terms = "A sua privacidade é importante para nós. É política do ShopeeTracker respeitar a sua privacidade em relação a qualquer informação sua que possamos coletar nesta conversa. Solicitamos informações pessoais apenas quando realmente precisamos delas para lhe fornecer um serviço. Fazemo-lo por meios justos e legais, com o seu conhecimento e consentimento. Também informamos por que estamos coletando e como será usado. Apenas retemos as informações coletadas pelo tempo necessário para fornecer o serviço solicitado. Quando armazenamos dados, protegemos com criptografia de ponta a ponta dentro de meios comercialmente aceitáveis ​​para evitar perdas e roubos, bem como acesso, divulgação, cópia, uso ou modificação não autorizados. Não compartilhamos informações de identificação pessoal publicamente ou com terceiros."

user_accepted = False
user = {}
login = ''
password = ''
order_id = ''
chat_id = ''
login_message_id = 0
password_message_id = 0

def get_chat_and_message_id(message):
  global chat_id
  chat_id = message.chat.id
  return getattr(message, "id")

@app.on_message(filters.command("start"), group=-1)
async def getting_user_info(client, message):
  get_chat_and_message_id(message)
  await message.reply('Olá! Eu sou um rastreador de pacotes não rastreáveis!')
  await app.send_message(chat_id, "O que deseja fazer?\n\n/rastrear")
  raise StopPropagation
  
@app.on_message(filters.command("rastrear"), group=-1)
async def sending_accept_term(client, message):
  await message.reply('Vou precisar de suas credenciais. Por favor, leia nosso termo de privacidade antes de continuar')
  await app.send_message(chat_id, privacy_terms)
  await app.send_message(chat_id, "\n/aceitar 🆗\n\n/rejeitar ❌")
  raise StopPropagation

@app.on_message(filters.command("aceitar"), group=-1)
async def login_type(client, message):
  print(message.text)
  user_accepted = True
  chat = message.chat
  user['telegram_id'] = chat.id
  user['first_name'] = chat.first_name
  user['last_name'] = chat.last_name
  user['username'] = chat.username if not None else chat.first_name
  user_service.create_user(telegram_id=user['telegram_id'], first_name=user['first_name'], last_name=user['last_name'], username=user['username'])
  if not user_accepted:
    await app.send_message(chat_id, "Uma pena. Caso mude de ideia, digite /start e começaremos novamente!")
  await app.send_message(chat_id, "Qual sua forma de login preferida na Shopee?\n\n/email\n/telefone\n/username")
  raise StopPropagation
  
@app.on_message(filters.command(commands=['email', 'telefone', 'username']), group=-1)
async def getting_login_type(client, message):
  if message.text == '/email':
    await message.reply("Informe o email da sua conta Shopee, por favor.")
  elif message.text == '/telefone':
    await message.reply("Informe o telefone da sua conta Shopee, por favor.")
  elif message.text == '/username':
    await message.reply("Informe o nome de usuário da sua conta Shopee, por favor.")
  raise StopPropagation

@app.on_message(filters.text)
async def getting_login(client, message):
  global login
  global login_message_id
  global password
  global password_message_id
  global order_id
  
  # Getting Login and asking for password
  if not login_message_id:
    login_message_id = get_chat_and_message_id(message)
  if message.id == login_message_id:
    login = message.text
    await message.reply("Agora informe a senha da sua conta Shopee, e fique tranquilo, ela será rapidamente apagada dessa conversa.")
    
  # Getting password and asking for order id
  if message.id != login_message_id:
    if not password_message_id:
      password_message_id = get_chat_and_message_id(message)
    if not password and message.id == password_message_id:
      password = message.text
      await app.delete_messages(chat_id, [login_message_id, (login_message_id-1), password_message_id, (password_message_id-1)])
      await app.send_message(chat_id, "Falta pouco para rastrear seu pacote! Agora, informe o número do seu pedido.")
    
  # Getting order id and making the flow
  if message.id != password_message_id:
    if order_id:
      from Flow import Flow
      # Creating Webdriver Object
      scrapper = Flow()
      scrapper.check_order_track_status(login, password, order_id)
    if not order_id and message.text != login:
      order_id = message.text
      print(message, order_id)
      raise ContinuePropagation()
    
app.run()