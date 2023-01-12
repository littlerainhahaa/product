products = []
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = input('請輸入商品價格:') #因為若沒輸入品名,就不須問價格,所以寫在break之後
    products.append([name,price])  #上面這行可以寫成這樣
print(products)

products[0][0] #products第0格清單中的 再第0格 (如何存取二維清單)

for p in products:
    print(p[0], '的價格是', p[1])