li = [
    {'item': 'rau muong', 'amount': 400},
    {'item': 'rau cai', 'amount': 300}, 
    {'item': 'rau muong', 'amount': 750},
    {'item': 'rau ngot', 'amount': 250},
    {'item': 'rau muong', 'amount': 750},
    {'item': 'rau cai', 'amount': 350},
    {'item': 'ca rot', 'amount': 550},
    {'item': 'bi ngo', 'amount': 200}]

# 1. Danh sách các loại mặt hàng
items_sold = []
for order in li:
  if order['item'] not in items_sold:
    items_sold.append(order['item'])
print(f"Ket qua 1: {items_sold}")

# 2. Tổng trọng lượng
total_weight = 0
for order in li:
  total_weight += order['amount']
print(f"Ket qua 2: {total_weight}")

# 3. Thống kê trọng lượng theo từng mặt hàng
item_weights = {}
for order in li:
  item = order['item']
  amount = order['amount']
  if item in item_weights:
    item_weights[item] += amount
  else:
    item_weights[item] = amount
print(f"Ket qua 3: {item_weights}")

# 4. Danh sách mặt hàng bán được duy nhất 1 đơn
single_sale_items = []
for item in item_weights:
  if item_weights[item] == li[items_sold.index(item)]['amount']:
    single_sale_items.append(item)
print(f"Ket qua 4: {single_sale_items}")