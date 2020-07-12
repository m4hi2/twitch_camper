import random

from time import sleep

from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = Firefox()

url = 'https://twitch.tv'
driver.get(url)

gg = False
go = 0
go = int(input("READY? : "))
status = ""

moji_spam = [':)', ':(', ':o', ':z', 'B)', ':\\', ';)', ';p', ':p', 'R)', 'o_O', ':D', '>(', '<3', ':)', ':(', ':o', ':z', 'B)', ':\\', ';)', ';p', 
            ':p', 'R)', 'o_O', ':D', '>(', '<3', '<3', 'R)', ':>', '<]', ':7', ':(', ':P', ';P', ':O', ':\\', ':|', ':s', ':D', 'o_O', '>(', ':)', 
            'B)', ';)', '#/', '4Head', 'ANELE', 'ArgieB8', 'ArsonNoSexy', 'AsexualPride', 'AsianGlow', 'BCWarrior', 'BOP', 'BabyRage', 'BatChest', 
            'BegWan', 'BibleThump', 'BigBrother', 'BigPhish', 'BisexualPride', 'BlackLivesMatter', 'BlargNaut', 'BloodTrail', 'BrainSlug', 'BrokeBack', 
            'BuddhaBar', 'CarlSmile', 'ChefFrank', 'CoolCat', 'CoolStoryBob', 'CorgiDerp', 'CrreamAwk', 'CurseLit', 'DAESuppy', 'DBstyle', 'DansGame', 
            'DarkMode', 'DatSheffy', 'DendiFace', 'DogFace', 'DoritosChip', 'DrinkPurple', 'DxCat', 'EarthDay', 'EleGiggle', 'EntropyWins', 'ExtraLife', 
            'FBBlock', 'FBCatch', 'FBChallenge', 'FBPass', 'FBPenalty', 'FBRun', 'FBSpiral', 'FBtouchdown', 'FUNgineer', 'FailFish', 'FootBall', 'FootGoal', 
            'FootYellow', 'FrankerZ', 'FreakinStinkin', 'FutureMan', 'GayPride', 'GenderFluidPride', 'GingerPower', 'GivePLZ', 'GrammarKing', 'GreenTeam', 
            'GunRun', 'HSCheers', 'HSWP', 'HassaanChop', 'HassanChop', 'HeyGuys', 'HolidayCookie', 'HolidayLog', 'HolidayOrnament', 'HolidayPresent', 
            'HolidaySanta', 'HolidayTree', 'HotPokket', 'IntersexPride', 'InuyoFace', 'ItsBoshyTime', 'JKanStyle', 'Jebaited', 'JonCarnage', 'KAPOW', 
            'Kappa', 'KappaClaus', 'KappaPride', 'KappaRoss', 'KappaWealth', 'Kappu', 'Keepo', 'KevinTurtle', 'Kippa', 'KomodoHype', 'KonCha', 'Kreygasm',
            'LUL', 'LesbianPride', 'MVGame', 'Mau5', 'MaxLOL', 'MercyWing1', 'MercyWing2', 'MikeHogu', 'MingLee', 'MorphinTime', 'MrDestructoid', 
            'NinjaGrumpy', 'NomNom', 'NonBinaryPride', 'NotATK', 'NotLikeThis', 'OSFrog', 'OhMyDog', 'OneHand', 'OpieOP', 'OptimizePrime', 'PJSalt', 
            'PJSugar', 'PMSTwin', 'PRChase', 'PanicVis', 'PansexualPride', 'PartyHat', 'PartyTime', 'PeoplesChamp', 'PermaSmug', 'PicoMause', 'PinkMercy', 
            'PipeHype', 'PixelBob', 'PogChamp', 'Poooound', 'PopCorn', 'PorscheWIN', 'PowerUpL', 'PowerUpR', 'PraiseIt', 'PrimeMe', 'PunOko', 'PunchTrees', 
            'PurpleStar', 'RaccAttack', 'RalpherZ', 'RedCoat', 'RedTeam', 'ResidentSleeper', 'RitzMitz', 'RlyTho', 'RuleFive', 'SMOrc', 'SSSsss', 'SabaPing', 
            'SeemsGood', 'SeriousSloth', 'ShadyLulu', 'ShazBotstix', 'SingsMic', 'SingsNote', 'SmoocherZ', 'SoBayed', 'SoonerLater', 'Squid1', 'Squid2', 
            'Squid3', 'Squid4', 'StinkyCheese', 'StoneLightning', 'StrawBeary', 'SuperVinlin', 'SwiftRage', 'TBAngel', 'TF2John', 'TPFufun', 'TPcrunchyroll', 
            'TTours', 'TakeNRG', 'TearGlove', 'TehePelo', 'ThankEgg', 'TheIlluminati', 'TheRinger', 'TheTarFu', 'TheThing', 'ThunBeast', 'TinyFace', 'TombRaid', 
            'TooSpicy', 'TransgenderPride', 'TriHard', 'TwitchLit', 'TwitchRPG', 'TwitchSings', 'TwitchUnity', 'TwitchVotes', 'UWot', 'UnSane', 'UncleNox', 
            'VALRadiant', 'VirtualHug', 'VoHiYo', 'VoteNay', 'VoteYea', 'WTRuck', 'WholeWheat', 'WutFace', 'YouDontSay', 'YouWHY', 'bleedPurple', 'cmonBruh', 
            'copyThis', 'duDudu', 'imGlitch', 'mcaT', 'panicBasket', 'pastaThat', 'riPepperonis', 'twitchRaid']


while go == 1:
    if not gg:
        try:
            channel_status = driver.find_element_by_class_name("channel-status-info").text
        except:
            print(f"Channel Status Not found.")
        if channel_status != "OFFLINE":
            try:
                watch_now = driver.find_element_by_partial_link_text("Watch")
                watch_now.click()
                gg = True
            except:
                print("no gg yet")


        if status != channel_status:
            status = channel_status
            print(status)

    if gg:
        try:
            chat_box = driver.find_element_by_tag_name("textarea")
        
            chat_box.send_keys(" ".join(random.choices(moji_spam, k = 10)))
            chat_box.send_keys(Keys.RETURN)
        except:
            print("Chatbox not found.")

        sleep(100)
