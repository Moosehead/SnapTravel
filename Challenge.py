hotelOptions = []
desiredPlace = []

def hotelFinder(N, Q):
  print("Enter city, supplier, and price: ")
  for i in range(N):
    city, supplier, price = input().split(",")
    hotelOptions.append((city, supplier, float(price)))
  print("Enter city and days until check-in: ")
  for j in range(Q):
    city2, daysUntCheckin = input().split(",")
    desiredPlace.append((city2, int(daysUntCheckin)))
  for k in range(Q):
    prices = []
    for l in range(N):
      if hotelOptions[l][0] == desiredPlace[k][0]:
        if hotelOptions[l][1] == 'A' and desiredPlace[k][1] == 1:
          prices.append(format(1.5* (hotelOptions[l][2]), '.2f'))
        elif hotelOptions[l][1] == 'B' and desiredPlace[k][1] < 3:
          continue
        elif hotelOptions[l][1] == 'C' and desiredPlace[k][1] > 7:
          prices.append(format(0.9 * (hotelOptions[l][2]), '.2f'))
        elif hotelOptions[l][1] == 'D' and desiredPlace[k][1] < 7:
          prices.append(format(1.1 * (hotelOptions[l][2]), '.2f'))
        else:
          prices.append(hotelOptions[l][2])
    print((', ').join(str(x) for x in sorted(prices)) if len(prices) > 0 else 'None')

N, Q = input().split(" ")
hotelFinder(int(N), int(Q))
