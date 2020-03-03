import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("고정위키 서버 구동 ")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):

    if message.content.startswith('고정위키 명령어'):
        await message.channel.send("'고정위키 규칙'")
        await message.channel.send("'문서이름' 작성 '문서내용'")
        await message.channel.send("'문서이름' 열람")
        await message.channel.send("'문서목록'")

    if message.content.startswith('고정위키 규칙'):
        await message.channel.send("고정위키는 모든 고정로드가 읽고 편집할 수 있으며 표현의 자유가 적용됩니다!")
        await message.channel.send("고정위키는 권리자가 신고해도 아무런 효력이 없습니다!")
        await message.channel.send("고정로드 과반수의 동의없이 문서를 삭제하는것은 위법입니다!")
        await message.channel.send("문서를 수정할 때는 무조건 수정한 사람의 이름을 남겨야 합니다!")

    a = str("박성주")
    a2 = str("park")
    b = str("김경주")
    b2 = str("kim")
    c = str("장예찬")
    c2 = str("banana")
    d = str("고정길")
    d2 = str("go")
    e = str("뽕천길")
    e2 = str("bong")
    f = str("땡고추")
    f2 = str("pep")

    if message.content.startswith('문서목록'):
        await message.channel.send(a)
        await message.channel.send(b)
        await message.channel.send(c)
        await message.channel.send(d)
        await message.channel.send(e)
        await message.channel.send(f)
        'await message.channel.send("김경주")'
        'await message.channel.send("김경주")'
        'await message.channel.send("김경주")'
        'await message.channel.send("김경주")'
        'await message.channel.send("김경주")'
        'await message.channel.send("김경주")'
        'await message.channel.send("김경주")'
        'await message.channel.send("김경주")'

    '1번 박성주'
    if message.content.startswith(a + ' 작성'):
        a2 = message.content[6:]
        a1 = open("박성주.txt", "w")
        a1.write(a2)
        a1.close()
        await message.channel.send("작성 완료!")

    if message.content.startswith(a + ' 열람'):
        a2 = open("박성주.txt")
        await message.channel.send(a2.read())
        a1.close

    '2번 김경주'
    if message.content.startswith(b + ' 작성'):
        b2 = message.content[6:]
        b1 = open("김경주.txt", "w")
        b1.write(b2)
        b1.close()
        await message.channel.send("작성 완료!")

    if message.content.startswith(b + ' 열람'):
        b2 = open("김경주.txt")
        await message.channel.send(b2.read())
        b1.close

    '3번 장예찬'
    if message.content.startswith(c + ' 작성'):
        c2 = message.content[6:]
        c1 = open("장예찬.txt", "w")
        c1.write(c2)
        c1.close()
        await message.channel.send("작성 완료!")

    if message.content.startswith(c + ' 열람'):
        c2 = open("장예찬.txt")
        await message.channel.send(c2.read())
        c1.close

    '4번 고정길'
    if message.content.startswith(d + ' 작성'):
        d2 = message.content[6:]
        d1 = open("고정길.txt", "w")
        d1.write(d2)
        d1.close()
        await message.channel.send("작성 완료!")

    if message.content.startswith(d + ' 열람'):
        d2 = open("고정길.txt")
        await message.channel.send(d2.read())
        d1.close

    '5번 뽕천길'
    if message.content.startswith(e + ' 작성'):
        e2 = message.content[6:]
        e1 = open("뽕천길.txt", "w")
        e1.write(e2)
        e1.close()
        await message.channel.send("작성 완료!")

    if message.content.startswith(e + ' 열람'):
        e2 = open("뽕천길.txt")
        await message.channel.send(e2.read())
        e1.close

    '6번 땡고추'
    if message.content.startswith(f + ' 작성'):
        f2 = message.content[6:]
        f1 = open("땡고추.txt", "w")
        f1.write(f2)
        f1.close()
        await message.channel.send("작성 완료!")

    if message.content.startswith(f + ' 열람'):
        f2 = open("땡고추.txt")
        await message.channel.send(f2.read())
        f1.close

access_token = os.environ["BOT_TOKEN"]        
client.run("access_token")
