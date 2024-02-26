import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

"""
    This is case of loading gpt-3.5.turbo to echo something
"""

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)
print(chat_completion.choices[0].message)


response = client.images.generate(
  model="dall-e-3",
  prompt="A 3D cube being stretched along the x-axis, showing elongation.",
  n=1,
  size="1024x1024"
)
print(response)

response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input="In the beginning Elohim created hashomayim and haaretz. And the earth was tohu vavohu; and darkness was upon the face of the deep. And the Ruach Elohim was hovering upon the face of the waters. And Elohim said, Let there be light: and there was light. And Elohim saw the light, that it was tov; and Elohim divided the ohr from the choshech. And Elohim called the light Yom, and the darkness He called Lailah. And the erev and the boker  were Yom Echad. And Elohim said, Let there be a raki'a (expanse, dome, firmament) in the midst of the mayim (waters), and let it divide the mayim from the mayim. And Elohim made the raki'a, and divided the waters under the raki'a from the waters which were above the raki'a; and it was so. And Elohim called the raki'a Shomayim (Heaven). And the erev and the boker were Yom Sheni (Day Two, the Second Day). And Elohim said, Let the waters under the heaven be gathered together unto one place, and let the yabashah (dry land) appear; and it was so. And Elohim called the yabashah Eretz (Earth); and the mikveh (gathering together of the waters) called He Seas; and Elohim saw that it was tov. And Elohim said, Let the earth bring forth vegetation, the herb yielding zera (seed), and the fruit tree yielding pri (fruit) after its kind, whose seed is in itself, upon the earth; and it was so. And the earth brought forth vegetation, and herb yielding zera (seed) after its kind, and the tree yielding fruit, whose seed was in itself, after its kind; and Elohim saw that it was tov (good). And the erev and the boker were Yom Shlishi (Day Three, the Third Day). And Elohim said, Let there be lights in the raki'a of the heaven to divide the day from the night; and let them be for otot (signs), and for mo'adim (seasons), and for yamim (days), and shanim (years); And let them be for lights in the raki'a of the heaven to give light upon the earth; and it was so. And Elohim made two great lights; the greater light to rule the day, and the lesser light to rule the night; He made the kokhavim (stars) also. And Elohim set them in the raki'a of the heaven to give light upon the earth, And to rule over the day and over the night, and to divide the light from the darkness; and Elohim saw that it was tov. And the erev and the boker were Yom Revi'i (Day Four, the Fourth Day). And Elohim said, Let the waters bring forth an abundance of living creatures, and fowl that may fly above the earth in the open raki'a of heaven. And Elohim created great sea creatures, and every living creature that moveth, which the waters brought forth in abundance, after their kind, and every winged fowl after its kind; and Elohim saw that it was tov. And Elohim blessed them, saying, Be fruitful, and multiply, and fill the waters in the seas, and let fowl multiply in the earth. And the erev and the boker were Yom Chamishi (Day Five, the Fifth Day). And Adonai said, Let the earth bring forth the living creature after its kind, cattle, and creeping thing, and beast of the earth after its kind; and it was so. And Adonai made the beast of the earth after its kind, and cattle after their kind, and every thing that creepeth upon the earth after its kind; and Adonai saw that it was tov. And Adonai said, Let Us make man in Our tzelem, after Our demut: and let them have dominion over the fish of the sea, and over the fowl of the air, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon ha'aretz (the earth). So Adonai created humankind in His own tzelem, in the tzelem Elohim (image of Adonai) created He him; zachar (male) and nekevah (female) created He them. And Adonai blessed them, and Adonai said unto them, Be fruitful, and multiply, and fill the earth, and subdue it:and have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moveth upon the earth.",
)
response.stream_to_file("output.mp3")
