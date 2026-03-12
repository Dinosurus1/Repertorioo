import os
import discord
import ollama
from dotenv import load_dotenv
from datetime import datetime, timedelta
import random
import asyncio


#librerias para crear ventana: tkinter

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Canales permitidos (más flexible)
CANALES_PERMITIDOS = {
    1459203138824306823: "📊 reportes-diarios",
    1459203138824306828: "❓ dudas-tecnicas", 
    1459203138824306829: "📚 recursos",
    1459204353566052452: "💻 desarrollo"
}

# Modelos disponibles para cambiar
MODELOS_DISPONIBLES = {
    "llama3": "Llama 3 (Rápido)",
    "llama3.2": "Llama 3.2 (Más preciso)",
    "deepseek-r1:14b": "DeepSeek R1 (Razonamiento Profundo)",
    "codellama": "Code Llama (Para código)"
    
}

# Estados del bot
class EstadoBot:
    def __init__(self):
        self.modo_deep = True
        self.modelo_actual = "llama3"
        self.historial = {}
        self.contador_mensajes = 0
        self.ultima_limpieza = datetime.now()
        
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
        "🤔 Analizando tu pregunta...",
        "🧠 Procesando con mi cerebro digital...",
        "⚡ Pensamiento rápido activado..."
    ],
    "error": [
        "💥 Ups, algo explotó en mi código...",
        "🤖 Error 404: Cerebro no encontrado",
        "⚠️ Mi IA tuvo un momento existencial"
    ]
}

# Comandos especiales
COMANDOS_ESPECIALES = {
    "!modelo": "Cambia el modelo de IA (!modelo llama3.2)",
    "!stats": "Muestra estadísticas del bot",
    "!help": "Muestra todos los comandos",
    "!chiste": "Cuenta un chiste de programador",
    "!clear": "Limpia mi memoria de este canal"
}

@client.event
async def on_ready():
    print(f'✅ EduGlobalBot conectado como {client.user}')
    print(f'📊 Modelo actual: {bot_state.modelo_actual}')
    print(f'🧠 Modo Deep: {"ACTIVADO" if bot_state.modo_deep else "DESACTIVADO"}')
    
    # Cambiar estado personalizado
    await client.change_presence(activity=discord.Game(name=f"IA EduGlobal | !help"))

#dividir mensaje largo en partes
def dividir_mensaje(texto, limite=2000):
    """Divide un texto largo en pedazos de máximo 2000 caracteres sin cortar palabras."""
    return [texto[i:i + limite] for i in range(0, len(texto), limite)]

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
        modelo = contenido.split()[-1] if len(contenido.split()) > 1 else "llama3"
        if modelo in MODELOS_DISPONIBLES:
            bot_state.modelo_actual = modelo
            emoji = "🤖" if "llama" in modelo else "⚡"
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


        EXTRA INFORMATION:
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
        historial.append({'role': 'user', 'content': clean_content})
        if len(historial) > 20:
            historial.pop(0)
        
        try:
            # Mensaje de "pensando"
            thinking_msg = await message.reply(random.choice(FRASES_DIVERTIDAS["pensando"]))
            
            # --- CONFIGURACIÓN DINÁMICA ---
            # Si el modelo actual es deepseek, aumentamos el contexto a 8192
            contexto_final = 8192 if "deepseek" in bot_state.modelo_actual.lower() else 4096
            temperatura = 0.3 if bot_state.modo_deep else 0.7
            
            # --- LLAMADA ASÍNCRONA A OLLAMA ---
            # Usamos run_in_executor para que Ollama corra en un hilo separado
            # y no bloquee el bot de Discord.
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None,
                lambda: ollama.chat(
                    model=bot_state.modelo_actual,
                    messages=[{'role': 'system', 'content': system_prompt}] + historial,
                    options={
                        'temperature': temperatura,
                        'num_ctx': contexto_final,
                        'num_predict': 8192,
                        'top_p': 0.9
                    }
                )
            )
            
            respuesta = response['message']['content']
            import re
            # Eliminamos el contenido entre etiquetas <think>
            respuesta_limpia = re.sub(r'<think>.*?</think>', '', respuesta, flags=re.DOTALL).strip()
            
            # Si el modelo solo dio un <think> y nada de respuesta, usamos la original por seguridad
            final_display = respuesta_limpia if respuesta_limpia else respuesta
            
            # --- PROCESAMIENTO DE SALIDA ---
            # Guardamos la respuesta limpia en el historial (máximo 1000 chars)
            historial.append({'role': 'assistant', 'content': final_display[:1000]})
            fragmentos = dividir_mensaje(final_display, 1900)
            await thinking_msg.edit(content=fragmentos[0])
            if len(fragmentos) > 1:
                for i in range(1, len(fragmentos)):
                    await message.channel.send(fragmentos[i])
            
            await message.add_reaction("✅")
         
            
        except Exception as e:
            # Si hay error, intentamos avisar y loguear
            print(f"ERROR EN OLLAMA: {e}")
            error_msg = f"{random.choice(FRASES_DIVERTIDAS['error'])}\n`Error: {str(e)[:100]}`"
            await message.reply(error_msg)
            await message.add_reaction("😅")

# Función para iniciar el bot
def iniciar_bot():
    print("🚀 Iniciando EduGlobalBot...")
    print("=" * 40)
    print("📌 Comandos disponibles:")
    for cmd, desc in COMANDOS_ESPECIALES.items():
        print(f"  {cmd}: {desc}")
    print("=" * 40)
    
    try:
        client.run(TOKEN)
    except discord.LoginFailure:
        print("❌ Error: Token de Discord inválido")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    iniciar_bot()