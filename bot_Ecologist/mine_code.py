import os
import discord
import random
from discord.ext import commands

print(os.listdir("jokes"))
print(os.listdir('info'))
print(os.listdir('mem'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "/", intents=intents)

# Говорит нам что бот запущен
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def waste(ctx):
    img_name = random.choice(os.listdir('info'))
    with open(f'info/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def joke(ctx):
    joke_list = os.listdir("jokes")
    joke_file = random.choice(joke_list)
    with open(f"jokes/{joke_file}", "r", encoding="utf-8") as f:
        joke_text = f.read()
    await ctx.send(joke_text)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('mem'))
    with open(f'mem/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def eco_info(ctx):
    with open(f"options/decomposition_information.txt", "r", encoding="utf-8") as f:
        information_text = f.read()
    await ctx.send(information_text)

@bot.command()
async def play(ctx, game = "1"):
    if game == "1":
        await ctx.send("Добро пожаловать в игру экология!")
        await ctx.send("Ваша задача - правильно утилизировать отходы, выбрав соответствующий контейнер.")
        await ctx.send("У вас есть 5 попыток. Поехали!")

        # Список типов отходов и соответствующих контейнеров
        waste_types = {
            "Бумага": "Синий контейнер",
            "Пластик": "Желтый контейнер",
            "Стекло": "Зеленый контейнер",
            "Металл": "Красный контейнер"
        }

        score = 0
        attempts = 5

        while attempts > 0:
            # Выбираем случайный тип отхода
            waste_type = random.choice(list(waste_types.keys()))

            await ctx.send(f"\nТип отхода: {waste_type}")
            msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
            user_input = msg.content

            if user_input.lower() == waste_types[waste_type].lower():
                score += 1
                await ctx.send("Правильно!")
            else:
                await ctx.send("Неправильно!")

            attempts -= 1

        await ctx.send(f"\nИгра окончена! Ваш счет: {score}/5")


# Игра 2
    if game == "2":
        await ctx.send('Добро пожаловать в игру "Экологический защитник"!')
        await ctx.send('Вы - эколог, чья задача защитить окружающую среду от разрушения.')
        await ctx.send('''Ваша цель - собрать как можно больше мусора и предотвратить загрязнение природы.''')
        await ctx.send('Удачи!')

        score = 0

        while True:
            await ctx.send('Что вы хотите сделать? (собрать мусор / пропустить)')
            action = await bot.wait_for('message')

            if action.content == "собрать мусор":
                collected = random.randint(1, 5)
                await ctx.send(f"Вы собрали {collected} кг мусора!")
                score += collected
            elif action.content == "пропустить":
                await ctx.send("Вы решили пропустить этот раз и продолжить свой путь.")
            else:
                await ctx.send("Неправильное действие! Попробуйте еще раз.")

            await ctx.send(f"Ваш текущий счет: {score} кг мусора")

            await ctx.send('Хотите продолжить игру? (да / нет)')
            play_again = await bot.wait_for('message')
            if play_again.content != "да":
                break

        await ctx.send(f"Игра окончена. Вы собрали {score} кг мусора. Спасибо за игру!")

@bot.command()
async def fire(ctx):
    await ctx.send('\n**Как избежать пожара в здание:**\n```Не оставляйте без присмотра включенные в сеть электробытовые приборы.``` ```Не включайте в одну розетку одновременно несколько мощных энергопотребителей - это может привести к перегрузке в электросети и возгоранию.``` ```Своевременно заменяйте неисправные выключатели, розетки и электропроводку.``` ```Нельзя обертывать электролампы и светильники бумагой, тканью и другими горючими материалами.``` ```Не бросайте в мусоропровод или с балкона непогашенные окурки.``` ```В случае возникновения пожара звоните по телефону 01 (112 для абонентов сотовой связи).``` ')

@bot.command()
async def forest(ctx):
    await ctx.send('\n**Как избежать пожара в лесу:**\n```Не бросать горящие спички и окурки на землю.``` ```Не оставлять стеклянные предметы.``` ```Не оставлять промасленные или пропитанные горючими веществами предметы.``` ```Не парковать автомобили в неположенном месте.``` ```Не разжигать костры в пожароопасный период.``` ```Не сжигать мусор в лесу.```')

@bot.command()
async def хелп(ctx):
    await ctx.send('\n**Мои команды:**\n```>привет - Вывод сообщения с приветом.``` ```>здание - даёт инструкции по тому как избежать пожара в здании.``` ```>лес - даёт инструкции по тому как избежать пожара в лесу.``` ```>glass - показывает цвет бака в который надо выбрасывать стекло.``` ```>organic - показывает цвет бака в который надо выбрасывать органику.``` ```>paper - показывает цвет бака в который надо выбрасывать бумагу.``` ```>plastic - показывает цвет бака в который надо выбрасывать пластик.``` ```>mem - команда которая показывает один рандомный мем про экологию.```')



bot.run("TOKEN")
