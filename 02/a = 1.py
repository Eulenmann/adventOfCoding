                        a = 1
                        b = 0
                        if a < teile:
                            if a == 1:
                                teil1 =  num_str[:divisor]
                            if a == 2:
                                teil2 =  num_str[divisor:divisor*2]   
                            if a == 3:
                                teil3 =  num_str[divisor*2:divisor*3]
                            if a == 4:
                                teil4 =  num_str[divisor*3:divisor*4]
                            if a == 5:
                                teil5 =  num_str[divisor*4:divisor*5]
                            if a == 6:
                                teil6 =  num_str[divisor*5:divisor*6]
                            a += 1


                                                    old_solution = solution
                        solution += number
                        print("Neue Zahl gefunden: {number}")
                        print("Rechnung: alte Lösung = {old_solution} + Zahl = {solution}")
                        break