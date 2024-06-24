def cric():
  """to create the game of cricket"""
  import random as r
  import time
  import sys
  from datetime import datetime , timedelta
  x = 3
  dteam = input("""press team no.to choose your team\n
  1.INDIA            2.AUSRALIA\n
  3.PAKISTAN         4.SRI LANKA\n
  5.ENGLAND          6.NEW ZEALAND
  """)
  while x==3:
    if dteam == "1":
      u_r_team = "INDIA"
      break
    if dteam == "2":
      u_r_team = "AUSRALIA"
      break
    if dteam == "3":
      u_r_team = "PAKISTAN"
      break
    if dteam == "4":
      u_r_team = "SRI LANKA"
      break
    if dteam == "5":
      u_r_team = "ENGLAND"
      break
    if dteam == "6":
      u_r_team = "NEW ZEALAND"
      break
    else:
      dteam = input("""press team no.to choose your team\n
  1.INDIA            2.AUSRALIA\n
  3.PAKISTAN         4.SRI LANKA\n
  5.ENGLAND          6.NEW ZEALAND
  """)
      break
  op_team = r.choice(["INDIA","AUSRALIA","PAKISTAN","SRI LANKA","ENGLAND","NEW ZEALAND"])
  while u_r_team == op_team:
    op_team = r.choice(["INDIA","AUSRALIA","PAKISTAN","SRI LANKA","ENGLAND","NEW ZEALAND"])
  print("you choosed for ",u_r_team)
  print("opponent choosed for ",op_team)
  whether = r.choice(["very sunny","sunny","cloudy"])
  stadium = r.choice(["wankhede stadium,mumbai","jawaralal nehru stadium,delhi","cheepak stadium,chennai"])
  p_time = (datetime.now() + timedelta(hours = 5,minutes = 30)).strftime('%I:%M')
  matchno = r.randint(1,15)
  if whether == "very sunny":
     chance_rain = r.randint(1,40)
     temperature_f = str(r.randint(45,50)) + "°farenheit"
  if whether == "little sunny":
     chance_rain = r.randint(1,30)
     temperature_f = str(r.randint(30,40)) + "°farenheit"
  if whether == "cloudy":
      chance_rain = r.randint(55,90)
      temperature_f = str(r.randint(25,30)) + "°farenheit"
  comment = ["welcome  to this wonderfull cricket match today","and it was a" + " "+ whether +"whether here", "and there is a huge fans are surrounded in" +" "+stadium,"at" +" "+p_time]
  for line in  comment :
    print(line)
    time.sleep(1)
  print("############  MATCH AND GROUND DETAILS ############")
  print("""
total overs : 10              match no.   :""" , matchno,"""\n
whether     :""",whether,             """chances of rain :""",chance_rain,"""%\n
temperature :""",temperature_f,"""\n
""")
  z = 1
  x = 2
  toss = input("""pls select your choice for toss
press 0 for tail
press 1 for head
 """)
  coin = r.randint(0,1)
  coin = str(coin)
  if toss == coin:
    a_toss = input("""choose
  1 for bating
  or
  2 for bowling""")
    if a_toss == "batting":
      b = "bowl"
      print( u_r_team, "won the toss and choosed to",a_toss,"first")
      print(op_team,"has to",b)
  if toss  != coin:
    b = r.choice(["bowl","batting"])
    if b == "batting":
      a_toss = "bowl"
      print(op_team,"won the toss and choosed to",b,"first")
      print( u_r_team,"has to",a_toss)
  if z == 1:
    if a_toss == "batting":
      total_runs = 0
      total_balls = 60
      extras = 0
      wide = 0
      nballs = 0
      wickets = 0
      while total_balls > 0  and wickets < 10:
        runs = r.choice([0,1,2,4,6])
        total_runs += runs
        total_balls -= 1
        m = r.choice(["wide","wicket","no ball","just","thanks","for","seeing","my","code"])
        if m == "wide":
          extras += 1
          wide += 1
          total_balls += 1
        if m == "wicket":
          wickets += 1
          total_balls -=  1
        if m == "no ball":
          if m == "wicket":
            extras += 1
            nballs +=1
            wickets += 0
            total_balls += 1
      print("total score of",u_r_team,"is",total_runs,"/",wickets)
      print("""
remaing balls =""",total_balls,"""\n
total wickets =""",wickets,"""\n
total extras =""",extras,"""\n
total wide =""",wide,"""\n
total no.of no balls =""",nballs)
      print(op_team,"has to bat now")
      time.sleep(2)
      print(op_team,"need",total_runs+1,"runs to win")
      time.sleep(2)
      print("please wait opponent score is loading.....")
      time.sleep(2)
      print("suming up")
      time.sleep(2)

      total_runs_2 = 0
      total_balls2 = 60
      extras2 = 0
      wide2 = 0
      nballs2 = 0
      wickets2 = 0
      while total_balls2 > 0  and wickets2 < 10:
        run2 = r.choice([0,1,2,4,6])
        total_runs_2 += run2
        total_balls2 -= 1
        m2 = r.choice(["wide","wicket","no ball","just","thanks","for","seeing","my","code"])
        if m2 == "wide":
          extras2 += 1
          wide2 += 1
          total_balls2 += 1
        if m2 == "wicket":
          wickets2 += 1
          total_balls2 -=  1
        if m2 == "no ball":
          if m2 == "wicket":
           extras2 += 1
           nballs2 +=1
           wickets2 += 0
           total_balls2 += 1

      time.sleep(2)
      print(op_team,"score is",total_runs_2,"/",wickets2)
      print("score of",u_r_team, "is",total_runs,"/",wickets)
      time.sleep(2)
      print("results are loading.....")
      time.sleep(3)
      if total_runs < total_runs_2:
        print( "score of" ,u_r_team,"is",total_runs,"/",wickets)
        print("""
remaing balls =""",total_balls2,"""\n
total wickets =""",wickets2,"""\n
total extras =""",extras2,"""\n
total wide =""",wide2)
        print(u_r_team,"lost the match by",10 - wickets2,"wickets")
      if total_runs > total_runs_2:
        print("score of",u_r_team,"is",total_runs,"/",wickets)
        print("""
remaing balls =""",total_balls2,"""\n
total wickets =""",wickets2,"""\n
total extras =""",extras2,"""\n
total wide =""",wide2)
        print("congratulations")

        print(u_r_team,"won by",total_runs - total_runs_2,"runs")
  if a_toss != "batting":
    print(u_r_team ,"choosed for bowl first ")
    print(op_team,"has to bat now")
    a_toss = "batting"
    d = 1
    if d == 1:
      opo_run = 0
      opo_balls = 60
      opo_extras = 0
      opo_wide = 0
      opo_nballs = 0
      opo_wickets = 0
      while opo_balls > 0  and opo_wickets < 10:
        run_s = r.choice([0,1,2,4,6])
        opo_run += run_s
        opo_balls -= 1
        n = r.choice(["wide","wicket","no ball","just","thanks","for","seeing","my","code"])
        if n == "wide":
          opo_extras += 1
          opo_wide += 1
          opo_balls += 1
        if n == "wicket":
          opo_wickets += 1
          opo_balls -=  1
        if n == "no ball":
          if n == "wicket":
            opo_extras += 1
            opo_nballs +=1
            opo_wickets += 0
            opo_balls += 1
    print(op_team,"score is",opo_run,"/",opo_wickets)
    print("""
remaing balls =""",opo_balls,"""\n
total wickets =""",opo_wickets,"""\n
total extras =""",opo_extras,"""\n
total wide =""",opo_wide)
    print(u_r_team ,"has to bat now")
    print(u_r_team ,"need",opo_run+1,"to win this match")
    if a_toss == "batting":
      o_run = 0
      o_balls = 60
      o_extras = 0
      o_wide = 0
      o_nballs = 0
      o_wickets = 0
      while o_balls > 0  and opo_wickets < 10:
        run_s = r.choice([0,1,2,4,6])
        o_run += run_s
        o_balls -= 1
        p = r.choice(["wide","wicket","no ball","just","thanks","for","seeing","my","code"])
        if p == "wide":
          o_extras += 1
          o_wide += 1
          o_balls += 1
        if p == "wicket":
          o_wickets += 1
          o_balls -=  1
        if p == "no ball":
          if p == "wicket":
              o_extras += 1
              o_nballs +=1
              o_wickets += 0
              o_balls += 1
      if o_run > opo_run:
        print(u_r_team ,"score is",o_run,"/",o_wickets)
        print("""
remaing balls =""",o_balls,"""\n
total wickets =""",o_wickets,"""\n
total extras =""",o_extras,"""\n
total wide =""",o_wide)
        print("congragulations")
        print(u_r_team ,"won the match by",10 - opo_wickets,"wickets")

      if o_run < opo_run:
        print(u_r_team ,"lost the game by",opo_run-o_run,"runs")
        print("score of", u_r_team , "is",o_run,"/",o_wickets)
        print("""
remaing balls =""",o_balls,"""\n
total wickets =""",o_wickets,"""\n
total extras =""",o_extras,"""\n
total wide =""",o_wide)
        print("sorry",u_r_team,"lost the game by",(opo_run-o_run),"runs")


cric()



