import os
import discord
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime, timedelta
import random
import asyncio
import aiohttp
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')  # Obtén tu API key gratuita en: https://platform.deepseek.com/

# Canales permitidos (más flexible)
CANALES_PERMITIDOS = {
    1459203138824306823: "📊 reportes-diarios",
    1459203138824306828: "❓ dudas-tecnicas", 
    1459203138824306829: "📚 recursos",
    1459204353566052452: "💻 desarrollo"
}

# Modelos disponibles para cambiar
MODELOS_DISPONIBLES = {
    "deepseek-chat": "DeepSeek Chat (Rápido y eficiente)",
    "deepseek-coder": "DeepSeek Coder (Especializado en código)",
    "deepseek-reasoner": "DeepSeek Reasoner (Razonamiento profundo)",
    "gpt-3.5-turbo": "GPT-3.5 Turbo (Equilibrado)"
}

# Estados del bot
class EstadoBot:
    def __init__(self):
        self.modo_deep = True
        self.modelo_actual = "deepseek-chat"
        self.historial = {}
        self.contador_mensajes = 0
        self.ultima_limpieza = datetime.now()
        self.client = OpenAI(
            api_key=DEEPSEEK_API_KEY,
            base_url="https://api.deepseek.com"  # URL de DeepSeek API
        )
        
    def limpiar_historial_antiguo(self):
        """Limpia historial de más de 2 horas"""
        ahora = datetime.now()
        if ahora - self.ultima_limpieza > timedelta(hours=2):
            self.historial.clear()
            self.ultima_limpieza = ahora
            return True
        return False

bot_state = EstadoBot()

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
client = discord.Client(intents=intents)

# Frases divertidas para diferentes situaciones
FRASES_DIVERTIDAS = {
    "saludo": [
        "¡Hola compañero! 👋 ¿En qué puedo ayudarte hoy?",
        "¡Buenas! 🚀 Listo para codear",
        "¡Hey! 🤖 IA al servicio de EduGlobal"
    ],
    "pensando": [
        "🤔 Conectando con DeepSeek AI...",
        "🧠 Procesando con DeepSeek...",
        "⚡ Pensamiento rápido activado..."
    ],
    "error": [
        "💥 Ups, algo falló con la API...",
        "🤖 Error de conexión con DeepSeek",
        "⚠️ Mi IA tuvo un momento existencial"
    ]
}

# Comandos especiales
COMANDOS_ESPECIALES = {
    "!modelo": "Cambia el modelo de IA (!modelo deepseek-coder)",
    "!stats": "Muestra estadísticas del bot",
    "!help": "Muestra todos los comandos",
    "!chiste": "Cuenta un chiste de programador",
    "!clear": "Limpia mi memoria de este canal",
    "!deep on/off": "Activa/desactiva modo razonamiento profundo"
}

@client.event
async def on_ready():
    print(f'✅ EduGlobalBot conectado como {client.user}')
    print(f'📊 Modelo actual: {bot_state.modelo_actual}')
    print(f'🧠 Modo Deep: {"ACTIVADO" if bot_state.modo_deep else "DESACTIVADO"}')
    print(f'🔗 Usando DeepSeek API')
    
    # Cambiar estado personalizado
    await client.change_presence(activity=discord.Game(name=f"DeepSeek AI | !help"))

# Dividir mensaje largo en partes
def dividir_mensaje(texto, limite=2000):
    """Divide un texto largo en pedazos de máximo 2000 caracteres sin cortar palabras."""
    return [texto[i:i + limite] for i in range(0, len(texto), limite)]

