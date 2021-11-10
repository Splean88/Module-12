per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
invest_sum = float(input('Please write a sum which you want to invest for deposit:'))
deposit_TKB = int((per_cent['TKB'])*(invest_sum/100))
deposit_SKB = int((per_cent['SKB'])*(invest_sum/100))
deposit_VTB = int((per_cent['VTB'])*(invest_sum/100))
deposit_SBER = int((per_cent['SBER'])*(invest_sum/100))
deposit = deposit_TKB, deposit_SKB, deposit_VTB, deposit_SBER
deposit_i = max(deposit)
print(deposit)
print('Max sum which you can earn is-', deposit_i)
