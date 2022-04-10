# nomeowbahh, a bot designed to spam meowbahh.
___________
by running this bot, you spam ping meowbahh. However, you must use
an account. Normal bots won't work because they need to be accepted
by a user with manage members permissions. So a workaround is something called
a **self bot**. Self bots work by making an account then using the account
as a bot.

to host this, simply create a new account or sacrifice your own account lmao

once in, go to https://discord.com/app and press `F12` or `CTRL+SHIFT+I`, depending
on how you normally open google developer tools. Once in, you want to head over
to the **application page**

![finding application](https://github.com/Dekriel/nomeowbahh/blob/main/images/app.png)

(NOTE: if you can't see it, simply press the `>>` and you will hopefully see
a dropdown menu. Select **Application**.

once you have done the following, press `CTRL+SHIFT+M` to activate device **device toolbar**. This
is really important for the next step.

under the menu bar, you will find

![img_1.png](https://github.com/Dekriel/nomeowbahh/blob/main/images/img_1.png)

select the `Filter` searchbar and type in "token". You will see
a key for "token" (**NOT** to be confused with token**s**) and copy the `value`.

what you want to do next is open `main.py`, edit it (using notepad, notepad++ or whatever you prefer)
and then replace `"YOUR TOKEN HERE"` with the token. Remember to **save the file**.

# ONCE YOU HAVE FINISHED
_____
**(remember: having python installed is VERY IMPORTANT! download it here https://python.org remember to add
python to PATH)**

find the downloaded folder and then press extract all. Then copy the path.

open `cmd` and type `pip install -r requirements.txt`

and `cd` to the correct directory (cd means "change directory"). The directory is the path 
where you extracted the zipped folder. Once you are in the directory, type `python main.py`.
Once you see the prompt "ready", go to meowbahh's server https://discord.gg/meowbahhh (important!! since the code
depends on you inside meowbahh's server) and type `.start`. after 2 seconds, the bot should start 
spam pinging meowbahh. This is really effective if lots of people download the code 
and host it on their device!

# changing code
____
if you want it to send different messages, simply edit the `await ctx.send(...)` and replace
it with your **own message**. (Note, it has to be in quotes. Else python will raise an error)

if you want to change the time between spamming, change the `await asyncio.sleep(...)` with 
your own number (no quotes this time because it's an integer) but you **CANNOT REMOVE THE LINE!!!!**
discord will ratelimit your bot and then you will get millions of errors.

**please note, if you want to stop the bot, press `CTRL+C`**

# FAQ
___
**Q: who is meowbahh?**

A: meowbahh is a racist, ableist PNGtuber/tiktoker/youtuber who has said terrible things
and demeaning of other religions. She has to be stopped.

**Q: what has meowbahh said?**

A: *probably* not appropriate for GitHub, but she has told people to kill themselves,
said racist slurs and said that she could take allah on in a fight. She also said that her
own "religon" (meowism) is the only real religon.

**Q: help! I'm getting errors! what do I do?**

A: contact me `Dekriel#9922` on discord!

**Q: problems with setting up!**

A: see the answer above :D

**want to check out an anti-meowbahh discord server?**
https://discord.gg/htbnqhSr
