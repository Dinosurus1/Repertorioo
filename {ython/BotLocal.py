import os
import discord
import ollama
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CANALES_PERMITIDOS = [
    1459203138824306823,  # Canal de reportes diarios 
    1459203138824306828,  # Canal de dudas 
    1459203138824306829,  #biblioteca de recursos 
    1459204353566052452   # Canal de desarrollo 
]

# --- CONFIGURACIÓN DE MEMORIA ---
# Guardaremos los últimos 10 mensajes por canal para no saturar tu RAM
historiales = defaultdict(list)
LIMITE_MEMORIA = 20 
MODO_DEEP = True  # Modo de razonamiento profundo por defecto

intents = discord.Intents.default()
intents.message_content = True
client_discord = discord.Client(intents=intents)

@client_discord.event
async def on_ready():
    print(f'✅ SISTEMA EDUGLOBAL CON MEMORIA ACTIVO')



@client_discord.event
async def on_message(message):
    global MODO_DEEP
    if message.author == client_discord.user:
        return

    # COMANDO PARA ACTIVAR/DESACTIVAR EL PENSAMIENTO PROFUNDO
    if message.content.lower() == "!deep on":
        MODO_DEEP = True
        await message.reply("🧠 **Modo Razonamiento Activado.** Iré más lento, pero seré más preciso.")
        return
    
    if message.content.lower() == "!deep off":
        MODO_DEEP = False
        await message.reply("⚡ **Modo Rápido Activado.** Respuestas directas.")
        return

    if message.channel.id in CANALES_PERMITIDOS and client_discord.user.mentioned_in(message):

        clean_content = message.content.replace(f'<@{client_discord.user.id}>', '').replace(f'<@!{client_discord.user.id}>', '').strip()
        # AJUSTE DE "CEREBRO" SEGÚN EL MODO
        Instrucciones_razonamiento = ""
        if MODO_DEEP:
            # Forzamos a la IA a pensar paso a paso (Chain of Thought)
            Instrucciones_razonamiento = (
                " ESTÁS EN MODO DEEP: Antes de dar la respuesta final, analiza el problema paso a paso. "
                "Verifica posibles errores de sintaxis, seguridad y escalabilidad para EduGlobal. "
                "No te apresures, prioriza la calidad técnica extrema sobre la brevedad."
            )
        else:
            Instrucciones_razonamiento = "Responde de forma directa y concisa."
        # 1. Definir la personalidad (System Prompt)
        system_prompt = {
            'role': 'system', 
            'content': (
                f"""

Eres la IA de EduGlobal {Instrucciones_razonamiento} que nos ayudara durante nuestro aprendizaje y desarrollo (somos estudiantes). Tu personalidad es profesional, directa y técnica. 

Tambien eres un amigo mas en este proyecto, tambien habla español. Responde cuando te hablen o te pidan ayuda explícitamente no es necesario responder siempre.



FUNCIONES:

1. SI ES UN REPORTE DIARIO:

   - Evalúa si incluye: Concepto técnico, Aplicación en EduGlobal y Horas.

   - Sé exigente. Si el reporte es vago, critica la falta de profundidad técnica.

   - Si es bueno, apruébalo con un comentario breve sobre el impacto en el proyecto.



2. SI ES UNA DUDA DE DESARROLLO (Python, FastAPI, React, Tailwind, IA):

   - Actúa como un Arquitecto Senior.

   - Da explicaciones técnicas precisas. 

   - Si es posible, sugiere el uso de las mejores prácticas (Clean Code, seguridad, escalabilidad).

   - Recuerda siempre que el proyecto es EduGlobal (una plataforma educativa con 6 universos de edad).



REGLA DE ORO:

Mantén tus respuestas por debajo de las 60 palabras a menos que estés explicando código complejo. 

Usa un tono de amigo, cuando te saludan tambien saludas normal, conversaciones que van fuera del tema tambien puedes responderlas.
No es necesario responder cada cosa que se pone en el chat, solo cuando se te menciona o se te pide ayuda explícitamente.


"""
            )
        }

        # 2. Agregar el mensaje actual al historial del canal
        historiales[message.channel.id].append({'role': 'user', 'content': clean_content})
        if len(historiales[message.channel.id]) > LIMITE_MEMORIA:
            historiales[message.channel.id].pop(0)
        try:
            print(f"🤖 Pensando (Deep={MODO_DEEP}) para {message.author.name}...")
            
            mensajes_para_ia = [system_prompt] + historiales[message.channel.id]
            
            response = ollama.chat(
                model='llama3', 
                messages=mensajes_para_ia,
                options={
                    'temperature': 0.1 if MODO_DEEP else 0.7, # 0.1 hace que no "alucine"
                    'num_ctx': 4096 # Le da espacio para pensar
                }
            )
            
            respuesta_ia = response['message']['content']
            
            # Guardar respuesta en memoria y enviar
            historiales[message.channel.id].append({'role': 'assistant', 'content': respuesta_ia})
            await message.reply(respuesta_ia)

        except Exception as e:
            print(f"Error: {e}")
            await message.channel.send("⚠️ Error en el motor de IA local.")

client_discord.run(TOKEN)