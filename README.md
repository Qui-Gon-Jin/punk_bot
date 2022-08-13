# Punk Bot
## Discord bot for Cyberpunk 2020 tabletop game

Bot created to play Cyberpunk 2020 tabletop RPG over Discord more natively, by supporting throw mechanics and counting rules from them.

To add bot to your discord server click [here](https://discord.com/api/oauth2/authorize?client_id=1007383360856928387&permissions=2048&scope=bot), then choose server.
___

Rolls are looking the same as they presented in a corebook:
```
!r *stat* *skill*
!r 4 6
```
If you need some extra of d10 dices
```
!r *number_of_dices*d*dice_type*
!r 4d10
```
Also bot is able to calculate your initiative
```
!i *REF*
!i 6
```
You can request percent check from a bot by typing
```
!r %
```
Implemented modificators option, whiuch can be used with every other base comand like this
(Dividing is automatically rounds down, according to corebook)
```
!r 3 4 +4
!r 4 5 -1
!r 2 8 *2
!r 3 2 /2
!i 3 +4
!r % +25
```
Also bot counts natural roll 1 as fail and marks it, as well as 10 will be critical success.
Every result equal 0 or less will be considered as 1.

____
## Bot installation

To run bot on your own, first download or clone repository, then create [discord bot token](https://discord.com/developers/applications) and put it to new file "token.txt" near to bot.py.
Bot primary uses "discord" libruary, so before starting it make shure you installed it
```
pip install discord
```
____
## In development

- [X] Abilitie to make initiative calculation with !i n
- [X] Add % rolling
- [X] Add modifiers
- [X] Add fail (natural 1) and critical success (natural 10)

- [ ] create module to correct show tables
- [ ] Add generating of Run, Leap, Lift, BTM and Save
- [ ] Add career skills list
- [ ] Add commands to generate stats (random, fast and table for cinematic)
- [ ] special abilitie level table
- [ ] Add rolls for generating background
- [ ] Add Fast and Dirty expandables