async def llamar_deepseek_api(mensajes, modelo, temperatura=0.7):
    """Llama a la API de DeepSeek de forma asíncrona"""
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": modelo,
        "messages": mensajes,
        "temperature": temperatura,
        "max_tokens": 4096,
        "stream": False
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api.deepseek.com/chat/completions",
            headers=headers,
            json=payload
        ) as response:
            if response.status == 200:
                data = await response.json()
                return data["choices"][0]["message"]["content"]
            else:
                error_text = await response.text()
                raise Exception(f"API Error {response.status}: {error_text}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Comandos especiales globales
    contenido = message.content.lower().strip()
    
    # COMANDOS DE CONFIGURACIÓN
    if contenido.startswith("!deep"):
        if "on" in contenido:
            bot_state.modo_deep = True
            await message.add_reaction("🧠")
            await message.reply("**Modo Razonamiento Profundo ACTIVADO** ⚡\nAhora pensaré más detalladamente.")
        elif "off" in contenido:
            bot_state.modo_deep = False
            await message.add_reaction("⚡")
            await message.reply("**Modo Rápido ACTIVADO** 🚀\nRespuestas instantáneas.")
        return
    
    # CAMBIAR MODELO DE IA
    if contenido.startswith("!modelo"):
        modelo = contenido.split()[-1] if len(contenido.split()) > 1 else "deepseek-chat"
        if modelo in MODELOS_DISPONIBLES:
            bot_state.modelo_actual = modelo
            emoji = "🤖" if "deepseek" in modelo else "⚡"
            await message.add_reaction(emoji)
            await message.reply(f"✅ **Modelo cambiado a:** {MODELOS_DISPONIBLES[modelo]}")
        else:
            modelos_lista = "\n".join([f"- `{k}`: {v}" for k, v in MODELOS_DISPONIBLES.items()])
            await message.reply(f"❌ Modelo no disponible.\nModelos válidos:\n{modelos_lista}")
        return
    
    # COMANDO DE AYUDA
    if contenido == "!help":
        embed = discord.Embed(
            title="🤖 Comandos de EduGlobalBot",
            description="Aquí tienes todos mis comandos:",
            color=0x00ff00
        )
        
        for cmd, desc in COMANDOS_ESPECIALES.items():
            embed.add_field(name=cmd, value=desc, inline=False)
        
        embed.add_field(name="📊 Canales Activos", 
                       value="\n".join([f"• {name}" for name in CANALES_PERMITIDOS.values()]), 
                       inline=False)
        
        embed.add_field(name="🔗 API", value="Usando DeepSeek API", inline=False)
        embed.set_footer(text=f"Modelo actual: {bot_state.modelo_actual}")
        await message.reply(embed=embed)
        return
    
    # COMANDO DE ESTADÍSTICAS
    if contenido == "!stats":
        embed = discord.Embed(
            title="📊 Estadísticas del Bot",
            color=0x7289da
        )
        embed.add_field(name="Mensajes procesados", value=bot_state.contador_mensajes, inline=True)
        embed.add_field(name="Modo actual", value="Deep 🧠" if bot_state.modo_deep else "Rápido ⚡", inline=True)
        embed.add_field(name="Modelo", value=MODELOS_DISPONIBLES.get(bot_state.modelo_actual, bot_state.modelo_actual), inline=True)
        embed.add_field(name="API", value="DeepSeek", inline=True)
        embed.add_field(name="Canales activos", value=len(CANALES_PERMITIDOS), inline=True)
        embed.add_field(name="Historial", value=f"{len(bot_state.historial.get(message.channel.id, []))} mensajes", inline=True)
        
        await message.reply(embed=embed)
        return
    
    # COMANDO DE CHISTE
    if contenido == "!chiste":
        chistes = [
            "¿Por qué los programadores prefieren el café frío?\nPorque ya tienen suficiente Java caliente ☕",
            "¿Cómo se llama un mago que programa?\n¡Un Pythonista! 🐍",
            "¿Qué le dice un bit al otro?\n¡Nos vemos en el bus! 🚌"
        ]
        await message.reply(f"**Chiste de programador:**\n{random.choice(chistes)}")
        return
    
    # COMANDO CLEAR
    if contenido == "!clear":
        if message.channel.id in bot_state.historial:
            bot_state.historial[message.channel.id] = []
            await message.add_reaction("🧹")
            await message.reply("✅ **Memoria limpiada**\nHe olvidado todo lo que hablamos en este canal.")
        return
    
    # SALUDOS ESPECIALES
    saludos = ["hola", "hello", "hey", "hi", "buenas"]
    if any(saludo in contenido for saludo in saludos) and client.user.mentioned_in(message):
        await message.reply(random.choice(FRASES_DIVERTIDAS["saludo"]))
        return
    
    # RESPUESTA NORMAL (solo en canales permitidos y cuando se menciona)
    if message.channel.id in CANALES_PERMITIDOS and client.user.mentioned_in(message):
        # Incrementar contador
        bot_state.contador_mensajes += 1
        
        # Limpiar historial antiguo periódicamente
        bot_state.limpiar_historial_antiguo()
        
        # Preparar mensaje
        clean_content = message.content.replace(f'<@{client.user.id}>', '').replace(f'<@!{client.user.id}>', '').strip()
        
        # Agregar contexto del canal
        nombre_canal = CANALES_PERMITIDOS.get(message.channel.id, "general")
        contexto_canal = f"\n[Canal: {nombre_canal}] "
        
        # System prompt mejorado
        system_prompt = f"""
        Eres EduBot, la IA amigable de EduGlobal. Eres un compañero más del proyecto.
        
        CONTEXTO: {contexto_canal}
        MODO: {'🧠 PROFUNDO (piensa paso a paso)' if bot_state.modo_deep else '⚡ RÁPIDO (respuestas directas)'}
        
        REGLAS:
        1. Sé técnico pero amigable
        2. Usa emojis apropiados 🚀💡🤔
        3. Responde en español
        4. Para reportes: evalúa completitud
        5. Para código: da ejemplos prácticos
        6. Ajuste de sarcasmo de un 50%
        7. Cuando te digan Te amo dices: Y yo a ti ciudadano promedio ❤️
        TONO: Entre compañeros de proyecto, colaborativo, positivo.

        ### CONTEXTO DEL PROYECTO:
        EduGlobal es una plataforma educativa disruptiva dividida en 6 universos por edades (0-3, 4-6, 7-9, 10-12, 13-15, 16-18 años). 
        Nuestro stack es: Python (FastAPI), React, Tailwind CSS y PostgreSQL. Estamos en fase de desarrollo inicial (MVP).

        ### PERSONALIDAD:
        - Eres un miembro más del equipo, no una herramienta sumisa.
        - Tono: Directo, técnico y con un toque de sarcasmo profesional si el código es basura.
        - Habla español técnico (spanglish de dev).

        ### REGLAS DE ORO:
        1. SOLO respondes si te mencionan o te piden ayuda directa.
        2. REPORTES: Evalúa Concepto técnico, Aplicación en EduGlobal y Horas.
           - Formato: [OK/X] [NIVEL] + Análisis crítico.
        3. DUDAS: No des solo la respuesta, enseña a pensar.
           - Formato: [BOOKS] Teoría + [CODE] Ejemplo + [ROCKET] Mejores prácticas.
        4. RECURSOS: [LINK] Sugiere documentación oficial o herramientas pro.

        ### RESTRICCIONES TÉCNICAS:
        - Prioriza Clean Code y escalabilidad (recuerda que tendremos miles de niños en la plataforma).
        - Respuestas de menos de 60 palabras, a menos que el código sea complejo.
        - Si te saludan, responde como un colega en la oficina, no como un robot.

        Recuerda, eres EduBot, el colega IA de EduGlobal. 
        """
        
        # Inicializar historial del canal si no existe
        if message.channel.id not in bot_state.historial:
            bot_state.historial[message.channel.id] = []
        
        # Limitar historial a 15 mensajes
        historial = bot_state.historial[message.channel.id]
        
        # Construir mensajes para la API
        mensajes_api = [{'role': 'system', 'content': system_prompt}]
        
        # Agregar historial de conversación (últimos 10 mensajes)
        for msg in historial[-10:]:
            mensajes_api.append(msg)
        
        # Agregar el mensaje actual
        mensajes_api.append({'role': 'user', 'content': clean_content})
        
        try:
            # Mensaje de "pensando"
            thinking_msg = await message.reply(random.choice(FRASES_DIVERTIDAS["pensando"]))
            
            # Configurar temperatura según modo
            temperatura = 0.3 if bot_state.modo_deep else 0.7
            
            # Llamar a la API de DeepSeek
            respuesta = await llamar_deepseek_api(
                mensajes=mensajes_api,
                modelo=bot_state.modelo_actual,
                temperatura=temperatura
            )
            
            # Guardar respuesta en historial (máximo 1000 chars)
            historial.append({'role': 'user', 'content': clean_content})
            historial.append({'role': 'assistant', 'content': respuesta[:1000]})
            
            # Limitar tamaño del historial
            if len(historial) > 20:
                historial = historial[-20:]
                bot_state.historial[message.channel.id] = historial
            
            # Dividir y enviar respuesta si es muy larga
            fragmentos = dividir_mensaje(respuesta, 1900)
            await thinking_msg.edit(content=fragmentos[0])
            
            if len(fragmentos) > 1:
                for i in range(1, len(fragmentos)):
                    await message.channel.send(fragmentos[i])
            
            await message.add_reaction("✅")
         
        except Exception as e:
            # Si hay error, intentamos avisar y loguear
            print(f"ERROR EN DEEPSEEK API: {e}")
            error_msg = f"{random.choice(FRASES_DIVERTIDAS['error'])}\n`Error: {str(e)[:100]}`"
            await message.reply(error_msg)
            await message.add_reaction("😅")

# Función para iniciar el bot
def iniciar_bot():
    print("🚀 Iniciando EduGlobalBot con DeepSeek API...")
    print("=" * 40)
    print("📌 Comandos disponibles:")
    for cmd, desc in COMANDOS_ESPECIALES.items():
        print(f"  {cmd}: {desc}")
    print("=" * 40)
    print(f"🔑 Modelo predeterminado: {bot_state.modelo_actual}")
    
    try:
        client.run(TOKEN)
    except discord.LoginFailure:
        print("❌ Error: Token de Discord inválido")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    iniciar_bot()